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
        # check for duplicate submission
        elif form.errors.items() == [('callsign', [u'Passcode request with this Callsign already exists.'])]:
            try:
                passcode_request = PasscodeRequest.objects.get(callsign=form.data['callsign'])
            except PasscodeRequest.DoesNotExist:
                # this should never happen
                passcode_request = None
            
            form = PasscodeRequestForm(request.POST, instance=passcode_request)
            if form.is_valid():
                # overwrite the old request
                form.save()
                
                if passcode_request.status == 'pending':
                    return HttpResponseRedirect('complete')
                else:
                    passcode_request.resend_mail()
                    return render_to_response(
                        'status.html',
                        {
                            'passcode_request': passcode_request,
                        },
                        RequestContext(request, {}),
                    )
    else:
        form = PasscodeRequestForm()
    
    return render_to_response(
        'request.html',
        {
            'form': form,
        },
        RequestContext(request, {}),
    )