from django.urls import path

from . import views

app_name='beauty'

urlpatterns = [
	path('', views.home, name='home'),
	path('book_time/', views.book_time, name='book_time'),
	path('service/', views.service, name='service'),
	path('product/',views.product,name='product'),
	path('about/',views.about,name='about'),
	path('homelist/',views.homelist,name='homelist'),
]