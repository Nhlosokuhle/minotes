from django.urls import path
from . import views

app_name = 'minotes'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:note_id>/delete/', views.delete_note, name='delete_note'),
    path('delete_all', views.delete_all_notes, name='delete_all_notes'),
]
