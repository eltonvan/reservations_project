from typing import Any, List
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import  ReservationsForm

from .models import Reservation


class ResDeleteView(DeleteView):
    model = Reservation 
    success_url = '/reservations_project/reservations'
    template_name = 'reservations/res_delete.html'
   

class NotesUpdateView(UpdateView):
    model = Reservation
    success_url = '/reservations_project/reservations'
    form_class = ReservationsForm

class NotesCreateView(CreateView):
    model = Reservation
    #fields = ['title', 'text']
    success_url = '/reservations_project/reservations'
    form_class = ReservationsForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = ReservationsForm
    template_name = 'reservations/res_list.html'
    context_object_name = 'reservations'
    login_url = '/admin' # redirect not logged in users
    #paginate_by = 10
    def get_queryset(self) -> QuerySet[Any]:
        return self.request.user.notes.all()



class NotesDetailView(DetailView):
    model = Reservation
    context_object_name = 'reservation'



