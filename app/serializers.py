from rest_framework import serializers
from .models import Books, Authors, Publishers, Users


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Books


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Authors


class PublishersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Publishers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Users
