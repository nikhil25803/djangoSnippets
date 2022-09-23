from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User

class userLogin(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attribute):
        username = attribute.get('username')
        password = attribute.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'Wrong Credentials'
                raise serializers.ValidationError(msg, code='authorization')

        attribute['user'] = user
        return attribute




class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]