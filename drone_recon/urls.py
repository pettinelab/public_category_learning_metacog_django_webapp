from django.urls import path
from django.conf.urls.static import static # new
from django.conf import settings # new

from . import views

app_name = 'drone_recon'

urlpatterns = [
    path("", views.index, name="index"),
    path('game', views.game, name='game'),
    path('welcome', views.welcome, name='welcome'),
    path('alreadycompleted', views.alreadyCompleted, name='alreadycompleted'),
    path('attentionfailure', views.alreadyCompleted, name='attentionfailure'),
    path("consentform", views.consentform, name="consentform"),
    path("questionnaires", views.questionnaires, name="questionnaires"),
    path('token', views.token, name='token'),
    path('fishy', views.fishy, name='fishy'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
