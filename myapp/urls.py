from django.urls import path

# from mycourses.views.personalteacher import CreateCourse, ShowCourses, ShowCourse, CreateLesson, CreateStudent, \
#     ShowLesson, UpdateLesson, ShowStudent, UpdateStudent
# from mycourses.views.views import *
# from mycourses.views.signup import *
from .views import Home

urlpatterns = [

    path('', Home.as_view(), name='home'),

]
