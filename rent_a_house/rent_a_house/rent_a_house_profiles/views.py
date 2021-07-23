from django.shortcuts import render, redirect

from rent_a_house.rent_a_house_profiles.forms import ProfileEditForm
from rent_a_house.rent_a_house_profiles.models import Profile


def profile(req):
    return render(req, 'profile.html')


def edit_profile(req):
    user_profile = Profile.objects.get(pk=req.user.id)
    if req.method == 'POST':
        form = ProfileEditForm(req.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')
    else:
        form = ProfileEditForm(instance=user_profile)

    context = {
        'form': form,
    }
    return render(req, 'edit_profile.html', context)

