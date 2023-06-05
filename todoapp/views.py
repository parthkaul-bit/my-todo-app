from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import ToDoItem
from .serializers import ToDoItemSerializer

class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CreateToDoItem(generics.CreateAPIView): #create
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    authentication_classes = [BasicAuthentication] #basic-auth
    permission_classes = [IsAuthenticated]

class RetrieveToDoItem(generics.RetrieveAPIView): #read-one
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    authentication_classes = [BasicAuthentication] #basic-auth
    permission_classes = [IsAuthenticated]

class ListToDoItems(generics.ListAPIView): #read-all
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    authentication_classes = [BasicAuthentication] #basic-auth
    permission_classes = [IsAuthenticated]

class UpdateToDoItem(generics.RetrieveUpdateAPIView): #update
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    authentication_classes = [BasicAuthentication] #basic-auth
    permission_classes = [IsAuthenticated]

class DeleteToDoItem(generics.DestroyAPIView): #delete
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    authentication_classes = [BasicAuthentication] #basic-auth
    permission_classes = [IsAuthenticated]