from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
import datetime
from rest_framework import generics

class RegisterView(APIView):
    def post(self, request):
        serializer = StudentSRL(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class LoginView(APIView):       
    def post(self,request):
        login = request.data.get('login')
        parol = request.data.get('password')
        student = Student.objects.filter(login=login,password=parol).first()
        if student:
            return Response("login togri")
        else:
            return Response("student topilmadi")
        


class RegisterTeacherView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginTeacherSRL(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class LoginTeacherView(APIView):
    def post(self, request, *args, **kwargs):
        login = request.data.get('login')
        password = request.data.get('password')
        user = Teacher.objects.filter(login = login, password = password).first()
        if user:
            return Response('success')
        else:
            return Response('fail')



class CreateGroupView(APIView):
    def post(self, request):
        serializers = GroupSRL(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
        

    def get(self,request):
        groups = Group.objects.all()
        if groups:
            serializers = GroupSRL(groups, many=True)
            return Response(serializers.data)
        else:
            return Response('SORY NOT GROUP CRATE SAM')
        

class EditGroupView(APIView):
    def get(self, request, id):
        group = Group.objects.filter(id=id).first()
        if group:
            serializers = GroupSRL(group)
            return Response(serializers.data)
        else:
            return Response('SORRY error')
        

    def patch(self, request, id):
        group = Group.objects.filter(id=id).first()
        if group:
            serializers = GroupSRL(instance= group,data= request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        else:
            return Response('SORRY GROUP NOT FOUND!')
        

    def delete(self, request, id):
        group = Group.objects.filter(id=id).first()
        if group: 
            group.delete()
            return Response('GROUP DELETED!')
        else:
            return Response('SORRY GROUP NOT FOUND!')


class HomeWorkView(APIView):
    def post (self, request):
        serializers = HomeWorkSRL(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
        

    def get(self, request):
        homework = HomeWork.objects.all()
        if homework:
            serializers = HomeWorkSRL(homework, many = True)
            return Response(serializers.data)
        else:
            return Response('No Homework found')


class HomeWorkEditView(APIView):
    def get(self, request, id):
        homework = HomeWork.objects.filter(id=id).first()
        if homework:
            serializers = HomeWorkSRL(homework)
            return Response(serializers.data)
        else:
            return Response('No Homework found')
        

    def delete(self, request, id):
        homework = HomeWork.objects.filter(id=id).first()
        if homework: 
            homework.delete()
            return Response('HOMEWORK DELETED!')
        else:
            return Response('SORRY HOMEWORK NOT FOUND!')


    def post(self, request, id):
        homework = HomeWork.objects.filter(id=id).first()
        if homework:
            homework.file = request.data.get('file')
            diedline = int(homework.time) + 3
            if homework.time <= datetime.datetime.today and datetime.datetime.today <= diedline:
                homework.save()
                return Response('Uploaded')
            else:
                return Response('Chopildi, Vaqtida yuklash kerefi!')
        else:
            return Response('SORRY HomeWork NOT FOUND!')
        


class PostCoinView(APIView):
    def post(self, request):
        serializers = CoinSRL(data=request.data)
        id = request.data.get('student')
        coins = request.data.get('coins')
        student = Student.objects.filter(id=id).first()
        if student:
            if serializers.is_valid():
                student.coin += coins
                student.save()
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        


class HackatonView(generics.CreateAPIView):
    serializers_class = HackatonSRL
    queryset = Hackaton.objects.all()
    

class HackatonGetView(generics.ListAPIView):
    serializers_class = HackatonSRL
    queryset = Hackaton.objects.all()


class EditHackatonView(generics.RetrieveUpdateDestroyAPIView):
    serializers_class = HackatonSRL
    queryset = Hackaton.objects.filter(id=id).first()