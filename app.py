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
from detective_stories import DetectiveStories
from medical_thriller_stories import MedicalThrillerStories
from biblical_stories import BiblicalStories
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
    # Define default values for placeholders
    default_values = {
        'character': "Jedi",
        'noun': "star",
        'verb': "launch",
        'adjective': "galactic",
        'sidekick': "droid",
        'weapon': "lightsaber",
        'vehicle': "Millennium Falcon",
        'animal': "wampa",
        'substance': "kyber crystals",
        'color': "purple",
        'planet': "Tatooine",
        'food': "blue milk",
        'quest': "rescue the princess",
        'villian': "Sith Lord"
    }

    # Get form data and replace empty strings with default values
    prompts = {}
    for key, default_value in default_values.items():
        
        # Fetch the input and check if it's empty or None, then use the default
        input_value = request.args.get(key)
        prompts[key] = input_value if input_value and input_value.strip() else default_value
        
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
    
    default_values = {
        'captain': "Zorak",
        'noun': "starship",
        'verb': "launch",
        'adjective': "warp-speed",
        'species': "Vulcan",
        'starship': "USS Phoenix",
        'creature': "Gorn",
        'tech': "tricorder",
        'substance': "acid",
        'color': "purple",
        'planet': "Kronos",
        'food': "milk",
        'quest': "Negotiate Peace Treaty with the Romulans",
        'villain': 'Romulan',
        'phenomenon':"wormhole"
    }

# Get form data and replace empty strings with default values
    prompts = {}
    for key, default_value in default_values.items():
        
        # Fetch the input and check if it's empty or None, then use the default
        input_value = request.args.get(key)
        prompts[key] = input_value if input_value and input_value.strip() else default_value
        
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
    default_values = {
        'character': "Captain Jack Sparrow",
        'noun': "crow's nest",
        'verb': "plunder",
        'adjective': "treacherous",
        'sidekick': "parrot",
        'weapon': "cannon",
        'creature': "Kraken",
        'ship': "Black Pearl",
        'substance': "rum",
        'color': "purple",
        'location': "Skull Island",
        'food': "salted pork",
        'treasure': "Aztec Gold",
        'villain': "One Eyed Willie",
    }

# Get form data and replace empty strings with default values
    prompts = {}
    for key, default_value in default_values.items():
        
        # Fetch the input and check if it's empty or None, then use the default
        input_value = request.args.get(key)
        prompts[key] = input_value if input_value and input_value.strip() else default_value

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
    default_values = {
        'character': "Knight Sir Lancelot",
        'noun': "lance",
        'verb': "joust",
        'adjective': "noble",
        'sidekick': "squire",
        'weapon': "Magic Sword",
        'creature': "troll",
        'magical_item': "enchanted amulet",
        'substance': "mana",
        'color': "purple",
        'kingdom': "Avalon",
        'food': "venison",
        'quest': "Retrieve the Holy Grail",
        'villain': "Evil Sorcerer",
    }

# Get form data and replace empty strings with default values
    prompts = {}
    for key, default_value in default_values.items():
        
        # Fetch the input and check if it's empty or None, then use the default
        input_value = request.args.get(key)
        prompts[key] = input_value if input_value and input_value.strip() else default_value

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
    default_values = {
        'character': "Thunderbolt",
        'noun': "candy",
        'verb': "fly",
        'adjective': "treacherous",
        'sidekick': "Speedster",
        'weapon': "energy gauntlet",
        'creature': "Kraken",
        'superpower': "invisibility",
        'substance': "acid",
        'color': "purple",
        'identity': "Alex Storm",
        'food': "diet coke",
        'quest': "save the city from destruction",
        'villain': "Shadow King",
        'location': "Gothom",
    }

# Get form data and replace empty strings with default values
    prompts = {}
    for key, default_value in default_values.items():
        
        # Fetch the input and check if it's empty or None, then use the default
        input_value = request.args.get(key)
        prompts[key] = input_value if input_value and input_value.strip() else default_value


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


@app.route('/detective')
def detective():
    """
    Collect user input for the detective themed Mad Lib Story.

    Returns
    -------
    Renders the detective HTML input form page.

    """
    return render_template('detective.html')


@app.route('/detective-stories')
def detective_stories():
    """Show detective story results."""

    # Define default values for placeholders
    default_values = {
        'character': "Sherlock Holmes",
        'noun': "building",
        'verb': "plunge",
        'adjective': "honorable",
        'sidekick': "Watson",
        'weapon': "lead pipe",
        'creature': "dog",
        'clue': "a bloody glove",
        'substance': "acid",
        'color': "purple",
        'motive': "a secret affair",
        'food': "diet coke",
        'alibi': "working late at the office",
        'suspect': "Miss Scarlett",
        'location': "the library",
        'crime': "secretary found dead",
    }

    # Get form data and replace empty strings with default values
    prompts = {}
    for key, default_value in default_values.items():
        # Fetch the input and check if it's empty or None, then use the default
        input_value = request.args.get(key)
        prompts[key] = input_value if input_value and input_value.strip() else default_value

    # Select a random story
    random_key = random.choice(list(DetectiveStories.keys()))
    random_value = DetectiveStories[random_key]

    # Generate the story using the prompts dictionary
    text = random_value.generate(prompts)

    return render_template('detective-stories.html', prompts=prompts, text=text)


@app.route('/medical-thriller')
def medical_thriller():
    """
    Collect user input for the medical thriller themed Mad Lib Story.

    Returns
    -------
    Renders the medical thriller HTML input form page.

    """
    return render_template('medical-thriller.html')


@app.route('/medical-thriller-stories')
def medical_thriller_stories():
    """Show medical thriller story results."""

    # Define default values for placeholders
    default_values = {
        'character': "Dr. Evelyn Hartman",
        'noun': "building",
        'verb': "plunge",
        'adjective': "life-threatening",
        'patient': "John Doe",
        'illness': "COVID",
        'creature': "dog",
        'procedure': "emergency surgery",
        'substance': "acid",
        'color': "purple",
        'hospital': "Saint Mercy General",
        'food': "diet coke",
        'lab': "experimental drug formula",
        'villain': "Rogue Scientist",
        'equipment': "scalpel",
        'crime': "harvested organs",
    }

    # Get form data and replace empty strings with default values
    prompts = {}
    for key, default_value in default_values.items():
        # Fetch the input and check if it's empty or None, then use the default
        input_value = request.args.get(key)
        prompts[key] = input_value if input_value and input_value.strip() else default_value

    # Select a random story
    random_key = random.choice(list(MedicalThrillerStories.keys()))
    random_value = MedicalThrillerStories[random_key]

    # Generate the story using the prompts dictionary
    text = random_value.generate(prompts)

    return render_template('medical-thriller-stories.html', prompts=prompts, text=text)


@app.route('/biblical')
def biblical():
    """
    Collect user input for the biblical themed Mad Lib Story.

    Returns
    -------
    Renders the biblical HTML input form page.

    """
    return render_template('biblical.html')


@app.route('/biblical-stories')
def biblical_stories():
    """Show biblical story results."""

    # Define default values for placeholders
    default_values = {
        'character-male': "John the Baptist",
        'character-female': "Virgin Mary",
        'noun': "boat",
        'verb': "pray",
        'adjective': "holy",
        'weapon': "battle axe",
        'miracle': "heal the blind",
        'creature': "donkey",
        'emotion': "peaceful",
        'object': "Noah's Ark",
        'color': "purple",
        'location': "Bethlehem",
        'food': "venison",
        'quest': "spread the good news",
        'villain': "Pontius Pilate",
        'weather': "thunderstorms",
        'commandment': "thou shall not steal",
    }

    # Get form data and replace empty strings with default values
    prompts = {}
    for key, default_value in default_values.items():
        # Fetch the input and check if it's empty or None, then use the default
        input_value = request.args.get(key)
        prompts[key] = input_value if input_value and input_value.strip() else default_value

    # Select a random story
    random_key = random.choice(list(BiblicalStories.keys()))
    random_value = BiblicalStories[random_key]

    # Generate the story using the prompts dictionary
    text = random_value.generate(prompts)

    return render_template('biblical-stories.html', prompts=prompts, text=text)



if __name__ == "__main__":
    app.run(debug=True)
