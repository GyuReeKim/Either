from django.urls import path
from . import views

app_name = "questions"

urlpatterns = [
    path('', views.index, name="index"),
    # Create
    path('question-create/', views.question_create, name="question_create"),
    path('<int:question_id>/detail/<int:choice_id>/', views.detail, name="detail"),
    path('<int:question_id>/pick-count/<int:pick_num>/', views.pick_count, name="pick_count"),
    path('<int:question_id>/answer-create/<int:choice_id>/', views.answer_create, name="answer_create"),
    # Update
    path('<int:question_id>/question-update/', views.question_update, name="question_update"),
    # Delete
    path('<int:question_id>/question-delete/', views.question_delete, name="question_delete"),
    path('<int:question_id>/answer-delete/<int:choice_id>/', views.answer_delete, name="answer_delete"),
]
