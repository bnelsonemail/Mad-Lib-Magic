"""
Module defines a Flask web application for generating and displaying.

Madlibs stories based on user input. Users can navigate to the homepage,
fill out a form with various prompts, and view the generated story.
"""

from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension
from stories import STORIES
# DevelopmentConfig, ProductionConfig, TestingConfig
from config import DevelopmentConfig
import random
from dotenv import load_dotenv, find_dotenv


# load environment variables from the .env file
load_dotenv(find_dotenv())

app = Flask(__name__)

# Call config files
app.config.from_object(DevelopmentConfig)
# app.config['DEBUG'] = 'DEBUG_TB_INTERCEPT_REDIRECTS = True'
# debug = DebugToolbarExtension(app)

# Initialize the debug toolbar
# debug = DebugToolbarExtension(app)


@app.route('/')
def homepage():
    """Render the user to the homepage via render template."""
    return render_template('home.html')


@app.route('/form')
def form():
    """Collect input from the submitted form."""
    return render_template('form.html')


@app.route('/stories')
def stories():
    """Show story results."""
    place = request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    plural_noun = request.args['plural_noun']
    animal = request.args['animal']
    substance = request.args['substance']
    color = request.args['color']
    food = request.args['food']
    superhero = request.args['superhero']
    prompts = {
        'place': place,
        'noun': noun,
        'verb': verb,
        'adjective': adjective,
        'plural_noun': plural_noun,
        'animal': animal,
        'substance': substance,
        'color': color,
        'food': food,
        'superhero': superhero
        }

    # Select a random story
    random_key = random.choice(list(STORIES.keys()))
    random_value = STORIES[random_key]

    # Generate the story using the prompts dictionary
    text = random_value.generate(prompts)

    return render_template('stories.html', prompts=prompts, text=text)


if __name__ == "__main__":
    app.run(debug=True)
