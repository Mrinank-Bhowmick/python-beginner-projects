import requests
import random

# this is the key which you can get from newsapi.org
key = 'Your NewsApi.org KEY'

def rand_news(country , category):
    params = {
        'country':country,
        'category':category,
        'apiKey':key
    }

    # this is the api endpoint , it is kind of like a page which stores all the news and returns it 

    response = requests.get("https://newsapi.org/v2/top-headlines",params=params)
    
    if response.status_code == 200:
        data  = response.json()
        articles = data.get("articles")

        if articles:
            rand_article = random.choice(articles) # python function to get a random element
            print("\t\t\t\tTitle\n",rand_article['title'][1:])
            print()
            print(rand_article['url'])


# An infinite loop until you stop the program with ctrl+c on terminal , takes input for your taste of news
while(True):
        print("Enter 1 for India")
        print("Enter 2 for USA")
        print("Enter 3 for Russia")
        print("Enter 4 for world")

        input1 = (int)(input()) # Python takes input in string by default , type casting to int 

        print("Enter 1 for Politics")
        print("Enter 2 for Sports")
        print("Enter 3 for Technology/Space")
        print("Enter 4 for All")

        input2 = (int)(input())

        # Dictionaries in python , They store key value pairs to make mapping easier

        Region={1:"in" , 2:"us" , 3:"ru" , 4:None}
        Cat = {1:"politics" , 2:"sports" , 3:"technology" , 4:"general"}

        # This is how you access a dict's value using key and make a function call
        rand_news(Region[input1],Cat[input2])
        
