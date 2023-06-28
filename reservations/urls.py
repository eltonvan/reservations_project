from django.urls import path

from . import views

urlpatterns = [
    path('reservations', views.ResListView.as_view(), name = 'reservations.list'),
    path('reservations/<int:pk>', views.ResDetailView.as_view(), name = 'reservations.detail'),
    path('reservations/<int:pk>/edit', views.ResUpdateView.as_view(), name = 'reservations.update'),
    path('reservations/<int:pk>/delete', views.ResDeleteView.as_view(), name = 'reservations.delete'),

    path('reservations/new', views.ResCreateView.as_view(), name = 'reservations.new'),

] 