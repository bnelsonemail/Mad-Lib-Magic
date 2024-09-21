"""
Module defines a Flask web application for generating and displaying.

Madlibs stories based on user input. Users can navigate to the homepage,
fill out a form with various prompts, and view the generated story.
"""

from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import STORIES
from star_wars_stories import StarWarsStories
from star_trek_stories import StarTrekStories
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
debug = DebugToolbarExtension(app)

# Initialize the debug toolbar
# debug = DebugToolbarExtension(app)


@app.route('/')
def homepage():
    """Render the user to the homepage via render template."""
    return render_template('home.html')


# Surprise Me Routing


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


# Star Wars Routing


@app.route('/star-wars')
def star_wars():
    """
    Collect user input for the star wars themed Mad Lib Story.

    Returns
    -------
    Renders the Star Wars HTML input form page.

    """
    return render_template('star-wars.html')


@app.route('/star-wars-stories')
def star_wars_stories():
    """Show star wars story results."""
    character = request.args['character']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    sidekick = request.args['sidekick']
    weapon = request.args['weapon']
    vehicle = request.args['vehicle']
    animal = request.args['animal']
    substance = request.args['substance']
    color = request.args['color']
    planet = request.args['planet']
    food = request.args['food']
    quest = request.args['quest']
    villian = request.args['villian']
    prompts = {
        'character': character,
        'noun': noun,
        'verb': verb,
        'adjective': adjective,
        'sidekick': sidekick,
        'weapon': weapon,
        'vehicle': vehicle,
        'animal': animal,
        'substance': substance,
        'color': color,
        'planet': planet,
        'food': food,
        'quest': quest,
        'villian': villian
    }

    # Select a random story
    random_key = random.choice(list(StarWarsStories.keys()))
    random_value = StarWarsStories[random_key]

    # Generate the story using the prompts dictionary
    text = random_value.generate(prompts)

    return render_template('star-wars-stories.html', prompts=prompts, text=text)


# Star Trek Routing


@app.route('/star-trek')
def star_trek():
    """
    Collect user input for the star trek themed Mad Lib Story.

    Returns
    -------
    Renders the Star Trek HTML input form page.

    """
    return render_template('star-trek.html')


@app.route('/star-trek-stories')
def star_trek_stories():
    """Show star trek story results."""
    captain = request.args['captain']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    species = request.args['species']
    starship = request.args['starship']
    creature = request.args['creature']
    tech = request.args['tech']
    substance = request.args['substance']
    color = request.args['color']
    planet = request.args['planet']
    food = request.args['food']
    quest = request.args['quest']
    villain = request.args['villain']
    phenomenon = request.args['phenomenon']
    prompts = {
        'captain': captain,
        'noun': noun,
        'verb': verb,
        'adjective': adjective,
        'species': species,
        'starship': starship,
        'creature': creature,
        'tech': tech,
        'substance': substance,
        'color': color,
        'planet': planet,
        'food': food,
        'quest': quest,
        'villain': villain,
        'phenomenon':phenomenon
    }

    # Select a random story
    random_key = random.choice(list(StarTrekStories.keys()))
    random_value = StarTrekStories[random_key]

    # Generate the story using the prompts dictionary
    text = random_value.generate(prompts)

    return render_template('star-trek-stories.html', prompts=prompts, text=text)


if __name__ == "__main__":
    app.run(debug=True)
