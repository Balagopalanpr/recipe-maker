from django.shortcuts import render
from django.contrib.auth.models import User
from .models import recipe,Review
from.serializers import recipeserializers,UserSerializers,reviewSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


# Create your views here.

class recipeViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = recipe.objects.all()
    serializer_class = recipeserializers

class userViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class reviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = reviewSerializers


class User_logout(APIView):
    # permission_classes = [IsAuthenticated,]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg':"logout sucessfully"},status=status.HTTP_200_OK)


class createreview(APIView):
    def post(self,request):
        r=reviewSerializers(data=request.data)
        if(r.is_valid()):
            r.save()
            return Response(r.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class detailreview(APIView):
    # permission_classes = [IsAuthenticated,]
    def get_object(request,pk):
        try:
            return recipe.objects.get(pk=pk)

        except:
            raise Http404
    def get(self,request,pk):
        r=self.get_object(pk)
        rev=Review.objects.filter(recipe_name=r)
        revdet=reviewSerializers(rev,many=True)
        return Response(revdet.data)

class cuisinefilter(APIView):
    def get(self,request):
        query=self.request.query_params.get('cuisine')
        Recipe=recipe.objects.filter(cuisine=query)
        r=recipeserializers(Recipe,many=True)
        return Response(r.data)

class mealfilter(APIView):
    def get(self,request):
        query=self.request.query_params.get('meal')
        Recipe=recipe.objects.filter(meal=query)
        r=recipeserializers(Recipe,many=True)
        return Response(r.data)

class Ingredientfilter(APIView):
    def get(self,request):
        query=self.request.query_params.get('ingredients')
        Recipe=recipe.objects.filter(ingredients=query)
        r=recipeserializers(Recipe,many=True)
        return Response(r.data)


