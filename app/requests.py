# from app import app
import urllib.request,json#help create a connection to the api url and send request and json modules that will format the JSON response to a python dictionary
from .models import Movie



#Getting api key
api_key = None
#ABOVE WE HAVE IMPORTE THE APP INSTANCE AND FORM IT WE GET THE API KEY FROM THE CONFIG OBJECT

#Getting the movie base url
base_url = None#Accessing configuration objects



def configure_requests(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']


def get_movies(category):
    '''
    Function that gets the json response to our url request 
    '''

    get_movies_url = base_url.format(category,api_key)
    #We use the .format() method on the base_url and pass in the movie category and the api_key. This will replace the {} curly brace placeholders in the base_url with the category and api_key respectively.



#We then use with as our context manager to send a request using theurllib.request.urlopen() function that takes in the get_movies_url as an argument and sends a request as url
    with urllib.request.urlopen(get_movies_url)as url:
        get_movies_data = url.read()#We use the read() function to read the response and store it in a get_movies_datavariable.
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)


    return movie_results



def process_results(movie_list):#it takes in a list of dictionaries
    '''
    Function that processes the movie results and transform them to a of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details


    Returns:
        movie_result: A list of movie Objects
    '''

    movie_results = []# this is where we will store our newly created movie objects.
    for movie_item in movie_list:
        id = movie_item.get('id')#method and pass in the keys so that we can access the values
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')
#We use the values we get to create a new movie object then we append it to our empty list

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)


    return movie_results


def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url)as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')


            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)


    return movie_object

# search movie function 
def search_movie(movie_name):
    search_movie_url =  'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url)as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)



    search_movie_results = None

    if search_movie_response['results']:
        search_movie_list = search_movie_response['results']
        search_movie_results = process_results(search_movie_list)

    return search_movie_results
