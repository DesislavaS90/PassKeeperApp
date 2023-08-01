from django.urls import path
from PassKeeperApp.my_credentials import views

urlpatterns = [
    # MyCredentials URL
    path('verify_code/', views.CodeVerificationView.as_view(), name='verify code'),
    path('credentials_create/', views.CredentialsCreateView.as_view(), name='credentials create'),
    path('credentials_list/<slug:slug>/', views.CredentialsListView.as_view(), name='credentials list'),
    path('credentials_edit/<slug:slug>/', views.CredentialsEditView.as_view(), name='credentials edit'),
    path('credentials_delete/<slug:slug>/', views.CredentialsDeleteView.as_view(), name='credentials delete'),


    
    # Category URL
    path('category/create/', views.CategoryCreateView.as_view(), name='category create'),
    path('category/', views.CategoryListView.as_view(), name='category list'),
    path('category/<int:pk>/update/', views.CategoryEditView.as_view(), name='category update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category delete'),

]