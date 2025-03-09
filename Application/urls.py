from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("homepage", views.homepage, name="homepage"),
    path("response", views.response, name="response"),
    path("history_render_category", views.history_render_category, name="history_render_category"),
    path("past_entries/<int:category_id>/", views.past_entries, name="past_entries"),
]