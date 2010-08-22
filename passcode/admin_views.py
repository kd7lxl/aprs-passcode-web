from models import *
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required

def approve(request, passcode_request_id):
    passcode_request = PasscodeRequest.objects.get(id=passcode_request_id)
    passcode_request.approve()
    return HttpResponseRedirect('/admin/passcode/passcoderequest/')

def deny(request, passcode_request_id):
    passcode_request = PasscodeRequest.objects.get(id=passcode_request_id)
    passcode_request.deny()
    return HttpResponseRedirect('/admin/passcode/passcoderequest/')
