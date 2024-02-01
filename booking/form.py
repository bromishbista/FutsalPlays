from django import forms
from .models import *

from django.core.exceptions import ValidationError
from .models import Book_futsal

from django.forms import DateInput
class BookFutsalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookFutsalForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = Book_futsal
        fields = ['phone', 'futsal', 'date', 'start_time', 'duration']
        widgets = {
     
            'date': DateInput(attrs={'type': 'date'}),
        }

    
    def clean(self):
        cleaned_data = super().clean()
        futsal = cleaned_data.get('futsal')
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        duration = cleaned_data.get('duration')
        end_time = (datetime.combine(date, start_time) + timedelta(hours=duration)).time()
        bookings = Book_futsal.objects.filter(futsal=futsal, date=date)
        for booking in bookings:
            if start_time < booking.end_time() and end_time > booking.start_time:
                raise forms.ValidationError(f'The futsal is already booked from {booking.start_time.strftime("%I:%M %p")} to {booking.end_time().strftime("%I:%M %p")} on {date}.')
            return cleaned_data