from django import forms

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
    pass


class DeleteOffer(OfferForm):
    pass
