from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializer import *
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import Http404

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
    
class CheckAuthorizationView(APIView):
    def get(self, request):
        # Assuming request.user is an instance of CustomUser
        if request.user.is_authenticated:
            if getattr(request.user, 'authorization', False):
                return Response({'authorized': True}, status=status.HTTP_200_OK)
            else:
                return Response({'authorized': False}, status=status.HTTP_200_OK)
        else:
            return Response({'authorized': False}, status=status.HTTP_401_UNAUTHORIZED)
        
class ArticleView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ArticleEditView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        return self.put(request, pk, format)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    