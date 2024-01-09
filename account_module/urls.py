from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('register/', views.RegisterView.as_view(), name='register_page'),
                  path('login/', views.LoginView.as_view(), name='login_page'),
                  path('logout/', views.LogoutView.as_view(), name='logout_page'),
                  path('forget-pass/', views.ForgetPasswordView.as_view(), name='forget_password_page'),
                  path('reset-pass/<active_code>/', views.ResetPasswordView.as_view(), name='reset_password_page'),
                  path('activate-account/<email_active_code>/', views.ActivateAccountView.as_view(),
                       name='activate_account'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
