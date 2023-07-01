from django.urls import path

from webapp.views import guests_list_view,\
    guest_create_view, guest_update_view, guest_delete_view

urlpatterns = [
    path('', guests_list_view, name="index"),
    path('guests/add/', guest_create_view, name="guest_add"),
    path('guest/<int:pk>/update/', guest_update_view, name="guest_update_view"),
    path('guest/<int:pk>/delete/', guest_delete_view, name="guest_delete_view")
]