from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def default():
   return render_template('default.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/form')
def form():
   return render_template('form.html')

@app.route('/form/result', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       return render_template("result.html", first_name = request.form.get("fname"), 
       last_name = request.form.get("lname"))

if __name__ == '__main__':
   app.run()
