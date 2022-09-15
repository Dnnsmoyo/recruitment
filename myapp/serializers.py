from rest_framework import serializers

from .models import Vacancy, Application, Rejected, Accepted
  
class VacancySerializer(serializers.ModelSerializer):
    # Get the image url by serializing `ImageField`

    class Meta:
        # Model to be serialized
        model = Vacancy
        # Fields to bce serialized 
        fields = '__all__'
 
class ApplicationSerializer(serializers.ModelSerializer):
    # Get the image url by serializing `ImageField`


    class Meta:
        # Model to be serialized
        model = Application
        # Fields to be serialized 
        fields = '__all__'
        
  
class RejectedSerializer(serializers.ModelSerializer):
    # Get the image url by serializing `ImageField`


    class Meta:
        # Model to be serialized
        model = Rejected
        # Fields to be serialized 
        fields = '__all__'
        
        
class AcceptedSerializer(serializers.ModelSerializer):
    # Get the image url by serializing `ImageField`


    class Meta:
        # Model to be serialized
        model = Accepted
        # Fields to be serialized 
        fields = '__all__' 
