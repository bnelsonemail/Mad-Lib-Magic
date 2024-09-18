"""Madlibs Stories."""


class Story:
    """A Madlibs story.

    To create a story, pass a list of prompts and the text
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


# Collection of stories
STORIES = {
    'story1': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """Once upon a time in a long-ago {place}, there lived a large
        {adjective}
        {noun}. It loved to {verb} {plural_noun} and enjoyed a feast of {food}
        every day. One day, while {verb}ing, it encountered a {color} {animal}
        that was guarding a treasure made of {substance}. Just as things were
        getting tense, {superhero} appeared to help resolve the situation and
        bring peace to the {place}."""
    ),
    'story2': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """One day, a {adjective} {noun} decided to go on an adventure. It
        packed a {adjective} {noun} and a {adjective} {noun}. Along the way, it
        met a {adjective} {animal} who offered it a {food} in exchange for a
        {noun}. Together, they {verb} through the {adjective} {place} until
        they found the {plural_noun} of their dreams. Just when they thought
        their journey was over, {superhero} appeared and helped them navigate
        through the {adjective} challenges they faced."""
    ),
    'story3': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """
        Once upon a time, a {adjective} {noun} discovered a secret recipe
        for a magic potion. The ingredients included twelve {plural_noun}, a
        dash of {adjective} {substance}, a sprinkle of {adjective} {substance},
        and a hint of {food}. When the {noun} mixed it all together, it turned
        into a {adjective} {color} {noun} that could {verb} anyone who drank
        it! Just as the potion was about to be tested, {superhero} swooped in
        to see if it could help save the day.
        """
    ),
    'story4': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """At the {place} Zoo, a {adjective} {animal} managed to escape from
        its enclosure. It ran through the {place}, knocking over
        {plural_noun} and causing a {adjective} commotion. The zookeepers
        tried to {verb} it with a {noun} made of {substance}, but the {color}
        {animal} was too fast! Just when all hope seemed lost, {superhero}
        arrived with a special {food} that the {animal} couldn't resist.
        Eventually, it was lured back to its cage with a trail of {food}."""
        ),
    'story5': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """In the middle of the {place}, there was an enchanted forest where
        all the {plural_noun} were made of {substance}. One day, a {adjective}
        traveler found a {color} {noun} lying on the ground. When they picked
        it up, it began to {verb}, and all the {animal} in the forest gathered
        around, speaking in {adjective} voices. Just as the traveler pondered
        what to do next, {superhero} appeared with a basket of {food}.
        Together,they decided to take the {noun} to the {place} to solve the
        mystery, sharing the {food} along the way."""
        ),

    'story6': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """Deep in the heart of {place}, a {adjective} wizard was brewing a
        magical potion in a {noun} made of {substance}. The potion required a
        {color} {animal}, a handful of {plural_noun}, and a pinch of {food}. As
        the wizard began to {verb} the ingredients, the potion bubbled and
        turned into a {adjective} {color} liquid. Just then, {superhero}
        arrived to witness the magic. When the potion was complete, it had the
        power to {verb} anyone who drank it!"""
        ),

    'story7': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """Legend says that buried deep in the {place} lies a chest full of
        {plural_noun}. A group of {adjective} adventurers set out on a quest to
        find it. Along the way, they encountered a {color} {animal} guarding a
        {noun} made of {substance}. To pass, they had to {verb} the {animal}
        using only a {adjective} {noun} and a delicious {food} they found in
        the {place}. Just as the adventurers were about to give up, {superhero}
        appeared and helped them with the final challenge."""
        ),

    'story8': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """During a stormy night, a shipwrecked sailor washed ashore on a
        {adjective} island in the middle of the {place}. The island was covered
        in {color} {plural_noun} and the air smelled of {substance}. As the
        sailor began to explore, they encountered a {adjective} {animal} that
        seemed to be guarding a {noun}. The sailor realized that the only way
        off the island was to {verb} the {animal} using a {adjective} {noun}
        they found buried in the sand and a bit of {food} they had saved from
        the ship. Just as hope seemed lost, {superhero} arrived to assist in
        the daring escape."""
        ),

    'story9': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """In a hidden laboratory deep within the {place}, a {adjective}
        scientist was working on a secret experiment. They were trying to
        create a {color} {noun} that could {verb} on its own. The lab was
        filled with {plural_noun} and the smell of {substance} hung in the air.
        One day, a {adjective} {animal} wandered into the lab, knocking over a
        {noun}, and causing the experiment to go terribly wrong! Now, the lab
        is filled with {color} {plural_noun} that can {verb}! Just as the
        chaosen sued, {superhero} burst in, armed with a special {food} to help
        contain the situation."""
        ),

    'story10': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """
        On a quiet evening in the {place}, the sky suddenly turned {color} as
        a fleet of alien {plural_noun} descended from the clouds. The aliens,
        resembling {adjective} {animal}, landed their ships made of {substance}
        and began to {verb} all the {plural_noun} they could find. In a
        desperate attempt to save the {place}, the townspeople used a {noun}
        and some {food} to create a {adjective} device that would {verb} the
        aliens back into space. Just when it seemed all hope was lost,
        {superhero} arrived to lend a hand in the final showdown.
        """
        ),

    'story11': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """In the middle of {place}, there was a mysterious cave where a
        {adjective} {animal} lived. The cave walls were lined with {substance},
        and the {color} glow filled the entire space. One day, a {adjective}
        traveler found a {noun} inside the cave and discovered that it had the
        power to {verb}. With the help of {superhero}, they used the {noun} to
        bring {food} to everyone in the land."""
        ),

    'story12': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """High in the mountains of {place}, a {color} dragon guarded a hoard
        of {plural_noun}. The dragon was known to be {adjective} and could
        breathe fire made of {substance}. One day, a group of adventurers set
        out with a {noun} to try and {verb} the dragon. With a special recipe
        of {food}, they sought the help of {superhero} to tame the beast and
        share the {plural_noun} with everyone."""
        ),

    'story13': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """Deep in the enchanted forest of {place}, a {adjective} witch was
        known for brewing potions in her {color} cauldron. The potions
        required {plural_noun} and a sprinkle of {substance}. One day, the
        witch found a {noun} that could {verb} all by itself. But when a
        {adjective} {animal} entered her cottage, chaos ensued. Luckily,
        {superhero} arrived with a basket of {food} to calm the situation."""
        ),

    'story14': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """On a distant planet in the {place} galaxy, there lived a colony of
        {adjective} aliens. They communicated by {verb}ing with their
        {plural_noun} made of {substance}. One day, a {color} meteor crashed
        into their world, bringing with it a {noun} that could change
        everything. With the help of {superhero}, they discovered that the
        meteor contained a new source of {food} that could sustain their
        entire species."""
        ),

    'story15': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """In a bustling marketplace in the heart of {place}, a {adjective}
        merchant sold {plural_noun} made of {substance}. One day, a {color}
        {animal} wandered into the market, causing a scene by trying to {verb}
        everything in sight. The merchant, using a {noun} they found in the
        market, and with the help of {superhero}, managed to calm the {animal}
        by offering it some delicious {food}."""
        ),

    'story16': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """At the {place} Carnival, there was a {adjective} ride that everyone
        wanted to try. It was decorated with {plural_noun} and powered by a
        special {substance}. One day, a {color} {animal} escaped from its
        enclosure and started to {verb} all over the carnival. Just when things
        seemed out of control, {superhero} arrived with a snack of {food} to
        lure the {animal} back to safety."""
        ),

    'story17': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """In the quiet village of {place}, there was an ancient legend about
        a {adjective} treasure hidden deep within the woods. The treasure was
        said to be guarded by a {color} {animal} that could {verb} anyone who
        came near. One day, a group of villagers, armed with a {noun} and a
        stash of {food}, set out to find the treasure. With the help of
        {superhero}, they were able to outwit the {animal} and uncover the
        {plural_noun}."""
            ),

    'story18': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """On a rainy day in {place}, a {adjective} inventor was busy creating
        a new {noun} that could {verb} {plural_noun}. The workshop was filled
        with the scent of {substance}, and a {color} light flickered from the
        machine. Just as the invention was about to be tested, a {adjective}
        {animal} knocked over the equipment. Fortunately, {superhero} arrived
        with some {food} to save the day and finish the invention."""
        ),

    'story19': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """In the ancient ruins of {place}, archaeologists discovered a {color}
        {noun} that was said to have the power to {verb}. The ruins were filled
        with {plural_noun} made of {substance}, and the air was thick with
        mystery. A {adjective} {animal} guarded the {noun}, making it difficult
        to retrieve. But with the help of {superhero} and a well-timed offering
        of {food}, the archaeologists managed to uncover the secret of the
        {noun}."""
        ),

    'story20': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """In the magical kingdom of {place}, a {adjective} {animal} ruled over
        all. The kingdom was known for its {color} {plural_noun} made of
        {substance}. One day, the {animal} decreed that a {noun} should be
        created that could {verb} throughout the land. However, a mysterious
        curse threatened the kingdom, and only the brave {superhero}, with a
        special dish of {food}, could save the day."""
        ),

    'story21': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """In the dark forests of {place}, a powerful sorcerer was on a quest
        to find the ancient {noun} that could {verb} the fate of the kingdom.
        The forest was filled with {adjective} creatures and glowing {color}
        {plural_noun} made of {substance}. As the sorcerer ventured deeper, a
        {adjective} {animal} appeared, guarding a hidden stash of {food}. With
        the help of {superhero}, the sorcerer was able to retrieve the {noun}
        and save the realm."""
        ),

    'story22': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """In a remote Jedi temple on {place}, a young Padawan faced their
        final trial. The temple was adorned with ancient {plural_noun} made of
        {substance}, and the air was filled with the scent of {adjective}
        incense. The Padawan was tasked with finding a {color} {noun} that
        could {verb} when held by the true heir of the Force. Along the way,
        they encountered a {adjective} {animal} that challenged their strength.
        With the guidance of {superhero} and a ration of {food}, the Padawan
        completed the trial and became a Jedi Knight."""
        ),

    'story23': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """In the heart of {place}, a great battle raged between the forces of
        good and evil. The knights of the realm, clad in {color} armor made of
        {substance}, fought bravely against the dark sorcerer and his army of
        {adjective} {plural_noun}. A brave knight wielded a legendary {noun}
        that could {verb} enemies with a single strike. As the battle reached
        its climax, {superhero} arrived with a feast of {food} to restore the
        knights' strength and turn the tide of battle."""
        ),

    'story24': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """In a hidden laboratory on the distant planet of {place}, a
        {adjective} sorcerer of the Sith was crafting a powerful {color}
        potion. The lab was filled with ancient {plural_noun} and the walls
        were coated with a mysterious {substance}. The potion required the
        essence of a {adjective} {animal} and a rare {noun} that could {verb}
        across the galaxy. Just as the sorcerer was about to complete his work,
        {superhero} intervened, offering a unique {food} that could neutralize
        the potion's effects and save the galaxy from darkness."""
        ),

    'story25': Story(
        ["place", "noun", "verb", "adjective", "plural_noun", "animal",
         "substance", "color", "food", "superhero"],
        """On the planet {place}, a legendary knight discovered an ancient
        starship hidden beneath a {color} mountain. The starship was powered by
        {substance} and guarded by {adjective} {plural_noun} that could {verb}
        anyone who approached. The knight, armed with a {noun} and a trusty
        {adjective} {animal}, boarded the starship. With the help of
        {superhero} and a stash of {food}, the knight unlocked the starship's
        secrets and embarked on a new adventure across the galaxy."""
        ),
}

# Example usage of the Story class
# ans = {
#     "place": "forest",
#     "noun": "dragon",
#     "verb": "collect",
#     "adjective": "mighty",
#     "plural_noun": "treasures"
# }
