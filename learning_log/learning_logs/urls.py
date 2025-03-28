"""Defines URL patterns for learning_logs."""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "learning_logs"
urlpatterns = [
    # Home page.
    path("", views.index, name="index"),
    # Login page.
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    # Show all topics.
    path("topics/", views.topics, name="topics"),
    # Detail page for a single topic.
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    # Page for adding a new topic.
    path("new_topic/", views.new_topic, name="new_topic"),
    # Page for adding a new entry.
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
    # Page for editing an entry.
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
]
