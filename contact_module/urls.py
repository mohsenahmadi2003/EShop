from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.ContactUsView.as_view(), name='contact_us_page'),
                  path('create-profile/', views.CreateProfileView.as_view(), name='create_profile_page'),
                  path('profiles/', views.ProfilesView.as_view(), name='profiles_page'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
