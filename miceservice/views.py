from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from miceservice.forms import EventForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def participant(request):
    return render(request, 'participant.html')


class Organizer(View):
    form_class = EventForm
    template_name = 'organizer.html'
    context = {'form': None}

    def get(self, request):
        form = self.form_class()
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = self.form_class(request.POST)
        self.context['form'] = form

        if form.is_valid():
            form.save()
        print(form.errors)

        return redirect('/')
