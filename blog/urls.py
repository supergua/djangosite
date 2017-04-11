from django.conf.urls import url
from blog import views as blog_views

app_name = 'blog'

urlpatterns = [
    url(r'^$', blog_views.index, name='index'),
    ]