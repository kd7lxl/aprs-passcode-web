from django.db import models
from django.core.validators import EMPTY_VALUES

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
        # generate passcode
        self.passcode = ''
        return self.passcode
    
    def approve(self):
        # TODO: generate passcode, send email
        self.status = 'approved'
        self.save()
    
    def deny(self):
        # TODO: send email
        self.status = 'denied'
        self.save()
    
    def approve_link(self):
        return u'<a href="/admin/passcode/passcoderequest/%s/approve">Approve</a>' % (self.id)
    approve_link.allow_tags = True
    approve_link.verbose_name = 'Approve'
    
    def deny_link(self):
        return u'<a href="/admin/passcode/passcoderequest/%s/deny">Deny</a>' % (self.id)
    deny_link.allow_tags = True
    deny_link.verbose_name = 'Deny'
    
    class Meta:
        ordering = ['-submitted']
    
    def __unicode__(self):
        return u'%s (%s)' % (self.full_name, self.callsign)