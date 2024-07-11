from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializer import *
from rest_framework.response import Response
from django.contrib.auth import get_user_model

# Create your views here.
class ReactView(APIView):
    def get(self, request):
        output = [{"employee": output.employee,
                   "department":output.department,}
                   for output in React.objects.all()]
        
        return Response(output)
    
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

User = get_user_model()
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer