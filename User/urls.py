from django.urls import path 
from .views import *

urlpatterns = [
    path('student/register/', RegisterView.as_view()),
    path('student/login/', LoginView.as_view()),
    path('teacher/register/', RegisterTeacherView.as_view()),
    path('teacher/login/', LoginTeacherView.as_view()),
    path('group/', CreateGroupView.as_view()),
    path('group/<int:id/', EditGroupView.as_view()),
    path('homework/', HomeWorkView.as_view()),
    path('Hackaton', HackatonView.as_view()),
    path('Hackaton', HackatonGetView.as_view()),
    path('Hackaton/<int:id/', EditHackatonView.as_view()),
]