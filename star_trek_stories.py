"""Madlibs Star Trek Stories."""


class StarTrekStory:
    """A Mad Libs Star Trek Story.

    To create a Star Trek story, pass a list of prompts and the text
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
StarTrekStories = {
    'st_story1': StarTrekStory(
        ["captain", "species", "villian", "starship", "tech",
         "substance", "color", "planet", "food", "quest", "adjective", "verb",
         "noun", "creature", "phenomenon"],
         """ 
        In the far reaches of space, Captain {captain} of the USS {starship}
        embarked on a daring mission. Their mission: to find the rare
        substance known as {substance}, a precious material believed to
        possess unimaginable powers. The search led the crew to the
        mysterious planet {planet}, home to the elusive species {species}.
        
        However, the captain’s crew wasn't the only one seeking this rare
        substance. A notorious villain by the name of {villain} was also
        after it, using their formidable tech {tech} to gain an upper hand.
        They'd do anything to claim the {color} substance for themselves.
        
        As the starship descended through the atmosphere of the strange
        planet, the crew was greeted by the sight of giant creatures known
        as {creature} roaming across the horizon, devouring the local food
        known as {food}. The atmosphere was thick with a strange phenomenon
        called {phenomenon}, which made the air shimmer in a/an {adjective}
        hue.
        
        The captain, determined to complete the {quest}, ordered their team
        to {verb} into action. With bravery in their hearts and the fate of
        the galaxy on the line, they ventured deep into the unknown. After
        many challenges, the captain found the {noun}, which would change
        the future of the Federation forever.
        
        The adventure had only just begun.
        """
    ),
    'st_story2': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        Captain {captain} faced their most dangerous foe yet: the {species}
        warlord {villain}, who had captured the USS {starship} and stolen a
        powerful {tech}. This {substance}-powered weapon was hidden on
        {planet}, a place known for its {adjective} landscape. The team had
        to {verb} quickly before the {color} explosion of the {phenomenon}
        sealed their fate.
        
        Upon arrival, the crew encountered a native {creature}, known for
        eating {food}, and together they sought the legendary {noun}, which
        held the key to completing their {quest}.
        """
    ),
    'st_story3': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        Deep in uncharted space, Captain {captain} and the crew of the USS
        {starship} received a distress call from the {species} colony on
        {planet}. A terrifying villain, {villain}, had developed a {tech}
        that could turn the precious {substance} of the planet into a {color}
        substance capable of destroying entire worlds.
        
        The crew, led by the brave captain, needed to {verb} through {adjective}
        weather conditions and survive the hostile {creature} of {planet}.
        Their only hope was to find the ancient {noun} before the {phenomenon}
        rendered their {quest} impossible.
        """
    ),
    'st_story4': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        On a routine mission, Captain {captain} of the USS {starship}
        discovered a mysterious {color} energy source on {planet}. This
        strange {substance} had piqued the interest of a villainous {species}
        warlord named {villain}, who sought to harness its power with their
        {tech}.
        
        While investigating, the crew encountered a massive {creature}
        feasting on the local {food}. As the crew attempted to {verb} closer,
        a dangerous {phenomenon} struck, turning the mission into a {adjective}
        race against time. The quest for the {noun} became the key to the
        entire galaxy's survival.
        """
    ),
    'st_story5': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        Captain {captain} and the crew of the USS {starship} were dispatched
        to {planet} after reports of a strange {phenomenon} affecting the
        {species} inhabitants. A powerful {villain}, armed with a mysterious
        {tech}, had been manipulating the local {substance}, turning it into
        {color} crystals.
        
        The crew’s mission was to {verb} the crystals before they fell into
        the wrong hands. The crew faced not only the villain but also
        dangerous {creature} swarms and strange weather patterns. Their
        only chance at success lay in recovering the legendary {noun} to
        complete their {quest}.
        """
    ),
    'st_story6': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        The crew of the USS {starship} was investigating a series of strange
        energy readings from the planet {planet}. Captain {captain} led an
        away team to uncover the source of the anomaly. Their discovery was
        shocking—a villain named {villain} was using advanced {tech} to
        harness a rare {substance}, causing the planet’s {adjective} sky to
        shimmer with {color} light.
        
        The planet’s native {species}, desperate for help, shared tales of a
        {creature} that had guarded the fabled {noun} for centuries. To save
        the planet, the captain had to {verb} past the dangerous {phenomenon}
        and recover the {noun} in time to complete their {quest}.
        """
    ),
    'st_story7': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        Captain {captain} and the crew of the USS {starship} found themselves
        in orbit around {planet}, where a mysterious {phenomenon} had caused
        a breakdown in communication with the {species} colony below. 
        The crew learned that the dangerous {villain} was using {tech} to
        manipulate the planet's core, turning the rare {substance} into {color}
        crystals with disastrous effects.
        
        To stop the villain, the crew had to venture into the wilds of {planet},
        where they encountered the legendary {creature}, known for eating 
        {food}. As they raced to complete the {quest}, they had to {verb} 
        their way through a maze of {adjective} challenges in order to retrieve
        the ancient {noun} that could save the colony.
        """
    ),
    'st_story8': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        The starship USS {starship}, under the command of Captain {captain},
        was sent to investigate an unusual reading near the planet {planet}.
        The crew soon discovered a deadly {phenomenon} caused by a device
        designed by the villainous {species} scientist, {villain}. This device
        used {tech} to convert the planet's natural {substance} into dangerous
        {color} radiation, threatening the entire sector.
        
        The captain and their team were tasked with dismantling the device and
        stopping the {adjective} plan. Along the way, they had to {verb} past 
        aggressive {creature} that guarded the site. The mission led to the 
        discovery of an ancient {noun}, said to be the key to completing the 
        crew's urgent {quest}.
        """
    ),
    'st_story9': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        On their latest adventure, Captain {captain} and the crew of the USS
        {starship} received a distress signal from the {species} homeworld,
        {planet}. A ruthless villain, {villain}, had developed a new {tech}
        that could transform the planet's valuable {substance} into a {color}
        weapon of mass destruction.
        
        To stop the villain, the crew needed to retrieve an ancient {noun}
        hidden deep within the planet's {adjective} caverns. Along the way, 
        they encountered the fearsome {creature}, known for its taste for 
        {food}. Their success depended on their ability to {verb} through 
        treacherous terrain and end the villain's evil {quest}.
        """
    ),
    'st_story10': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        When the USS {starship} arrived at the planet {planet}, Captain
        {captain} and their crew discovered the aftermath of a devastating
        attack by the villain {villain}, who had used advanced {tech} to
        weaponize the rare {substance}. This {substance} emitted a {color}
        light that rendered entire regions of the planet uninhabitable.
        
        The crew's only hope was to find the {noun}, a fabled relic that could
        neutralize the {substance}'s effects. However, they first had to {verb}
        their way through dangerous {adjective} conditions and avoid being 
        detected by the planet's native {creature}, known for their love of 
        {food}. The quest to save the planet had just begun.
        """
    ),
    'st_story11': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        Captain {captain} was called to the planet {planet}, where the {species}
        inhabitants were facing the threat of total destruction. The villain
        {villain} had developed a {tech} capable of extracting the planet's
        {substance}, turning it into a powerful {color} energy source that 
        could wipe out entire solar systems.
        
        To stop this catastrophic plan, the crew had to navigate through the
        treacherous environment of {planet}, where they encountered the rare
        {creature} that subsisted on {food}. The captain's team needed to {verb}
        past the {adjective} landscape to find the legendary {noun}, which 
        was rumored to be the only way to thwart the villain and complete the 
        {quest}.
        """
    ),
    'st_story12': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        The USS {starship} was dispatched to the remote planet {planet}, where
        a strange {phenomenon} was interfering with all starship navigation.
        Captain {captain} and their team soon learned that {villain}, a rogue
        member of the {species}, had harnessed {tech} to alter the very fabric
        of space-time using the planet's {substance}. 

        To restore balance, the crew needed to find the legendary {noun}, which
        could undo the damage caused by the {phenomenon}. As they ventured into
        the heart of the planet, they encountered a massive {creature} known 
        for feeding on {food}. Their only chance was to {verb} past the
        {adjective} hazards to complete the {quest} and save the galaxy.
        """
    ),
        'st_story13': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        When the USS {starship} approached the desolate planet {planet},
        Captain {captain} and their crew discovered the {species} were under
        siege by the notorious villain {villain}. Armed with a powerful {tech},
        {villain} was harvesting the rare {substance}, which emitted a deadly
        {color} glow that threatened the planet’s survival.

        To stop this menace, the crew had to {verb} across the treacherous
        {adjective} landscape, while fending off attacks from the local 
        {creature}, known for its taste for {food}. The key to their success
        lay in finding the ancient {noun}, which could turn the tide in their
        {quest} to save the planet.
        """
    ),
    'st_story14': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        The USS {starship}, led by Captain {captain}, received a distress call
        from the {species} colony on {planet}. Their vital {substance} had 
        been corrupted by the villain {villain}, who used {tech} to alter its
        structure, turning it into {color} crystals that destabilized the planet.

        The crew faced an urgent mission to {verb} into the dangerous {adjective}
        wilderness, where they would confront the fearsome {creature} that had 
        adapted to this new environment. Their only hope lay in finding the
        legendary {noun} before the {phenomenon} overtook the planet, ending
        their {quest}.
        """
    ),
    'st_story15': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        During an exploratory mission to {planet}, Captain {captain} of the USS
        {starship} discovered a hidden {species} base under siege by the villain
        {villain}. Using their stolen {tech}, {villain} had turned the planet's
        precious {substance} into a volatile {color} substance capable of 
        destroying ships in orbit.

        The crew’s mission: {verb} their way past hostile {creature} nests and
        the volatile {phenomenon} sweeping the planet. With only hours left to 
        complete their {quest}, they searched for the lost {noun} that could
        neutralize the threat and restore peace to {planet}.
        """
    ),
    'st_story16': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        The mysterious planet {planet} held the key to solving the Federation's
        energy crisis. Captain {captain} of the USS {starship} led an expedition
        to retrieve the rare {substance}, but soon found themselves in a race
        against time. The villain {villain} was also after the substance, using
        their {tech} to extract it and turn it into a {color} energy weapon.

        To stop the villain, the crew had to {verb} past the planet's {adjective}
        jungles, evade the deadly {creature}, and confront the {phenomenon} that
        threatened to consume the planet. Only the legendary {noun} could ensure
        success in their dangerous {quest}.
        """
    ),
    'st_story17': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        Captain {captain} of the USS {starship} was sent to the remote planet
        {planet}, where the villain {villain} had activated a deadly {tech}.
        The device was powered by the local {substance}, which turned into a
        {color} energy field that threatened to destroy the planet's delicate
        ecosystem.

        The crew had to {verb} into action, navigating {adjective} terrain,
        dodging hostile {creature}, and managing to avoid the dangerous 
        {phenomenon} plaguing the planet. Their goal was to find the ancient 
        {noun} that could deactivate the device and complete their {quest}.
        """
    ),
    'st_story18': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        The crew of the USS {starship} was assigned a top-secret mission to
        investigate the remote planet {planet}, where a strange {phenomenon} was
        draining the planet's energy. Captain {captain} led the away team, but
        soon discovered that the villain {villain} had created a dangerous {tech}
        that transformed the planet’s {substance} into a deadly {color} force.

        The team faced a series of challenges as they tried to {verb} past the 
        native {creature}, known for its love of {food}. Time was running out, 
        and only the discovery of the ancient {noun} would allow the crew to 
        complete their {quest} and save {planet}.
        """
    ),
    'st_story19': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        When the USS {starship} encountered a temporal anomaly near {planet}, 
        Captain {captain} and the crew were thrust into a deadly situation. 
        The villain {villain} had used {tech} to manipulate time, turning the 
        planet’s natural {substance} into a {color} energy vortex.

        With time itself unstable, the crew had to {verb} carefully. They 
        encountered hostile {creature} and the volatile effects of the anomaly. 
        Their only hope was to retrieve the {noun} before the {phenomenon} 
        destroyed the planet. The {quest} to restore the timeline had begun.
        """
    ),
    'st_story20': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        Captain {captain} received orders to investigate the disappearance of
        several ships near {planet}. The crew of the USS {starship} soon 
        discovered that the villain {villain} was using advanced {tech} to 
        harness the local {substance} and convert it into a {color} weapon 
        capable of causing a {phenomenon} that would rip space apart.

        Racing against time, the crew had to {verb} through hostile {adjective}
        environments, evading the planet’s dangerous {creature} that thrived 
        on {food}. To complete their {quest}, they needed to find the fabled 
        {noun}, which held the key to disabling the weapon and saving the 
        quadrant.
        """
    ),
    'st_story21': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        Captain {captain} of the USS {starship} was tasked with exploring the
        distant planet {planet}, where a new species, {species}, had been
        discovered. Upon arrival, the crew found the villain {villain} using
        advanced {tech} to harvest the planet’s {substance}, creating a {color}
        weapon that could threaten the entire system.

        To stop {villain}, the crew had to {verb} through the dense, {adjective}
        forests, evade the {creature}, and uncover the legendary {noun}. Along
        the way, they battled the strange {phenomenon} that enveloped the planet,
        all while racing against time to complete their {quest}.
        """
    ),
    'st_story22': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        The USS {starship}, led by Captain {captain}, arrived at {planet} after
        a mysterious distress signal from the {species} colonists. They
        discovered the villain {villain} had unleashed a {phenomenon} caused
        by manipulating the planet's core {substance}. The {color} storm was
        destabilizing the planet's surface.

        The crew had to {verb} into the {adjective} depths of the planet,
        encountering strange {creature} that thrived on the local {food}. Their
        only hope lay in recovering the ancient {noun}, which could reverse the
        effects and save the colony, completing their daring {quest}.
        """
    ),
    'st_story23': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        While patrolling near the border of Federation space, Captain {captain}
        of the USS {starship} was called to investigate strange readings from
        the distant planet {planet}. There, the villain {villain}, of the
        {species}, had constructed a massive {tech} that turned the planet's
        valuable {substance} into a {color} crystal, capable of harnessing
        dangerous cosmic energy.

        The crew's mission: {verb} through the {adjective} underground tunnels,
        past the dangerous {creature} that fed on {food}, to find the lost
        {noun}. Only with it could they stop the crystal’s destructive force
        and complete their urgent {quest}.
        """
    ),
    'st_story24': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        The USS {starship} was dispatched to {planet} to study a strange
        {phenomenon} affecting its atmosphere. Captain {captain} soon
        discovered the {species} scientist {villain} was behind it, using an
        illegal {tech} to convert the planet’s {substance} into a deadly {color}
        gas.

        To stop the villain, the crew had to {verb} through the planet’s
        {adjective} terrain, where they encountered the {creature}, a species
        known for consuming {food}. Their only hope lay in finding the ancient
        {noun} that could neutralize the gas and complete their {quest}.
        """
    ),
    'st_story25': StarTrekStory(
        ["captain", "species", "villain", "starship", "tech", "substance",
         "color", "planet", "food", "quest", "adjective", "verb", "noun",
         "creature", "phenomenon"],
        """ 
        Captain {captain} of the USS {starship} was sent to the faraway {planet}
        to investigate reports of a strange {phenomenon}. Upon arrival, the crew
        discovered that the villain {villain}, a rogue member of the {species},
        had activated a dangerous {tech}, turning the planet's {substance} into
        {color} crystals that destabilized the environment.

        The crew needed to {verb} quickly through the {adjective} landscape,
        facing off against the territorial {creature}, which thrived on {food}.
        They searched for the legendary {noun}, the only object powerful enough
        to stop the phenomenon and complete their {quest}.
        """
    ),
}
    