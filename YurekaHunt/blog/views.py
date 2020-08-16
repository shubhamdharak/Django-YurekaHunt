from django.urls import reverse
from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.views.generic import ( 
    ListView,
    DetailView,
    CreateView,
)

from .models import Blog, BlogComment
from .forms import BlogForm, contactForm

class HomeList(ListView):
    paginate_by = 3
    model = Blog
    context_object_name = "blogs"   # if name not given then render as object_list in html
    template_name = "blog/home.html"
    
def detail_blog(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    comment = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict ={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    
    context = {
        "object" : post,
        "comment": comment,
        "reply": replyDict,
    }
    return render(request, 'blog/blog_detail.html', context)

@login_required(login_url="/account/login/")
def create(request):
    form = BlogForm()
    if request.method=="POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {
                "form":form,
                "success":"Your Hunt is NOW Live."
            }
            return render(request,'blog/blog_create.html', context)
    return render(request, 'blog/blog_create.html', {"form":form})

def search(request):
    q = request.GET['search']
    body = Blog.objects.filter(body__icontains=q)
    title = Blog.objects.filter(title__icontains=q)
    queryset = body.union(title)
    return render(request,"blog/search.html", context={'blogs': queryset})

@login_required(login_url="/account/login")
def postComment(request, pk):
    if request.method=="POST":
        comment = request.POST.get('postC')
        user = request.user
        post = get_object_or_404(Blog, id=pk)
        parentNo = request.POST.get('parent')
        if parentNo=="":
            commit = BlogComment(comment=comment,post=post,user=user)
            commit.save()
        else:
            parent = BlogComment.objects.get(sno=parentNo) 
            commit = BlogComment(comment=comment,post=post,user=user, parent=parent)
            commit.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# @login_required(login_url="/account/login/")
def upvotes(request):
    if request.method =='GET':
        post_id = request.GET['post_id']
        post = Blog.objects.get(id=post_id)
        post.upvote +=1
        post.save() 
     
        data = {
            "success":"success",
            "upvote":post.upvote
        }
        return JsonResponse(data)

def about(request):
    return render(request, "blog/about.html")

def contact(request):
    form = contactForm()
    if request.method=="POST":
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            form = contactForm()
            return render(request,'blog/contact.html',{"form":form, "success": "Thank You for contact us. We will inform you shortly !"})
        else:
            return render(request,'blog/contact.html',{"form":form, "error": "Something went wrong!"})

    return render(request, "blog/contact.html",{"form":form})

# class BlogDetailView(DetailView):
#     template_name = 'blog/blog_detail.html'
#     # queryset = BlogComment.objects.all()
#     def get_object(self):
#         id_ = self.kwargs.get('slug')
#         return get_object_or_404(Blog, slug=id_) 
    
 
    # def get_context_data(self, **kwargs): 
    #     context = super().get_context_data(**kwargs)                      
    #     context["comment"] = BlogComment.objects.filter(post=post)
    #     print(context['comment'])
    #     return context
