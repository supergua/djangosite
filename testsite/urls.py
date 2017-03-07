from django.conf.urls import url
from testsite import views

app_name = 'testsite'
urlpatterns = [
    url(r'^$', views.home, name='home'),
]
