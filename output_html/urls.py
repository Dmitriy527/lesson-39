from django.urls import path

from output_html.views import page

urlpatterns = [
    path('', page, name='page'),
]