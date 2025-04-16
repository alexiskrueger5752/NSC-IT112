from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/about')
def about():
   return render_template('about.html')

if __name__ == '__main__':
   app.run()
'''
@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/about')
def my_info():
   return 'My name is Alexis Krueger'

if __name__ == '__main__':
   app.run()
'''

'''
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run()'''
