'''
Functions and classes for custom forms used in the drone_recon experiment.

By Warren Woodrich Pettine, M.D.
Last updated 2021-08-02
'''

import random

from django import forms
from django.forms import ModelForm, modelformset_factory, BaseModelFormSet, BaseFormSet
from django.utils.html import format_html

from drone_recon.global_variables import *
from drone_recon.models import Subject, Session, QuestionnaireQ


class RegistrationForm(forms.Form):
    """Used for initial user registration

    Args:
        forms (forms.Form): Django forms object
    """
    if not PROLIFIC: # Otherwise, these parameters are passed through the URL.
        user_ID = forms.CharField(label="Your ID Number")
        subject_source = forms.CharField(label="Who Sent You", required=True,
                                         widget=forms.Select(choices=SUBJECT_SOURCES))
    # age = forms.CharField(label="Age", required=True, widget=forms.Select(choices=AGES))
    age = forms.IntegerField(label="Age", required=True, widget=forms.Select(choices=AGES_NUMERIC))
    education = forms.CharField(label="Education Level", required=True, widget=forms.Select(choices=EDUCATION))
    sex = forms.CharField(label="Sex assigned at birth", required=True, widget=forms.Select(choices=SEX))
    gender = forms.CharField(label="Gender identity", required=True, widget=forms.Select(choices=GENDERS))
    start_time = forms.DateTimeField(label='start_time',required=True, widget=forms.HiddenInput())


def makeSubstancesConditionalDict(substances):
    """For building a conditional response to the substances questions.

    Args:
        substances (_type_): dictionary of substances set using global_variables.SUBSTANCES.

    Returns:
        dict: built dictionary for use in the javascript.
    """
    conditional_questions_dict = {}
    for key in substances:
        if key[0] in ['alcohol','caffeine','other']:
            conditional_questions_dict[key[0]] = {}
            conditional_questions_dict[key[0]]['questions'] = [f'{key[0]}_detail']
            conditional_questions_dict[key[0]]['enable'] = [0]
            conditional_questions_dict[key[0]]['disable'] = [1]
    return conditional_questions_dict


def fixSubstanceConditionalForm(form_data):
    """Processes the global variable SUBSTANCE to create additional global variables, if necessary.

    Args:
        form_data (dict): form with data from the user.

    Returns:
        dict: form_data
    """
    for substance in SUBSTANCES:
        if substance[0] in ['alcohol', 'caffeine', 'other']:
            if substance[0] == 'alcohol':
                global ALCOHOL_AMOUNT
                ALCOHOL_AMOUNT.append(('NA',''))
            elif substance[0] == 'caffeine':
                global CAFFEINE_TYPES
                CAFFEINE_TYPES.append(('NA',''))
            if f'{substance[0]}_detail' not in form_data.keys():
                form_data[f'{substance[0]}_detail'] = 'NA'
    return form_data


class makeSubstancesRadioForm(forms.Form):
    """Creates the form class that asks about substance use using radio buttons and aditional details.

    Args:
        forms (forms.Form): Django forms variable.
    """
    def __init__(self, *args, **kwargs):
        substances = kwargs.pop('substances')
        super(makeSubstancesRadioForm, self).__init__(*args, **kwargs)
        for substance in substances:
            self.fields[substance[0]] = forms.ChoiceField(widget=forms.RadioSelect(attrs={'id':substance[0]}),
                                            label=substance[1],choices=[(True,'Yes'), (False,'No')])
            if substance[0] == 'caffeine':
                self.fields[f'{substance[0]}_detail'] = forms.ChoiceField(\
                    widget=forms.Select(attrs={'id': f'{substance[0]}_detail','disabled':True}),
                                            label='What form of caffeine?',choices=CAFFEINE_TYPES)
            if substance[0] == 'alcohol':
                self.fields[f'{substance[0]}_detail'] = forms.ChoiceField(widget=forms.Select(\
                    attrs={'id': f'{substance[0]}_detail','disabled':True}),
                                                    label='How many drinks?', choices=ALCOHOL_AMOUNT)
            if substance[0] == 'other':
                self.fields[f'{substance[0]}_detail'] = forms.CharField(min_length=0, max_length=1000,
                                        widget=forms.TextInput(attrs={'id': f'{substance[0]}_detail','disabled':True}),
                                                                        label='What substance?')


class makeMentalHealthHistoryRadioAgeForm(forms.Form):
    """Creates the form class for mental health questions.

    Args:
        forms (forms.Form): Django forms variable.
    """
    def __init__(self, *args, **kwargs):
        mh_history = kwargs.pop('mh_history')
        super(makeMentalHealthHistoryRadioAgeForm, self).__init__(*args, **kwargs)
        # self.mh_history = mh_history
        age_choices = [(None,'Please Select a Response')] + [(0,'NA')] + [(i,i) for i in np.arange(1,40).astype(int)] + [(41,'Over 40')]
        for condition in mh_history:
            self.fields[condition[0]] = forms.ChoiceField(widget=forms.RadioSelect,label=condition[1],
                                                          choices=[(True,'Yes'), (False,'No')])
            self.fields[f'{condition[0]}-age'] = forms.IntegerField(label=format_html(f"Age of <u>{condition[1].lower()}</u> diagnosis"),
                                        widget=forms.Select(choices=age_choices),required=True,
                                        help_text=f'Select N/A if answer is No')


class substancesModelForm(ModelForm):
    """Creaes the model form for the substances question from a single list. This is not used in the current version.

    Args:
        ModelForm (ModelForm): Django ModelForm class.
    """
    def __init__(self, *args, **kwargs):
        super(substancesModelForm, self).__init__(*args, **kwargs)
        self.fields['substances'].required = False

    class Meta:
        model = Session
        fields = ('substances',)
        widgets = {
            'substances': forms.CheckboxSelectMultiple(choices=SUBSTANCES,attrs={"required": False,'initial':['None']})
        }


class sleepModelForm(ModelForm):
    """Creates form class for leep questions

    Args:
        ModelForm (ModelForm): Django ModelForm class.
    """
    def __init__(self,*args,**kwargs):
        super(sleepModelForm, self).__init__(*args,**kwargs)
        self.fields['sleep_quality'].label = "Please describe the quality of your sleep last night."
        self.fields['sleep_quantity'].label = "How many hours did you sleep last night?"

    class Meta:
        model = Session
        fields = ('sleep_quality','sleep_quantity')
        widgets = {
            'sleep_quality': forms.Select(choices=SLEEP_QUALITY,
                                    attrs={"required": True, 'initial': ['None']}),
            'sleep_quantity': forms.Select(choices=SLEEP_QUANTITY,
                                          attrs={"required": True, 'initial': ['None']})
        }


class mentalHealthModelForm(ModelForm):
    """Creates form class for mental health questions. This is not used in the current version.

    Args:
        ModelForm (ModelForm): Django ModelForm class.
    """
    def __init__(self, *args, **kwargs):
        super(mentalHealthModelForm,self).__init__(*args, **kwargs)
        self.fields['psych_history'].required = False

    class Meta:
        model = Subject
        fields = ('psych_history',)
        widgets = {
            'psych_history': forms.CheckboxSelectMultiple(
                choices=MH_HISTORY,attrs={"required": False,'initial':['None']})
        }


class timezoneModelForm(ModelForm):
    """Creates hidden form class to record the timezone.

    Args:
        ModelForm (ModelForm): Django ModelForm class.
    """
    class Meta:
        model = Session
        fields = ('timezone',)
        widgets = {'timezone': forms.HiddenInput()}


def makeMentalHealthModelForm(
        label='Have you received a formal diagnosis for any of the following? Check all that apply.',
                                instance=None):
    """Form function for mental health questions. This is not used in the current version.

    Args:
        label (str, optional): _description_. Defaults to 'Have you received a formal diagnosis for any of the following? Check all that apply.'.
        instance (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    form = mentalHealthModelForm(instance=instance)
    form.fields['psych_history'].label = label
    form.fields['psych_history'].initial = ['None']
    return form


def makeSubstancesModelForm(label='In the last two hours, have you used any of the following?',
                                instance=None):
    """Creates a form for the substances question. This is not used in the current version.

    Args:
        label (str, optional): _description_. Defaults to 'In the last two hours, have you used any of the following?'.
        instance (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    form = substancesModelForm(instance=instance)
    form.fields['substances'].label = label
    form.fields['substances'].initial = ['None']
    return form


class BaseQuestionnaireFormSet(BaseModelFormSet):
    """Used to create a formset for the questionnaires.

    Args:
        BaseModelFormSet (BaseModelFormSet): Django BaseModelFormSet class.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = QuestionnaireQ.objects.none()


def makeQuestionnaireFormSet(questionnaires):
    """Creates a formset for the questionnaires using the global variable QUESTIONNAIRES.

    Args:
        questionnaires (dict): dictionary of questionnaire names and questions.

    Returns:
        formset: A formset of questions combining all the questionnaires.
    """
    initial = []
    for questionnaire_name, questionnaire in zip(questionnaires.keys(), questionnaires.values()):
        for question in list(questionnaire.keys()):
            initial_form = {
                'questionnaire_name': questionnaire_name,
                'answer': forms.IntegerField(label=question, widget=forms.RadioSelect(choices=[(v,k) for k,v in questionnaire[question]['answers'].items()])),
                'possible_answers': questionnaire[question]['answers'],
                'question': question,
                'questionnaire_question_number': questionnaire[question]['question_number'],
                'subscale': questionnaire[question]['subscale']
            }
            initial.append(initial_form)

    QuestionnaireFormSet = modelformset_factory(QuestionnaireQ,
                      exclude=('session',),
                      widgets={'questionnaire_name'
                               '': forms.HiddenInput(),
                                   'possible_answers': forms.HiddenInput(),
                                   'subscale': forms.HiddenInput(),
                                   'question': forms.HiddenInput(),
                                   'questionnaire_question_number': forms.HiddenInput()
                                   },
                      formset=BaseQuestionnaireFormSet,
                      extra=len(initial))

    formset = QuestionnaireFormSet(prefix=f'questionnaireformeset_id_{random.randint(100000, 999999)}')
    # formset = QuestionnaireFormSet()

    for f in range(len(formset.forms)):
        formset.forms[f].fields['question'].initial = initial[f]['question']
        formset.forms[f].fields['possible_answers'].initial = initial[f]['possible_answers']
        formset.forms[f].fields['questionnaire_name'].initial = initial[f]['questionnaire_name']
        formset.forms[f].fields['subscale'].initial = initial[f]['subscale']
        formset.forms[f].fields['questionnaire_question_number'].initial = initial[f]['questionnaire_question_number']
        formset.forms[f].fields['answer'].widget = forms.RadioSelect(
            choices=[(v, k) for k, v in initial[f]['possible_answers'].items()],
            attrs={"required": True})
        formset.forms[f].fields['answer'].label = initial[f]['question']

    return formset

class attentionCheckList(forms.Form):
    """Class used for list of attention check questions.

    Args:
        forms (forms.Form): Django forms variable.
    """
    label = 'Have you been reading closely? If so, choose prosochiphelia from the following fake conditions.'
    attention_checkbox = forms.CharField(label=label, required=False, widget=\
    forms.CheckboxSelectMultiple(choices=ATTENTION_CHECK_HISTORY,attrs={"required": False,'initial':['None']}))


def fixSubstanceConditionalForm(form_data):
    """Adds additional global variables to the form data if they are not present.

    Args:
        form_data (dict): Response data from the user.

    Returns:
        dict: form_data
    """
    for substance in SUBSTANCES:
        if substance[0] in ['alcohol', 'caffeine', 'other']:
            if substance[0] == 'alcohol':
                global ALCOHOL_AMOUNT
                ALCOHOL_AMOUNT.append(('NA',''))
            elif substance[0] == 'caffeine':
                global CAFFEINE_TYPES
                CAFFEINE_TYPES.append(('NA',''))
            if f'{substance[0]}_detail' not in form_data.keys():
                form_data[f'{substance[0]}_detail'] = 'NA'
    return form_data


def processSubstanceForm(session,form_substance,substances=None):
    """Processes data from the substances form and saves it to the session in the db. 

    Args:
        session (Django.db.models): Django session model object.
        form_substance (Django form): form from the user containing substance responses.
        substances (dict, optional): substances to look for. Defaults to None.

    Returns:
        int: 0
    """
    if substances is None:
        substances = SUBSTANCES
    substance_list, substances_detail_vars = [], []
    for substance in substances:
        if substance[0] in ['alcohol','caffeine','other']:
            substances_detail_vars.append(f'{substance[0]}_detail')
        if eval(form_substance.data[substance[0]]):
            substance_list.append(substance[0])
    for substance_detail in substances_detail_vars:
        substance_list.append(f'{substance_detail}-{form_substance.data[substance_detail]}')
    session.substances = substance_list
    session.save()
    return 0


def processMentalHealthHistoryForm(session,form_mh_history,mh_history=None):
    """Processes data from the mental health history form and saves it to the session in the db.

    Args:
        session (Django.db.models): Django session model object.
        form_mh_history (Django form): Form from the user containing mental health history responses.
        mh_history (dict, optional): mental health conditions to look for. Defaults to None.

    Returns:
        int: 0
    """
    if mh_history is None:
        mh_history = MH_HISTORY
    mh_history_list = []
    for mh in mh_history:
        if eval(form_mh_history.data[mh[0]]):
            age_diagnosis = form_mh_history.data[f'{mh[0]}-age']
            mh_history_list.append(f'{mh[0]}-{age_diagnosis}')
    subject = Subject.objects.filter(sessions=session)[0]
    subject.psych_history = mh_history_list
    subject.save()
    return 0


def makeMentalHealthConditionalDict(mh_history):
    """Modifies the global variable MH_HISTORY to make it compatible with the javascript for conditional questions.

    Args:
        mh_history (dict): mental health conditions to look for.

    Returns:
        dict: conditional_questions_dict
    """
    conditional_questions_dict = {}
    for key in mh_history:
        conditional_questions_dict[key[0]] = {}
        conditional_questions_dict[key[0]]['questions'] = [f'{key[0]}_age']
        conditional_questions_dict[key[0]]['enable'] = [0]
        conditional_questions_dict[key[0]]['disable'] = [1]
    return conditional_questions_dict


class makeMentalHealthHistoryRadioAgeForm(forms.Form):
    """Creates the form class for mental health questions. This is not used in the current version.

    Args:
        forms (forms.Form): Django forms variable.
    """
    def __init__(self, *args, **kwargs):
        mh_history = kwargs.pop('mh_history')
        super(makeMentalHealthHistoryRadioAgeForm, self).__init__(*args, **kwargs)
        # self.mh_history = mh_history
        age_choices = [(None,'Please Select a Response')] + [(i,i) for i in np.arange(1,40).astype(int)] + [(41,'Over 40')]
        for condition in mh_history:
            self.fields[condition[0]] = forms.ChoiceField(widget=forms.RadioSelect(attrs={'id':condition[0]}),
                                                          label=condition[1],choices=[(True,'Yes'), (False,'No')],)
            self.fields[f'{condition[0]}-age'] = forms.IntegerField(label=format_html(f"Age of <u>{condition[1].lower()}</u> diagnosis"),
                                        widget=forms.Select(choices=age_choices, attrs={'disabled':True,'id':f'{condition[0]}_age'}),
                                        required=True)



def makeConditionalFormSet(questionnaire,conditional_questions=None):
    """Creates a formset for the questionnaires using the global variable QUESTIONNAIRES.

    Args:
        questionnaire (dict): set of questions for the questionniare
        conditional_questions (sixr, optional): Conditional questions. Defaults to None.

    Returns:
        formset, conditional_questions_dict
    """
    # Make the formset
    formset = makeQuestionnaireFormSet(questionnaire)

    if conditional_questions is not None:
        # Disable relevant questions
        disabled_question_numbers = [element for key in conditional_questions.keys() for element in conditional_questions[key]['questions']]
        for f in range(len(formset.forms)):
            q_id = f"{formset.forms[f].fields['questionnaire_name'].initial}_" +\
                   f"{formset.forms[f].fields['questionnaire_question_number'].initial}"
            formset.forms[f].fields['answer'].widget.attrs['id'] = q_id
            if formset.forms[f].fields['questionnaire_question_number'].initial in disabled_question_numbers:
                formset.forms[f].fields['answer'].widget.attrs['disabled'] = True
                formset.forms[f].fields['answer'].widget.attrs['required'] = False

        # Make a dictionary that javascript can use to index the questions
        questionnaire_name = formset.forms[0].fields['questionnaire_name'].initial
        conditional_questions_dict = {}
        for key in conditional_questions:
            key_id = questionnaire_name + '_' + key
            conditional_questions_dict[key_id] = {
                'questions': [],
                'enable': conditional_questions[key]['enable'],
                'disable': conditional_questions[key]['disable']
            }
            for q_num in conditional_questions[key]['questions']:
                val_id = f"{questionnaire_name}_{q_num}"
                conditional_questions_dict[key_id]['questions'].append(val_id)

    return formset, conditional_questions_dict


class CombinedFormSet(BaseFormSet):
    """Joins multiple formsets into a single formset class

    Args:
        BaseFormSet (BaseFormSet): Django BaseFormSet class.

    Returns:
        _type_: _description_
    """
    min_num = 1  # set the minimum number of forms to 1
    extra = 1  # set the number of extra empty forms to 1
    max_num = 10000
    def __init__(self, *args, **kwargs):
        self.formsets = kwargs.pop('formsets')
        super().__init__(*args, **kwargs)

    def forms(self):
        forms = []
        for formset in self.formsets:
            forms += formset.forms
        return forms


def checkAttention(formset,form_att_check,max_n_failures=2):
    """Processes attention check questions and returns if they passed.

    Args:
        formset (formset): Django formset object.
        form_att_check (form): Separate form with attention check questions.
        max_n_failures (int, optional): Number of questions they can get wrong before failing. Defaults to 2.

    Returns:
        boolean: passed_attention_check
    """
    # Check if they got the psych history one right
    if form_att_check.cleaned_data["attention_checkbox"] is not None:
        fail_attention_checkbox = not (('pass_attention_check' in form_att_check.cleaned_data["attention_checkbox"]) and \
                                    ('fail_attention_check' not in form_att_check.cleaned_data["attention_checkbox"]))
    else:
        fail_attention_checkbox = False
    # Check for the hidden questions
    fail_att_questionnaire = 0
    fail_bapq_question = 0
    att_check_first_question_response, att_check_second_question_response = np.nan, np.nan
    for question in formset.cleaned_data:
        if (question['questionnaire_name'] == 'att_check') and (question['questionnaire_question_number'] == 1):
            fail_att_questionnaire += (question['answer'] != 5)
            att_check_first_question_response = question['answer']
        if (question['questionnaire_name'] == 'att_check') and (question['questionnaire_question_number'] == 2) & \
                (att_check_first_question_response != np.nan):
            fail_att_questionnaire += (question['answer'] != att_check_first_question_response)
        if (question['questionnaire_name'] == 'att_check') and (question['questionnaire_question_number'] == 2) & \
                (att_check_first_question_response == np.nan):
            att_check_second_question_response = question['answer']
        if (question['questionnaire_name'] == 'bapq') and (question['subscale'] == 'Attention Check'):
            fail_bapq_question = (question['answer'] != 5)
    if np.isnan([att_check_first_question_response, att_check_second_question_response]).sum() == 0:
        fail_att_questionnaire += att_check_first_question_response != att_check_second_question_response
    passed_attention_check = (fail_att_questionnaire + fail_bapq_question + fail_attention_checkbox) <= max_n_failures
    # Return if they got enough right
    return passed_attention_check