from django.conf.urls import url
from . import api, onetime
import sys
sys.path.append('../util')
# from util.sample_generator import create_world

urlpatterns = [
    url('init', api.initialize, name='init'),
    url('move', api.move, name='move'),
    url('say', api.say, name='say'),
    url('home', onetime.home, name='home'),
]
# create_world()
# onetime.onetimer()




