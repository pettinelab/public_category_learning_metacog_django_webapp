from django.contrib import admin

from .models import Stimulus, Session, Subject, Trial, Recruitment

# Register your models
admin.site.register(Stimulus)
admin.site.register(Session)
admin.site.register(Subject)
admin.site.register(Trial)
admin.site.register(Recruitment)