from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth import login
from . import serializers

class LoginView(views.APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.UserLoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)



class ProfileView(generics.RetrieveAPIView):
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user