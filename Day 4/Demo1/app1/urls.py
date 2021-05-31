from django.urls import path, include
from app1.views import HTML_View

urlpatterns = [
    path('Index/',HTML_View),
]
