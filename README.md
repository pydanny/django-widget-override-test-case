# Resolved: Django Widget Override Test Case

The process of overriding the Django form widget HTML doesn't match the official documentation. Couldn't figure it out even after a brief look at the source code. This test case pares down the problem to the barest minimum example.

Resolution:

``` python
# settings.py
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'
```

# How to Run

1. Run manage.py migrate
2. Run manage.py runserver
3. Go to 127.0.0.1:8000

Reference documentation:

* https://docs.djangoproject.com/en/1.11/ref/forms/renderers/#overriding-built-in-widget-templates
* https://docs.djangoproject.com/en/1.11/ref/forms/renderers/#templatessetting


There should not be any form fields displayed. However, form field is displayed.

Reference Ticket:

* https://code.djangoproject.com/ticket/28088

# Thanks!

@fapolloner
