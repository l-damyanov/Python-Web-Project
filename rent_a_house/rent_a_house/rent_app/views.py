from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from rent_a_house.common.forms import CommentForm
from rent_a_house.rent_a_house_auth.models import RentAHouseUser
from rent_a_house.rent_a_house_profiles.models import Profile
from rent_a_house.rent_app.forms import CreateOffer, EditOffer, DeleteOffer
from rent_a_house.rent_app.models import Offer, Rate


def home_page(req):
    return render(req, 'home_page.html')


def offers(req):
    all_offers = Offer.objects.all()
    paginator = Paginator(all_offers, 12)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'offers': all_offers,
        'page_obj': page_obj,
    }

    return render(req, 'offers.html', context)


@login_required(login_url='sign in')
def my_offers(req):
    all_my_offers = Offer.objects.all()
    user_offers = [o for o in all_my_offers if o.user_id == req.user.id]
    paginator = Paginator(user_offers, 12)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'offers': all_my_offers,
        'user_offers': user_offers,
        'page_obj': page_obj
    }

    return render(req, 'my_offers.html', context)


def offer_details(req, pk):
    offer = Offer.objects.get(pk=pk)
    offer.stars_count = offer.rate_set.count()

    owner = Profile.objects.get(pk=offer.user_id)
    owner_email = RentAHouseUser.objects.get(pk=offer.user_id).email

    is_rated_by_user = offer.rate_set.filter(user_id=req.user.id).exists()

    context = {
        'offer': offer,
        'is_rated': is_rated_by_user,
        'owner': owner,
        'owner_email': owner_email,
        'comment_form': CommentForm(
            initial={
                'offer_id': pk,
            }
        ),
        'comments': offer.comment_set.all(),
    }

    return render(req, 'offer_details.html', context)


@login_required(login_url='sign in')
def my_offer_details(req, pk):
    offer = Offer.objects.get(pk=pk)

    context = {
        'offer': offer,
    }

    return render(req, 'my_offer_details.html', context)


@login_required(login_url='sign in')
def create_offer(req):
    if req.method == 'POST':
        form = CreateOffer(req.POST, req.FILES)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.user = req.user
            offer.save()
            return redirect('home page')
    else:
        form = CreateOffer()

    context = {
        'form': form,
    }

    return render(req, 'create_offer.html', context)


@login_required(login_url='sign in')
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


@login_required(login_url='sign in')
def delete_offer(req, pk):
    offer = Offer.objects.get(pk=pk)
    if req.method == 'POST':
        offer.delete()
        return redirect('home page')
    else:
        form = DeleteOffer(instance=offer)

    context = {
        'form': form,
        'offer': offer,
    }

    return render(req, 'delete_offer.html', context)


@login_required(login_url='sign in')
def rate_offer(req, pk):
    offer = Offer.objects.get(pk=pk)
    rated = offer.rate_set.filter(user_id=req.user.id).first()
    if rated:
        rated.delete()
    else:
        rate = Rate(
            offer=offer,
            user=req.user,
        )
        rate.save()
    return redirect('offer details page', offer.id)


def comment_offer(req, pk):
    form = CommentForm(req.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = req.user
        comment.save()

    return redirect('offer details page', pk)
