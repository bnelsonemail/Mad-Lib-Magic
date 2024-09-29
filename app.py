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
from pirate_stories import PirateStories
from medieval_stories import MedievalStories
from superhero_stories import SuperheroStories
from shadow_hunter_stories import ShadowHunterStories
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


# Pirate Story Routing

@app.route('/pirate')
def pirate():
    """
    Collect user input for the pirate themed Mad Lib Story.

    Returns
    -------
    Renders the Pirate HTML input form page.

    """
    return render_template('pirate.html')


@app.route('/pirate-stories')
def pirate_stories():
    """Show pirate story results."""
    character = request.args['character']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    sidekick = request.args['sidekick']
    weapon = request.args['weapon']
    creature = request.args['creature']
    ship = request.args['ship']
    substance = request.args['substance']
    color = request.args['color']
    location = request.args['location']
    food = request.args['food']
    treasure = request.args['treasure']
    villain = request.args['villain']
    prompts = {
        'character': character,
        'noun': noun,
        'verb': verb,
        'adjective': adjective,
        'sidekick': sidekick,
        'weapon': weapon,
        'creature': creature,
        'ship': ship,
        'substance': substance,
        'color': color,
        'location': location,
        'food': food,
        'treasure': treasure,
        'villain': villain,
    }

    # Select a random story
    random_key = random.choice(list(PirateStories.keys()))
    random_value = PirateStories[random_key]

    # Generate the story using the prompts dictionary
    text = random_value.generate(prompts)

    return render_template('pirate-stories.html', prompts=prompts, text=text)


# Medieval Adventure Routing


@app.route('/medieval')
def medieval():
    """
    Collect user input for the medieval themed Mad Lib Story.

    Returns
    -------
    Renders the Medieval HTML input form page.

    """
    return render_template('medieval.html')


@app.route('/medieval-stories')
def medieval_stories():
    """Show medieval story results."""
    character = request.args['character']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    sidekick = request.args['sidekick']
    weapon = request.args['weapon']
    creature = request.args['creature']
    magical_item = request.args['magical_item']
    substance = request.args['substance']
    color = request.args['color']
    kingdom = request.args['kingdom']
    food = request.args['food']
    quest = request.args['quest']
    villain = request.args['villain']
    prompts = {
        'character': character,
        'noun': noun,
        'verb': verb,
        'adjective': adjective,
        'sidekick': sidekick,
        'weapon': weapon,
        'creature': creature,
        'magical_item': magical_item,
        'substance': substance,
        'color': color,
        'kingdom': kingdom,
        'food': food,
        'quest': quest,
        'villain': villain,
    }

    # Select a random story
    random_key = random.choice(list(MedievalStories.keys()))
    random_value = MedievalStories[random_key]

    # Generate the story using the prompts dictionary
    text = random_value.generate(prompts)

    return render_template('medieval-stories.html', prompts=prompts, text=text)


# Superhero Adventure Routing


@app.route('/superhero')
def superhero():
    """
    Collect user input for the superhero themed Mad Lib Story.

    Returns
    -------
    Renders the Superhero HTML input form page.

    """
    return render_template('superhero.html')


@app.route('/superhero-stories')
def superhero_stories():
    """Show superhero story results."""
    character = request.args['character']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    sidekick = request.args['sidekick']
    weapon = request.args['weapon']
    creature = request.args['creature']
    superpower = request.args['superpower']
    substance = request.args['substance']
    color = request.args['color']
    identity = request.args['identity']
    food = request.args['food']
    quest = request.args['quest']
    villain = request.args['villain']
    location = request.args['location']
    prompts = {
        'character': character,
        'noun': noun,
        'verb': verb,
        'adjective': adjective,
        'sidekick': sidekick,
        'weapon': weapon,
        'creature': creature,
        'superpower': superpower,
        'substance': substance,
        'color': color,
        'identity': identity,
        'food': food,
        'quest': quest,
        'villain': villain,
        'location': location,
    }

    # Select a random story
    random_key = random.choice(list(SuperheroStories.keys()))
    random_value = SuperheroStories[random_key]

    # Generate the story using the prompts dictionary
    text = random_value.generate(prompts)

    return render_template('superhero-stories.html', prompts=prompts, text=text)


@app.route('/shadow-hunter')
def shadowhunter():
    """
    Collect user input for the shadow hunter themed Mad Lib Story.

    Returns
    -------
    Renders the shadow hunter HTML input form page.

    """
    return render_template('shadow-hunter.html')


@app.route('/shadow-hunter-stories')
def shadow_hunter_stories():
    """Show shadow hunter story results."""

    # Define default values for placeholders
    default_values = {
        'character': "Kaelith Blackthorn",
        'noun': "lance",
        'verb': "joust",
        'adjective': "noble",
        'sidekick': "Selene Nightshade",
        'weapon': "Magic Eclipseblade",
        'creature': "Troll",
        'ability': "riftwalk",
        'substance': "mana",
        'color': "purple",
        'artifact': "The Bloodshard Amulet",
        'food': "venison",
        'quest': "The Hunt for the Shattered Sigil",
        'villain': "Lucian Voidstrike",
        'realm': "The Veil of Duskmire",
    }

    # Get form data and replace empty strings with default values
    prompts = {}
    for key, default_value in default_values.items():
        # Fetch the input and check if it's empty or None, then use the default
        input_value = request.args.get(key)
        prompts[key] = input_value if input_value and input_value.strip() else default_value

    # Select a random story
    random_key = random.choice(list(ShadowHunterStories.keys()))
    random_value = ShadowHunterStories[random_key]

    # Generate the story using the prompts dictionary
    text = random_value.generate(prompts)

    return render_template('shadow-hunter-stories.html', prompts=prompts, text=text)

if __name__ == "__main__":
    app.run(debug=True)
