from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [
                  path('', views.ArticlesListView.as_view(), name='articles_list'),
                  path('cat/<str:category>', views.ArticlesListView.as_view(), name='articles_by_category_list'),
                  path('<pk>/', views.ArticleDetailView.as_view(), name='articles_detail'),
                  path('add-article-comment', views.add_article_comment, name='add_article_comment'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
