# MOVIE API and ML

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)

## About <a name = "about"></a>
A Movie API and ML Recommendation system is a dynamic software solution that combines data from various movie databases with machine learning algorithms. It provides users with personalized movie recommendations based on their preferences and viewing history. This technology enhances the user experience by suggesting movies that align with their tastes, ultimately increasing user engagement and satisfaction.

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites
* activate venv in local system
```
.\anprsys\Scripts\activate
```
* install requirements for code to run
```
pip  install -r requirements.txt
```

### Get API KEY from [**Rapidapi**]('https://rapidapi.com/studio)
* Reference youtube link for How to get [**API key**](https://www.youtube.com/watch?v=ytNyibPQFhw)
* Create .env file for apikey

```
X-RapidAPI-Key= 'your_api_key_here'
```

### Runnning in local Host
```
cd MovieApi_and_ML\movieapi\manage.py
```
- Run server
```
py manage.py runserver
```



