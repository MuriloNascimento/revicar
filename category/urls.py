from django.conf.urls import patterns, url

from category import views

urlpatterns = patterns('',
  url(r'^$', views.CategoryList.as_view(), name='category_list'),
  url(r'^new$', views.CategoryCreate.as_view(), name='category_new'),
  url(r'^edit/(?P<pk>\d+)$', views.CategoryUpdate.as_view(), name='category_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.CategoryDelete.as_view(), name='category_delete'),
)