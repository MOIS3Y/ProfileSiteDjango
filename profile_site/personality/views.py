from django.shortcuts import render
from personality.models import Skill, SocialLink


# Create your views here.
def index(request):
    """
    docstring
    """
    social_links = SocialLink.objects.all()
    skills = Skill.objects.all()

    context = {
        'title': 'About Me',
        'social_links': social_links,
        'skills': skills
    }
    return render(request, 'personality/index.html', context=context)
