from django.urls import path
from website.views import *
urlpatterns = [
    path('', index_page),
    path('my-accont/', account_page),
    path('contact/', contact_page)
]
