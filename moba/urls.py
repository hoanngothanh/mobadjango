from django.conf.urls import url
from moba import views

urlpatterns = [
    url(r'^herolist/$', views.HeroListList.as_view(),
        name=views.HeroListList.name),
    url(r'^herolist/(?P<hero_id>.+)/$', views.HeroListDetail.as_view(),
        name=views.HeroListDetail.name),
    url(r'^hero/$', views.HeroListView.as_view(),
        name=views.HeroListView.name),
    url(r'^hero/(?P<hero_id>.+)/$', views.HeroDetailView.as_view(),
        name=views.HeroDetailView.name),
    url(r'^ability/$', views.AbilityListView.as_view(),
        name=views.AbilityListView.name),
    url(r'^ability/(?P<hero_id>.+)/$', views.AbilityOfHeroView.as_view(),
        name=views.AbilityOfHeroView.name),
    url(r'^dcm/$', views.DamagaCooldownManaView.as_view(),
        name=views.DamagaCooldownManaView.name),
    url(r'^dcm/(?P<hero_id>.+)/$', views.DcmOfHeroView.as_view(),
        name=views.DcmOfHeroView.name),
    url(r'^hero-item/$', views.HeroItemView.as_view(),
        name=views.HeroItemView.name),
    url(r'^hero-items/(?P<id>.+)/$', views.HeroItemListView.as_view(),
        name=views.HeroItemListView.name),
]
