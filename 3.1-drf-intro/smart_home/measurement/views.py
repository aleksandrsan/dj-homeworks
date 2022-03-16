
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorsSerializer, MeasurementSerializer


#GET и POST api/sensors/
class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    #def get(self, request):
    #    return self.list(request)

    #def post(self, request):
    #    return self.create(request)


#GET и PATCH api/sensors/<pk>
class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    #def patch(self, request, pk):
    #    return self.partial_update()


#POST api/measurements/
class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
