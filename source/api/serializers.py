from rest_framework import serializers
from webapp.models import Image, ImageComment


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageComment
        fields = '__all__'
