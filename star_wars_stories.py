"""Madlibs Star Wars Stories."""


class StarWarsStory:
    """A Mad Libs Star Wars Story.

    To create a Star Wars story, pass a list of prompts and the text
    of the template.

    Example
    -------
        >>> s = Story(["noun", "verb"],
        ...           "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary of
    {prompt: answer} pairs:

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, prompts, template):
        """Initialize a story with given prompts and template text."""
        self.prompts = prompts
        self.template = template

    def generate(self, answers):
        """Substitute answers into the template to generate the story."""
        text = self.template
        for key, val in answers.items():
            text = text.replace(f"{{{key}}}", val)
        return text


# Collection of Star Wars Themed Stories
StarWarsStories = {
    'sw_story1': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        In a galaxy far, far away, the brave Jedi {character} and their loyal
        {sidekick} set out on a mission to defeat the evil {villian}. Armed
        with a {weapon} and piloting the {vehicle}, they encounter a wild
        {animal} on {planet}, where a lake of {substance} bubbles ominously.
        The {color} sky darkens as they must {verb} quickly to complete their
        {quest}. Will the {adjective} {character} save the day, or will the
        galaxy fall to the forces of darkness?
        Along the way, they stop for some {food} while protecting the
        legendary {noun}.
        """
    ),

    'sw_story2': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        The notorious {villian} has stolen the sacred {noun} from the planet
        {planet}. Only {character}, along with their trusty {sidekick}, can
        recover it. Armed with a {weapon} and aboard their {vehicle}, they
        venture across the galaxy, encountering dangerous {animal} on their
        quest. The villain has hidden the {noun} in a cave filled with
        {substance}, and only by using {color} energy can they defeat him.
        The mission is {adjective}, but {character} must {verb} to finish the
        {quest}. After some {food} to regain strength, they are ready to face
        their greatest challenge.
        """
    ),

    'sw_story3': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        On the desolate planet {planet}, the fearless Jedi {character} and
        their {adjective} companion {sidekick} are hunting the evil {villian}.
        Using the mighty {weapon}, they defeat {animal}, but they must hurry,
        as the {color} sands begin to shift. They hop into the {vehicle} to
        {verb} to the location of the hidden {noun}. However, they must cross
        rivers of {substance} and evade creatures feeding on {food}. With the
        fate of the galaxy at stake, they must complete their {quest} before
        {villian} strikes again.
        """
    ),

    'sw_story4': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        In the darkest corners of {planet}, {character} and {sidekick} must
        face the wicked {villian}. Armed with a {weapon}, they set out on their
        {quest}, knowing that the fate of the galaxy rests in their hands.
        Along the way, they encounter fierce {animal}, lakes of {substance},
        and a strange {color} mist covering the planet. After a brief stop for
        {food}, they must {verb} to stop the villain and recover the precious
        {noun}. Will the {adjective} hero prevail, or will darkness consume
        them all?
        """
    ),

    'sw_story5': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        On {planet}, {character} and their trusted {sidekick} receive word that
        {villian} has taken control of a {color} weapon that can turn {noun}
        into dust. They grab their {weapon}, hop into the {vehicle}, and
        {verb} towards the villain's lair. But on their way, they must battle
        {animal} that lurk in the dangerous forest and cross streams filled
        with {substance}. Completing their {quest} won't be easy, but after a
        hearty meal of {food}, they feel {adjective} and ready to stop
        {villian}.
        """
    ),

    'sw_story6': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        When the sinister {villian} threatens to destroy {planet} with a deadly
        {substance}, it's up to {character} and {sidekick} to stop them. They
        board the {vehicle} and {verb} across the galaxy. On the way, they
        encounter a fearsome {animal} and must use their {weapon} to defend
        themselves. At last, they arrive at the {adjective} villain’s lair, but
        not before sharing some {food}. Using the {color} stone hidden in the
        {noun}, they embark on their quest to {quest} to bring peace to the galaxy.
        """
    ),

    'sw_story7': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        Deep in the heart of {planet}, {character} and {sidekick} must stop
        {villian} from using the ancient {noun} to enslave the galaxy. Armed
        with a {weapon} and riding their {vehicle}, they set off on a
        {quest}. Along the way, they encounter {animal} and pools of bubbling
        {substance}. The air turns {color} as they push forward, stopping only
        for a bite of {food}. Will the {adjective} hero {verb} in time to stop
        the ultimate disaster, or will {villian} claim victory?
        """
    ),

    'sw_story8': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        The peaceful planet {planet} has been overrun by the villainous
        {villian}, and it's up to {character} and their {adjective} sidekick
        {sidekick} to save it. With the {color} sun setting, they grab their
        {weapon} and jump into their {vehicle}. Along the way, they battle
        fierce {animal} and make their way through fields of {substance}.
        After a meal of {food}, they are ready to {verb} and complete their
        {quest} to recover the stolen {noun}.
        """
    ),

    'sw_story9': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        The galaxy is on the brink of collapse. {villian} has seized control
        of the {noun}, and only {character} and their {sidekick} can stop them.
        Armed with a {weapon}, they board the {vehicle} and race towards
        {planet}. Along the way, they must fend off wild {animal} and avoid
        pools of {substance}. The {color} sky is filled with tension as they
        stop briefly to eat {food}. Only by completing their {adjective} quest
        can they {verb} and bring balance back to the galaxy. Only when they 
        {quest} will the galaxy be safe from the evil influences of the dark 
        side of the Force!
        """
    ),

    'sw_story10': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        On the forgotten planet of {planet}, {character} and {sidekick} face
        the evil {villian}. Armed with the ancient {weapon} and riding the
        {vehicle}, they must navigate through {color} mountains and defeat the
        monstrous {animal}. In order to complete their {quest}, they must cross
        dangerous rivers of {substance} and refuel with some {food}. Will the
        {adjective} {character} {verb} in time to save the precious {noun}, or
        will {villian} succeed in their dark plans?
        """
    ),

    'sw_story11': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        When {villian} steals the {noun}, the fate of the galaxy falls into
        the hands of {character} and their {adjective} companion {sidekick}.
        Piloting the {vehicle} and armed with the legendary {weapon}, they
        embark on a quest to {quest} to recover the {noun}. On {planet}, they face off
        against dangerous {animal} and wade through swamps of {substance}.
        After a quick bite of {food}, they must {verb} to stop {villian}'s
        evil plans under the {color} sky.
        """
    ),

    'sw_story12': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        As the {color} sun rises over {planet}, {character} and {sidekick}
        prepare for their final battle against {villian}. Equipped with a
        {weapon}, they board the {vehicle} and head into the unknown. Along
        the way, they encounter a fearsome {animal}, cross rivers of
        {substance}, and feast on {food}. They must {verb} to complete their
        {adjective} quest to {quest} and retrieve the stolen {noun} before it’s too late.
        """
    ),

    'sw_story13': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        In the barren deserts of {planet}, {character} and their faithful
        {sidekick} must stop {villian} from acquiring the powerful {noun}.
        Armed with a {weapon}, they board their {vehicle} and {verb} across
        treacherous dunes filled with {animal}. The air is thick with {color}
        dust, and the only thing keeping them going is a feast of {food}. With
        their quest to {quest} nearly complete, they must navigate a river of
        {substance} to stop {villian} and save the galaxy with their
        {adjective} bravery.
        """
    ),

    'sw_story14': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        The evil {villian} has stolen a {color} {noun} from the sacred vaults
        of {planet}. Only {character}, accompanied by their {sidekick}, can
        retrieve it. Armed with the powerful {weapon}, they board the
        {vehicle} and set off on a dangerous quest to {quest}. Along the way, they face
        {animal} and bubbling rivers of {substance}. After enjoying some
        {food}, they gather their strength and {verb} to confront {villian} in
        the final showdown. Will the {adjective} heroes save the day?
        """
    ),

    'sw_story15': StarWarsStory(
        ["character", "sidekick", "villian", "weapon", "vehicle", "animal",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun"],
        """
        In the swamps of {planet}, the {adjective} Jedi {character} and their
        brave sidekick {sidekick} are on a mission to stop {villian}. With the
        {weapon} in hand, they fly across the sky in the {vehicle}. They
        encounter dangerous {animal} and strange pools of {substance}. Taking
        a break for some {food}, they prepare for the final stage of their
        quest to {quest}. They must {verb} quickly to save the sacred {noun} 
        before the {color} forces of darkness consume the planet.
        """
    )
}
