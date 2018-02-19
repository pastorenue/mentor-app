from django.shortcuts import render
from .models import Subscription
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

def new_subscription(request):
    """
    Creates a newsletter subscription for a user

    ARGS:
        request
    """

    if request.method == "POST":
        params = request.POST
        email = params.get('email')
        name = params.get('name')
        letter_type = params.get('type')
        company = params.get('company')

        subscription = Subscription(
            email=email,
            name=name,
            letter_type=letter_type,
            name_of_company=company
        )

        #Save the subscription to the database
        subscription.save()
        messages.success(request, "Your Newsletter subscription was successfully created. \
                        You can now receive our periodic news digests and business tips")
    return HttpResponseRedirect(reverse('home'))