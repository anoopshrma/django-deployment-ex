from django.conf.urls import url
from app_two import views
app_name='app_two'
urlpatterns = [
    url(r'^userlogin/',views.user_login,name='login'), 
    url(r'^register/',views.register,name='register'),
    url(r'^formpage/',views.forminfo,name='forminfo'),
    url(r'^user/',views.userinfo,name='userinfo'),
    url(r'^$',views.index,name='index'),
]