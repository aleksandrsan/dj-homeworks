# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorsSerializer, SensorUpdateSerializer, MeasurementAddSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


    def get(self, request):
        return self.list(request)


    def post(self, request):
        return self.create(request)




class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk):
        serializer = SensorUpdateSerializer(pk, data=request.data, partial=True)
        return serializer.save()

class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementAddSerializer
