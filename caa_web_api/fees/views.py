from django.shortcuts import render
from django.views.generic import (TemplateView,)

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
                    print ("Paynow success. Now do other stuff here")
                    amt =str(ut.amount) 
                    student_num = ut.student_number
                    #context['message'] = resp
                    context['message'] = "Your transaction of $" + amt +" was successfully, paid to student number " + student_num + "thank for your payment."
                 
                else:
                    print ("Paynow unsuccessful. Come back to this page later.")
                    context['message'] = "Paynow unsuccessful. Come back to this page later."
                    
        else:
            context['message'] = "Encountered a problem with reference number! - No reference"
        return render(request, self.template_name, context)
