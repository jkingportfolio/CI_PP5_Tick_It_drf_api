"""
A module for views in the contact app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import generics
# Internal
from .models import Contact
from .serializers import ContactSerializer
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    # def contact(request):
    #     """
    #     A function based view for the contact page with form to get
    #     contact details and reason for contacting
    #     """
    #     contact_form = ContactForm()
    #     form_submit = False
    #     if request.method == 'POST':
    #         contact_form = ContactForm(request.POST)
    #         if contact_form.is_valid():
    #             contact_form.save()
    #             messages.success(request, 'Thank you for your message!'
    #                              ' We will be in touch soon!')
    #             form_submit = True
    #             return redirect('dashboard')
    #     else:
    #         contact_form = ContactForm()
    #         context = {
    #             'contact_form': contact_form,
    #         }
    #     return render(request, 'contact/contact.html', context)
