from models import *
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required

def approve(request, passcode_request_id):
    passcode_request = PasscodeRequest.objects.get(id=passcode_request_id)
    passcode_request.action_by = request.user
    passcode_request.approve()
    return HttpResponseRedirect(request.META['HTTP_REFERER'] if request.META['HTTP_REFERER'] != '' else '/admin/passcode/passcoderequest/')
approve = staff_member_required(approve)

def deny(request, passcode_request_id):
    passcode_request = PasscodeRequest.objects.get(id=passcode_request_id)
    passcode_request.action_by = request.user
    passcode_request.deny()
    return HttpResponseRedirect(request.META['HTTP_REFERER'] if request.META['HTTP_REFERER'] != '' else '/admin/passcode/passcoderequest/')
deny = staff_member_required(deny)
