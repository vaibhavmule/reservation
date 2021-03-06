from django import forms

from booking.models import Ticket


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('first_name', 'last_name', 'gender')
