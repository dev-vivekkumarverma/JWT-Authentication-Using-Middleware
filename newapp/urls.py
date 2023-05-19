from django.urls import path
from .views import authentication_view,say_hello
urlpatterns = [
    path('auth/',authentication_view,name="authentication_url"),
    path("resp/",say_hello,name="say_hello"),
]
