import numpy as np
import os
from drone_recon.questionnaires import *

global PROLIFIC, DEPLOYMENT, DEBUG, PAYMENT_TOKEN, PAYMENT_TOKEN_LENGTH, ATTENTION_FAILURE_TOKEN,\
    WEBAPP_USE, PROJECT_NAME, GAME, TUTORIAL_VERSION, TASK_VERSION, CONFIDENCE_VERSION, SUBJECT_SOURCES,\
    AGES_NUMERIC, GENDERS, SEX, EDUCATION, MH_HISTORY, ATTENTION_CHECK_HISTORY, SLEEP_QUALITY, SLEEP_QUANTITY,\
    SUBSTANCES, QUESTIONNAIRES, QUESTIONNAIRES_CONDITIONAL, CONDITIONAL_QUESTIONS, CAFFEINE_TYPES, \
    PROHIBITED_BROWSERS, ALCOHOL_AMOUNT, REQUIRE_FULLSCREEN, MAX_N_ATTENTION_FAILURES, DEFAULT_WEBAPP_USE


# http://127.0.0.1:8000/?WEBAPP_USE=task&PROLIFIC_PID=wtest&SESSION_ID=foo&STUDY_ID=bar
# https://dronerecongame.azurewebsites.net/?WEBAPP_USE=task&PROLIFIC_PID=warrentest&SESSION_ID=foo&STUDY_ID=bar


PROLIFIC = True # If the task is being run on Prolific
DEPLOYMENT = True # If the task is in deployment mode, rather than development. Dev removes some settings
ATTENTION_CHECK = True # Include the attention check in the task
INITIAL_TEST = True # Whether initial test or retest
if INITIAL_TEST: 
    RETEST_NUMBER = None
else:
    RETEST_NUMBER = 1 # Set the retest number here
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

PAYMENT_TOKEN = 'set_payment_token' # Set the payment token here. Users are given this to provide mTurk or Prolific.
PAYMENT_TOKEN_LENGTH = 8 # Length of the payment token when automatically generated
ATTENTION_FAILURE_TOKEN = 'A9DK21L' # Token to give users who fail the attention check

PROHIBITED_BROWSERS = [] #['Safari'] # List of browsers that are not allowed to run the task
REQUIRE_FULLSCREEN = True # Whether to require fullscreen for the task
# WEBAPP_USE = 'both' # 'both', 'task', 'screen' # What the webapp is being used for. 'screen' only has questionniares, 'task' only the task
PROJECT_NAME = 'pilots' # Name of the project
GAME = 'category_metacog-v0' # Name of the game. Allows for versioning of the task
MAX_N_ATTENTION_FAILURES = 2 # Maximum number of attention check failures before their responses are rejected
TUTORIAL_VERSION = 1 # Version of the tutorial
TASK_VERSION = 1 # Version of the task
CONFIDENCE_VERSION = 1 # Version of the confidence rating

SUBJECT_SOURCES = [('internal', 'Internal')] # List of sources for subjects when PROLIFIC is False

#What we're using the webapp for when nothing is specified in the path
if os.environ.get('DJANGO_ENV') == 'production':
    DEFAULT_WEBAPP_USE = os.environ.get('DEFAULT_WEBAPP_USE')
else:
    DEFAULT_WEBAPP_USE = 'both' # 'screen', 'task', 'both'

## SUBJECT PROFILE QUESTIONS
AGES_NUMERIC = [(None,'Please Select Response')] + [(i,i) for i in np.arange(18,100).astype(int)]
GENDERS = [('','Please Select Response'),('female', 'Female'), ('male', 'Male'), ('trans_male', 'Trans Male/Trans Man'),
           ('trans_female', 'Trans Female/Trans Woman'),('genderqueer', 'Genderqueer/Gender NonConforming'),
           ('other', 'Different Identity'),('none', 'Prefer not to say')]
SEX = [('','Plese Select Response'),('female', 'Female'), ('male', 'Male')]
EDUCATION = [('','Please Select Response'),('<highschool', "Some Highschool"), ('highschool', 'Highschool Graduate'),
             ('<college', 'Some College'),
             ('college', 'College Graduate'), ('postgrad', 'Postgraduate')]
MH_HISTORY = [('asd','Autism spectrum disorder'),('adhd','Attention deficit hyperactivity disorder'),
              ('ocd','Obsessive compulsive disorder'),('depression','Depression'),
              ('bipolar','Bipolar disorder'),('schizophrenia','Schizophrenia'),('schizotypy','Schizotypal personality'),
              ('addiction','Substance use disorder')]
# MH_HISTORY = [('asd','Autism spectrum disorder')]
ATTENTION_CHECK_HISTORY = [('fail_attention_check','Femur dissolution'),('fail_attention_check','Malconforsethia'),
              ('pass_attention_check','Prosochiphelia'),('fail_attention_check','Retinal dermatitis')]
## Subject each-session questions
SLEEP_QUALITY = [(None,'Please Select Response'),(0,'Bad'), (1,'Fair'), (2,'Good')]
SLEEP_QUANTITY = [(None,'Please Select Response')] + [(i,i) for i in np.arange(0,12).astype(int)] + [(12,'>12')]
SUBSTANCES = [('caffeine','Caffeine'),('adhd_stimulants','ADHD medication (e.g. Ritalin)'),('alcohol','Alcohol'),
              ('tobacco','Tobacco'),('marijuana','Marijuana'),('opioids','Opioids'),('illicit_stimulants',
              'Cocaine or meth'),('other','Other performance-alterning substances not listed')]
# SUBSTANCES = [('caffeine','Caffeine')]
CAFFEINE_TYPES = [('','Plese Select Response'),('coffee','Coffee'),('tea','Tea'),('energy_drink','Energy drink'),('soda','Soda'),
                  ('energy_drink','Caffeine pill'),('other','Other')]
ALCOHOL_AMOUNT = [('','Plese Select Response'),('1','One drink'),('1','Two drinks'),('3+','Three or more drinks')]

## SPECIFY THE  QUESTIONNAIRS TO USE
if ATTENTION_CHECK:
    QUESTIONNAIRES = {
        'bfi10': QUESTIONNAIRE_BFI_10,
        'bapq': QUESTIONNAIRE_BAPQ,
        'att_check': QUESTIONNAIRE_ATTENTION_CHECK,
        'asrs': QUESTIONNAIRE_ASRS,
        'phq9': QUESTIONNAIRE_PHQ9,        
    }
else:
    QUESTIONNAIRES = {
        'test': QUESTIONNAIRE_TEST,
    }
    
## SPECIFY QUESTIONNAIRES WITH CONDITIONAL QUESTIONS
QUESTIONNAIRES_CONDITIONAL = {
    # 'cape_pos_neg': QUESTIONNAIRE_CAPE_POS_NEG,
    # 'c-ssrs': QUESTIONNAIRE_C_SSRS,
}

CONDITIONAL_QUESTIONS = {
    # 'cape_pos_neg': QUESTIONNAIRE_CAPE_POS_NEG_CONDITIONAL,
    # 'c-ssrs': QUESTIONNAIRE_C_SSRS_CONDITIONAL,
}