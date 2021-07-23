from django import forms

from rent_a_house.rent_a_house_profiles.models import Profile


class ProfileEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        exclude = ('user', 'is_complete')
