from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomeList, 
    create,
    detail_blog,
    search,
    upvotes,
    postComment,
    about,
    contact,
)

urlpatterns = [
    path("", HomeList.as_view(), name='home'),
    path('blog/create/', create, name="create"),
    path("blog/<slug:slug>/", detail_blog, name="detail"),
    path('blog/upvotes',upvotes, name='upvotes'),
    path("blog/post-comment/<int:pk>",postComment, name="post-comment" ),
    path("search", search, name='search'),

    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
