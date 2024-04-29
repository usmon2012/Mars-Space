from django.urls import path 
from .views import *

urlpatterns = [
    path('admin/register/', RegisterAdminView.as_view()),
    path('admin/login/', LoginAdminView.as_view()),
]