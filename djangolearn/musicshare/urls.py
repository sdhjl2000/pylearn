from django.conf.urls.defaults import *
from models import Ticket
from musicshare import views

info_dict = {
    'queryset': Ticket.objects.all()
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^all/$',views.all_ticket),
    (r'^new/$', 'django.views.generic.create_update.create_object', { 'model': Ticket } ),
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
)