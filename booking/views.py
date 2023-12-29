

import math
from django.shortcuts import render, redirect, get_object_or_404
from groupchat.models import UserGroups

from django.views import View
import requests
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Futsal
from django.db.models import Q



def LoginView(request):
    return render(request, 'login.html')



