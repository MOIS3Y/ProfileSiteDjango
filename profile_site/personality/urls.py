from django.urls import path
from personality.views import index

app_name = 'personality'

urlpatterns = [
    path('', index, name='index')
]
