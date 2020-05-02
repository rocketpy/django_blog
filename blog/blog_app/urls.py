from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('languages', views.LanguageView)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', include(router.urls))
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

"""
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
"""
