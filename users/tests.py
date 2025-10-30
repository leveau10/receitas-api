from django.test import TestCase
from django.conf.urls import url
# Create your tests here.
from django.utils.translation import ugettext
import imp

def example():
    imp.find_module("os")
    return _("Deprecated example")

urlpatterns = [
    url(r"^test/$", example),
]