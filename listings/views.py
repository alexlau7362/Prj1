from django.shortcuts import render
# 3-5
from . models import Listing  # . current directory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def listings(request):
    # add 2025-3-5 get all Listing records in the table
    #
    # query set not execute until for loop using in template eng.
    # listings = Listing.objects.filter()   query set  
    # listings = Listing.objects.filter().exist()   check for non-empty query set (API)  
    #listings = Listing.objects.all() 
    # listings = Listing.objects.get() not a query set
    # -ve latest input record display first
    # filter is_published is a parameter, order_by is query set
    # query set
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # 2025-3-6
    paginator = Paginator(listings, 3)  # 3 record in 1 page
    page = request.GET.get('page')   # GET htpp:GET method. get fcn() obtain the page number
    paged_listings = paginator.get_page(page)
    context = {'listings': paged_listings }   # import paged_listings to template eng and assigned to variable context
    #
    return render(request, 'listings/listings.html', context )

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
    