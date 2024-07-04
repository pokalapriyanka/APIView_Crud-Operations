from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import *
from app.serializers import *


class ProductCrud(APIView):
    def get(self,request):
        LPO=Product.objects.all()
        MSPO=ProductMS(LPO,many=True)
        return Response(MSPO.data)


    def post(self,request):
        '''PMSD=ProductSerializer(data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'Suceess':'Product is inserted succesfully'})
        else:
            return Response({'failed':'Product is not inserted'})

         def post(self,request):'''
        rjd=request.data
        PDO=ProductMS(data=rjd)
        if PDO.is_valid():
            PDO.save()
            return Response({'success':'Data is inserted successfully'})
        else:
            return Response({'Failed':'Issues while inserting'})
