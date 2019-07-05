from django.urls import path
import app_board.views

urlpatterns = [
    path('<int:post_id>', app_board.views.detail, name="detail"), #<type:name>
    path('new/', app_board.views.new, name="new"),
    # create.html을 호출하라는 게 아니라 create함수를 호출하라는 걸로 받아들이자
    path('create/', app_board.views.create, name="create"),
    path('<int:post_id>/delete/', app_board.views.delete, name="delete"),
    path('<int:post_id>/edit/', app_board.views.edit, name="edit"),
    path('<int:post_id>/update/', app_board.views.update, name="update"),
]