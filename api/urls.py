from django.http.response import HttpResponse, JsonResponse
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    # Authentication
    path("signInUser/", views.signInUser),
    path("signUpUser/", views.signUpUser),
    path("signUpInstitute/", views.signUpInstitute),
    path("signIn Institute/", views.signInInstitute),
    path("signOut/", views.signOut),
    path("changePassword/", views.changePassword),
    path("forgotPassword/", views.forgotPassword),
    # Admin
    path("addClass/", views.addClass),
    path("removeClass/", views.removeClass),
    path("addStudent/", views.addStudent),
    path("removeStudent/", views.removeStudent),
    path("addExam/", views.addExam),
    path("removeExam/", views.addExam),
    # User
    path("userProfile/", views.userProfile),
    path("fetchExams/", views.fetchExams),
]
