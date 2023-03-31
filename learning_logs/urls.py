"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # When Django examines a requested URL, this pattern
    # will match any URL that has the base URL followed by topics.

    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    path('new_topic/', views.new_topic, name='new_topic'),
]

