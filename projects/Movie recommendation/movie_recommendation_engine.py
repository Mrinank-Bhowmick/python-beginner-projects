#!/usr/bin/env python
# coding: utf-8

# ### recommendation engines :
#
#
#
# ### youtube - popularity based
#
#
#
# ### amazon/flipkart/movie recommendation/google recommendation - content based
#
#
#
# ### netflix - collaborative filltering based

# In[1]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movie_dataset.csv")  # can be found online


# if you visualize the dataset, you will see that it has extra info about that movie , we dont need all of them. So we choose keywords, cast,genres and director column to use  as our feature set(the so called "content" of the movie)

# In[2]:


features = ["keywords", "cast", "genres", "director"]


# our next task is to create a function for combining the values of these columns into a single string.

# In[3]:


def combine_features(row):
    return (
        row["keywords"]
        + " "
        + row["cast"]
        + " "
        + row["genres"]
        + " "
        + row["director"]
    )


# now we need to call this function over each row of our dataframe. but before doing that we need to clean and preprocess the data for our use. we will fill all the NaN values with blank string in the dataframe

# In[4]:


for feature in features:
    df[feature] = df[feature].fillna("")  # filling all NaNs with blank string
df["combined_features"] = df.apply(
    combine_features, axis=1
)  # applying combined_features()


# In[5]:


df.iloc[0].combined_features


# now that we have obtained the combined strings, we can now feed these strings to a CountVectorizer() object for getting the count matrix

# In[6]:


cv = CountVectorizer()  # creating new CountVectorizer() object
count_matrix = cv.fit_transform(
    df["combined_features"]
)  # feeding combined strings(movie counts) to COuntVectorizer() object


# at this point 60% work is done. now we need to obtain the cosine similarity matrix from the count matrix

# In[7]:


cosine_sim = cosine_similarity(count_matrix)


# now we will define two helper funtions to get movie title from movie index and vice versa

# In[8]:


def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]


def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]


# the next step is to get the title of the movie that the user currently likes. then we will find the index of that movie. aftert that, we will access the row corresponding to this movie in the similarity matrix. thus, we will get the similarity scores of all other movies from the current movie. then we will enumerate through all the similarity scores of that movie to make a tuple of movie index and similarity score . this will convert a row of similarity scores like this- [1 0.5 0.2 0.9] to this- [(0,1) (1,0.5) (2,0.2) (3,0.9)]. here each term is in this form- (movie index, similarity score)

# In[9]:


movie_user_likes = "Avatar"
movie_index = get_index_from_title(movie_user_likes)
similar_movies = list(
    enumerate(cosine_sim[movie_index])
)  # accessing the row corresponding


# now comes the most vital point. we will sort the list similar_movies according to similarity scores in descending order. since the most similar movie to a given movie will be itself, we will discard the first element after sorting the movies

# In[10]:


sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]


# In[15]:


print(len(sorted_similar_movies))


# now we will run a loop to print first 5 entries from sorted_similar_movies list

# In[12]:


i = 0
print("Top 5 similar movies to " + movie_user_likes + " are:\n")
for element in sorted_similar_movies:
    print(get_title_from_index(element[0]))
    i = i + 1
    if i > 5:
        break


# In[ ]:
