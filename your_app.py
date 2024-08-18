from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Set configuration for development
app.config['SECRET_KEY'] = "your_secret_key"
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

# Initialize the debug toolbar
debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    """This function will render the user to the homepage via render template"""
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/stories')
def stories():
    return render_template('stories.html')







if __name__ == "__main__":
    app.run(debug=True)
