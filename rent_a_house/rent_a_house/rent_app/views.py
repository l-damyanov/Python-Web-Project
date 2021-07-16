from django.shortcuts import render, redirect

from rent_a_house.rent_app.forms import CreateOffer, EditOffer
from rent_a_house.rent_app.models import Offer


def home_page(req):
    return render(req, 'home_page.html')


def offers(req):
    all_offers = Offer.objects.all()
    context = {
        'offers': all_offers,
    }

    return render(req, 'offers.html', context)


def my_offers(req):
    all_my_offers = Offer.objects.all()

    context = {
        'offers': all_my_offers,
    }

    return render(req, 'my_offers.html', context)


def offer_details(req, pk):
    offer = Offer.objects.get(pk=pk)

    context = {
        'offer': offer,
    }

    return render(req, 'offer_details.html', context)


def my_offer_details(req, pk):  # TODO pk!
    offer = Offer.objects.get(pk=pk)

    context = {
        'offer': offer,
    }

    return render(req, 'my_offer_details.html', context)


def create_offer(req):
    if req.method == 'POST':
        form = CreateOffer(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateOffer()

    context = {
        'form': form,
    }

    return render(req, 'create_offer.html', context)


def edit_offer(req, pk):
    offer = Offer.objects.get(pk=pk)
    if req.method == 'POST':
        form = EditOffer(req.POST, req.FILES, instance=offer)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateOffer(instance=offer)

    context = {
        'form': form,
        'offer': offer,
    }

    return render(req, 'edit_offer.html', context)


def profile(req):
    return render(req, 'profile.html')
