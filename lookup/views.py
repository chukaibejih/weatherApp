from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    if request.method == "POST":
        city = request.POST['city']
        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f4c512f8a2f906ebc2663e7ab082ad9c")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        
        return render (request, 'home.html', {'api': api})


    else:        

        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Lagos&appid=f4c512f8a2f906ebc2663e7ab082ad9c")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        
        return render (request, 'home.html', {'api': api})
