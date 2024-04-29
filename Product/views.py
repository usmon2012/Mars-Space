from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializers import *


class ProductView(APIView):
    def post(self, request):
        serializers = ProductSRL(data=request.data)
        if serializers.is_valid(serializers.save()):
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
         

class ProductEditView(APIView):
    def get(self, request, id):
        product = Product.objects.filter(id=id).first()
        if product:
            serializers = ProductSRL(product, many = True)
            return Response(serializers.data)
        else:
            return Response("Bunday maxsulot topilmadi")


class UpdateView(APIView):
    def patch(self, request, id):
        product = Product.objects.filter(id = id).first()
        if product:
            serializers = ProductSRL(instance=product ,data=request.data, partial = True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        else:
            return Response("Bunday maxsulot topilmadi")
        


class DeleteView(APIView):
    def delete(self, request, id):
        product = Product.objects.filter(id = id).first()
        if product:
           product.delete()
           return Response('ochirildi')
        else:
            return Response('Bunday maxsulot topilmadi')
        

class GetAllView(APIView):
    def get(self,request):
        product = Product.objects.all()
        if product:
            serializers = ProductSRL()
       