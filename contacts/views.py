from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
# Create your views here.


def contact(request):
    if request.method == 'POST':
        # if post, capture the fields, naming is for database table contact
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user has made inquiry already  --only for logged in users !!!--
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        #set to database variable by adding the property values to the model class
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                    phone=phone,message=message, user_id=user_id)
        #save it
        contact.save()

        #send mail  -head, -body, -mail from(settings.py), -mail to list of addresses(cc), -errormessages on or off
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for' + listing + '. Sign in to the admin panel for more info',
            'r.voorsmit@gmail.com',
            [realtor_email, 'renevoorsmit@gmail.com'],
            fail_silently=False

        )
        #return a message --must be recievable in the page where redirect goes--
        messages.success(request, 'Thank you for your request, a realtor will take contact soon')

        #redirect to page of the listing where the inquiry was about 
        return redirect('/listings/'+listing_id)
        #return redirect('/listing/'+listing_id)
        