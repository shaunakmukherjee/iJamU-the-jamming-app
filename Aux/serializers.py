from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False, allow_blank=True, max_length=100)
    password = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance