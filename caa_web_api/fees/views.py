from django.shortcuts import render
from django.views.generic import (TemplateView,ListView)
from .models import Transaction
import json
import requests
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# displays payment form
class PayFeesView(TemplateView):
    template_name = 'fees/make_payment.html'
    
    def get(self, request, node=False):
        """ context manipulation """
        context = self.get_context_data()
        return render(request, self.template_name, context)

# displays results
class PayFeesReturnView(TemplateView):
    template_name = 'fees/payment_result.html'

    def get(self, request, node=False):
        """ context manipulation """
        context = self.get_context_data()
        if "reference" in request.GET:
            reference = request.GET["reference"]
            try:
                ut = Transaction.objects.get(reference=reference)
            except:
                context['message'] = "Encountered a problem with reference number! - No transaction"
            else:
                # context['payload'] = ut

                if ut.status:
                    print ("Paynow success. Now do caa stuff here")
                    amt =str(ut.amount) 
                    student_num = ut.student_number
                    date_of_transaction =str(ut.date)

                    headers = {
                        'content-type': 'application/json'
                    }
                    payload = {
                        "username": ut.email,
                        "fullname": ut.fullname,
                        "student_number": student_num ,
                        "date_of_transaction": date_of_transaction,
                        "reference_number": ut.reference,
                        "amount": amt,
                        "requesting_number": ut.requesting_number 
                    }
                    url = 'http://127.0.0.1:8000/pastel/update/'
                    r = requests.post(url, data=json.dumps(payload),headers=headers)
                    r1 = json.loads(r.content)
                    print(r1)
                      #context['message'] = resp
                    context['message'] = "Your transaction of $" + "<b>" + amt + "</b>" + " was successfully, paid to your CAA account " +"<b>" + student_num + "</b> " +" thank you for your payment."
                 
                else:
                    print ("Paynow unsuccessful. Come back to this page later.")
                    context['message'] = "Paynow unsuccessful. Come back to this page later."
                    
        else:
            context['message'] = "Encountered a problem with reference number! - No reference"
        return render(request, self.template_name, context)

class TransactionListView(LoginRequiredMixin,ListView):

    """ displaying a list of transactions """
    model = Transaction
    context_object_name = 'payment_list'
    template_name='fees/payments_list.html'

    def get_queryset(self, **kwargs):
        return Transaction.objects.all()  
