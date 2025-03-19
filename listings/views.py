from django.shortcuts import render, get_object_or_404
# 3-5
from . models import Listing  # . current directory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F
from listings.choices import price_choices, bedroom_choices, district_choices

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

    # Q object
    # listings = Listing.objects.filter(Q(district='tst')|Q(district='mk'))

    # F object
    # listings = Listing.objects.filter(district=F('address'))

    # 2025-3-6
    paginator = Paginator(listings, 3)  # 3 record in 1 page
    page = request.GET.get('page')   # GET htpp:GET method. get fcn() obtain the page number
    paged_listings = paginator.get_page(page)
    context = {'listings': paged_listings }   # import paged_listings to template eng and assigned to variable context
    #
    return render(request, 'listings/listings.html', context )

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title__icontains=title)

    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            queryset_list = queryset_list.filter(district__iexact=district)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            price = int(price)
            queryset_list = queryset_list.filter(price__lte=price)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    paginator = Paginator(queryset_list, 3)  # 3 record in 1 page
    page = request.GET.get('page')   # GET htpp:GET method. get fcn() obtain the page number
    paged_listings = paginator.get_page(page)
    values = request.GET.copy()
    if 'page' in values:
        del values["page"]

    context = {
        'price_choices': price_choices,
        'district_choices': district_choices,
        'bedroom_choices': bedroom_choices,
        'listings': paged_listings,
        'values': values
    }
    return render(request, 'listings/search.html', context)
    