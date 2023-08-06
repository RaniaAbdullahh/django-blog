from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from .models import Post,Category
from .forms import CommentForm
from django.db.models import Q
# Create your views here.


class PostListView(ListView):
    template_name = 'core/frontpage.html'
    # model = Post
    queryset = Post.objects.filter(status = Post.ACTIVE)
    context_object_name ='posts'


class PostDetailView(DetailView):
    
    def get(self, request, *args, **kwargs):
        context = {}
        print(request.user)
        print(kwargs)
        slug = kwargs.get('slug','no such slug ')
        # post = Post.objects.filter(slug=slug)
        post = get_object_or_404(Post,slug=slug,status=Post.ACTIVE  )
        # print(123,post[0])
        form = CommentForm()
        context['post'] = post
        context['form' ]= form

        return render(request, 'blog/post_detail.html',context)
    

    def post(self, request, *args, **kwargs):

        slug = kwargs.get('slug','no such slug ')
        category_slug = kwargs.get('category_slug','no such slug ')
        post = get_object_or_404(Post,slug=slug)

        form= CommentForm(request.POST)
        if form.is_valid():
           comment = form.save(commit=False)
           comment.post = post
           comment.save()

           return redirect('post_detail',category_slug=category_slug,slug=slug)


# category veiw (function bases)

def category(request,slug):
    category = get_object_or_404(Category,slug=slug)
    posts = category.posts.filter(status= Post.ACTIVE)

    return render(request,'blog/category.html',{'posts':posts,'category':category})


   
def search(request):
   query = request.GET.get('query','')
   posts = Post.objects.filter(status= Post.ACTIVE).filter(Q(title__icontains=query)|Q(body__icontains=query)|Q(intro__icontains=query))

   return render(request, 'blog/search.html',{'posts':posts, 'query':query})