# offline ma signup ,signin , and logout no code lakho aema logout fuc nu name logout nai aapvanu km ke ae name alredy used thayelu che
from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]

