from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.hello_world),    # 127.0.0.1:8000/
    path("api/auth/", include("users.api_urls")),
    path("api/blog/", include("blog.api_urls")),
    path("api/product/", include("product.api_urls")), # 127.0.0.1:8000/api/product/
    path("api/brand/", include("brand.api_urls")), # 127.0.0.1:8000/api/brand/
    path("api/todo/", include("todo.api_urls")),    # 127.0.0.1:8000/api/todo/
    path("todo/", include("todo.urls")),    # 127.0.0.1:8000/todo/
    path("random/template/", views.RandomNumberTemplateView.as_view()),
    path("random/view/", views.RandomNumberView.as_view()),
    # 127.0.0.1:8000/api-auth/login/
    path('api-auth/', include('rest_framework.urls')),
    # path("api-auth/login/", auth_views.LoginView.as_view(), name='login'),
    # 127.0.0.1:8000/api-auth/logout/ -> session flush
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
]
