from django.db import models
from django.core.validators import EMPTY_VALUES
from django.core.mail import send_mail
from django.conf import settings

import callpass


class PasscodeRequest(models.Model):
    full_name = models.CharField(max_length=100)
    callsign = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    submitted = models.DateTimeField(auto_now_add=True)
    last_action = models.DateTimeField(auto_now=True)
    action_by = models.ForeignKey('auth.User', related_name='requests_modified', null=True, blank=True)
    status = models.CharField(max_length=20,choices=(
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('denied', 'denied'),
    ), blank=True)
    passcode = models.CharField(max_length=5, blank=True, null=True)
    
    def save(self):
        if self.status in EMPTY_VALUES:
            self.status = 'pending'
        super(PasscodeRequest, self).save()
    
    def generate_passcode(self):
        self.passcode = callpass.do_hash(self.callsign)
        return self.passcode
    
    def approve(self):
        self.generate_passcode()
        self.status = 'approved'
        self.save()
        send_mail(
            'APRS-IS Passcode Approved!',
            '''
            %s,
            
            Your APRS-IS passcode for %s is %s.
            ''' % (self.full_name, self.callsign, self.passcode),
            settings.EMAIL_FROM,
            [self.email],
            fail_silently=False
        )
    
    def deny(self):
        self.status = 'denied'
        self.save()
        send_mail(
            'APRS-IS Passcode Denied!',
            '''
            %s,
            
            Your APRS-IS passcode request for %s was denied.
            ''' % (self.full_name, self.callsign),
            settings.EMAIL_FROM,
            [self.email],
            fail_silently=False
        )
    
    def qrz(self):
        return u'<a href="http://www.qrz.com/db/%s">%s</a>' % (self.callsign, self.callsign)
    qrz.allow_tags = True
    
    def approve_link(self):
        return u'<a href="%s/approve">Approve</a>' % (self.id)
    approve_link.allow_tags = True
    
    def deny_link(self):
        return u'<a href="%s/deny">Deny</a>' % (self.id)
    deny_link.allow_tags = True
    
    class Meta:
        ordering = ['-submitted']
    
    def __unicode__(self):
        return u'%s (%s)' % (self.full_name, self.callsign)