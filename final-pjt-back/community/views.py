from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import ReviewSerializer, CommentSerializer
from .models import Comment, Review

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def reviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def review_create(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_update_or_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        if not request.user.review_set.filter(pk=review_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        if not request.user.review_set.filter(pk=review_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        review.delete()
        return Response({'id':review_pk},status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST'])
def comment_create(request, review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    if request.method == 'GET':
        comments = review.comment_set.order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT','DELETE'])    
def comment_update_or_delete(request, comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
    if request.method == 'DELETE':
        comment.delete()
        return Response({'id':comment_pk},status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)