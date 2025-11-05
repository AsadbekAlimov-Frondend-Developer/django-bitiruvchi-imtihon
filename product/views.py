from tkinter.ttk import Notebook
from django.shortcuts import render,get_object_or_404
from .models import PRODUCT
from .serializers import ProductSerializer, ProductSerializer
from rest_framework.generics import ListAPIView,DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductListView(ListAPIView):
    queryset = PRODUCT.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(DestroyAPIView):
    queryset = PRODUCT.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(APIView):
    def post(self, request):
        malumot = request.data
        serializer = ProductSerializer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            info = {
                'holat': 'Mahsulot muvaffaqiyatli qoshildi',
                'ular': serializer.data  
            }
            return Response(info)
        else:
            return Response(serializer.errors)


class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(PRODUCT, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    

class ProductMixedAPIView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(PRODUCT, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            product = PRODUCT.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({'status': 'serializer is not valid'})
        except PRODUCT.DoesNotExist:
            return Response({'status': 'bunday id li PRODUCT mavjud emas'})

    def patch(self, request, pk):
        try:
            product = PRODUCT.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({'status': 'serializer is not valid'})
        except PRODUCT.DoesNotExist:
            return Response({'status': 'bunday id li PRODUCT mavjud emas'})

    def delete(self, request, pk):
        product = get_object_or_404(PRODUCT, pk=pk)
        product.delete()
        return Response({'status': 'PRODUCT deleted successfully'})


class ProductUpdateAPIView(APIView):
    def put(self,request,pk):
        try:
            product=PRODUCT.objects.get(pk=pk)
            serializer=ProductSerializer(product,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'status':'serializer is not available'})
        except:
            return Response({'status':'bunday id li contact mavjud emas'})


    def patch(self,request,pk):
        try:
            product=PRODUCT.objects.get(pk=pk)
            serializer=ProductSerializer(product, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)    
            else:
                return Response({'status':'serializer is not available'})
        except:
            return Response({'status':'bunday id li contact mavjud emas'})