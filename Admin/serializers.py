from  rest_framework import serializers
from .models import * 


class AdminSRL(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'