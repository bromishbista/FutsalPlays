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

#class form breadcrumbsForm
class BeadcrumbsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BeadcrumbsForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Beadcrumbs
        fields = '__all__'


# creating class for AboutForm 
class AboutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AboutForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


#creating  class for futsal form
class FutsalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FutsalForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
             field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Futsal
        fields = '__all__'

#class for details form 
class DetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DetailsForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Details
        fields = '__all__'


#creating class for team and match form
        
from django import forms
from .models import Team, Match

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'team_image', 'location_url', 'location', 'join_date', 'players']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'team_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            # 'location_url': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'join_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'players': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['futsal', 'date', 'first_team', 'first_image', 'second_team', 'second_image', 'start_time', 'end_time', 'playercount', 'gametype']
        widgets = {
            'futsal': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'first_team': forms.Select(attrs={'class': 'form-control'}),
            'first_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'second_team': forms.Select(attrs={'class': 'form-control'}),
            'second_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'playercount': forms.Select(attrs={'class': 'form-control'}),
            'gametype': forms.Select(attrs={'class': 'form-control'}),
        }