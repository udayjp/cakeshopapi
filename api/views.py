from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from .serializers import *

# Create your views here.

class CakeListView(generics.ListAPIView):
    queryset=Cake.objects.all()
    serializer_class=CakeSerializer

class CakeSearchListView(generics.ListAPIView):
    serializer_class = CakeSerializer
    def get_queryset(self):
        cakename = self.kwargs['name']
        return Cake.objects.filter(name=cakename)

class CakeCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Cake.objects.all()
    serializer_class=CakeSerializer

class CakeDetailsRetrieveView(generics.RetrieveAPIView):
    queryset=Cake.objects.all()
    serializer_class=CakeSerializer

class UserRegistrationView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            if user:
                return Response("Registered successfully!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CartCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Cart.objects.all()
    serializer_class=AddtoCartSerializer
    
class CartView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        data=Cart.objects.filter(userid=request.user)
        serializer = CartSerializer(data,context={'request':request},many=True)
        return Response(serializer.data)  
    
    def delete(self, request, pk, format=None):
        data = Cart.objects.get(id=pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)         

class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class OrdersView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        data=Orders.objects.filter(userid=request.user)
        serializer = OrdersSerializer(data,context={'request':request},many=True)
        return Response(serializer.data)  

    def post(self,request):
        serializer=AddtoOrdersSerializer(data=request.data)
        if serializer.is_valid():
            order=serializer.save()
            if order:
                return Response("Ordered successfully!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        data = Cart.objects.filter(userid=request.user)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   