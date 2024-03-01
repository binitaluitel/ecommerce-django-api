from django.shortcuts import render
from ecommerce.models import *
from rest_framework.response import Response
from .serializer import *
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def getProduct(request):
    products = product.objects.all()
    serialized_data = ProductSerializer(products,many=True)
    return Response(serialized_data.data)
    

@api_view(['GET'])
def singleProductDetail(request,product_id):
    product1 = product.objects.get(pk=product_id)
    serialized_json = ProductSerializer(product1,many=False)
    return Response(serialized_json.data)

@api_view(['POST'])
def addProduct(request):
    request_data = request.data
    serialized_data = ProductSerializer(data=request_data, many =  False)
    if serialized_data.is_valid(raise_exception=True):
        serialized_data.save()
        return Response({'message':'Product Added  Successfully'})
    
@api_view(['POST'])
def editProduct(request,product_id):
    product1  =  product.objects.get(pk=product_id)
    serialized_data = ProductSerializer(product1,data=request.data, many = False, partial = True)
    if serialized_data.is_valid(raise_exception=True):
        serialized_data.save()
        return Response({'message':'Product Added  Successfully'})
    

@api_view(['GET'])
def deleteProduct(Request,product_id):
    product1 = product.objects.get(pk=product_id)
    product1.delete()
    return Response({'message':'Product Deleted  Successfully'})
