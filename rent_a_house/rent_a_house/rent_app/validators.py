import os

from django.core.exceptions import ValidationError


def validate_image_format(data):
    image_format = os.path.splitext(data.name)[1]
    valid_image_formats = ('.jpeg', '.jpg', '.png')

    if image_format.lower() not in valid_image_formats:
        raise ValidationError('Supported image formats are: .jpeg, .jpg, .png!')


def validate_title(data):
    title = data.split(' ')
    for word in title:
        if word[0].upper() != word[0]:
            raise ValidationError('Title must start with a capital letter!')
