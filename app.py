from flask import Flask, render_template, url_for, request, redirect, session
#from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///table.db'

db = SQLAlchemy(app)

@app.route('/')
def default():
   return render_template('default.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/fortune' , methods =["GET", "POST"])
def fortune():
   if request.method == "POST":
      name = request.form.get("user")
      color = request.form.get("color")
      number = request.form.get("number")
      return redirect(url_for('result', user=name, color=color, number=number))
   return render_template('fortune.html')

@app.route('/fortune/result')
def result():
      name = request.args.get("user")
      color = request.args.get("color")
      number = request.args.get("number")
      return render_template("result.html", name=name, color=color, 
                              number=number) 

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    movie_name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    director = db.Column(db.String(100))
    genre = db.Column(db.String(100))

    def __init__(self, movie_name, year, director, genre):
      self.movie_name = movie_name
      self.year = year
      self.director = director
      self.genre = genre

@app.route('/database')
def database():
      return render_template('database.html', movies=Movies.query.all())

@app.route('/database/detail')
def database_details():
      name = request.args.get("name")
      year = request.args.get("year")
      director = request.args.get("director")
      genre = request.args.get("genre")
      return render_template("database_details.html", name=name, 
                              year=year, director=director, genre=genre) 
    
with app.app_context():
    db.drop_all()
    db.create_all() 
    if Movies.query.count() == 0:
      all_movies = [
         Movies(movie_name='The Departed', year=2006, director='Martin Scorsese', genre='Crime'),
         Movies(movie_name='Snatch', year=2000, director='Guy Ritchie', genre='Comedy'),
         Movies(movie_name='The Italian Job', year=2003, director='F. Gary Gray', genre='Action'),
         Movies(movie_name='The Big Hit', year=1998, director='Kirk Wong', genre='Comedy')
      ]
      db.session.add_all(all_movies)
      db.session.commit()

if __name__ == '__main__':
   app.run()
