from django.shortcuts import render
import requests
import os
from .predict import get_recommendations
from dotenv import load_dotenv

load_dotenv()
RapidAPIKey = os.getenv("X-RapidAPI-Key")


# Create your views here.
def movie(request):
    url = "https://online-movie-database.p.rapidapi.com/title/find"

    querystring = {"q": "Iron man"}
    Obs = []
    image_urls = []
    actor_names = []

    headers = {
        "X-RapidAPI-Key": RapidAPIKey,
        "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])[0:5]
        for i in range(5):
            Ob = results[i]["title"]
            image_url = results[i]["image"]["url"]
            actor_name = results[i]["principals"][0]["name"]
            Obs.append(Ob)
            image_urls.append(image_url)
            actor_names.append(actor_name)

    context = {
        "title": Obs,
        "poster": image_urls,
        "actor_name": actor_names,
    }
    return render(request, "index.html", context)


def predict(request):
    predict = None
    if request.method == "POST":
        title = request.POST.get("title")
        predict = get_recommendations(title)
    context = {"predict1": predict}
    return render(request, "predict.html", context)
