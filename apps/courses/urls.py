from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add),
    url(r'^remove_confirm/(?P<course_id>\d+)$', views.remove_confirm),
    url(r'^remove_course/(?P<course_id>\d+)$', views.remove_course)
    # url(r'^reset$', views.reset)

]
