from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('index', views.index, name='index'),
	path('galeria', views.galeria, name='galeria'),
	path('form', views.form, name='form'),
	path('post/new/', views.post_new, name='post_new'),

]
