# mysite_project\mysite\mysite\views.py

# from django.http import Http404, HttpResponse, HttpResponseRedirect
# from django.shortcuts import render
# import datetime
# from blog.forms import ContactForm 
# from django.core.mail import send_mail, get_connection

# # ...

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             con = get_connection('django.core.mail.backends.console.EmailBackend')
#             send_mail(
#                 cd['subject'],
#                 cd['message'],
#                 cd.get('email', 'noreply@example.com'),
#                 ['siteowner@example.com'],
#                 connection=con
#             )
#             return HttpResponseRedirect('/contact/thanks/')
#     else:
#         form = ContactForm(
#         	initial={'subject': 'I love your site!'}
#         )

#     return render(request, 'contact_form.html', {'form': form})