from  rest_framework import serializers
from .models import * 


class StudentSRL(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class LoginStudent(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "['login', 'password']"

class LoginTeacherSRL(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class GroupSRL(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class HomeWorkSRL(serializers.ModelSerializer):
    class Meta:
        model = HomeWork
        fields = "__all__"


class CoinSRL(serializers.ModelSerializer):
    class Meta:
        model = Coins
        fields = "__all__"


class HackatonSRL(serializers.ModelSerializer):
    class Meta:
        model = Hackaton
        fields = "__all__"

