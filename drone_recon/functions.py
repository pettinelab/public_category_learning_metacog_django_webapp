'''
Contains helper functions for setting up the DB and running the task. 

'''


from django.core.files import File
from azure.storage.blob import BlobServiceClient
from secrets import token_urlsafe
from glob import glob
import os
from urllib.request import urlretrieve
import copy
from drone_recon.models import Stimulus
from drone_recon.global_variables import *


def buildStimulusDB(file_dir='../drone_pngs',account_url='https://dronereconstorage.blob.core.windows.net',container_name='media-public',
                    source='local',file_base='',use=''):
    """ 
    Helper function that adds stimuli to the database. Supply the path to the folder containing the stimuli. It can load images
    either from a local directory, or from Azure's blob storage.
    Args:
        file_dir (str, optional): Where the files are stored locally. Only used when building locally. Defaults to '../drone_pngs'.
        account_url (str, optional): Where the files are stored in the cloud. Used when building on the cloud. Defaults to 'https://dronereconstorage.blob.core.windows.net'.
        container_name (str, optional): Container in blob storage where the images are located. Defaults to 'media-public'.
        source (str, optional): Whether to build 'local' or from 'blog_storage'. Defaults to 'blob_storage'.
        file_base (str, optional): The start of the file name. Defaults to ''.
        use (str, optional): Whether the stimuli are used for the 'task', 'tutorial', 'schematic', 'feedback' or something else. 
            This is used for filtering when searching the table after DB creation. Defaults to ''.
    
    The uses are "task" and "tutorial", 'schematic', and 'feedback'
    """
    if source not in ['blob_storage','local']:
        raise ValueError('Invalid source. Must be "url" or "local"')
    if source == 'blob_storage':
        blob_service_client = BlobServiceClient(account_url=account_url)
        container_client = blob_service_client.get_container_client(container=container_name)
        blob_list = container_client.list_blobs()
        blob_names = [blob.name for blob in blob_list]
        for blob_name in blob_names:
            if blob_name[:len(file_base)] == file_base:
                name = blob_name.split('.')[0]
                #Check if it exists
                if Stimulus.objects.filter(name=name).exists():
                    print('Existing stimulus found')
                else: # Create new entry
                    print('No existing stimulus found. Creating new entry')
                    stimulus = Stimulus(name=name,use=use)
                    file_url = f'{account_url}/{container_name}/{blob_name}'
                    url_content, _ = urlretrieve(file_url)
                    stimulus.image.save(os.path.basename(file_url), File(open(url_content, 'rb')))
    elif source == 'local':
        #Loop through each image file
        f_names = glob(os.path.join(file_dir,file_base) + '*' + '.png')
        for f in range(len(f_names)):
            print(f'Processing stimulis {f} of {len(f_names)-1}')
            name = os.path.basename(f_names[f]).split('.')[0]
            #Check if it exists
            if Stimulus.objects.filter(name=name).exists():
                print('Existing stimulus found')
            else: # Create new entry
                print('No existing stimulus found. Creating new entry')
                stimulus = Stimulus(name=name,use=use)
                stimulus.image.save(os.path.basename(f_names[f]), File(open(f_names[f], 'rb')))
    return 0
            

def createFullStimulusDB(file_dir='/Users/wwp9/Dropbox/_PettineLab/code/tasks/drone_recon_category_metacog/local_jspsych/img/',
                    account_url='https://dronereconstorage.blob.core.windows.net',container_name='media-public',
                    source='local'):
    """
    Automatically creates the full stimulus database for the task, tutorial, schematics and feedback. This is a wrapper for buildStimulusDB.
    Args:
        file_dir (str, optional): _description_. Defaults to '/Users/wwp9/Dropbox/_PettineLab/code/tasks/drone_recon_category_metacog/local_jspsych/img/'.
        account_url (str, optional): _description_. Defaults to 'https://dronereconstorage.blob.core.windows.net'.
        container_name (str, optional): _description_. Defaults to 'media-public'.
        source (str, optional): _description_. Defaults to 'local'.
    """
    print('Build the main stimuli')
    use = 'task'
    file_base = '0-'
    buildStimulusDB(file_dir=file_dir,account_url=account_url,container_name=container_name,source=source,file_base=file_base,use=use)
    print('Build the tutorial stimuli')
    use = 'tutorial'
    file_base = 'training_'
    buildStimulusDB(file_dir=file_dir,account_url=account_url,container_name=container_name,source=source,file_base=file_base,use=use)
    print('Build schematic stimuli')
    use = 'schematic'
    file_base = 'schematic_'
    buildStimulusDB(file_dir=file_dir,account_url=account_url,container_name=container_name,source=source,file_base=file_base,use=use)
    print('Build feedback stimuli')
    use = 'feedback'
    file_base = 'feedback_'
    buildStimulusDB(file_dir=file_dir,account_url=account_url,container_name=container_name,source=source,file_base=file_base,use=use)
    
    
def getStimulusURLs(use='task'):
    """
    Gets the stimulus URL locations from the database.

    Args:
        use (str, optional): _description_. Defaults to 'task'.

    Returns:
        _type_: _description_
    """
    stimuli = Stimulus.objects.filter(use=use)
    stimulus_urls = []
    for s in stimuli:
        stimulus_urls.append(s.image.url)
    return stimulus_urls

 
def tutorialParameters(version=1):
    """
    Specifies the parameters for the tutorial blocks. Only a single version is currently supported, but it
    is easy to extend with other versions.

    Args:
        version (int, optional): version of the tutorial. Defaults to 1.

    Raises:
        ValueError: incorrect version

    Returns:
        dicts: tutorial_types, tutorial_types_keys, tutorial_train_stimuli, tutorial_test_stimuli
    """
    if version==1:
        # Names and keys associated with each drone type
        tutorial_types = ['Army','Navy']
        tutorial_types_keys = ['j','k']
        # Dictionaries with stimulus/reward associations of each block
        tutorial_train_stimuli = [{
                'stimulus': Stimulus.objects.filter(use='tutorial',name='training_A_prototype')[0].image.url,
                'correct_response': tutorial_types_keys[0], 
                'drone_type': tutorial_types[0], 
                'block': 'tutorial_train'
            },{
                'stimulus': Stimulus.objects.filter(use='tutorial',name='training_A_d1_1')[0].image.url,
                'correct_response': tutorial_types_keys[0], 
                'drone_type': tutorial_types[0], 
                'block': 'tutorial_train'
            },{
                'stimulus': Stimulus.objects.filter(use='tutorial',name='training_B_prototype')[0].image.url,
                'correct_response': tutorial_types_keys[1], 
                'drone_type': tutorial_types[1], 
                'block': 'tutorial_train'                
            },{
                'stimulus': Stimulus.objects.filter(use='tutorial',name='training_B_d1_1')[0].image.url,
                'correct_response': tutorial_types_keys[1], 
                'drone_type': tutorial_types[1], 
                'block': 'tutorial_train'                
            }
        ]
        tutorial_test_stimuli = [{
                'stimulus': Stimulus.objects.filter(use='tutorial',name='training_A_prototype')[0].image.url,
                'correct_response': tutorial_types_keys[0], 
                'drone_type': tutorial_types[0], 
                'block': 'tutorial_test'
            },{
                'stimulus': Stimulus.objects.filter(use='tutorial',name='training_A_d1_2')[0].image.url,
                'correct_response': tutorial_types_keys[0], 
                'drone_type': tutorial_types[0], 
                'block': 'tutorial_test'
            },{
                'stimulus': Stimulus.objects.filter(use='tutorial',name='training_A_d1_3')[0].image.url,
                'correct_response': tutorial_types_keys[0], 
                'drone_type': tutorial_types[0], 
                'block': 'tutorial_test'
            },{
                'stimulus': Stimulus.objects.filter(use='tutorial',name='training_B_prototype')[0].image.url,
                'correct_response': tutorial_types_keys[1], 
                'drone_type': tutorial_types[1], 
                'block': 'tutorial_test'
            },{
                'stimulus': Stimulus.objects.filter(use='tutorial',name='training_B_d1_2')[0].image.url,
                'correct_response': tutorial_types_keys[1], 
                'drone_type': tutorial_types[1], 
                'block': 'tutorial_test'
            },
            {
                'stimulus': Stimulus.objects.filter(use='tutorial',name='training_B_d1_3')[0].image.url,
                'correct_response': tutorial_types_keys[1], 
                'drone_type': tutorial_types[1], 
                'block': 'tutorial_test'
            },
        ]   
    else:
        raise ValueError('Invalid tutorial version. Only version 1 is currently supported.')
    return tutorial_types, tutorial_types_keys, tutorial_train_stimuli, tutorial_test_stimuli


def confidenceParameters(version=1):
    """
    Builds the confidence labels and keys for the task. Only a single version is currently supported, but it
    is easy to extend with other versions.
    
    In version 1, it implements the standard four confidence levels commonly used in metacognition tasks.

    Args:
        version (int, optional): version number. Defaults to 1.

    Raises:
        ValueError: incorrect version

    Returns:
        lists: confidence_labels, confidence_keys
    """
    if version == 1:
        confidence_labels = ['50-62%','63-75%','75-87%','88-100%']
        confidence_keys = ['1','2','3','4']
    else:
        raise ValueError('Invalid confidence version. Only version 1 is currently supported.')
    return confidence_labels, confidence_keys


def taskParameters(version=1,initial_test=True):
    """
    Builds the task parameters. Only a single version is currently supported, but it is easy to extend 
    with other versions.
    
    Version 0 is a short task used for development
    Version 1 is the full task used for data collection

    Args:
        version (int, optional): version of the task. Defaults to 1.
        initial_test (bool, optional): whether it is initial test or later. Defaults to True.

    Returns:
        dicts: drone_types, drone_types_keys, train_stimuli, test_stimuli
    """
    if version == 0:
         # Names and keys associated with each drone type
        drone_types = ['friendly','hostile']
        drone_types_keys = ['n','m']
        # Placeholder dictionaries for faster building
        train_A_dict = {'stimulus': "placeholder",  
                        'correct_response': drone_types_keys[0], 
                        'drone_type': drone_types[0], 
                        'block': 'train'}
        train_B_dict = copy.deepcopy(train_A_dict)
        train_B_dict['correct_response'] = drone_types_keys[1]
        train_B_dict['drone_type'] = drone_types[1]
        test_A_dict = copy.deepcopy(train_A_dict)
        test_A_dict['block'] = 'test'
        test_B_dict = copy.deepcopy(train_B_dict)
        test_B_dict['block'] = 'test'
        # Stimuli names
        train_A_stimuli = ['A_prototype','A_d1_1']
        train_B_stimuli = [stim.replace('A_','B_') for stim in train_A_stimuli]
        test_A_stimuli = ['A_prototype','A_d1_3']
        test_B_stimuli = [stim.replace('A_','B_') for stim in test_A_stimuli]
        # Build dictionaries
        train_stimuli = []
        for stim in train_A_stimuli:
            train_A_dict['stimulus'] = Stimulus.objects.filter(use='task',name=stim)[0].image.url
            train_stimuli.append(copy.deepcopy(train_A_dict))
        for stim in train_B_stimuli:
            train_B_dict['stimulus'] = Stimulus.objects.filter(use='task',name=stim)[0].image.url
            train_stimuli.append(copy.deepcopy(train_B_dict))
        test_stimuli = []
        for stim in test_A_stimuli:
            test_A_dict['stimulus'] = Stimulus.objects.filter(use='task',name=stim)[0].image.url
            test_stimuli.append(copy.deepcopy(test_A_dict))
        for stim in test_B_stimuli:
            test_B_dict['stimulus'] = Stimulus.objects.filter(use='task',name=stim)[0].image.url
            test_stimuli.append(copy.deepcopy(test_B_dict))       
    elif version == 1:
        # Names and keys associated with each drone type
        drone_types = ['friendly','hostile']
        drone_types_keys = ['n','m']
        # Placeholder dictionaries for faster building
        train_A_dict = {'stimulus': "placeholder",  
                        'correct_response': drone_types_keys[0], 
                        'drone_type': drone_types[0], 
                        'block': 'train'}
        train_B_dict = copy.deepcopy(train_A_dict)
        train_B_dict['correct_response'] = drone_types_keys[1]
        train_B_dict['drone_type'] = drone_types[1]
        test_A_dict = copy.deepcopy(train_A_dict)
        test_A_dict['block'] = 'test'
        test_B_dict = copy.deepcopy(train_B_dict)
        test_B_dict['block'] = 'test'
        # Stimuli names
        if initial_test:
            train_A_stimuli = ['A_prototype','A_d1_1','A_d1_2','A_d2_1','A_d2_2','A_d2_3','A_d3_1','A_d3_2',\
                'A_d3_3','A_d4_1','A_d4_2']
            train_B_stimuli = [stim.replace('A_','B_') for stim in train_A_stimuli]
            test_A_stimuli = ['A_prototype','A_d1_3','A_d1_4','A_d1_5','A_d1_6','A_d1_7','A_d2_4','A_d2_5',\
                'A_d2_6','A_d2_7','A_d2_8','A_d3_4','A_d3_5','A_d3_6','A_d3_7','A_d3_8','A_d4_3','A_d4_4',\
                'A_d4_5','A_d4_6','A_d4_7']
            test_B_stimuli = [stim.replace('A_','B_') for stim in test_A_stimuli]
        elif RETEST_NUMBER == 1: 
            train_A_stimuli =  ['0-A-1_1-B-1_2-C-1_3-D-2_4-E-1_5-A-3_6-B-3_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-1_3-D-2_4-E-1_5-A-3_6-B-3_7-C-3_8-D-3_9-E-3',
                                '0-A-1_1-B-1_2-C-1_3-D-1_4-E-1_5-A-3_6-B-3_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-2_3-D-2_4-E-1_5-A-3_6-B-3_7-C-3_8-D-3_9-E-3',
                                '0-A-1_1-B-1_2-C-2_3-D-2_4-E-1_5-A-4_6-B-3_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-1_3-D-1_4-E-1_5-A-3_6-B-4_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-2_2-C-1_3-D-2_4-E-1_5-A-3_6-B-3_7-C-4_8-D-3_9-E-3',
                                '0-A-1_1-B-1_2-C-1_3-D-1_4-E-1_5-A-3_6-B-4_7-C-3_8-D-4_9-E-4',
                                '0-A-1_1-B-1_2-C-2_3-D-2_4-E-1_5-A-4_6-B-4_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-2_2-C-2_3-D-2_4-E-2_5-A-3_6-B-3_7-C-4_8-D-4_9-E-3',
                                '0-A-1_1-B-2_2-C-1_3-D-1_4-E-1_5-A-4_6-B-3_7-C-3_8-D-4_9-E-4']
            train_B_stimuli =  ['0-A-2_1-B-2_2-C-2_3-D-1_4-E-2_5-A-4_6-B-4_7-C-4_8-D-3_9-E-4',
                                '0-A-1_1-B-2_2-C-2_3-D-1_4-E-2_5-A-4_6-B-4_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-2_2-C-2_3-D-1_4-E-2_5-A-4_6-B-4_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-1_2-C-2_3-D-1_4-E-1_5-A-4_6-B-4_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-1_2-C-2_3-D-1_4-E-2_5-A-4_6-B-3_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-2_2-C-2_3-D-1_4-E-2_5-A-4_6-B-3_7-C-3_8-D-3_9-E-4',
                                '0-A-2_1-B-2_2-C-1_3-D-2_4-E-2_5-A-4_6-B-4_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-1_2-C-2_3-D-2_4-E-2_5-A-4_6-B-4_7-C-4_8-D-4_9-E-4',
                                '0-A-1_1-B-2_2-C-2_3-D-1_4-E-1_5-A-4_6-B-4_7-C-4_8-D-3_9-E-3',
                                '0-A-1_1-B-2_2-C-2_3-D-2_4-E-2_5-A-3_6-B-4_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-2_2-C-2_3-D-1_4-E-2_5-A-3_6-B-3_7-C-4_8-D-4_9-E-3']
            test_A_stimuli =   ['0-A-1_1-B-1_2-C-1_3-D-2_4-E-1_5-A-3_6-B-3_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-1_3-D-2_4-E-1_5-A-3_6-B-4_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-2_3-D-2_4-E-1_5-A-3_6-B-3_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-1_3-D-2_4-E-1_5-A-4_6-B-3_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-1_3-D-2_4-E-1_5-A-3_6-B-3_7-C-4_8-D-4_9-E-3',
                                '0-A-2_1-B-1_2-C-1_3-D-2_4-E-1_5-A-3_6-B-3_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-2_2-C-2_3-D-2_4-E-1_5-A-3_6-B-3_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-1_3-D-2_4-E-1_5-A-3_6-B-3_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-1_2-C-1_3-D-2_4-E-1_5-A-3_6-B-3_7-C-4_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-1_3-D-2_4-E-2_5-A-3_6-B-4_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-1_3-D-2_4-E-2_5-A-3_6-B-3_7-C-4_8-D-4_9-E-3',
                                '0-A-1_1-B-2_2-C-1_3-D-2_4-E-2_5-A-3_6-B-3_7-C-4_8-D-4_9-E-3',
                                '0-A-2_1-B-2_2-C-1_3-D-2_4-E-1_5-A-3_6-B-4_7-C-3_8-D-4_9-E-3',
                                '0-A-2_1-B-1_2-C-1_3-D-2_4-E-2_5-A-4_6-B-3_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-2_3-D-2_4-E-2_5-A-4_6-B-3_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-1_3-D-1_4-E-2_5-A-3_6-B-4_7-C-3_8-D-4_9-E-3',
                                '0-A-2_1-B-2_2-C-2_3-D-2_4-E-2_5-A-3_6-B-3_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-1_3-D-2_4-E-2_5-A-4_6-B-3_7-C-4_8-D-4_9-E-4',
                                '0-A-2_1-B-1_2-C-1_3-D-2_4-E-2_5-A-4_6-B-4_7-C-3_8-D-4_9-E-3',
                                '0-A-2_1-B-2_2-C-1_3-D-2_4-E-1_5-A-3_6-B-4_7-C-3_8-D-3_9-E-3',
                                '0-A-1_1-B-1_2-C-2_3-D-2_4-E-1_5-A-4_6-B-4_7-C-3_8-D-4_9-E-4']
            test_B_stimuli =   ['0-A-2_1-B-2_2-C-2_3-D-1_4-E-2_5-A-4_6-B-4_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-2_2-C-2_3-D-1_4-E-2_5-A-4_6-B-4_7-C-3_8-D-3_9-E-4',
                                '0-A-2_1-B-2_2-C-2_3-D-1_4-E-2_5-A-4_6-B-4_7-C-4_8-D-4_9-E-4',
                                '0-A-2_1-B-2_2-C-1_3-D-1_4-E-2_5-A-4_6-B-4_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-2_2-C-2_3-D-1_4-E-1_5-A-4_6-B-4_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-2_2-C-2_3-D-1_4-E-2_5-A-4_6-B-3_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-2_2-C-2_3-D-2_4-E-2_5-A-4_6-B-4_7-C-3_8-D-3_9-E-4',
                                '0-A-2_1-B-2_2-C-2_3-D-1_4-E-1_5-A-3_6-B-4_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-2_2-C-2_3-D-1_4-E-2_5-A-4_6-B-4_7-C-3_8-D-4_9-E-4',
                                '0-A-2_1-B-1_2-C-2_3-D-2_4-E-2_5-A-4_6-B-4_7-C-4_8-D-3_9-E-4',
                                '0-A-1_1-B-2_2-C-2_3-D-1_4-E-2_5-A-3_6-B-4_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-2_2-C-1_3-D-1_4-E-1_5-A-4_6-B-3_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-1_2-C-1_3-D-1_4-E-2_5-A-4_6-B-4_7-C-4_8-D-4_9-E-4',
                                '0-A-1_1-B-2_2-C-1_3-D-1_4-E-2_5-A-4_6-B-4_7-C-4_8-D-4_9-E-4',
                                '0-A-2_1-B-2_2-C-1_3-D-1_4-E-2_5-A-4_6-B-4_7-C-3_8-D-3_9-E-3',
                                '0-A-1_1-B-2_2-C-1_3-D-1_4-E-2_5-A-3_6-B-4_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-1_2-C-2_3-D-1_4-E-2_5-A-3_6-B-4_7-C-3_8-D-3_9-E-3',
                                '0-A-2_1-B-2_2-C-2_3-D-2_4-E-1_5-A-4_6-B-3_7-C-3_8-D-3_9-E-4',
                                '0-A-2_1-B-1_2-C-2_3-D-1_4-E-1_5-A-3_6-B-3_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-1_2-C-2_3-D-2_4-E-2_5-A-3_6-B-3_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-1_2-C-2_3-D-2_4-E-2_5-A-4_6-B-3_7-C-4_8-D-4_9-E-4']
        elif RETEST_NUMBER == 2:
            train_A_stimuli =  ['0-A-1_1-B-2_2-C-1_3-D-2_4-E-1_5-A-4_6-B-4_7-C-3_8-D-4_9-E-4',
                                '0-A-1_1-B-2_2-C-1_3-D-1_4-E-1_5-A-4_6-B-4_7-C-3_8-D-4_9-E-4',
                                '0-A-1_1-B-2_2-C-1_3-D-2_4-E-2_5-A-4_6-B-4_7-C-3_8-D-4_9-E-4',
                                '0-A-1_1-B-2_2-C-2_3-D-2_4-E-1_5-A-4_6-B-4_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-2_3-D-2_4-E-1_5-A-4_6-B-4_7-C-3_8-D-4_9-E-4',
                                '0-A-1_1-B-2_2-C-1_3-D-1_4-E-1_5-A-4_6-B-4_7-C-3_8-D-4_9-E-3',
                                '0-A-2_1-B-2_2-C-1_3-D-1_4-E-2_5-A-4_6-B-4_7-C-3_8-D-4_9-E-4',
                                '0-A-1_1-B-2_2-C-2_3-D-2_4-E-1_5-A-3_6-B-4_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-2_2-C-1_3-D-2_4-E-1_5-A-4_6-B-4_7-C-4_8-D-3_9-E-3',
                                '0-A-1_1-B-2_2-C-2_3-D-1_4-E-1_5-A-4_6-B-4_7-C-4_8-D-4_9-E-3',
                                '0-A-1_1-B-2_2-C-1_3-D-2_4-E-2_5-A-3_6-B-4_7-C-4_8-D-4_9-E-3']
            train_B_stimuli =  ['0-A-2_1-B-1_2-C-2_3-D-1_4-E-2_5-A-3_6-B-3_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-1_2-C-2_3-D-1_4-E-2_5-A-4_6-B-3_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-1_2-C-2_3-D-2_4-E-2_5-A-3_6-B-3_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-1_2-C-2_3-D-2_4-E-2_5-A-3_6-B-3_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-1_2-C-1_3-D-1_4-E-2_5-A-3_6-B-4_7-C-4_8-D-3_9-E-3',
                                '0-A-1_1-B-1_2-C-2_3-D-1_4-E-1_5-A-3_6-B-3_7-C-4_8-D-3_9-E-3',
                                '0-A-1_1-B-1_2-C-2_3-D-1_4-E-2_5-A-4_6-B-4_7-C-4_8-D-3_9-E-3',
                                '0-A-1_1-B-1_2-C-2_3-D-2_4-E-2_5-A-4_6-B-3_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-2_2-C-2_3-D-1_4-E-1_5-A-3_6-B-3_7-C-4_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-2_3-D-1_4-E-2_5-A-3_6-B-4_7-C-3_8-D-3_9-E-4',
                                '0-A-2_1-B-1_2-C-2_3-D-2_4-E-2_5-A-4_6-B-3_7-C-3_8-D-4_9-E-3']
            test_A_stimuli =   ['0-A-1_1-B-2_2-C-1_3-D-2_4-E-1_5-A-4_6-B-4_7-C-3_8-D-4_9-E-4',
                                '0-A-1_1-B-2_2-C-1_3-D-2_4-E-1_5-A-3_6-B-4_7-C-3_8-D-4_9-E-4',
                                '0-A-1_1-B-2_2-C-1_3-D-2_4-E-1_5-A-4_6-B-4_7-C-3_8-D-3_9-E-4',
                                '0-A-1_1-B-2_2-C-1_3-D-2_4-E-1_5-A-4_6-B-4_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-2_2-C-2_3-D-2_4-E-1_5-A-4_6-B-4_7-C-3_8-D-4_9-E-4',
                                '0-A-1_1-B-2_2-C-1_3-D-2_4-E-1_5-A-4_6-B-4_7-C-4_8-D-4_9-E-4',
                                '0-A-1_1-B-2_2-C-1_3-D-1_4-E-2_5-A-4_6-B-4_7-C-3_8-D-4_9-E-4',
                                '0-A-1_1-B-1_2-C-1_3-D-2_4-E-1_5-A-4_6-B-4_7-C-4_8-D-4_9-E-4',
                                '0-A-2_1-B-1_2-C-1_3-D-2_4-E-1_5-A-4_6-B-4_7-C-3_8-D-4_9-E-4',
                                '0-A-1_1-B-2_2-C-1_3-D-1_4-E-1_5-A-4_6-B-3_7-C-3_8-D-4_9-E-4',
                                '0-A-1_1-B-2_2-C-2_3-D-2_4-E-1_5-A-4_6-B-3_7-C-3_8-D-4_9-E-4',
                                '0-A-1_1-B-1_2-C-1_3-D-1_4-E-1_5-A-4_6-B-4_7-C-3_8-D-4_9-E-3',
                                '0-A-2_1-B-2_2-C-1_3-D-2_4-E-2_5-A-4_6-B-4_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-1_3-D-2_4-E-1_5-A-4_6-B-4_7-C-3_8-D-3_9-E-3',
                                '0-A-1_1-B-2_2-C-1_3-D-2_4-E-1_5-A-3_6-B-4_7-C-4_8-D-4_9-E-3',
                                '0-A-1_1-B-2_2-C-1_3-D-1_4-E-1_5-A-4_6-B-3_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-2_2-C-1_3-D-2_4-E-2_5-A-3_6-B-3_7-C-3_8-D-4_9-E-3',
                                '0-A-1_1-B-1_2-C-2_3-D-2_4-E-2_5-A-4_6-B-4_7-C-4_8-D-4_9-E-4',
                                '0-A-2_1-B-1_2-C-1_3-D-2_4-E-1_5-A-4_6-B-3_7-C-3_8-D-3_9-E-4',
                                '0-A-2_1-B-1_2-C-1_3-D-2_4-E-1_5-A-4_6-B-4_7-C-4_8-D-4_9-E-3',
                                '0-A-1_1-B-2_2-C-1_3-D-1_4-E-1_5-A-3_6-B-4_7-C-3_8-D-3_9-E-3']
            test_B_stimuli =   ['0-A-2_1-B-1_2-C-2_3-D-1_4-E-2_5-A-3_6-B-3_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-1_2-C-2_3-D-1_4-E-2_5-A-3_6-B-4_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-1_2-C-2_3-D-1_4-E-2_5-A-3_6-B-3_7-C-3_8-D-3_9-E-3',
                                '0-A-1_1-B-1_2-C-2_3-D-1_4-E-2_5-A-3_6-B-3_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-2_2-C-2_3-D-1_4-E-2_5-A-3_6-B-3_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-1_2-C-1_3-D-1_4-E-2_5-A-3_6-B-3_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-1_2-C-2_3-D-1_4-E-2_5-A-4_6-B-3_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-1_2-C-2_3-D-1_4-E-2_5-A-3_6-B-4_7-C-4_8-D-4_9-E-3',
                                '0-A-2_1-B-1_2-C-2_3-D-1_4-E-2_5-A-4_6-B-4_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-1_2-C-2_3-D-1_4-E-1_5-A-3_6-B-3_7-C-3_8-D-3_9-E-3',
                                '0-A-2_1-B-2_2-C-2_3-D-1_4-E-2_5-A-4_6-B-3_7-C-4_8-D-3_9-E-3',
                                '0-A-2_1-B-2_2-C-2_3-D-1_4-E-1_5-A-3_6-B-3_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-1_2-C-2_3-D-2_4-E-1_5-A-3_6-B-3_7-C-3_8-D-3_9-E-3',
                                '0-A-1_1-B-2_2-C-2_3-D-1_4-E-2_5-A-4_6-B-3_7-C-4_8-D-3_9-E-3',
                                '0-A-1_1-B-1_2-C-1_3-D-1_4-E-2_5-A-3_6-B-3_7-C-4_8-D-3_9-E-4',
                                '0-A-2_1-B-2_2-C-1_3-D-1_4-E-2_5-A-4_6-B-3_7-C-4_8-D-3_9-E-3',
                                '0-A-1_1-B-1_2-C-2_3-D-2_4-E-2_5-A-3_6-B-4_7-C-3_8-D-3_9-E-3',
                                '0-A-1_1-B-1_2-C-2_3-D-1_4-E-2_5-A-3_6-B-3_7-C-3_8-D-4_9-E-4',
                                '0-A-2_1-B-1_2-C-1_3-D-1_4-E-2_5-A-4_6-B-3_7-C-4_8-D-4_9-E-4',
                                '0-A-2_1-B-2_2-C-2_3-D-1_4-E-1_5-A-4_6-B-3_7-C-4_8-D-4_9-E-3',
                                '0-A-2_1-B-2_2-C-1_3-D-1_4-E-1_5-A-3_6-B-3_7-C-4_8-D-3_9-E-4']
        else:
            raise ValueError('Error in the determination of initial test or retest stimuli')
        # Build dictionaries
        train_stimuli = []
        for stim in train_A_stimuli:
            train_A_dict['stimulus'] = Stimulus.objects.filter(use='task',name=stim)[0].image.url
            train_stimuli.append(copy.deepcopy(train_A_dict))
        for stim in train_B_stimuli:
            train_B_dict['stimulus'] = Stimulus.objects.filter(use='task',name=stim)[0].image.url
            train_stimuli.append(copy.deepcopy(train_B_dict))
        test_stimuli = []
        for stim in test_A_stimuli:
            test_A_dict['stimulus'] = Stimulus.objects.filter(use='task',name=stim)[0].image.url
            test_stimuli.append(copy.deepcopy(test_A_dict))
        for stim in test_B_stimuli:
            test_B_dict['stimulus'] = Stimulus.objects.filter(use='task',name=stim)[0].image.url
            test_stimuli.append(copy.deepcopy(test_B_dict))
    else:
        raise ValueError('Invalid task version. Only version 1 is currently supported.')
    return drone_types, drone_types_keys, train_stimuli, test_stimuli


def getPaymentToken():
    """
    Either make a payment token or use the global variable.

    Returns:
        _type_: _description_
    """
    if PAYMENT_TOKEN is None:
        payment_token = token_urlsafe(PAYMENT_TOKEN_LENGTH)
    else:
        payment_token = copy.copy(PAYMENT_TOKEN)
    return payment_token


def createWelcomeMessage(new_user=True,webapp_use=None):
    """
    Standard text use for welcome message

    Args:
        new_user (bool, optional): Whether they are a new user. Defaults to True.
        webapp_use (_type_, optional): 'screen', 'task' or 'both'. If none, it gets it from the global variable. Defaults to None.

    Returns:
        _type_: _description_
    """
    if webapp_use is None:
        webapp_use = DEFAULT_WEBAPP_USE
    if new_user:
        welcome_message = 'Please answer some questions about yourself before we get started.'
    else:
        if webapp_use == 'screen':
            welcome_message = 'Thanks for coming back! Please answer a series of questions on the next screen. We ' +\
                              'will use those answers to determine if you are eligible for future studies.'
        elif webapp_use == 'both':
            welcome_message = 'Thanks for coming back! Please answer a series of questions on the next screen. Once ' \
                              'those are completed, you will move onto the game.'
        elif webapp_use == 'task':
            welcome_message = "Thanks for coming back! We really appreciate you taking the time to return. You will " +\
             "Get ready to do some drone reconnaissance!"
    return welcome_message


def getProlificPaymentTokens(webapp_use,initial_test=True):
    """
    Standard tokens used in the prolific experiments. It is best to unify the ones here with the ones
    used during task creation. If they don't match, it creates issues.
    
    Args:
        param webapp_use: specifies what one is doing with the webapp. Options are 'screen', 'task' or 'both'
    
    Return: 
        strs: payment_token, attention_failure_token
    """
    if webapp_use not in ['screen','task','both']:
        raise ValueError(f"{webapp_use} invalid for webapp_use. Valid values are 'screen', 'task' or 'both'")
    # Set different token for each one
    if webapp_use == 'screen':
        payment_token = 'set_screen_payment_token'
        attention_failure_token = 'set_screen_attention_failure_token'
    elif webapp_use == 'task':
        if initial_test:
            payment_token = 'set_initial_test_payment_token' 
            attention_failure_token = 'set_initial_test_attention_failure_token'
        else:
            payment_token = 'set_retest_payment_token'
            attention_failure_token = 'set_retest_payment_attention_failure_token'
    elif webapp_use == 'both':
        payment_token = 'set_both_payment_token'
        attention_failure_token = 'set_both_attention_failure_token'

    return payment_token, attention_failure_token