from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy

from .forms import ArticleForm
from .models import Article

class Index(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    ordering = ['-date']

class DetailArticleView(DetailView):
    model = Article
    template_name = 'blog/blog_post.html'
    context_object_name = 'article'

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('index')

class CreateBlogView(View):
    template_name = 'blog/create_blog.html'

    def get(self, request):
        form = ArticleForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, self.template_name, {'form': form})
