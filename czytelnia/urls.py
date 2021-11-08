"""czytelnia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from ninja.renderers import BaseRenderer

import orjson
import yaml

from book.api import api as book_router
from comment.api import api as comment_router
from user.api import api as user_router
from .views import index

class MyRenderer(BaseRenderer):
    media_type = "text/plain"

    def render(self, request, data, *, response_status):
        if 'yaml' in request.headers['Content-Type']:
            return yaml.dump(data)
        else:
            return orjson.dumps(data)

api = NinjaAPI(renderer=MyRenderer())
api.add_router("books/", book_router)
api.add_router("comments/", comment_router)
api.add_router("users/", user_router)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path("api/", api.urls),
    #path('books/', include('book.urls'))
]
