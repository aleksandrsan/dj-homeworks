from rest_framework import serializers

from .models import Sensor, Measurement



class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorSerializer(serializers.ModelSerializer):

    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'discription', 'measurements']

class SensorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'discription']


class SensorUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['discription']


class MeasurementAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature']

