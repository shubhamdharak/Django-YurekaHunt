from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog.models import Blog
from .serializer import BlogSerializer

api_url = {
    'List': 'post-list/',
    'Create': 'post-create/',
    'Detail': 'post-detail/<int:id>/',
    'Update': 'post-update/<int:id>/',
    'Delete': 'post-delete/<int:id>/',
}


def api_urls(request):
    return render(request, 'api/doc.html')
    # return Response(api_url, status=status.HTTP_200_OK)

@api_view(['GET',])
def post_list(request):
    blog = Blog.objects.all()
    if request.method== 'GET':
        serializer = BlogSerializer(blog,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET',])
def detail_view(request, slug):
    try:
        blog = get_object_or_404(Blog, id=slug)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method== 'GET':
        serializer = BlogSerializer(blog, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)