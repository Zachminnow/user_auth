from django.shortcuts import render, redirect
from .forms import ContactForm, FeedbackForm
from .models import ContactModel
from django.views.generic import ListView
# from django.http import HttpResponse
import datetime


# Create your views here.
class ContactListView(ListView):
    model = ContactModel
    template_name = "learn/contact_list.html"
    context_object_name = 'messages'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.date.today()
        return context


def dashboard(request):
    messages = ContactModel.objects.all()
    context = {
        'messages': messages
    }
    return render(request, 'learn/dashboard.html', context)


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            form.save()
        return redirect('dashboard')
    else:
        form = ContactForm()

    return render(request, 'learn/contact.html', {'form': form})


def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = FeedbackForm()
    return render(request, "learn/feedback_form.html", {'form': form})


def thank_you(request):
    return render(request, 'feedback/thank_you.html')
