from django.conf.urls import url
from . import api, onetime
import sys
sys.path.append('../util')
from util.sample_generator import create_world

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('home', onetime.home),
]
# create_world()
# onetime.onetimer()




