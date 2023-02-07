from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

@api_view(['GET'])
def index (request):
    date=datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    message='server is live at:'
    return Response(data=message+date ,status=status.HTTP_200_OK)
