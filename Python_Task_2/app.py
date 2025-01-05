from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# In-memory data storage
movies = []  # List to store movies
reviews = {}  # Dictionary to store reviews for each movie

@app.route('/')
def home():
    return render_template('home.html', movies=movies)

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        if title:  # Add movie if title is not empty
            movies.append(title)
            reviews[title] = []  # Initialize empty review list for the movie
        return redirect(url_for('home'))
    return render_template('add_movies.html')

@app.route('/movie/<title>', methods=['GET', 'POST'])
def movie_details(title):
    if request.method == 'POST':
        review = request.form['review']
        if review:
            reviews[title].append(review)
        return redirect(url_for('movie_details', title=title))
    return render_template('movie_details.html', title=title, reviews=reviews[title])

if __name__ == '__main__':
    app.run(debug=True)
