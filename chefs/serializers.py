from rest_framework import serializers
from .models import Chef, Cooker, Assistantcook

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = '__all__'

class CookerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooker
        fields = '__all__'

class AssistantcookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assistantcook
        fields = '__all__'