from rest_framework.decorators import APIView
from .models import Covid
from .serializer import CovidSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class CovidView(APIView):

    def get(self, request):
        try:
            obj_ = Covid.objects.all()
            if obj_:
                serializer_ = CovidSerializer(obj_, many=True)
                if serializer_:
                    message = "Data Fetch Successfully"
                    return Response({"status": True, "response": serializer_.data, "message": message},
                                    status=HTTP_200_OK)
        except Exception as e:
            return Response(e)
