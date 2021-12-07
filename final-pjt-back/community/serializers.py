from rest_framework import serializers
from .models import Review,Comment


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user',)
        depth = 1
        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user','review','created_at','updated_at')
        depth = 1
