from dataclasses import field
from rest_framework import serializers
from base.models import Item
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        
        if data['username']:
            if User.objects.filter(username = data['username'].exists()):
                raise serializers.ValidationError('username is taken')


        if data['email']:
            if User.objects.filter(username = data['email'].exists()):
                raise serializers.ValidationError('email is taken')
