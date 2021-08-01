from django.urls import path
from resume.views import index

app_name = 'resume'

urlpatterns = [
    path('', index, name='index')
]
