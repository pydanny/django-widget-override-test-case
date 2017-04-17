from django import forms
from django.views.generic import FormView


class MyForm(forms.Form):
    hello = forms.CharField()



class MyFormView(FormView):

    form_class = MyForm

    template_name = 'hello.html'
