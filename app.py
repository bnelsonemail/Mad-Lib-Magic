from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import my_stories
import random

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
    """Collects input from the submitted form"""

    return render_template('form.html')



@app.route('/stories')
def stories():
    """show story results"""
    place = request.args['place']
    noun = request.args["noun"]
    verb = request.args['verb']
    adjective = request.args['adjective']
    plural_noun = request.args['plural_noun']
    animal = request.args['animal']
    substance = request.args['substance']
    color = request.args['color']
    prompts = {
        'place': place, 
        'noun': noun, 
        'verb': verb, 
        'adjective': adjective, 
        'plural_noun': plural_noun,
        'animal': animal,
        'substance': substance,
        'color': color}
    
    random_key = random.choice(list(my_stories.keys()))
    random_value = my_stories[random_key]
    text = random_value.generate(request.args)

    return render_template('stories.html', prompts = prompts, text = text )


if __name__ == "__main__":
    app.run(debug=True)
