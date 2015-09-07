"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name': 'Travis Swicegood',
    'bio': ("I'm the Campus Director for The Iron Yard in ATX and a sucker "
            "limited edition tshirts!"),
    'email': 'travis@domain51.com',
    'twitter_username': 'tswicegood',
    'github_username': "tswicegood",
    'headshot_url': \
        'https://s.gravatar.com/avatar/9e37f9dc53378c04bab413d352994b79?s=320',
}

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,
                'year': datetime.now().year,
            })
    )
