from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import *
from app.serializers import *


class ProductCrud(APIView):
    def get(self,request,pk):
        LPO=Product.objects.all()
        MSPO=ProductMS(LPO,many=True)
        return Response(MSPO.data)


    def post(self,request,pk):
        rjd=request.data
        PDO=ProductMS(data=rjd)
        if PDO.is_valid():
            PDO.save()
            return Response({'success':'Data is inserted successfully'})
        else:
            return Response({'Failed':'Issues while inserting'})

    def put(self,request,pk):
        rjd=request.data
        instance=Product.objects.get(pk=pk)
        LPO=ProductMS(instance,data=rjd)
        if LPO.is_valid():
            LPO.save()
            return Response({'updated':'Updated success'})
    def patch(self,request,pk):
        rjd=request.data
        instance=Product.objects.get(pk=pk)
        LPO=ProductMS(instance,data=rjd,partial=True) 
        if LPO.is_valid():
            LPO.save()
            return Response({'partial updated':'Updated success'})

    def delete(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'delete':'Deleted Success'})