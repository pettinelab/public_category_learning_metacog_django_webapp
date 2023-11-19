'''
Contains the primary python code for managing the webapp

By Warren Woodrich Pettine, M.D.
Last Updated: 2023-08-30
'''

import json
import urllib
import os, logging
from datetime import datetime
from user_agents import parse
from django.db.models import Avg, Count
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.forms import modelformset_factory
from django import forms
from django.views.decorators.cache import never_cache
from drone_recon.models import Subject, Session, Trial, QuestionnaireQ, Stimulus, Strategy
from drone_recon.global_variables import *
from drone_recon.functions import getStimulusURLs, tutorialParameters, confidenceParameters, \
    taskParameters, getPaymentToken, createWelcomeMessage, getProlificPaymentTokens
from drone_recon.forms import processSubstanceForm, processMentalHealthHistoryForm, RegistrationForm,\
    timezoneModelForm, makeSubstancesRadioForm, sleepModelForm, makeMentalHealthHistoryRadioAgeForm,\
    makeQuestionnaireFormSet, attentionCheckList, checkAttention, CombinedFormSet, makeConditionalFormSet,\
    makeMentalHealthConditionalDict, makeSubstancesConditionalDict, fixSubstanceConditionalForm
from drone_recon.global_variables import *

import logging

    
# Get an instance of a logger
logger = logging.getLogger('django')

        
def extractURLParameters(request):
    """Obtains key task variables from the URL parameters

    Args:
        request (request): Django request object

    Returns:
        external_session_ID, external_study_ID, external_ID, webapp_use
    """
    external_session_ID = request.GET.get("SESSION_ID")
    external_study_ID = request.GET.get("STUDY_ID")
    external_ID = request.GET.get("PROLIFIC_PID")
    webapp_use = request.GET.get('WEBAPP_USE')
    # If no webapp use specificed, go with the default
    if webapp_use is None:
        webapp_use = DEFAULT_WEBAPP_USE
    # Make sure the required variables are present
    if DEPLOYMENT and ((external_ID == '') or (external_ID is None) or (external_study_ID == '') or \
        (external_study_ID is None) or (external_session_ID == '') or (external_session_ID is None)):
        return fishy(request)
    if (external_session_ID == '') or (external_session_ID is None):
        external_session_ID = 'test'
    if (external_study_ID == '') or (external_study_ID is None):
        external_study_ID = 'foo'
    if (external_ID == '') or (external_ID is None):
        external_ID = 'bar'  
    return external_session_ID, external_study_ID, external_ID, webapp_use


def index(request):
    """Index page for the webapp. This is the first page that is loaded. This can be modified

    Args:
        request (request): Django request object

    Returns:
        view: A re-direct to the consent form. 
    """
    try:
        return consentform(request)
    except:
        logger.error(f'Something went wrong in the index function')


def health(request):
    """Determine the health of the webapp. This is used by Azure to determine if the webapp is running

    Args:
        request (request): Django request object

    Returns:
        HttpResponse() or error
    """
    try:
        return HttpResponse()
    except Exception as e:
        logger.error('Error in %s', 'consentformProlific', exc_info=e)
        

def consentform(request):
    """Consent form for the webapp. This is the first page that is loaded. 

    Args:
        request (request):

    Returns:
        view: direct to the appropriate consent form
    """
    if PROLIFIC:
        # Prolific pulls URL parameters, so we use a different consent form.
        return consentformProlific(request)
    else:
        # The standard one doesn't pull parameters from the URL
        return consentformStandard(request)
    
    
def consentformStandard(request):
    """Standard request form, used when not using Prolific. User enters many key variables

    Args:
        request (_type_): _description_

    Returns:
        render: renders the page
    """
    try:
        link_url = 'drone_recon:welcome'
        return render(request, "drone_recon/consentform.html", {
            "link_url": link_url,
        })
    except Exception as e:
        logger.error('Error in %s', 'consentformStandard', exc_info=e)


def consentformProlific(request):
    """Request form for Prolific, where key variables are extracted from the URL. 

    Args:
        request (_type_): _description_

    Returns:
        render: renders the page.
    """
    try:
        #Grab information from the URL parameters
        external_session_ID, external_study_ID, external_ID, webapp_use = extractURLParameters(request)
        request.session['external_session_ID'] = external_session_ID
        request.session['external_study_ID'] = external_study_ID
        request.session['external_ID'] = external_ID
        request.session['webapp_use'] = webapp_use
        #Tell it where to send users
        link_url = 'drone_recon:welcome'
        return render(request, "drone_recon/consentform.html", {
            "link_url": link_url,
        })
    except Exception as e:
        logger.error('Error in %s', 'consentformProlific', exc_info=e)
    
    
def welcome(request):
    """Welcomes the user, creates a new session and process initial input variables. 

    Args:
        request (_type_): _description_

    Returns:
        Either the initial welcome screen or a re-direct to the next view
    """
    logger.info('In welcome function')
    check_sustance_form = False
    try:
        # return render(request, "drone_recon/welcome.html")
        if request.method == "POST":
            # Check the reCAPTCHA
            recaptcha_valid = True            
            if not DEBUG:
                ''' Begin reCAPTCHA validation '''
                recaptcha_response = request.POST.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'
                values = {
                    'secret': os.environ['GOOGLE_RECAPTCHA_SECRET_KEY'],
                    'response': recaptcha_response
                }
                data = urllib.parse.urlencode(values).encode()
                req = urllib.request.Request(url, data=data)
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode())                
                ''' End reCAPTCHA validation '''
                if not result['success']:
                    recaptcha_valid = False
            if recaptcha_valid:
                # Check if a new user needs to be created
                if (not 'external_ID' in request.session) or(('external_ID' in request.session) and\
                        (not Subject.objects.filter(external_ID=request.session['external_ID']).exists())):
                    # Go through and process the form for a new user
                    form = RegistrationForm(request.POST)
                    if form.is_valid():
                        #Create variables to be entered
                        if PROLIFIC:
                            if DEPLOYMENT:
                                subject_source = 'prolific'
                            else:
                                subject_source = 'internal'
                            if 'external_session_ID' in request.session.keys():
                                external_session_ID = request.session['external_session_ID']
                                external_study_ID = request.session['external_study_ID']
                                user_ID = request.session['external_ID']
                            else:
                                #Grab information from the URL parameters
                                external_session_ID, external_study_ID, user_ID, _ = extractURLParameters(request)
                        else:
                            user_ID = form.cleaned_data["user_ID"]
                            subject_source = form.cleaned_data["subject_source"]
                            external_study_ID = 'foo'
                            external_session_ID = 'bar'
                        age = form.cleaned_data["age"]
                        gender = form.cleaned_data["gender"]
                        sex = form.cleaned_data["sex"]
                        education = form.cleaned_data["education"]
                        start_time = form.cleaned_data["start_time"]
                        #Check if subject exists, if not create them
                        if Subject.objects.filter(external_ID=user_ID,external_source=subject_source).exists():
                            if DEPLOYMENT:
                                return alreadyCompleted(request)
                            subject = Subject.objects.filter(external_ID=user_ID)[0]
                        else:
                            subject = Subject(external_ID=user_ID, gender=gender, sex=sex, age=age,
                                              education=education,external_source=subject_source)
                            subject.save()
                    else:
                        raise ValueError('Invalid Form')
                else: # The user exists, and we have their info from the URL
                    user_ID = request.session['external_ID']
                    external_study_ID = request.session['external_study_ID']
                    external_session_ID = request.session['external_session_ID']
                    subject = Subject.objects.filter(external_ID=user_ID)[0]
                    start_time = datetime.now()
                # Logic as to whether one checks the forms
                check_sustance_form = True
                check_sleep_form = True
                #Create a new Session
                # payment_token = getPaymentToken()
                payment_token, attention_failure_token = getProlificPaymentTokens(request.session['webapp_use'],initial_test=INITIAL_TEST)
                end_time =  datetime.now() # Will update on each refres
                # Create the session 
                # Get the browser
                user_agent_string = request.META.get('HTTP_USER_AGENT', '')
                user_agent = parse(user_agent_string)
                browser = user_agent.browser.family
                browser_version = user_agent.browser.version_string
                # If they're just answering questionnaires
                session = Session(start_time=start_time, end_time=end_time, payment_token=payment_token,
                    subject=subject,external_session_ID=external_session_ID,browser=f'{browser}-{browser_version}',
                    external_study_ID=external_study_ID)
                session.project = PROJECT_NAME
                if request.session['webapp_use'] == 'screen':
                    session.task = 'screen'
                # If they're doing the task as well
                elif (request.session['webapp_use'] == 'game') or (request.session['webapp_use'] == 'both') or (request.session['webapp_use'] == 'task'):
                    session.task = GAME
                # Record session
                session.save()
                # Get the timezone
                timezone_form = timezoneModelForm(request.POST, instance=session)
                if timezone_form.is_valid():
                    timezone_form.save()
                else:
                    raise ValueError('Problem checking the timezone')
                # If we need to check for substances
                if check_sustance_form:
                    # form_substance = substancesModelForm(request.POST, instance=session)
                    form_data = request.POST.copy()
                    form_data = fixSubstanceConditionalForm(form_data)
                    form_substance = makeSubstancesRadioForm(form_data, substances=SUBSTANCES)
                    if form_substance.is_valid():
                        # form_substance.save()
                        processSubstanceForm(session, form_substance, substances=SUBSTANCES)
                    else:
                        raise ValueError('Problem with the checking substances in the welcome view')
                if check_sleep_form:
                    form_sleep = sleepModelForm(request.POST, instance=session)
                    if form_sleep.is_valid():
                        form_sleep.save()
                    else:
                        raise ValueError('Problem with the checking sleep in the welcome view')
                #Set variables for this visit to the site
                request.session['session_ID'] = session.id
                request.session['subject_ID'] = subject.id
                request.session['trial_number'] = 0
                request.method = 'GET'
                # Make sure they're not using a prohibited browser, if so, let them know
                if len(PROHIBITED_BROWSERS)>0:
                    for prohibited_browser in PROHIBITED_BROWSERS:
                        if prohibited_browser in browser:
                            return render(request, "drone_recon/prohibitedbrowser.html", {
                                "prohibited_browsers": PROHIBITED_BROWSERS,
                            })
                # Send them to the next page!
                if (request.session['webapp_use'] == 'screen') or (request.session['webapp_use'] == 'both'):
                    return questionnaires(request)
                elif request.session['webapp_use'] == 'task':
                    return game(request)
                else:
                    raise ValueError(f'{WEBAPP_USE} is invalid for WEBAPP_USE')
        if not DEBUG:                        
            recaptcha = {
                'bool': True,
                'src': 'https://www.google.com/recaptcha/api.js',
                'site_key': os.environ['GOOGLE_RECAPTCHA_SITE_KEY']
            }
        else:
            recaptcha = {
                'bool': False,
                'src': '',
                'site_key': ""
            }
        existing_subject = ('external_ID' in request.session) and \
                Subject.objects.filter(external_ID=request.session['external_ID']).exists()
        welcome_message = createWelcomeMessage(new_user=(existing_subject<1), webapp_use=request.session['webapp_use'])
        form_header_text = 'In the past two hours, have you had any of the following?'
        form_substances = makeSubstancesRadioForm(substances=SUBSTANCES)  
        conditional_questions_dict = makeSubstancesConditionalDict(SUBSTANCES)
        if not existing_subject:       
            form_demographics = RegistrationForm(initial={'start_time': datetime.now()})
        else:
            form_demographics = forms.Form()
        timezone_form = timezoneModelForm()
        form_sleep = sleepModelForm()
        return render(request, "drone_recon/welcome.html", {
            'form_header_text': form_header_text,
            'form_substances': form_substances,
            'form_demographics': form_demographics,
            'form_sleep': form_sleep,
            "timezone_form": timezone_form,
            "recaptcha": recaptcha,
            'welcome_message': welcome_message,
            'conditional_questions': conditional_questions_dict
        })
    except Exception as e:
        logger.error('Error in %s', 'consentformProlific', exc_info=e)


def alreadyCompleted(request):
    """If the user has already completed the task and is not eligible for retest, send them here

    Args:
        request (_type_): _description_

    Returns:
        render: Renders the page.
    """
    return render(request,"drone_recon/alreadycompleted.html")

               
def game(request):
    """Launches the onepage task for the game, and processes responses at the end of the session

    Args:
        request (_type_): _description_

    Returns:
        either renders the page or sends the user on.
    """
    if request.method == 'POST':
        print('Data posted')
        # Get the data from the POST request
        classification_data = json.loads(request.POST.get('classification_trials', ''))
        confidence_data = json.loads(request.POST.get('confidence_trials', ''))
        strategy_free_data = json.loads(request.POST.get('strategy_free', ''))
        strategy_radio_data = json.loads(request.POST.get('strategy_radio', ''))
        # Process and save data from the POST request
        session = Session.objects.filter(id=request.session['session_ID'])[0]
        ## First go through the classification trials
        for trial in classification_data['trials']:
            image = 'images/' + trial['stimulus'].split('/')[-1]
            logging.info(f"trial stimulus: {image}")
            stimulus = Stimulus.objects.filter(image=image)
            if len(stimulus) == 0:
                raise ValueError(f"Trial stimulus {image} not found during recording in DB")
            trial_db = Trial(stimulus_id=stimulus[0].id, 
                          session = session,
                          correct=(trial['response'] == trial['correct_response']),
                          correct_class = trial['drone_type'],
                          response = trial['type_selected'],
                          rt_classification = int(trial['rt']),
                          block=trial['block'], 
                          feedback_given = ('train' in trial['block']),
                          trial_number = int(trial['trial_index_aligned']))
            trial_db.save()
        ## Add the confidence ratings and confidence RT
        for trial in confidence_data['trials']:
            image = 'images/' + trial['stimulus'].split('/')[-1]
            logging.info(f"trial stimulus: {image}")
            stimulus = Stimulus.objects.filter(image=image)
            if len(stimulus) == 0:
                raise ValueError(f"Trial stimulus {image} not found during recording in DB")
            trial_db = Trial.objects.filter(stimulus_id=stimulus[0].id, 
                          session = session,
                          trial_number = trial['trial_index_aligned'])
            if len(trial_db) == 0:
                raise ValueError('When syncing confidence rating, trial not found in DB.')
            
            trial_db[0].confidence = int(trial['response'])
            trial_db[0].rt_confidence = int(trial['rt'])
            trial_db[0].save()
        # Include strategy reports
        if len(strategy_free_data['trials']) > 0:
            strategy_db = Strategy(session=session,
                                   prompt='free_response',
                                   response=strategy_free_data['trials'][0]['response']['Q0'])
            strategy_db.save()
        if len(strategy_radio_data['trials']) > 0:
            for prompt in strategy_radio_data['trials'][0]['response'].keys():
                strategy_db = Strategy(session=session,
                                    prompt=prompt,
                                    response=strategy_radio_data['trials'][0]['response'][prompt])
                strategy_db.save()
        # Update the session to reflect that the task is complete
        session.session_completed = True
        session.save()
        return JsonResponse({
                'success': True,
            })
    else:
        print('Request for game page received')
        # Pull the stimulus URLs from the DB (used in preloading)
        stim_schematic_urls = getStimulusURLs(use='schematic')
        stim_feedback_urls = getStimulusURLs(use='feedback')
        # Get the parameters
        confidence_labels, confidence_keys = confidenceParameters(version=CONFIDENCE_VERSION)
        tutorial_types, tutorial_types_keys, tutorial_train_stimuli, tutorial_test_stimuli = \
            tutorialParameters(version=TUTORIAL_VERSION)
        drone_types, drone_types_keys, train_stimuli, test_stimuli = \
            taskParameters(version=TASK_VERSION,initial_test=INITIAL_TEST)
        # Provide payment token
        return render(request, 'drone_recon/game.html',{
            'confidence_labels': confidence_labels,
            'confidence_keys': confidence_keys,
            'tutorial_types': tutorial_types,
            'tutorial_types_keys': tutorial_types_keys,
            'tutorial_train_stimuli': tutorial_train_stimuli,
            'tutorial_test_stimuli': tutorial_test_stimuli,
            'drone_types': drone_types,
            'drone_types_keys': drone_types_keys,
            'train_stimuli': train_stimuli,
            'test_stimuli': test_stimuli,
            'stim_schematic_urls': stim_schematic_urls,
            'stim_feedback_urls': stim_feedback_urls,
            'require_fullscreen': REQUIRE_FULLSCREEN,
            'initial_test': INITIAL_TEST
        })
        

def questionnaires(request):
    """Launches the questionnaires, and processes responses when they are returned

    Args:
        request (_type_): _description_

    Returns:
        renders the page or sends them on to the next stage.
    """
    logger.info('In questionnaires function')
    if request.method == "POST":
        # Process the formsets
        formset_data = request.POST.copy()
        formset_prefixes = [formset_data_key.split('-')[0] for formset_data_key in formset_data.keys() if
            ('questionnaireformeset_id' in formset_data_key) and (formset_data_key.split('-')[0] != 'initial')]
        formset_prefixes = np.unique(formset_prefixes)
        formset_list = []
        formset_att_check,formset_att_check_bool = [], False
        for formset_prefix in formset_prefixes:
            for i in range(int(formset_data[f'{formset_prefix}-TOTAL_FORMS'])):
                if formset_data[f'{formset_prefix}-{i}-questionnaire_name'] == 'att_check':
                    formset_att_check_bool = True
                form_prefix_answer = f'{formset_prefix}-{i}-answer'
                if form_prefix_answer not in formset_data.keys():
                    formset_data[form_prefix_answer] = 0
            formset_f = modelformset_factory(QuestionnaireQ, exclude=('session',))
            formset = formset_f(formset_data,prefix=formset_prefix)
            if not formset.is_valid():
                raise ValueError(f'Invalid formset for {formset_prefix}')
            else:
                formset_list.append(formset)
            if formset_att_check_bool:
                formset_att_check = formset
                formset_att_check_bool = False    
        # Set the MH diagnosis age to 0 if it's not there
        for condition in MH_HISTORY:
            if f'{condition[0]}-age' not in formset_data.keys():
                formset_data[f'{condition[0]}-age'] = 0
        formset_f = modelformset_factory(QuestionnaireQ, exclude=('session',))
        formset = formset_f(formset_data)
        # Get the other forms
        form_mh = makeMentalHealthHistoryRadioAgeForm(formset_data, mh_history=MH_HISTORY)
        form_att_check = attentionCheckList(request.POST)
        # Get session object
        session = Session.objects.filter(id=request.session['session_ID'])[0]
        session.end_time = datetime.now()
        if all([form_mh.is_valid(),form_att_check.is_valid()]):
            # Process the MH history form
            processMentalHealthHistoryForm(session, form_mh, mh_history=MH_HISTORY)
            # Process the questions from the formset
            for formset in formset_list:
                questions = formset.save(commit=False)
                for question in questions:
                    question.session = session
                    question.save()
            # Check that they were paying attention and take proper course
            if ATTENTION_CHECK:
                pass_attention_check = checkAttention(formset_att_check,form_att_check,max_n_failures=MAX_N_ATTENTION_FAILURES)
                # Save the checkbox answer
                question = QuestionnaireQ(session=session,questionnaire_name='att_check_list',subscale='NA',
                    possible_answers={'Fail':0,'Pass':1},question=form_att_check.label,questionnaire_question_number=0,
                    answer=(('pass_attention_check' in form_att_check.cleaned_data["attention_checkbox"]) and \
                        ('fail_attention_check' not in form_att_check.cleaned_data["attention_checkbox"])))
                question.save()
            else:
                pass_attention_check = True
            if not pass_attention_check:
                session.passed_attention_check = False
                session.save()
                return attentionfailure(request)
            else:
                request.method = 'GET'
                session.passed_attention_check = True
                session.questionnaire_completed = True
                session.save()
                if request.session['webapp_use'] == 'screen':
                    session.session_completed = True
                    session.save()
                    return token(request)
                elif (request.session['webapp_use'] == 'task') or (request.session['webapp_use'] == 'both'):
                    return game(request)
                else:
                    raise ValueError(f"{request.session['webapp_use']} is invalid for WEBAPP_USE")
        else:
            raise ValueError('Problem with the questionnaire formset processing.')

    else:
        # Make the conditional formsets
        formset_conditional_list, conditional_questions_formset_dict = [], {}
        for questionnaire in QUESTIONNAIRES_CONDITIONAL.keys():
            formset_conditional_tmp, conditional_questions_tmp = makeConditionalFormSet(
                {questionnaire: QUESTIONNAIRES_CONDITIONAL[questionnaire]},\
                conditional_questions=CONDITIONAL_QUESTIONS[questionnaire])
            formset_conditional_list.append(formset_conditional_tmp)
            for key in conditional_questions_tmp:
                conditional_questions_formset_dict[key] = conditional_questions_tmp[key]
        # Make the conditional dict for the mental health form and merge it with the other dictionary
        conditional_questions_dict = makeMentalHealthConditionalDict(MH_HISTORY)
        if len(conditional_questions_formset_dict) > 0:
            conditional_questions_dict = {**conditional_questions_dict, **conditional_questions_formset_dict}
        # Make the regular formsets and combine with the conditional
        formset_regular = makeQuestionnaireFormSet(QUESTIONNAIRES)
        formsets_combined = CombinedFormSet(formsets=formset_conditional_list + [formset_regular])
        # MAKE THE STANDARD FORMS
        form_mh = makeMentalHealthHistoryRadioAgeForm(mh_history=MH_HISTORY)
        form_att_check = attentionCheckList()
        return render(request, "drone_recon/questionnaires.html", {
            "formsets_combined": formsets_combined,
            'form_mh': form_mh,
            'form_att_check': form_att_check,
            'conditional_questions': conditional_questions_dict
        })


def attentionfailure(request):
    """View that renders page if they fail the attention check. Give them appropriate token.

    Args:
        request (_type_): _description_

    Returns:
        render
    """
    # They failed the attention test
    return render(request, "drone_recon/attentionfailure.html", {
        "token": ATTENTION_FAILURE_TOKEN,
    })


def token(request):
    """View to provide users with the payment token.

    Args:
        request (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        render
    """
    session = Session.objects.filter(id=request.session['session_ID'])[0]
    payment_token = session.payment_token
    if request.session['webapp_use'] == 'screen':
        token_message = f'Thanks for taking the time to answer the questions! We will analyze your responses and ' + \
            f'determine if you are eligible for future studies. Your payment token for the task is:<br><br>' +\
            f'{payment_token}<br><br>To register for payment, please enter that token in the Prolific page. ' +\
            'You can close this window.'
    elif (request.session['webapp_use'] == 'task') or (request.session['webapp_use'] == 'both'):
        token_message = f'Your payment code for the task is:<br><br>{payment_token}<br><br>To register for ' + \
            'payment, please enter that code in the Prolific recruitment page. You can close this window.'
    else:
        raise ValueError(f"{request.session['webapp_use']} is invalid for WEBAPP_USE")

    if session.session_completed:
        return render(request, "drone_recon/token.html", {
            'token_message': token_message
        })

    else:
        # They somehow got to the token page without completing the task
        return fishy(request)


def fishy(request):
    """View for if something strange happened and they are suspected to be cheating.
    Args:
        request (_type_): _description_

    Returns:
        render: page for fishy responses.
    """
    return render(request, "drone_recon/fishy.html")
