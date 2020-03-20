from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.utils.dateparse import parse_datetime
from rest_framework import status, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from .serializers import *
from .permissions import IsAdminUser, IsLoggedInUserOrAdmin


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=True)
    def events(self, request, pk=None):
        events = None
        user = MyUser.objects.get(pk=pk)
        active_start = parse_datetime(request.query_params.get('start', None))
        active_end = parse_datetime(request.query_params.get('end', None))
        print(active_start, active_end)
        if user.user_type == 'TEACHER':
            events = MyUser.objects.get(pk=pk).teacherEvents.filter(start__gte=active_start).filter(end__lte=active_end)
        elif user.user_type == 'STUDENT':
            events = MyUser.objects.get(pk=pk).studentEvents.filter(start__gte=active_start).filter(end__lte=active_end)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        permission_classes = []


class ValidateToken(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class EventList(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            events = None
            if request.user.user_type == 'TEACHER':
                events = request.user.teacherEvents.all()
            elif request.user.user_type == 'STUDENT':
                events = request.user.studentEvents.all()
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class SubjectListByTeacher(APIView):
    def get(self, request, format=None):
        subjects = Subject.objects.filter(user__email=request.query_params.get('teacher_email'))
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)


class TeacherListBySubject(APIView):
    def get(self, request, format=None):
        teachers = MyUser.objects.filter(subject__subject_name=request.query_params.get('subject_name'))
        serializer = MyUserSerializer(teachers, many=True)
        return Response(serializer.data)


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
