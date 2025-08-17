from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'stocks'

urlpatterns = [
    # Stock URLs
    path('', views.stock_list, name='stock_list'),

    # User Authentication URLs
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='stocks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='stocks:stock_list'), name='logout'),

    # Stock detail
    path("<str:symbol>/", views.stock_detail, name="stock_detail"),
]
