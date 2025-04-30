from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(content__icontains=q)
            )
        return queryset
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
