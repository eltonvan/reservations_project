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
    success_url = '/reservations'
    template_name = 'res_delete.html'
   

class ResUpdateView(UpdateView):
    model = Reservation
    success_url = '/reservations'
    form_class = ReservationsForm

class ResCreateView(CreateView):
    model = Reservation
   # template_name = 'res_form.html'
    success_url = '/reservations'
    form_class = ReservationsForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ResListView(LoginRequiredMixin, ListView):
    model = ReservationsForm
    template_name = 'res_list.html'
    context_object_name = 'reservations'
    login_url = '/admin' # redirect not logged in users
    #paginate_by = 10
    def get_queryset(self) -> QuerySet[Any]:
        return self.request.user.reservations.all()



class ResDetailView(DetailView):
    model = Reservation
    context_object_name = 'reservations'



