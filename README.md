aprs-passcode-web
=================

Web application for managing APRS-IS passcode requests, written for the Django web framework in Python.

Screenshots
-----------

Request form (completely unstyled--add your own css):

![aprs-passcode web request form](http://i.imgur.com/Cx6gf.png
"Request form")


Management interface request listing:

![aprs-passcode management interface](http://i.imgur.com/jmPCr.png
"Management interface request listing")

Install
-------

If you have Django 1.2 installed, you can run the test server with

    python manage.py runserver

For a production install, follow standard Django install procedures.

Before using the email feature (activated each time Approve or Deny is clicked from the admin interface), you must configure the mail server settings at the bottom of `settings.py`.

Sample mail server settings for Gmail:

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'YOURUSERNAME@gmail.com'
    EMAIL_HOST_PASSWORD = 'YOURPASSWORD'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_FROM = 'YOURNAME <%s>' % EMAIL_HOST_USER
