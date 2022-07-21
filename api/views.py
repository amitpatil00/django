from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
from .serializers import RegisterSerializer

from django.contrib.auth.models import User

from myproject.api import serializers


class RegisterAPI(APIView):

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
            }    , status.HTTP_402_BAD_REQUEST)

        serializer.save()

        return Response({'status': True, 'message':'user created'})


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)