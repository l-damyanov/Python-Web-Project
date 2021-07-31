from django import forms

from rent_a_house.common.models import Comment
from rent_a_house.rent_app.models import Offer


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['rows'] = '3'

    offer_id = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment
        fields = ('text', 'offer_id',)

    def save(self, commit=True):
        offer_pk = self.cleaned_data['offer_id']
        offer = Offer.objects.get(pk=offer_pk)
        comment = Comment(
            text=self.cleaned_data['text'],
            offer=offer,
        )

        if commit:
            comment.save()

        return comment
