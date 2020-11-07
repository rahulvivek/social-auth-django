from django.urls import path

from .views import FacebookGetPagesAPIView, FacebookPageUpdateAPIView

urlpatterns = [
    path('get_pages/', FacebookGetPagesAPIView.as_view()),
    path('update_page/', FacebookPageUpdateAPIView.as_view()),
]