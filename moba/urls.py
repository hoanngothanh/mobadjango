from django.conf.urls import url
from moba import views

urlpatterns = [
    url(r'^herolist/$', views.HeroListList.as_view(),
        name=views.HeroListList.name),

]
