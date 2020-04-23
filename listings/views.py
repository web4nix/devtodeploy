from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 
from .models import Listing

# Create your views here.


#def index(request):
    #context = { 'name':'REVO' }
#    listings = Listing.objects.all()
#    context = {'listings': listings}
#    return render(request, 'listings/listings.html', context)

def index(request):
    #listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # set number of Listings items from the listings variable
    paginator = Paginator(listings, 3)
    # GET request for a page using get_page()
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    # as context, instead of all listings, only the page requested
    context = {'listings': paged_listings}
    return render(request, 'listings/listings.html', context)



# get the listing data needed from the model
def listing(request, listing_id):
    #listings = Listing.objects.all()
    #context = {'list': listings.id}
    # if go to listing 10 in url show a 404 url
    # also grab the id out of the url (set in urls.py) 
    # pk stands for primary kay
    listing = get_object_or_404(Listing, pk=listing_id) #Return 404 error if no object found
#    other_images = []
    
    # iterate over photo_1 up to but not including photo_7 (doesn't exist)
    # append the url, only if it exists on the object. We get a ValueError
    # if it doesn't. The try/except block helps us mitigate this while
    # still throwing errors for other unexpected problems.
#    for n in range(1, 7):
#        try:
#            other_images.append(getattr(listing, f'photo_{n}').url)
#        except ValueError:
#            continue

    # We should now have a list with a variable length of 1-6 to pass 
    # onto the Django template. Pass it along with the listing in the 
    # context.
    context = {
        'listing': listing,
       # 'other_images': other_images
    }
    return render(request, 'listings/listing.html', context)



def search(request):
    return render(request, 'listings/search.html')
