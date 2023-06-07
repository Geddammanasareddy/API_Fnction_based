from django.shortcuts import render

# Create your views here.
from app.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.serializers import *

@api_view()
def EmployeeJData(request):
    EQS=Employee.objects.all()
    ESD=EmployeeMS(EQS,many=True)
    return Response(ESD.data)
