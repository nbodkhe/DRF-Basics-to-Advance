from django.forms.models import model_to_dict
from products.models import Product
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # instance = serializer.save()
            # print(instance)
            print(serializer.data)
            return Response(serializer.data)