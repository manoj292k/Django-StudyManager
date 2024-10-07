# studies/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('list/', views.study_list, name='study_list'),  # List view for studies
    path('detail/<int:id>/', views.study_detail, name='study_detail'),  # Detail view for individual study
# studies/urls.py
path('create/', views.create_study, name='create_study'),

]
