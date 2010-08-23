from models import *
from forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def passcode_request(request):
    if request.POST:
        form = PasscodeRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('complete')
    else:
        form = PasscodeRequestForm()
    
    return render_to_response(
        'request.html',
        {
            'form': form,
        },
        RequestContext(request, {}),
    )