from django import forms
from .models import Subscribers
from .models import Contact

class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscribers
        fields = ('email',)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('your_name', 'your_email', 'your_phone', 'your_message')
