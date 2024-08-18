"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

my_stories = {
    'story1': Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "animal", "substance", "color"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    ),
    'story2': Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "animal", "substance", "color"],
    """One day, a {adjective} {noun} decided to go on an adventure. It packed a {adjective} {noun} and a {adjective} {noun}. Along the way, it met a {adjective} {animal} who offered it a {noun} in exchange for a {noun}. Together, they {verb} through the {adjective} {place} until they found the {plural_noun} of their dreams"""
    ),
    'story3': Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "animal", "substance", "color"],
    """Once upon a time, a {adjective} {noun} discovered a secret recipe for a magic potion. The ingredients included twelve {plural_noun}, a dash of {adjective} {substance}, and a sprinkle of {adjective} {substance}. When the {noun} mixed it all together, it turned into a {adjective} {color} {noun} that could {verb} anyone who drank it!"""
    ),
    'story4': Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "animal", "substance", "color"],
    """At the {place} Zoo, a {adjective} {animal} managed to escape from its enclosure. It ran through the {place}, knocking over {plural_noun} and causing a {adjective} commotion. The zookeepers tried to {verb} it with a {noun} made of {substance}, but the {color} {animal} was too fast! Eventually, it was lured back to its cage with a trail of (plural noun)."""
    ),
    'story5': Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "animal", "substance", "color"],
    """In the middle of the {place}, there was an enchanted forest where all the {plural_noun} were made of {substance}. One day, a {adjective} traveler found a {color} {noun} lying on the ground. When they picked it up, it began to {verb}, and all the {animal} in the forest gathered around, speaking in {adjective} voices. The traveler decided to take the (noun) to the {place} to solve the mystery."""
    ),
    'story6': Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "animal", "substance", "color"],
    """Deep in the heart of {place}, a {adjective} wizard was brewing a magical potion in a {noun} made of {substance}. The potion required a {color} {animal} and a handful of {plural_noun}. As the wizard began to {verb} the ingredients, the potion bubbled and turned into a {adjective} {color} liquid. When the potion was complete, it had the power to {verb} anyone who drank it!"""
    ),
    'story7': Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "animal", "substance", "color"],
    """Legend says that buried deep in the {place} lies a chest full of {plural_noun}. A group of {adjective} adventurers set out on a quest to find it. Along the way, they encountered a {color} {animal} guarding a {noun} made of {substance}. To pass, they had to {verb} the {animal} using only a {adjective} {noun} they found in the {place}."""
    ),
    'story8': Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "animal", "substance", "color"],
    """During a stormy night, a shipwrecked sailor washed ashore on a {adjective} island in the middle of the {place}. The island was covered in {color} {plural_noun} and the air smelled of {substance}. As the sailor began to explore, they encountered a {adjective} {animal} that seemed to be guarding a {noun}. The only way off the island was to {verb} the {animal} using a {adjective} {noun} they found buried in the sand."""
    ),
    'story9': Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "animal", "substance", "color"],
    """In a hidden laboratory deep within the {place}, a {adjective} scientist was working on a secret experiment. They were trying to create a {color} {noun} that could {verb} on its own. The lab was filled with {plural_noun} and the smell of {substance} hung in the air. One day, a {adjective} {animal} wandered into the lab, knocking over a {noun}, and causing the experiment to go terribly wrong! Now, the lab is filled with {color} {plural_noun} that can {verb}!"""
    ),
    'story10': Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "animal", "substance", "color"],
    """On a quiet evening in the {place}, the sky suddenly turned {color} as a fleet of alien {plural_noun} descended from the clouds. The aliens, resembling {adjective} {animal}, landed their ships made of {substance} and began to {verb} all the {plural_noun} they could find. In a desperate attempt to save the {place}, the townspeople used a {noun} to create a {adjective} device that would {verb} the aliens back into space."""
    ),
    
}


# ans = {
#     "place": "forest",
#     "noun": "dragon",
#     "verb": "collect",
#     "adjective": "mighty",
#     "plural_noun": "treasures"
# }