from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
from .models import Vacancy, Application, Rejected, Accepted
from .serializers import VacancySerializer, RejectedSerializer, AcceptedSerializer, ApplicationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated  # <-- Here
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


class VacancyDetailView(DetailView):
    # specify the model to use
    model = Vacancy
 
class ApplicationDetailView(DetailView):
    # specify the model to use
    model = Application
   
class ApplicationCreateView(CreateView):
    model = Application
    fields = '__all__'
    
class VacancyCreateView(CreateView):
    model = Vacancy
    fields = '__all__'
    
def admin_panel(request):
   
   return render(request,'myapp/admin_panel.html')
   
class UserCreate(CreateView):
   
    # specify the model for create view
    model = User
    success_url='/'
  
    # specify the fields to be displayed
  
    fields = ['username','first_name','last_name','email','password']
    
def index(request):
    return render(request,'index.html')

class VacancyDetailView(DetailView):
    # specicyfy the model to use
    model = Vacancy

class ApplicationDetailView(DetailView):
    # specify the model to use
    model = Application

class VacancyList(APIView):
    #permission_classes = (IsAuthenticated,)             # <-- And here

    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        vacs = Vacancy.objects.all()
        serializer = VacancySerializer(vacs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class VacancyDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Vacancy.objects.get(pk=pk)
        except Vacancy.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vac = self.get_object(pk)
        serializer = VacancySerializer(vac)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        vac = self.get_object(pk)
        serializer = VacancySerializer(vac, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vac = self.get_object(pk)
        vac.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApplicationList(APIView):
    #permission_classes = (IsAuthenticated,)             # <-- And here

    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        apps = Application.objects.all()
        serializer = ApplicationSerializer(apps, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ApplicationDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Application.objects.get(pk=pk)
        except Application.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        application = self.get_object(pk)
        serializer = ApplicationSerializer(application)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        application = self.get_object(pk)
        serializer = ApplicationSerializer(application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        application = self.get_object(pk)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
        

class AcceptedList(APIView):
    #permission_classes = (IsAuthenticated,)             # <-- And here

    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        acc = Accepted.objects.all()
        serializer = VacancySerializer(acc, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AcceptedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class AcceptedDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Accepted.objects.get(pk=pk)
        except Accepted.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        acc = self.get_object(pk)
        serializer = AcceptedSerializer(acc)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        acc = self.get_object(pk)
        serializer = AcceptedSerializer(acc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        acc = self.get_object(pk)
        acc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form': form})

class RejectedList(APIView):
    #permission_classes = (IsAuthenticated,)             # <-- And here

    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        rej = Rejected.objects.all()
        serializer = RejectedSerializer(rej, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RejectedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class RejectedDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Rejected.objects.get(pk=pk)
        except Rejected.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        rej = self.get_object(pk)
        serializer = RejectedSerializer(rej)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        rej = self.get_object(pk)
        serializer = RejectedSerializer(acc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        rej = self.get_object(pk)
        rej.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


