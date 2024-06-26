from flask import Flask, redirect, render_template, request, abort

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True, movie_list = movie_repository.get_all_movies())


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page

    title = request.form.get('title')
    director = request.form.get('director')
    rating = request.form.get('rating')
    if not title or not director or not rating:
        abort(400)
    movie_repository.create_movie(title, director, rating)
    return redirect('/movies')



@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    movie_title = request.form.get('title')
    movie_rating = movie_repository.get_movie_by_title(movie_title)
    if movie_rating is None:
        print(f"Movie not found. Please try another movie")
    return render_template('search_movies.html',movie_rating=movie_rating)

@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    #call id
    movie = movie_repository.get_movie_by_id(movie_id)
    if movie == 'None':
        return 'Movie not found.'
    else:
        redirect(f'/movies/{movie_id}')
        return render_template('get_single_movie.html', movie=movie)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass