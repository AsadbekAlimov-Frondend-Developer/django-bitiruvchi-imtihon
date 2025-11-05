from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PRODUCT
from .serializers import ProductSerializer


class ProductListAPIView(APIView):
    def get(self, request):
        products = PRODUCT.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductCreateAPIView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            info = {
                'holat': 'Mahsulot muvaffaqiyatli qoshildi',
                'malumot': serializer.data
            }
            return Response(info)
        return Response(serializer.errors)



class ProductDetailView(RetrieveAPIView):
    queryset = PRODUCT.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(DestroyAPIView):
    queryset = PRODUCT.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        product = get_object_or_404(PRODUCT, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)



class ProductUpdateAPIView(APIView):

    def get(self, request, pk):
        product = get_object_or_404(PRODUCT, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(PRODUCT, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'status': 'serializer is not valid'})

    def patch(self, request, pk):
        product = get_object_or_404(PRODUCT, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'status': 'serializer is not valid'})


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
            return Response({'status': 'bunday id li product mavjud emas'})

    def patch(self, request, pk):
        try:
            product = PRODUCT.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({'status': 'serializer is not valid'})
        except PRODUCT.DoesNotExist:
            return Response({'status': 'bunday id li product mavjud emas'})

    def delete(self, request, pk):
        product = get_object_or_404(PRODUCT, pk=pk)
        product.delete()
        return Response({'status': 'product deleted successfully'})
