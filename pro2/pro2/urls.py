from django.contrib import admin
from django.urls import path
from . import view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.index, name = 'index'),
    path('analyze', view.analyze, name = 'analyze'),
    path('contact', view.contact, name = 'contact'),
    path('about', view.about, name = 'about'),
]
