# Create your views here.
from django.shortcuts  import render_to_response
from random import randint
from models import Ticket
from musicshare import models

def all_ticket(request):
    for i in range(1,10):
        new_model= models.Ticket.objects.create(user_id=i,case_number=randint(1000,2000), username='sss')
        new_model.save()
    book_list=Ticket.objects.all()[:10]

    return  render_to_response('list.html',{'book_list':book_list})