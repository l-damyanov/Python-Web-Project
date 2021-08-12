from django.contrib.auth import get_user
from django.shortcuts import render, redirect

from rent_a_house.rent_a_house_profiles.forms import ProfileEditForm, ProfileDeleteForm
from rent_a_house.rent_a_house_profiles.models import Profile
from rent_a_house.rent_app.models import Offer


def profile(req):
    my_offers_count = len([o for o in Offer.objects.all() if o.user_id == get_user(req).id])

    context = {
        'my_offers_count': my_offers_count,
    }

    return render(req, 'profile.html', context)


def edit_profile(req):
    user_profile = Profile.objects.get(pk=req.user.id)
    if req.method == 'POST':
        form = ProfileEditForm(req.POST, req.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')
    else:
        form = ProfileEditForm(instance=user_profile)

    context = {
        'form': form,
    }
    return render(req, 'edit_profile.html', context)


def delete_profile(req):
    user_profile = Profile.objects.get(pk=req.user.id)
    user = get_user(req)
    if req.method == 'POST':
        user.delete()
        return redirect('home page')
    else:
        form = ProfileDeleteForm(instance=user_profile)

    context = {
        'form': form,
    }
    return render(req, 'delete_profile.html', context)
