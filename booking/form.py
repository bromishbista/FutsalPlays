from django import forms
from .models import *
from django.core.exceptions import ValidationError
from .models import Book_futsal
from django.forms import DateInput
from .models import Blog



#booking futsal form
class BookFutsalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookFutsalForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = Book_futsal
        fields = ['phone', 'futsal', 'date', 'start_time', 'duration']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        futsal = cleaned_data.get('futsal')
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        duration = cleaned_data.get('duration')
        
        if date is None:
            raise forms.ValidationError("Date field is required.")

        end_time = (datetime.combine(date, start_time) + timedelta(hours=duration)).time()

        # Check if the booking date is today or in the future
        if date < datetime.now().date():
            raise forms.ValidationError("Booking date cannot be in the past.")

        # Exclude bookings from yesterday
        yesterday = datetime.now().date() - timedelta(days=1)
        bookings = Book_futsal.objects.filter(futsal=futsal, date__gte=yesterday)
        
        for booking in bookings:
            if (date == booking.date and
                (start_time < booking.end_time() and end_time > booking.start_time)):
                
                raise forms.ValidationError(f'The futsal is already booked from {start_time.strftime("%I:%M %p")} to {end_time.strftime("%I:%M %p")} on {date}.')







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
        fields = ['name', 'team_image', 'location', 'join_date', 'players']
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


# class for creating review 
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields=['text', 'rating']
    
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }


# for creating chat messgaes form
class ChatMessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = ChatMessage
        fields = ('message',)

    def __init__(self, user, futsal, *args, **kwargs):
        self.user = user
        self.futsal = futsal
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        instance.futsal = self.futsal
        if commit:
            instance.save()
        return instance
    
# classs for slider list form 
class SliderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SliderForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model =slider
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['slug','name', 'image', 'small_description', 'description']
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'small_description': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }