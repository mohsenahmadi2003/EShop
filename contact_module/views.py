from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactUsModelForm
from django.views.generic.edit import FormView


class ContactUsView(FormView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
