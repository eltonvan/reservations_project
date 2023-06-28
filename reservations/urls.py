from django.urls import path

from . import views

urlpatterns = [
    path('reservations', views.NotesListView.as_view(), name = ' reservations.list'),
    path('reservations/<int:pk>', views.NotesDetailView.as_view(), name = 'reservations.detail'),
    path('reservations/<int:pk>/edit', views.NotesUpdateView.as_view(), name = 'reservations.update'),
    path('reservations/<int:pk>/delete', views.NotesDeleteView.as_view(), name = 'reservations.delete'),

    path('reservations/new', views.NotesCreateView.as_view(), name = 'reservations.new'),

] 