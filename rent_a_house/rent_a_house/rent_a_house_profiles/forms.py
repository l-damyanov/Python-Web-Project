import os
from os.path import join

from django import forms
from django.conf import settings

from rent_a_house.rent_a_house_profiles.models import Profile


class ProfileEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        db_profile = Profile.objects.get(pk=self.instance.user_id)
        if commit:
            if self.cleaned_data['profile_image'] != db_profile.profile_image and db_profile.profile_image != '':
                image_path = join(settings.MEDIA_ROOT, str(db_profile.profile_image))
                os.remove(image_path)
        return super().save(commit)

    class Meta:
        model = Profile
        exclude = ('user', 'is_complete')


class ProfileDeleteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileDeleteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = Profile
        exclude = ('user', 'is_complete')
