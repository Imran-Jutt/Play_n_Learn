from django.conf.urls import url

from PlayNLearn import views

urlpatterns = [
    url(r'^$',views.signUp ,name="signUp"),
    url(r'^home',views.home ,name="home"),
]
