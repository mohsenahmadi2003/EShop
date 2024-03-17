from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from article_module.models import Article


def all_articles(request: HttpRequest):
    return render(request, 'admin_panel/articles_list.html')


class ArticlesListView(ListView):
    model = Article
    paginate_by = 12
    template_name = 'admin_panel/articles_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query
