from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

class Stimulus(models.Model):
    """Model class for a stimulus. 

    Args:
        models (models.Model): Django model object class

    Returns:
        str: name of stimulus
    """
    name = models.CharField(max_length=300)
    use = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name


class Subject(models.Model):
    """Model class for a subject.

    Args:
        models (models.Model): Django model object class
    """
    #Contains user index, external identification number, where they came from
    external_ID = models.CharField(max_length=64)
    external_source = models.CharField(max_length=64)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=20,default='')
    gender = models.CharField(max_length=100)
    education = models.CharField(max_length=20)
    is_bot = models.BooleanField(default=False)
    psych_history = models.JSONField(default=list,blank=True,null=True)


class Session(models.Model):
    """Model class for a session.

    Args:
        models (models.Model): Django model object class
    """
    #Summary details, such as length, number of stimuli seen, average performance, date, etc.
    n_trials = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    session_completed = models.BooleanField(default=False)
    questionnaire_completed = models.BooleanField(default=False)
    task_completed = models.BooleanField(default=False)
    total_reward = models.IntegerField(default=0)
    total_payment = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    payment_issued = models.BooleanField(default=False)
    final_performance = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    payment_token = models.CharField(max_length=40)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="sessions")
    external_study_ID = models.CharField(max_length=100,default='')
    external_session_ID = models.CharField(max_length=100,default='')
    perceived_difficulty = models.CharField(max_length=10, default="")
    task = models.CharField(max_length=100, default="")
    substances = models.JSONField(default=list,blank=True,null=True)
    sleep_quality = models.IntegerField(blank=True, null=True)
    sleep_quantity = models.IntegerField(blank=True, null=True)
    passed_attention_check = models.BooleanField(default=False)
    project = models.CharField(max_length=40,default='')
    timezone = models.CharField(max_length=200,default='')
    browser = models.CharField(max_length=200,default='')
   
    
class Strategy(models.Model):
    """Model class for after-session reporting of strategies.

    Args:
        models (models.Model): Django model object class
    """
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='strategies')
    prompt = models.CharField(max_length=1000)
    response = models.CharField(max_length=1000)
    
    
class Recruitment(models.Model):
    """Model class for tracking subject recruitment to studies

    Args:
        models (models.Model): Django model object class
    """
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="recruitment")
    session = models.OneToOneField(Session, on_delete=models.CASCADE, null=True, related_name="recruitment")
    prolific_study_id = models.CharField(max_length=100, default="")
    time = models.DateTimeField()
    task = models.CharField(max_length=100, default="")
    notes = models.CharField(max_length=1000, default="")
    source = models.CharField(max_length=100, default="")
    accepted = models.BooleanField(null=True, default=None)
    
    
class Trial(models.Model):
    """Model class for an individual trial

    Args:
        models (models.Model): Django model object class
    """
    #All data pertinent for an individual trial
    stimulus = models.ForeignKey(Stimulus, on_delete=models.CASCADE, related_name='trials')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='trials')
    correct_class = models.CharField(max_length=100, default="")
    response = models.CharField(max_length=100, default="")
    confidence = models.FloatField(default=None, blank=True, null=True)
    correct = models.BooleanField(null=True)
    rt_classification = models.IntegerField(default=None,null=True)
    rt_confidence = models.IntegerField(default=None,null=True)
    feedback_given = models.BooleanField(default=False)
    block = models.CharField(max_length=100)
    trial_number = models.IntegerField(default=None)
    

class QuestionnaireQ(models.Model):
    """Model class for a questionnaire question

    Args:
        models (models.Model): Django model object class
    """
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='questionnaire_q')
    questionnaire_name = models.CharField(max_length=100)
    subscale = models.CharField(max_length=100,blank=True,null=True)
    possible_answers = models.JSONField(default=dict)
    question = models.CharField(max_length=1000)
    answer = models.IntegerField()
    questionnaire_question_number = models.IntegerField()