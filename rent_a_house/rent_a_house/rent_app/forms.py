import os
from os.path import join

from django import forms
from django.conf import settings

from rent_a_house.rent_app.models import Offer


class OfferForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'available':
                field.widget.attrs['class'] = 'form-available'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Offer
        fields = '__all__'


class CreateOffer(OfferForm):
    pass


class EditOffer(OfferForm):

    def save(self, commit=True):
        db_offer = Offer.objects.get(pk=self.instance.id)
        if commit:
            if self.cleaned_data['image'] != db_offer.image:
                image_path = join(settings.MEDIA_ROOT, str(db_offer.image))
                os.remove(image_path)
        return super().save(commit)


class DeleteOffer(OfferForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
