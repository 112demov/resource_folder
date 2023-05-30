from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormMixin, FormView
from django.urls import reverse_lazy
from .models import Post, Comment
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView


class PostListView(ListView):
    paginate_by = 5
    model = Post
    template_name = 'home/post_list.html'

    
class PostDetailView(FormView, DetailView):
    model = Post
    template_name = 'home/post_detail.html'
    form_class = CommentForm
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]

        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context
        
        
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.filter(status=True)
        if request.method == 'POST':
            form = CommentForm(data=request.POST)
            if form.is_valid():
                cmt = form.save(commit=False)
                cmt.author = request.user
                cmt.post = post
                cmt.save()
                return redirect('post_detail', pk)
        else:
            form = CommentForm()
        return render(request, 'home/post_detail.html', {'post': post,
                                           'comments': comments,
                                           'cmt': cmt,
                                           'form': form})
    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'home/post_new.html'
    fields = ['title', 'image', 'body']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'home/post_update.html'
    fields = ['title', 'image', 'body']
            
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'home/post_delete.html'
    success_url = reverse_lazy('home')

