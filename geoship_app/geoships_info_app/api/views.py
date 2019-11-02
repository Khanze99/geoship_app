from rest_framework.views import APIView
from rest_framework.response import Response


class ApiStart(APIView):

    def get(self, request):
        return Response(data={'api/': 'Welocome to service'})
