from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path("hobbies/", views.hobbies_index, name="hobbies_index"),
  path('hobbies/<int:hobby_id>/', views.hobbies_detail, name='hobbies_detail')
]