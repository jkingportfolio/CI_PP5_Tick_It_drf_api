"""
A module for urls in the packs app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path

# Internal:
from packs import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('packs/', views.PackList.as_view()),
    path('packs/<int:pk>/', views.PackDetail.as_view())
]
