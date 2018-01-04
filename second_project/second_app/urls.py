from django.conf.urls import url
from second_app import views

app_name = 'second_app'

urlpatterns = [
    #url(r'^users/', views.users,name='users'),
    #url(r'^register/', views.user_register, name='user_register'),
    url(r'^home/', views.home,name='home'),
    url(r'^formname', views.form_name_view, name = 'form_name_view'),
    url(r'^base/', views.base, name = 'base'),
    url(r'^base2/', views.base2, name = 'base2'),
    url(r'^other/', views.other, name = 'other'),
    url(r'^second_base/', views.second_base, name = 'second_base'),
    url(r'^second_register/', views.second_register, name = 'second_register'),
    url(r'^second_index/', views.second_index, name = 'second_index'),
    url(r'^user_login/', views.user_login, name = 'user_login')
]
