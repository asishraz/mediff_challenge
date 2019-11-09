from django.conf.urls import url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import add_record, show_records

router = DefaultRouter()
urlpatterns = router.urls
urlpatterns.append(url(r'insert-record', add_record))
urlpatterns.append(url(r'show-records', show_records))
