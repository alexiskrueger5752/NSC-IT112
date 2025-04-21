from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

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

if __name__ == '__main__':
   app.run()
