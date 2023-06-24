import datetime
from django import forms
import requests
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CityToLatLngForm(forms.Form):
    village_name = forms.CharField(max_length=100, label='Village Name', required=False)
    city_name = forms.CharField(max_length=100, label='City Name',required=True)
    state_name = forms.CharField(max_length=100, label='State Name',required=False)
    country = forms.CharField(max_length=100, label='Country',required=False)
    pin_code = forms.CharField(max_length=10, label='Pin Code',required=False)
    #add start date from today and end date from 7 days from today
    start_date = forms.DateField(
        label='Start Date',
        required=True,
        widget=forms.SelectDateWidget(),
        initial=datetime.date.today(),
        help_text='Should be less than End Date',
    )
    end_date = forms.DateField(
        label='End Date',
        required=True,
        widget=forms.SelectDateWidget(),
        initial=datetime.date.today() + datetime.timedelta(days=7),
        help_text='Should be greater than Start Date',
    )
    def __init__(self, *args, **kwargs):
        super(CityToLatLngForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.error_text_block = True
   

    def clean(self):
        cleaned_data = super().clean()
        village_name = cleaned_data.get('village_name')
        city_name = cleaned_data.get('city_name')
        state_name = cleaned_data.get('state_name')
        country = cleaned_data.get('country')
        pin_code = cleaned_data.get('pin_code')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        

        # Check if either village name or city name is provided
        if not village_name and not city_name:
            raise forms.ValidationError('Either Village Name or City Name must be provided.')

        # Check if city name contains only alphabetic characters and spaces
        if city_name and not city_name.replace(' ', '').isalpha():
            raise forms.ValidationError('City Name should only contain alphabetic characters and spaces.')

        # Check if state name contains only alphabetic characters and spaces
        if state_name and not state_name.replace(' ', '').isalpha():
            raise forms.ValidationError('State Name should only contain alphabetic characters and spaces.')

        # Check if country contains only alphabetic characters and spaces
        if country and not country.replace(' ', '').isalpha():
            raise forms.ValidationError('Country should only contain alphabetic characters and spaces.')

        # Check if pin code contains only digits
        if pin_code and not pin_code.isdigit():
            raise forms.ValidationError('Pin Code should only contain digits.')
        
        # Check if start date is greater than end date
        if start_date > end_date:
            raise forms.ValidationError('Start Date should be less than End Date.')
        
        #check if start date is grater than date today + 7 days
        if start_date > datetime.date.today() + datetime.timedelta(days=7):
            raise forms.ValidationError(f'Start Date should be less than {datetime.date.today() + datetime.timedelta(days=7)}.')
        
        # check if start date is less than today
        if start_date < datetime.date.today():
            raise forms.ValidationError('Start Date should be greater than today.')
        
        # check if end date is grater than today + 7 days
        if end_date > datetime.date.today() + datetime.timedelta(days=7):
            raise forms.ValidationError(f'End Date should be less than {datetime.date.today() + datetime.timedelta(days=7)}.')
        

        # Make a request to the Nominatim API
        query = ''
        if village_name:
            query += village_name + ', '
        if city_name:
            query += city_name + ', '
        if state_name:
            query += state_name + ', '
        if country:
            query += country + ', '
        if pin_code:
            query += pin_code + ', '
        query = query.rstrip(', ')

        url = f'https://nominatim.openstreetmap.org/search?q={query}&format=json'
        response = requests.get(url).json()

        # Check if the response is empty or invalid
        if not response:
            raise forms.ValidationError('Unable to retrieve coordinates for the given location.')

        return cleaned_data


from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Log in'))


class SignupForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sign up'))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email
    
    