from django.urls import path
from core import views



urlpatterns = [
    path('', views.index),
    path('watch/<int:pk>/', views.videoDetail, name="video-detail"),


    # Saving Comment to db
    path("ajax-save-comment/", views.ajax_save_comment, name="save-comment"),
    path("ajax-delete-comment/", views.ajax_delete_comment, name="delete-comment")
]