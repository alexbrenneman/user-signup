from flask import Flask, request,redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET','POST'])
def index():
    template = jinja_env.get_template('index.html')
    return template.render()

@app.route('/hello', methods = ['GET','POST'])
def username():
    template = jinja_env.get_template('index.html')
    username = request.args.get('username')
    return '<h1>Hello, ' + username + '</h1>'
    
   


app.run()