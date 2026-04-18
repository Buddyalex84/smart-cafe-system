from django .urls import path
from home import views



urlpatterns = [
    path('',views.Home,name='Home'),
    path('menu/',views.menu,name='nemu'),
    path('about/',views.About,name='about'),
    path('contact/',views.contact,name='rating'),


]
