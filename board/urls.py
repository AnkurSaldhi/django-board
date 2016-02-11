from django.conf.urls import url

from board import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^addboard$', views.add_board, name='add_board'),
	url(r'^login/$', views.Login, name='login'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^updatetask/(?P<task_id>[0-9]+)/$', views.update_task, name='updatetask'),]