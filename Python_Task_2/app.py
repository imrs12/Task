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

@app.route('/update_movie/<title>', methods=['GET', 'POST'])
def update_movie(title):
    if request.method == 'POST':
        new_title = request.form['title']
        if new_title:
            movies[movies.index(title)] = new_title
            reviews[new_title] = reviews.pop(title)
        return redirect(url_for('home'))
    return render_template('add_movies.html', title=title)

@app.route('/delete_movie/<title>', methods=['POST'])
def delete_movie(title):
    movies.remove(title)
    reviews.pop(title, None)
    return redirect(url_for('home'))

@app.route('/delete_review/<title>/<int:review_index>', methods=['POST'])
def delete_review(title, review_index):
    if title in reviews and 0 <= review_index < len(reviews[title]):
        reviews[title].pop(review_index)
    return redirect(url_for('movie_details', title=title))

if __name__ == '__main__':
    app.run(debug=True)
