from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import (
    TemplateView,
    DeleteView,
    UpdateView,
    CreateView,
    ListView,
    DetailView,
)
from news.models import Category, News
from news.forms import NewsCreateForm
# Create your views here.

class CategoryNewsView(View):
    def get(self, request, category_id, *args, **kwargs):
        template_name="news/categories.html"
        #category = Category.objects.get(pk=category_id)
        category = get_object_or_404(Category, pk=category_id)
        category_news_list= News.objects.filter(category=category)
        #catergory key from model.py
        return render(request, template_name, {"category_news_list": category_news_list, "category": category})

# class CategoryNewsView(ListView):
#     model = News
    #context_object_name = 'category_news_list'
    #template_name = 'news/categories.html'


    
#     pass

class NewsTemplateView(TemplateView):
     template_name = "index.html"

     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         categories = Category.objects.all()
         category_news_list = {}
         for category in categories:
             # context[category.title] = News.objects.filter(category=category)
             category_news_list[category] = News.objects.filter(category=category)
         context["news_list"] = News.objects.all().order_by("-created_at")[:4]
         context["trending_news"] = News.objects.order_by("-count")
         context["category_news_list"] = category_news_list
         return context

class NewsDetail(DetailView):
     model = News
     template_name = "news/single_news.html"
     context_object_name = "detail_news"

     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         self.object.count = self.object.count + 1
         self.object.save()
         context["popular_news"] = News.objects.order_by("-count")[:4]
         return context

class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    template_name = "news/create.html"
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("home")
    form_class = NewsCreateForm

    def form_valid(self, form):
        news = form.save(commit=False)
        title = form.cleaned_data["title"]
        slug = slugify(title)
        news.slug = slug
        news.author = self.request.user
        news.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    template_name = "news/update.html"
    fields = "title", "content", "cover_image", "category"
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("home")


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        return self.post(self, request, *args, **kwargs)
    

# class Comments(models.Model):
#     comment = models.TextField()
#     date = models.DateTimeField(default=timezone.now)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)

#     def _article(request, article_id):
#         try:
#             article = Article.objects.get(pk=article_id)
#             related_articles = Article.objects.filter(tags=article.tags).exclude(pk=article.pk)[:4]
#             context['article'] = article
#             context['related_articles'] = related_articles
#             context['form'] = CommentForm()
#             if request.method == 'POST':
#                 form = CommentForm(request.POST)
#                 if form.is_valid():
#                     comment = form.cleaned_data['comment']
#                     article.comments_set.create(comment=comment)
#             return render(request,'blog/article.html', context)
# except Exception as e:
#     #write error to file
#     return render(request,'blog/404.html')