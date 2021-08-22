from .models import SendSubmission
from django import forms

from django.utils.translation import gettext_lazy as _


CHOICES=[('yes','Yes'),
         ('no','No'),
         ('poster','Poster'),
         ]


class SendSubForm(forms.ModelForm):
    talk_s = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=CHOICES, label='Do you have a talk')
    invitation_s = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=CHOICES, label='Do you need a letter of invitation')

    class Meta:
        model = SendSubmission
        fields = ('name','surname','email','phone','organization','position','city','post_code_city', 'postal_address', 'web_site',
                  'fax','institute','abstract_title','upload_abstract','talk_s','section','invitation_s','message')

        labels = {
            'post_code_city': _('Post Code - City'), 'postal_address':_('Postal Address (without your name)'),
            'web_site': 'Web Site', 'abstract_title': _('Abstract Title'), 'upload_abstract':_('Upload Abstract'),

        }


NUMS= [
    ('one', 'one'),
    ('two', 'two'),
    ('three', 'three'),
    ('four', 'four'),
    ('five', 'fives'),

    ]

