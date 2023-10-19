import requests
import random


key = 'Your Key'

def rand_news(country , category):
    params = {
        'country':country,
        'category':category,
        'apiKey':key
    }

    response = requests.get("https://newsapi.org/v2/top-headlines",params=params)
    
    if response.status_code == 200:
        data  = response.json()
        articles = data.get("articles")

        if articles:
            rand_article = random.choice(articles)
            print("\t\t\t\tTitle\n",rand_article['title'][1:])
            print()
            print(rand_article['url'])


while(True):
        print("Enter 1 for India")
        print("Enter 2 for USA")
        print("Enter 3 for Russia")
        print("Enter 4 for world")

        input1 = (int)(input())

        print("Enter 1 for Politics")
        print("Enter 2 for Sports")
        print("Enter 3 for Technology/Space")
        print("Enter 4 for All")

        input2 = (int)(input())

        Region={1:"in" , 2:"us" , 3:"ru" , 4:None}
        Cat = {1:"politics" , 2:"sports" , 3:"technology" , 4:"general"}

        rand_news(Region[input1],Cat[input2])
        
