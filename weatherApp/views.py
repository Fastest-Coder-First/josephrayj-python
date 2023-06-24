import json
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .forms import CityToLatLngForm
import requests
from .models import SearchQuery
from django.contrib.auth.decorators import login_required
from .models import SearchQuery



def city_to_latlng(request):
    if request.method == 'GET':
        form = CityToLatLngForm()

        # Render the form
        return render(request, 'city_to_latlng.html', {'form': form})

    elif request.method == 'POST':
        form = CityToLatLngForm(request.POST)
        print(form.is_valid())
        # Validate the form data
        if form.is_valid():
            village_name = form.cleaned_data['village_name']
            city_name = form.cleaned_data['city_name']
            state_name = form.cleaned_data['state_name']
            country = form.cleaned_data['country']
            pin_code = form.cleaned_data['pin_code']
            startdate = form.cleaned_data['start_date'].strftime("%Y-%m-%d")
            enddate = form.cleaned_data['end_date'].strftime("%Y-%m-%d")
            
            # Construct the query string
            query_parts = []
            if village_name:
                query_parts.append(village_name)
            if city_name:
                query_parts.append(city_name)
            if state_name:
                query_parts.append(state_name)
            if country:
                query_parts.append(country)
            if pin_code:
                query_parts.append(pin_code)
            query = ', '.join(query_parts)

            # Make a request to the Nominatim API for lat/long coordinates
            url = f'https://nominatim.openstreetmap.org/search?q={query}&format=json'
            response = requests.get(url).json()

            # Extract latitude and longitude from the response
            if response:
                result = response[0]
                latitude = float(result['lat'])
                longitude = float(result['lon'])
                weatherUrl = r"https://api.open-meteo.com/v1/dwd-icon?latitude="+str(latitude)+"&longitude="+str(longitude)+r"&current_weather=true&daily=apparent_temperature_max,apparent_temperature_min,rain_sum,windspeed_10m_max,weathercode&temperature_unit=fahrenheit&forecast_days=3&start_date="+startdate+r"&end_date="+enddate+r"&timezone=auto"
                resp = requests.get(weatherUrl)
                apiMetaValues = json.loads(resp.text)
                
                # convert the apiMetaValues to a list of lists
                weatherTableByDate = [ [a,b,c,d,e,f] for a,b,c,d,e,f in zip(
                    apiMetaValues['daily']['time'],
                    apiMetaValues['daily']['apparent_temperature_max'],
                    apiMetaValues['daily']['apparent_temperature_min'],
                    apiMetaValues['daily']['rain_sum'],
                    apiMetaValues['daily']['windspeed_10m_max'],
                    apiMetaValues['daily']['weathercode'],
                ) ]
                
                # save the serach query if user is athenticated
                if request.user.is_authenticated:
                    search_query = SearchQuery(village_name=village_name, city_name=city_name, state_name=state_name, country=country, pin_code=pin_code, start_date=startdate, end_date=enddate, apiMetaValues=apiMetaValues, user=request.user , weatherTableByDate=weatherTableByDate)
                else :
                    search_query= SearchQuery(village_name=village_name, city_name=city_name, state_name=state_name, country=country, pin_code=pin_code, start_date=startdate, end_date=enddate, apiMetaValues=apiMetaValues, weatherTableByDate=weatherTableByDate)
                search_query.save()
                
                # render the weather details page
                return render(request,'weatherDetails.html',context={'apiMetaValues':apiMetaValues,'weatherTableByDate':weatherTableByDate})
            else:
                return JsonResponse({'error': 'Unable to retrieve coordinates for the given location.'}, status=400)
        else:
            # Form data is invalid, re-render the form with errors
            return render(request, 'city_to_latlng.html', {'form': form})


# create function to display the search query list
@login_required(login_url='/login/')
def search_query_list(request):
    search_queries = SearchQuery.objects.filter(user=request.user)
    return render(request, 'search_query_list.html', {'search_queries': search_queries})


# create function to display the search query details
@login_required(login_url='home')
def weather_detail(request, pk):
    search_query = get_object_or_404(SearchQuery, pk=pk)
    apiMetaValues = search_query.apiMetaValues
    return render(request, 'weatherDetails.html', apiMetaValues)


# create login and signup views

# import login  signup forms and authenticate ,  login
from .forms import LoginForm, SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login



def signin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    return render(request, 'login.html', {'form': form})



def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('signin')
    return render(request, 'signup.html', {'form': form})
