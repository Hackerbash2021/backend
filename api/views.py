from api.serializers import UserSerializer
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import (
    Organization,
    OrgClass,
    Exam,
    User,
    Admin,
)

# Create your views here.
@api_view(["POST"])
def signUpUser(request):
    name = request.data.get("name")
    email = request.data.get("email")
    password = request.data.get("password")
    phone = request.data.get("phone")

    data = {
        "name": name,
        "email": email,
        "password": password,
        "phone": phone,
        "is_staff": False,
    }
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def signUpInstitute(request):
    name = request.data.get("name")
    phone = request.data.get("phone")

    # accessibility


@api_view()
def signInUser(request):
    return Response(status=status.HTTP_200_OK, data={"message": "Heyy!"})


def signInInstitute(request):
    return Response(status=status.HTTP_200_OK, data={"message": "Heyy!"})


@api_view()
def fetchExams(request):
    # studentId = request.data.get("studentId")
    # organizationId = request.data.get("organizationId")
    organizationClassId = request.data.get("organizationClassId")
    # student = User.objects.get(id=studentId)
    # organization = Organization.objects.get(id=organizationId)

    exams = Exam.filter(org_class_id=organizationClassId)
    # ser exams => data
    serialzer = ExamSerializer(data=exams)
    data = serialzer.data

    return Response(status=status.HTTP_200_OK, data=data)