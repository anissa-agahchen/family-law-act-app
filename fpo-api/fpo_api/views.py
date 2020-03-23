
import json

from django.http import HttpResponse
from django.shortcuts import render
from api.models.User import User

def health(request):
    """
    Health check for OpenShift
    """
    return HttpResponse(User.objects.count())

def testing(request):
    return HttpResponse("Hello Testing")