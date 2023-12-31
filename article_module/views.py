from django.views.generic.list import ListView
from article_module.models import Article


class ArticlesListView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'article_module/articles_page.html'
