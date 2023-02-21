from django.contrib import admin
from django.urls import path
from .views import helloworldfunction, HelloworldClass

urlpatterns = [
    path("admin/", admin.site.urls),
    path('helloworld/', helloworldfunction),
    path('helloworld2/', HelloworldClass.as_view()),
]