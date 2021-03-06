from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.conf import settings

from accounts.forms import LoginForm
from .forms import BotExplicationForm

# Create your views here.
def index(request):
    if(request.method == 'POST'):
        user = request.user
        vote_form = BotExplicationForm(request.POST)

        if(vote_form.is_valid()):
            user.vote(is_bot=vote_form.is_bot, answers=vote_form.get_reasons())

    return render(request, "profiles/pages/index.html", {"form": LoginForm(), "vote_form": BotExplicationForm()})

def contato(request):
    return render(request, "profiles/pages/contato.html", {})

def guia(request):
    return render(request, "profiles/pages/guia.html", {})