from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name = 'viewPosts'),
    path('/<id>', views.update_view),
    path('/<id>/delete', views.delete_view)
]