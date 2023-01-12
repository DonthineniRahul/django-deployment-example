from django.conf.urls import url
from django.urls import path
from virat import views


app_name = "virat"

urlpatterns=[
		
	path('kohli/',views.kohli,name='kohli'),
	path('forms/',views.index,name='forms'),
	path('user_login',views.user_login,name='login'),

]