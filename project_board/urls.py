"""project_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import app_board.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_board.views.home, name="home"),
    path('board/<int:post_id>', app_board.views.detail, name="detail"), #<type:name>
    path('board/new', app_board.views.new, name="new"),
    # create.html을 호출하라는 게 아니라 create함수를 호출하라는 걸로 받아들이자
    path('board/create/', app_board.views.create, name="create"),
    path('board/<int:post_id>/delete/', app_board.views.delete, name="delete"),
    path('board/<int:post_id>/edit/', app_board.views.edit, name="edit"),
    path('board/<int:post_id>/update/', app_board.views.update, name="update"),
]
