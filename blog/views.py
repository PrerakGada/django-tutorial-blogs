from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from blog.forms import ArticleForm
from .models import Article


class Index(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/index.html'
    paginate_by = 1


class Featured(ListView):
    model = Article
    queryset = Article.objects.filter(featured=True).order_by('-date')
    template_name = 'blog/featured.html'
    paginate_by = 1


class DetailArticleView(DetailView):
    model = Article
    template_name = 'blog/blog_post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailArticleView, self).get_context_data(
            *args, **kwargs)
        context['liked_by_user'] = False
        article = Article.objects.get(id=self.kwargs.get('pk'))
        if article.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user'] = True
        return context



class DeleteArticleView(UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        article = Article.objects.get(id=self.kwargs.get('pk'))
        return self.request.user.id == article.author.id


class CreateBlogView(View):
    template_name = 'blog/create_blog.html'  # Create a template for the form

    def get(self, request):
        form = ArticleForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.save()
            return redirect('index')
        return render(request, self.template_name, {'form': form})
