from django.urls import path
from PassKeeperApp.my_credentials import views

urlpatterns = [
    # MyCredentials URL
    path('verify_code/', views.CodeVerificationView.as_view(), name='verify code'),
    path('credentials_create/', views.CredentialsCreateView.as_view(), name='create credentials'),
    path('credentials_list/', views.CredentialsListView.as_view(), name='list credentials'),
    path('credentials_edit/<slug:slug>/', views.CredentialsEditView.as_view(), name='edit credentials'),
    path('credentials_delete/<slug:slug>/', views.CredentialsDeleteView.as_view(), name='delete credentials'),


    
    # Category URL
    path('category/create/', views.CategoryCreateView.as_view(), name='create category'),
    path('category/<int:pk>/update/', views.CategoryEditView.as_view(), name='update category'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='delete category'),

]