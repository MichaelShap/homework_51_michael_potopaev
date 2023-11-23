from django.urls import path
from webapp.views import main_view, cat_view

urlpatterns = [
    path('', main_view),
    path('cat_stats/', cat_view)
]