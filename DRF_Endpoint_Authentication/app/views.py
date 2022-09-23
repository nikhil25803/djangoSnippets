from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework import generics

from . import serializers

class userLogin(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.userLogin(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=202)


class userProfile(generics.RetrieveAPIView):
    serializer_class = serializers.userSerializer

    def get_object(self):
        return self.request.user