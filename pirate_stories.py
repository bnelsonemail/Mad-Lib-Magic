"""Madlibs Pirate Stories."""


class PirateStory:
    """A Mad Libs Pirate Story.

    To create a Pirate story, pass a list of prompts and the text
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


# Collection of Pirate Themed Stories
PirateStories = {
    'p_story1': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship",
         "substance", "color", "location", "food", "treasure", "adjective", 
         "verb", "noun", "creature"],
         """Captain {character} and {sidekick} sailed the mighty {ship}. 
         Their journey to the {location} was fraught with danger. The villainous 
         {villain} awaited with a {color} {creature} guarding the stolen {treasure}. 
         With a trusty {weapon} in hand, they fought fiercely. The air smelled 
         of {food}, and the sea churned with {substance}. In the end, {character} 
         {verb} the villain's {noun}, claiming the {adjective} treasure for their 
         own."""
    ),

    'p_story2': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship",
         "substance", "color", "location", "food", "treasure", "adjective", 
         "verb", "noun", "creature"],
         """On a stormy night aboard the {ship}, {character} and {sidekick} faced 
         {villain}, a feared pirate known for his {adjective} deeds. The treasure 
         buried in {location} was said to be cursed by a {color} {creature}. 
         Armed with only a {weapon} and a pocket of {substance}, {character} 
         had to {verb} through danger, battling {villain} over a plate of {food}, 
         finally finding the {noun} that led to the lost {treasure}."""
    ),

    'p_story3': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship",
         "substance", "color", "location", "food", "treasure", "adjective", 
         "verb", "noun", "creature"],
         """{character} set sail aboard the {ship}, determined to recover the 
         {treasure} stolen by {villain}. The {adjective} winds howled through the 
         {location}, and {sidekick} warned of the {color} {creature} lurking in 
         the waters. With their trusty {weapon} and a bag of {food}, {character} 
         confronted the villain. After a {verb} with {substance} and steel, 
         {character} claimed victory and the prized {noun}."""
    ),

    'p_story4': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship",
         "substance", "color", "location", "food", "treasure", "adjective", 
         "verb", "noun", "creature"],
         """In the darkest depths of the {location}, {character} encountered 
         the ruthless {villain}, whose {color} {creature} prowled the waters 
         around the {ship}. With {sidekick} by their side, and wielding a 
         {weapon}, they battled to reclaim the cursed {treasure}. The air 
         thick with {substance}, {character} {verb} the villain's {noun}, 
         only to discover the treasure's {adjective} power. The taste of {food} 
         lingered in the cold air."""
    ),

    'p_story5': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship",
         "substance", "color", "location", "food", "treasure", "adjective", 
         "verb", "noun", "creature"],
         """Aboard the creaking {ship}, {character} and {sidekick} faced the 
         eerie {location}, where the villainous {villain} hid with the coveted 
         {treasure}. A {color} {creature} roamed the area, its eyes gleaming with 
         hunger. Armed with a {weapon} and a {noun}, {character} fought with 
         {substance} and fury, finally {verb} the {adjective} prize, as the 
         smell of {food} mixed with the salty sea breeze."""
    ),
    'p_story6': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """The notorious {character} and {sidekick} sailed the {ship} to the 
         cursed {location}. There, the {adjective} pirate {villain} waited with 
         a {weapon} made of {substance}. {character} had to {verb} across the 
         stormy sea, fending off the {color} {creature}. With a belly full of 
         {food}, they finally found the hidden {treasure}, stored in a 
         mysterious {noun}."""
    ),

    'p_story7': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """Captain {character} and their loyal {sidekick} set sail on the 
         {adjective} seas, hunting for the {treasure} hidden by {villain}. 
         They traveled to {location}, battling the waves and a {color} 
         {creature}. Armed with a {weapon}, {character} faced the villain 
         who tried to stop them with a {noun} filled with {substance}. The 
         scent of {food} filled the air as the battle raged, and {character} 
         {verb} to victory."""
    ),

    'p_story8': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """In the eerie {location}, {character} and {sidekick} searched for 
         the legendary {treasure}, guarded by {villain} and a {color} 
         {creature}. With a {weapon} made of {substance} in hand, they 
         journeyed through the {adjective} caves. As they {verb}, the scent 
         of {food} lingered, and they finally uncovered the treasure hidden 
         inside a {noun} aboard the cursed {ship}."""
    ),

    'p_story9': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """The {adjective} {ship} sailed under the command of {character}, 
         with {sidekick} at their side. Their journey led to the {location}, 
         where they sought {treasure} hidden by the vile {villain}. But before 
         they could claim it, a {color} {creature} rose from the sea. With 
         their {weapon}, they {verb} through the storm of {substance}, the air 
         filled with the smell of {food}, finally discovering a {noun} containing 
         their prize."""
    ),

    'p_story10': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """As the fog lifted over the {location}, {character} and {sidekick} 
         spotted the dreaded {villain} aboard the {adjective} {ship}. Armed 
         with a {weapon}, they ventured into the battle, dodging a {color} 
         {creature} in the water. The clash over the {treasure} was fierce, 
         with {substance} raining down. The smell of {food} lingered in the air 
         as they {verb} the final blow, securing the treasure hidden in a 
         {noun}."""
    ),
    'p_story11': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """Under the blood-red moon, {character} and {sidekick} sailed their 
         {adjective} {ship} to the eerie {location}, searching for the lost 
         {treasure}. The villainous {villain} guarded it with a {color} 
         {creature}. Armed with a {weapon} dripping with {substance}, {character} 
         {verb} through the mist, the scent of {food} filling the air. At last, 
         the {noun} revealed the cursed treasure."""
    ),

    'p_story12': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """Darkness fell as {character} was forced to walk the plank by the 
         ruthless {villain}. Below, the {color} {creature} circled the {ship}, 
         ready to strike. With {sidekick} watching helplessly, {character} 
         clutched a {noun} and {verb} off the edge. As the sea swallowed them, 
         they could taste the {food}, the scent of {substance} lingering, with 
         only the cursed {treasure} left behind."""
    ),

    'p_story13': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """In the foggy waters near {location}, {character} and {sidekick} 
         faced the dreaded {villain}. The {color} {creature} lurked beneath 
         their {adjective} {ship}, waiting for a chance to strike. As they 
         battled with a {weapon} covered in {substance}, {character} fought to 
         {verb} through the chaos, the taste of {food} bitter on their tongue, 
         before the {noun} revealed the ancient {treasure}."""
    ),

    'p_story14': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """The cursed {ship} sailed through the dark waters of {location}, with 
         {character} and {sidekick} on a desperate mission. The {adjective} 
         {villain} had stolen the {treasure} and set loose a {color} {creature}. 
         Armed with a {weapon}, {character} faced off, their hands slick with 
         {substance}. The smell of {food} mixed with the sea as they {verb} the 
         villain's {noun}, claiming the treasure once more."""
    ),

    'p_story15': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """Aboard the ghostly {ship}, {character} and {sidekick} braved the 
         cursed {location}. There, the {adjective} {villain} lay in wait, 
         guarding the {treasure} with a {color} {creature}. With a {weapon} 
         dripping {substance}, {character} {verb} through the battle. The 
         {noun} they carried held the key, and the scent of {food} lingered as 
         the treasure was claimed."""
    ),

    'p_story16': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """The cold waters around {location} were filled with mystery as 
         {character} and {sidekick} neared the hidden {treasure}. The feared 
         {villain} awaited aboard the {adjective} {ship}, a {color} {creature} 
         by their side. Armed with only a {weapon} and {substance}, {character} 
         {verb} through the thick fog, the scent of {food} in the air, 
         discovering the treasure beneath the ancient {noun}."""
    ),

    'p_story17': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """The sea roared as {villain} forced {character} to walk the plank 
         off the {adjective} {ship}. Below, the {color} {creature} waited in 
         the waters, ready to strike. {sidekick} watched in horror as {character} 
         clutched a {noun} and {verb} into the deep. The smell of {food} from 
         the villain's feast mixed with the salt air, while the cursed {treasure} 
         remained locked away in {location}."""
    ),

    'p_story18': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """In the cursed {location}, {character} and {sidekick} searched for 
         the fabled {treasure}, hidden by the notorious {villain}. The air was 
         thick with the scent of {food} and {substance}. Armed with a {weapon}, 
         {character} faced a {color} {creature} guarding the {adjective} prize. 
         After a fierce {verb}, they uncovered the treasure buried within the 
         ancient {noun} aboard their {ship}."""
    ),
    'p_story19': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """In the dark heart of {location}, {character} and {sidekick} sought 
         the legendary {treasure}. The {adjective} {villain} guarded it, hiding 
         aboard the cursed {ship}. As the winds howled and the sea churned with 
         {substance}, {character} prepared their {weapon}. With a fierce cry, 
         they charged, facing the {color} {creature} that awaited them. After a 
         brutal fight, the scent of {food} filled the air as {character} finally 
         {verb} the villain's {noun}, claiming the treasure and their victory."""
    ),

    'p_story20': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """The sea was calm as {character} sailed the {adjective} {ship} to the 
         remote {location}. Hidden deep within its caves was the fabled 
         {treasure}, guarded by the cruel {villain}. With {sidekick} by their 
         side, they prepared their {weapon}, aware that the {color} {creature} 
         lurked nearby. The air smelled of {food}, and the ground was slick with 
         {substance}. After a long battle, they finally {verb}, the {noun} 
         revealing the cursed prize they sought."""
    ),

    'p_story21': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """Beneath the looming cliffs of {location}, {character} and {sidekick} 
         prepared for their final confrontation with {villain}. The {color} 
         {creature} swam beneath the waves as the crew of the {adjective} {ship} 
         readied their {weapon}. With a smell of {food} in the air and 
         {substance} covering the deck, {character} charged forward. After a 
         fierce fight, they {verb}, leaving {villain}'s {noun} broken and the 
         treasure theirs at last."""
    ),

    'p_story22': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """The moon cast an eerie glow on the waters around {location}. 
         {character} and {sidekick} anchored their {adjective} {ship} and 
         crept ashore, searching for the hidden {treasure}. {villain} was near, 
         guarded by a {color} {creature}. With a {weapon} in hand and a bag of 
         {food} for sustenance, {character} {verb} through the fog. The ground 
         was soaked with {substance}, but at last, the {noun} revealed the 
         prize they sought."""
    ),

    'p_story23': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """In the darkest depths of {location}, {character} was forced to walk 
         the plank by the wicked {villain}. Below, the {color} {creature} 
         swam, waiting for its prey. {sidekick} watched helplessly from the 
         deck of the {ship}, a {noun} gripped in their hands. As {character} 
         {verb} into the waters, the scent of {food} hung in the air, and 
         {substance} stained the sea. The treasure lay hidden, still beyond 
         their reach."""
    ),

    'p_story24': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """On the deck of the {adjective} {ship}, {character} faced {villain}, 
         who held the {treasure} hostage. The {color} {creature} lurked nearby, 
         its eyes glowing in the moonlight. With a {weapon} dripping with 
         {substance}, {character} battled furiously, while {sidekick} 
         {verb} across the deck. The air was thick with the smell of {food}, 
         and the ancient {noun} finally revealed the treasure's true location."""
    ),

    'p_story25': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """In the dead of night, {character} and {sidekick} made their way to 
         {location}, where the {adjective} {villain} had hidden the fabled 
         {treasure}. Their {ship} creaked ominously as the {color} {creature} 
         circled beneath. Armed with a {weapon} soaked in {substance}, they 
         prepared for battle. The taste of {food} lingered as they {verb} into 
         the unknown, the {noun} offering clues to the cursed treasure's final 
         resting place."""
    ),

    'p_story26': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """As dawn broke over {location}, {character} and {sidekick} prepared 
         for the final leg of their journey. The {treasure} awaited, but 
         {villain} was close behind. Aboard their {adjective} {ship}, they 
         sharpened their {weapon}, knowing that the {color} {creature} lurked 
         below. The scent of {food} filled the air as they {verb}, leaving a 
         trail of {substance} behind. The ancient {noun} in their hands pulsed 
         with energy, leading them to their prize."""
    ),

    'p_story27': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """On the deck of the {adjective} {ship}, {character} and {sidekick} 
         prepared for their greatest challenge. {villain} awaited them in the 
         depths of {location}, where the {color} {creature} had been seen last. 
         Armed with a {weapon} and a sack of {food}, they faced the long battle 
         ahead. As {character} {verb} through the mist, the sound of {substance} 
         hitting the water grew louder. At last, the {noun} revealed the 
         {treasure}, but its curse was far worse than they had imagined."""
    ),

    'p_story28': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """The storm raged as {character} and {sidekick} battled across the 
         deck of the {ship}. {villain} had the {treasure} within reach, but the 
         {color} {creature} swirled in the depths below. As {character} wielded 
         their {weapon}, covered in {substance}, they {verb} through the chaos. 
         The scent of {food} mixed with the salt air as the battle raged. 
         Finally, the ancient {noun} revealed the treasure's secret, but it came 
         with a deadly price."""
    ),
    'p_story29': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """As the cursed {ship} drifted into the fog near {location}, 
         {character} and {sidekick} readied themselves. They knew that 
         {villain} and the {color} {creature} guarded the ancient {treasure}. 
         With a {weapon} soaked in {substance}, {character} stepped forward. 
         The taste of {food} was still on their lips as they {verb} into the 
         battle. At last, the {noun} gave them what they sought: the {adjective} 
         treasure of legend."""
    ),

    'p_story30': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """The wind howled as {character} faced {villain} at the bow of the 
         {adjective} {ship}. {sidekick} tried to hold off the {color} 
         {creature}, but the battle was fierce. Armed with a {weapon}, 
         dripping with {substance}, {character} struck out, the scent of 
         {food} in the air. As the final blow landed, they {verb}, claiming 
         the {noun} and the hidden {treasure} that had eluded them for so long."""
    ),

    'p_story31': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """The crew of the {adjective} {ship} gathered as {character} and 
         {sidekick} set off for {location}. Their goal was the lost {treasure} 
         that {villain} had hidden long ago. A {color} {creature} lurked in 
         the deep, waiting for the right moment to strike. With a {weapon} 
         and a pack of {food}, {character} braved the seas, the air thick 
         with {substance}. They finally {verb}, the {noun} leading them to the 
         prize they had so desperately sought."""
    ),

    'p_story32': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """{character} and {sidekick} navigated the treacherous waters of 
         {location}, searching for the {treasure}. The {adjective} {ship} 
         creaked under the weight of the {substance}-soaked decks. The vile 
         {villain} awaited them, and the {color} {creature} circled below. 
         With their {weapon} ready and the scent of {food} in the air, 
         {character} {verb} toward the battle, finally uncovering the 
         {noun} that hid the ancient treasure."""
    ),

    'p_story33': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """Under a blood-red moon, {character} and {sidekick} approached 
         {location}, their {adjective} {ship} barely afloat. The {color} 
         {creature} that guarded the {treasure} could be seen just beneath 
         the waves. With a {weapon} in hand and their hearts filled with 
         dread, they {verb} toward the shore. The smell of {food} mixed with 
         the tang of salt, and as the ground turned to {substance}, the {noun} 
         revealed the cursed treasure of {villain}."""
    ),

    'p_story34': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """As the storm raged on, {character} and {sidekick} battled across 
         the deck of the {adjective} {ship}. {villain} had the cursed 
         {treasure} within reach, but the {color} {creature} circled the ship, 
         waiting to strike. With a {weapon} soaked in {substance}, {character} 
         struck, the scent of {food} in the air. As they {verb}, the ancient 
         {noun} revealed the treasure, but its curse would soon be unleashed."""
    ),

    'p_story35': PirateStory(
        ["character", "sidekick", "villain", "weapon", "ship", "substance", 
         "color", "location", "food", "treasure", "adjective", "verb", "noun", 
         "creature"],
         """Aboard the {adjective} {ship}, {character} and {sidekick} were 
         trapped by the treacherous {villain}. The smell of {food} mixed with 
         the salty air as they faced a decision: walk the plank into the jaws 
         of the {color} {creature} below, or fight to reclaim the lost 
         {treasure}. Armed with a {weapon} and slick with {substance}, 
         {character} {verb}, discovering the {noun} that held the key to 
         their victory."""
    ),
}