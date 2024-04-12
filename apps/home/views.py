from typing import Any
from django.shortcuts import render
from django.http import HttpRequest
import json


def index(request: HttpRequest):

  context = {
    'permissions': json.dumps(list(request.user.get_all_permissions()))
  }

  return render(
    request=request,
    template_name='index.html',
    context=context
  )