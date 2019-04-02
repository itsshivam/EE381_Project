from django.conf.urls import url, include
from .views import (
        index,
        data_extract,
        data_save
)

urlpatterns = [
        url(r'^$', index),
        url(r'data_extract/$', data_extract),
        url(r'data_save/$', data_save),
]
