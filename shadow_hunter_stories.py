"""Madlibs Shadow Hunter Stories."""


class ShadowHunterStory:
    """A Mad Libs Shadow Hunter Story.

    To create a Shadow Hunter story, pass a list of prompts and the text
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
    
    
# Collection of Shadow Hunter Themed Stories
ShadowHunterStories = {
    'p_story1': ShadowHunterStory(
        ["character", "sidekick", "villain", "weapon", "ability",
         "substance", "color", "realm", "food", "quest", "adjective", 
         "verb", "noun", "creature", "artifact"],
        """In the {adjective} realm of {realm}, a brave warrior named 
        {character} embarked on a quest known as {quest}. Their loyal 
        sidekick, {sidekick}, accompanied them, always ready for battle 
        and armed with sharp instincts. The mission was dangerous: they 
        needed to stop the sinister {villain} from acquiring the ancient 
        {artifact}, which had the power to manipulate the very fabric of 
        time and space. 

        {character} and {sidekick} journeyed deep into the heart of 
        {realm}, battling through hordes of terrifying {creature}s. 
        Armed with their trusty {weapon}, a legendary blade forged in 
        the depths of the {substance} sea, they wielded their special 
        ability to {ability} and overcame impossible odds. 

        As they approached the {villain}'s lair, the {color} mist 
        thickened, signaling the proximity of dark magic. The final 
        battle was fierce—{character} had to {verb} their way past 
        {villain}'s minions while {sidekick} defended them with a 
        {noun} made from enchanted iron. After a grueling fight, 
        {character} retrieved the {artifact}, thwarting {villain}'s 
        evil plan.

        Exhausted, they returned to their homeland, where they 
        celebrated with a feast of {food}, and the skies of {realm} 
        were once again bathed in the warm glow of peace."""
    ),

    'p_story2': ShadowHunterStory(
        ["character", "sidekick", "villain", "weapon", "ability", 
         "substance", "color", "realm", "food", "quest", "adjective", 
         "verb", "noun", "creature", "artifact"],
        """{character}, known across {realm} for their {adjective} nature, 
        had been tasked with an epic quest: to recover the lost {artifact}, 
        an object of unimaginable power. Accompanied by their quick-witted 
        sidekick, {sidekick}, they ventured into the shadowy lands. Their 
        mission was to prevent {villain}, a master of dark magic, from 
        using the {artifact} to control the {creature}s that roamed the 
        land.

        Their path was treacherous, winding through dark forests filled 
        with howls of unseen beasts. Armed with the enchanted {weapon}, 
        a blade said to be blessed by ancient gods, {character} knew they 
        had a fighting chance. With the ability to {ability}, they moved 
        swiftly and silently, evading traps set by {villain} and his army 
        of followers. 

        At the climax of their journey, they faced {villain} in a battle 
        for the ages. The skies above turned {color} as their weapons 
        clashed. {sidekick} skillfully used a {noun} to shield them both 
        from {villain}'s dark spells. The battle raged on until, using 
        their {ability} one last time, {character} finally struck down 
        {villain}.

        The realm was saved, and {character} returned home, where they 
        were honored with a grand feast of {food}. The people of {realm} 
        celebrated as the air filled with the scent of victory, and the 
        {artifact} was safely stored away, never to be used for evil again."""
    ),

    'p_story3': ShadowHunterStory(
        ["character", "sidekick", "villain", "weapon", "ability", 
         "substance", "color", "realm", "food", "quest", "adjective", 
         "verb", "noun", "creature", "artifact"],
        """The {adjective} land of {realm} had long been peaceful, but 
        that peace was shattered when the wicked {villain} set their 
        sights on the legendary {artifact}, which was said to grant 
        control over the elements themselves. To prevent this catastrophe, 
        {character}, a renowned warrior, took up arms and began the quest 
        known as {quest}.

        Their sidekick, {sidekick}, had always been by their side, 
        courageous and wise beyond their years. Together, they carried 
        the mystical {weapon}, a blade forged from the essence of pure 
        {substance}, and journeyed through the darkest parts of {realm}. 

        Along their journey, they encountered terrifying {creature}s that 
        threatened to stop them at every turn. But {character}'s ability 
        to {ability} helped them navigate the treacherous lands, and 
        {sidekick} proved invaluable, always ready to defend them with a 
        {noun} crafted from enchanted oak.

        When they finally reached {villain}, the battle was long and 
        hard-fought. The sky burned with a {color} hue as the clash of 
        swords echoed throughout the land. At last, {character} managed 
        to {verb} their way to victory, vanquishing {villain} and 
        securing the {artifact} for good.

        After their great triumph, {character} and {sidekick} returned 
        home to a feast of {food}. The people of {realm} rejoiced, 
        knowing that peace had been restored once more."""
    ),

    'p_story4': ShadowHunterStory(
        ["character", "sidekick", "villain", "weapon", "ability", 
         "substance", "color", "realm", "food", "quest", "adjective", 
         "verb", "noun", "creature", "artifact"],
        """{character}, a {adjective} hero known far and wide across the 
        land of {realm}, was called upon for a task of utmost importance. 
        The evil {villain} had uncovered the fabled {artifact}, and their 
        plan was to use it to summon an army of {creature}s to lay waste 
        to the world. 

        Accompanied by their steadfast companion, {sidekick}, {character} 
        accepted the quest to recover the {artifact} and put an end to 
        {villain}'s reign of terror. Armed with the legendary {weapon}, 
        a weapon forged in the fires of {substance}, they journeyed across 
        treacherous landscapes and into the heart of danger.

        Along the way, {character} and {sidekick} encountered all manner 
        of creatures, but none could withstand the power of their 
        combined skills. With {character}'s ability to {ability} and 
        {sidekick}'s resourcefulness, they managed to {verb} their way 
        past every obstacle. The sky above was a deep {color} as they 
        finally reached {villain}'s lair.

        In a climactic battle, {character} and {villain} fought for 
        control of the {artifact}. The {villain}'s magic was strong, but 
        {character}'s determination was stronger. With a mighty swing of 
        their {weapon}, {villain} was defeated, and the world was saved 
        from destruction.

        Returning home, {character} and {sidekick} were welcomed as 
        heroes. A great feast of {food} was prepared in their honor, and 
        peace returned to {realm}, thanks to their bravery."""
    ),

    'p_story5': ShadowHunterStory(
        ["character", "sidekick", "villain", "weapon", "ability", 
         "substance", "color", "realm", "food", "quest", "adjective", 
         "verb", "noun", "creature", "artifact"],
        """{character}, the {adjective} warrior of {realm}, had always 
        been a defender of the innocent, but now they faced their 
        greatest challenge yet. The evil {villain} had obtained the 
        {artifact}, a powerful object capable of controlling the very 
        essence of life itself. With it, {villain} planned to summon 
        a horde of deadly {creature}s to conquer the land.

        {character}, along with their ever-faithful sidekick, 
        {sidekick}, embarked on a quest to stop {villain} and reclaim 
        the {artifact}. Armed with the legendary {weapon}, a sword 
        imbued with the power of {substance}, and their ability to 
        {ability}, they ventured into the darkest corners of {realm}.

        As they journeyed through {villain}'s twisted domain, the skies 
        above turned {color}, and the air grew thick with tension. 
        {character} and {sidekick} fought off legions of {creature}s, 
        using a {noun} to shield themselves from attacks. Despite the 
        overwhelming odds, they pressed on.

        The final battle was fierce, with {character} and {villain} 
        clashing in a struggle that would determine the fate of the 
        realm. Using their {ability}, {character} managed to {verb} 
        past {villain}'s defenses and deliver a decisive blow. The 
        {artifact} was recovered, and {villain}'s plans were thwarted.

        Victorious, {character} and {sidekick} returned home to a 
        hero's welcome, where a feast of {food} was held in their honor. 
        Peace was restored to {realm}, and the people once again 
        lived in safety, thanks to {character}'s courage."""
    ),

    'p_story6': ShadowHunterStory(
        ["character", "sidekick", "villain", "weapon", "ability", 
         "substance", "color", "realm", "food", "quest", "adjective", 
         "verb", "noun", "creature", "artifact"],
        """In the {adjective} realm of {realm}, {character} was a legend, 
        known for their extraordinary feats of bravery. But even legends 
        face challenges, and now, {character} had to embark on a quest 
        to retrieve the {artifact} before the evil {villain} could use 
        it to unleash an army of {creature}s upon the world.

        Accompanied by their loyal sidekick, {sidekick}, {character} set 
        off on their journey, wielding the powerful {weapon}, a weapon 
        forged from the purest {substance}. Their ability to {ability} 
        allowed them to move swiftly and silently through the shadows, 
        evading traps and ambushes set by {villain}'s followers.

        As they ventured deeper into the heart of {realm}, the skies 
        darkened to a deep {color}, and they knew the final battle was 
        approaching. {character} and {sidekick} fought off hordes of 
        {creature}s, using a {noun} as a shield to protect themselves 
        from the onslaught.

        When they finally confronted {villain}, the battle was fierce, 
        with the fate of the world hanging in the balance. But 
        {character}'s determination never wavered, and with a mighty 
        strike of their {weapon}, they defeated {villain} and 
        reclaimed the {artifact}.

        Their quest complete, {character} and {sidekick} returned home 
        to a hero's welcome. A great feast of {food} was held in their 
        honor, and the people of {realm} rejoiced, knowing that they 
        were safe once more, thanks to the bravery of {character}."""
    ),

    'p_story7': ShadowHunterStory(
        ["character", "sidekick", "villain", "weapon", "ability", 
         "substance", "color", "realm", "food", "quest", "adjective", 
         "verb", "noun", "creature", "artifact"],
        """{character}, a {adjective} warrior from the distant land of 
        {realm}, had faced many battles, but none as dangerous as the 
        one that awaited them now. The evil {villain} had uncovered the 
        {artifact}, a relic of immense power that could control the very 
        forces of nature. To stop {villain}, {character} embarked on the 
        quest known as {quest}.

        Their sidekick, {sidekick}, was with them every step of the way, 
        ready to defend their friend with their trusty {noun}. Together, 
        they carried the legendary {weapon}, a blade forged in the fires 
        of {substance}, and ventured into the darkest corners of {realm}.

        Along the way, they encountered terrifying {creature}s that 
        threatened to end their journey. But {character}'s ability to 
        {ability} allowed them to evade these creatures, while {sidekick} 
        used their quick thinking to protect them both. As they drew 
        closer to {villain}'s lair, the skies turned {color}, signaling 
        the presence of dark magic.

        The final battle was fierce, with {character} and {villain} 
        clashing in a battle that would determine the fate of {realm}. 
        But with their strength and determination, {character} managed 
        to {verb} past {villain}'s defenses and deliver the final blow.

        Victorious, {character} and {sidekick} returned home to a hero's 
        welcome. A great feast of {food} was prepared in their honor, 
        and the people of {realm} celebrated their victory, knowing 
        that they were safe once again."""
    ),

    'p_story8': ShadowHunterStory(
        ["character", "sidekick", "villain", "weapon", "ability", 
         "substance", "color", "realm", "food", "quest", "adjective", 
         "verb", "noun", "creature", "artifact"],
        """In the {adjective} land of {realm}, {character} was a warrior 
        without equal, known for their courage and skill in battle. But 
        now, they faced a challenge unlike any they had faced before. 
        The evil {villain} had obtained the {artifact}, a powerful relic 
        that could control the minds of {creature}s, and planned to use 
        it to conquer the land.

        {character} and their sidekick, {sidekick}, set off on a quest 
        to stop {villain} and reclaim the {artifact}. Armed with the 
        legendary {weapon}, a sword forged from the purest {substance}, 
        and their ability to {ability}, they ventured deep into the 
        heart of {realm}, battling all manner of foes along the way.

        The skies above turned {color} as they approached {villain}'s 
        lair, and the air grew thick with tension. {character} and 
        {sidekick} fought their way through hordes of {creature}s, 
        using a {noun} to protect themselves from the onslaught.

        In the final battle, {character} and {villain} clashed in a 
        struggle that would determine the fate of {realm}. But with 
        their strength and determination, {character} managed to 
        {verb} past {villain}'s defenses and deliver the final blow, 
        reclaiming the {artifact} and saving the land.

        Returning home, {character} and {sidekick} were welcomed as 
        heroes. A feast of {food} was held in their honor, and the 
        people of {realm} celebrated their victory, knowing that 
        they were safe once again."""
    ),

    'p_story9': ShadowHunterStory(
        ["character", "sidekick", "villain", "weapon", "ability", 
         "substance", "color", "realm", "food", "quest", "adjective", 
         "verb", "noun", "creature", "artifact"],
        """The {adjective} land of {realm} had always been peaceful, 
        but that peace was shattered when the evil {villain} obtained 
        the {artifact}, a relic of immense power that could control 
        the minds of {creature}s. To stop {villain}, {character} and 
        their sidekick, {sidekick}, set off on a quest known as 
        {quest}.

        Armed with the legendary {weapon}, a sword forged from the 
        purest {substance}, and their ability to {ability}, they 
        ventured deep into the heart of {realm}, battling all manner 
        of foes along the way.

        The skies above turned {color} as they approached {villain}'s 
        lair, and the air grew thick with tension. {character} and 
        {sidekick} fought their way through hordes of {creature}s, 
        using a {noun} to protect themselves from the onslaught.

        In the final battle, {character} and {villain} clashed in a 
        struggle that would determine the fate of {realm}. But with 
        their strength and determination, {character} managed to 
        {verb} past {villain}'s defenses and deliver the final blow, 
        reclaiming the {artifact} and saving the land.

        Returning home, {character} and {sidekick} were welcomed as 
        heroes. A feast of {food} was held in their honor, and the 
        people of {realm} celebrated their victory, knowing that 
        they were safe once again."""
    ),

    'p_story10': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """In the distant {adjective} lands of {realm}, a great darkness 
    began to spread. The once-peaceful realm had fallen under the 
    shadow of the wicked {villain}, who sought to take control of the 
    fabled {artifact}. Legend had it that whoever wielded the {artifact} 
    could command the ancient {creature}s of the realm, twisting them 
    into terrible instruments of destruction.

    {character}, the most skilled warrior of {realm}, had been chosen 
    by fate to embark on a dangerous quest—{quest}. This quest would 
    decide the future of their homeland, and it weighed heavily on 
    {character}'s heart. But {character} was not alone in this perilous 
    journey. By their side was the ever-loyal {sidekick}, a fierce 
    fighter known for their sharp mind and bravery in the face of 
    adversity. Together, they vowed to stop {villain} before the 
    {artifact} could fall into their wicked grasp.

    The journey was long and treacherous, and {character} and 
    {sidekick} faced countless obstacles along the way. They ventured 
    deep into the heart of {realm}, battling through forests where 
    towering {creature}s lurked in the shadows. These beasts, twisted 
    by dark magic, were relentless in their pursuit, but {character} 
    fought back with the legendary {weapon}, a blade infused with the 
    essence of {substance}. The weapon pulsed with power, its edges 
    glowing faintly with a {color} hue as it cleaved through the 
    monstrous enemies that stood in their path.

    As they pressed forward, {character} used their extraordinary 
    ability to {ability}, a skill that allowed them to outmaneuver 
    their foes, slipping past traps and ambushes with ease. {sidekick}, 
    ever-vigilant, wielded a {noun} to defend against surprise attacks 
    and protect {character} during their most dangerous encounters. 
    Their bond was unshakable, forged in the fires of countless battles.

    After days of grueling travel, they finally reached the 
    stronghold where {villain} awaited, guarded by a legion of 
    corrupted {creature}s. The skies above had darkened, and the air 
    crackled with the tension of impending doom. The final battle 
    began in a whirl of steel and magic as {character} and {villain} 
    clashed. The {villain}'s dark powers threatened to overwhelm them, 
    but with {sidekick} fighting by their side, {character} never 
    wavered.

    It was in the heat of battle that {character} saw an opening. 
    Summoning all their strength, they swung their {weapon} in a 
    powerful arc and delivered the final blow with a {color} {noun}. 
    The impact shattered {villain}'s defenses, and with a resounding 
    cry, {villain} was defeated. The {artifact} was reclaimed, its 
    power safely sealed away from those who would use it for evil.

    With peace restored to {realm}, {character} and {sidekick} returned 
    to their homeland as heroes. The people rejoiced and celebrated 
    their return with a grand feast, where tables were laden with 
    dishes of {food}, and goblets filled with the finest {substance}. 
    Under the bright skies of {realm}, which now gleamed with a fresh 
    dawn, the heroes basked in their victory, knowing that the darkness 
    had been vanquished and their land was safe once again."""
    ),
    
    'p_story11': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """In the {adjective} lands of {realm}, shadows clung to every corner, 
    and whispers of ancient horrors echoed in the night. {character} 
    had been summoned to embark on a deadly quest—{quest}. The villainous 
    {villain} had found the fabled {artifact}, a relic that could turn 
    entire armies into soulless {creature}s.

    With only their loyal sidekick, {sidekick}, by their side, {character} 
    ventured into the heart of {realm}, armed with the cursed {weapon}, 
    a blade that thirsted for the essence of {substance}. Along the way, 
    they faced unspeakable horrors, creatures born of nightmare and blood. 
    {character}'s ability to {ability} allowed them to slip between the 
    shadows, avoiding the watchful eyes of the {creature}s that roamed 
    the cursed lands.

    As they neared {villain}'s fortress, the sky turned {color}, an omen 
    of the dark magic that filled the air. The final confrontation was 
    brutal—{villain} unleashed a torrent of necromantic power, seeking 
    to tear {character} apart. But with {sidekick}'s aid, {character} 
    managed to {verb} their way through the waves of undead, striking 
    down {villain} with a {noun} infused with ancient magic.

    The {artifact} was destroyed, but the victory was hollow. The land 
    of {realm} had been poisoned by darkness, and though {character} and 
    {sidekick} returned victorious, their spirits were forever tainted. 
    They ate their victory meal of {food} in silence, washing it down 
    with the bitter taste of {substance}, knowing that some scars 
    could never heal."""
),

'p_story12': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """The depths of {realm} were a cold, {adjective} wasteland. Darkened 
    skies hung low over cursed fields where no life had flourished for 
    centuries. {character} and their sidekick, {sidekick}, descended into 
    this abyss in search of the {artifact}, which had been seized by 
    {villain}. It was said that the {artifact} could bend the wills of 
    even the most savage {creature}s.

    Armed with the dread {weapon}, a weapon that glowed with a sickly 
    {color} light, {character} cut through the legions of monstrous 
    beasts that guarded the entrance to {villain}'s lair. Using their 
    ability to {ability}, they weaved through the dense fog of poison 
    that hung in the air, never faltering in their mission.

    In the heart of the darkness, {villain} awaited. Their face was 
    twisted with malevolent glee, and they called upon the {creature}s 
    to rend {character} apart. But {sidekick}, wielding a mighty {noun}, 
    struck them down, clearing the path for {character} to face {villain} 
    head-on.

    The final blow came swiftly, and the {artifact} was recovered, but at 
    a cost. The darkness that tainted the realm had seeped into their 
    very souls. As they ate their meal of {food}, washed down with the 
    pungent {substance}, both {character} and {sidekick} knew that the 
    shadows of {realm} would forever haunt their dreams."""
),

'p_story13': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """In the far reaches of {realm}, there was a place where no light 
    touched the earth, a void filled with whispers of long-forgotten 
    nightmares. {character} had no choice but to venture into this 
    forsaken land, their quest—{quest}—weighed heavily upon them.

    With their sidekick, {sidekick}, {character} delved deeper into the 
    void, guided only by the faint glow of their {weapon}, a weapon 
    forged from the raw essence of {substance}. The whispers clawed at 
    their minds, twisting their thoughts and filling them with fear. 
    But {character} knew that if they failed, {villain} would use the 
    {artifact} to unleash untold horrors upon the world.

    As they approached the heart of the void, the ground trembled, and 
    monstrous {creature}s rose from the shadows. With their ability to 
    {ability}, {character} dodged their attacks, while {sidekick} 
    fought valiantly with a heavy {noun}, fending off the abominations.

    The final battle with {villain} was like fighting a nightmare given 
    flesh. The sky turned a burning {color} as the void itself seemed 
    to scream in agony. In the end, {character} struck down {villain} 
    with a mighty blow from their {weapon}, but the victory came with a 
    price. The whispers continued, echoing in their minds even as they 
    left the void.

    Back in the safety of the world, they sat down for a meager feast of 
    {food}, accompanied by a bitter cup of {substance}. But no amount of 
    food or drink could wash away the taint of the void that lingered 
    in their souls."""
),

'p_story14': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """In the desolate land of {realm}, the blood moon hung low in the 
    sky, casting a {color} glow over the barren earth. The air was thick 
    with the stench of decay, and the ground was littered with bones. 
    {character} and their sidekick, {sidekick}, were on a mission to 
    stop the sinister {villain} from performing a dark ritual with the 
    {artifact} that would bring forth a horde of ravenous {creature}s 
    into the world.

    Armed with the ancient {weapon}, a blade stained with the blood of 
    countless battles, {character} pressed forward, their ability to 
    {ability} keeping them one step ahead of the death traps that lined 
    the path. But every step brought them closer to the heart of the 
    blood moon’s curse.

    As they approached {villain}'s lair, they were ambushed by grotesque 
    beasts, creatures with eyes as black as the void and teeth as sharp 
    as blades. {sidekick} fought them off with a sacred {noun}, striking 
    with unmatched precision, while {character} battled their way 
    forward. 

    In the final confrontation, {villain} stood before an altar, the 
    {artifact} in hand, chanting in a language older than time itself. 
    {character} lunged forward, their {weapon} glowing with the power 
    of {substance}, and delivered a killing blow. The ritual was broken, 
    and the blood moon slowly faded.

    Though {realm} was saved, the price had been steep. {character} and 
    {sidekick} returned to a hollow victory, their meal of {food} and 
    {substance} tasting of ashes in their mouths. The blood moon may have 
    passed, but its curse still lingered in their hearts."""
),

'p_story15': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """Beneath the roiling waves of {realm}, there was a darkness that 
    few dared to explore. The waters had been cursed for generations, 
    but {villain} had found a way to harness the power of the 
    {artifact}, summoning monstrous {creature}s from the depths to do 
    their bidding.

    {character} and {sidekick} took to the treacherous seas, armed with 
    the legendary {weapon}, a spear forged from the enchanted essence 
    of {substance}. The waves crashed violently against their ship, 
    and the sea itself seemed to rise up in anger, but {character}'s 
    ability to {ability} kept the vessel steady, cutting through the 
    dark waters.

    As they neared {villain}'s stronghold, a massive {creature}, twisted 
    by the curse of the waters, emerged from the depths. {sidekick} 
    hurled a {noun} at the beast, striking its eye and sending it 
    crashing back into the sea. But the victory was short-lived— 
    {villain} awaited, their eyes gleaming with madness.

    The final battle took place beneath the waves, where the light of 
    the surface could not reach. {character} fought desperately, 
    their {weapon} cutting through the water with ease, but every 
    blow drained them. In a last-ditch effort, they {verb} toward 
    {villain}, striking them down and breaking the curse.

    Exhausted and nearly drowned, {character} and {sidekick} returned 
    to the surface. Their feast of {food} and {substance} was eaten in 
    near silence, for they both knew that some darkness could never be 
    washed away, even by the sea."""
),

'p_story16': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """In the crumbling remains of {realm}, a darkness had taken root, 
    spreading like a sickness through the land. The heart of this 
    corruption was {villain}, who had stolen the {artifact}, using its 
    power to summon {creature}s from the abyss. 

    {character}, known for their {adjective} resolve, was sent on a 
    quest—{quest}—to stop the madness. Alongside them was their 
    faithful companion, {sidekick}, who wielded a {noun} as fiercely 
    as any warrior.

    Armed with the cursed {weapon}, a weapon that pulsed with the 
    essence of {substance}, {character} fought through the corrupted 
    lands, their ability to {ability} keeping them ahead of the 
    spreading darkness. The ground beneath them shifted, twisted by 
    {villain}'s magic, and monstrous {creature}s rose to challenge 
    them at every step.

    The final battle was fought in a place where no light reached. 
    {villain}'s heart had turned black with corruption, and they 
    fought with the fury of a thousand damned souls. But with the 
    combined might of {character} and {sidekick}, {villain} was 
    finally brought down, the {artifact} shattered.

    The land of {realm} would heal, but {character} and {sidekick} 
    bore the scars of the battle. As they sat down to eat a meal of 
    {food} and {substance}, they could feel the lingering darkness in 
    their veins. The corruption may have been stopped, but its touch 
    was forever a part of them."""
),

'p_story17': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """Deep within the labyrinthine halls of {realm}, there was a place 
    where the damned souls of the past were said to linger. {character} 
    had been tasked with a perilous quest—{quest}—to retrieve the 
    {artifact} from the clutches of {villain}. It was said that 
    whoever controlled the {artifact} could summon the spirits of the 
    dead to do their bidding, turning even the bravest warrior into a 
    mindless puppet.

    With {sidekick} by their side, {character} descended into the 
    halls, their {weapon}, forged from the essence of {substance}, 
    glowing faintly in the darkness. The air was thick with the 
    stench of decay, and the walls whispered with the voices of 
    the dead.

    As they ventured deeper, they were confronted by {creature}s, 
    twisted shades of warriors long dead, their eyes burning with an 
    unholy {color} fire. {character}'s ability to {ability} allowed 
    them to evade their grasp, while {sidekick} struck them down with 
    a sacred {noun}.

    When they finally reached {villain}, the air grew colder, and the 
    shadows seemed to close in around them. {villain} fought with 
    the fury of the damned, calling upon the spirits of the dead to 
    defend them. But {character} and {sidekick} pressed forward, 
    and with one final strike, {villain} was defeated, their body 
    crumbling to dust.

    The {artifact} was sealed away, but the halls of the damned still 
    echoed in their minds. As they sat down to eat a meal of {food} 
    and {substance}, they could not shake the feeling that they had 
    brought something dark back with them from the depths."""
),

'p_story18': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """Once, the kingdom of {realm} had been a place of light and 
    beauty, but that was before the rise of {villain}. Using the power 
    of the {artifact}, they had torn the kingdom apart, unleashing 
    terrible {creature}s to lay waste to the land.

    {character}, one of the few remaining warriors of the old order, 
    had been sent on a final, desperate quest—{quest}—to recover the 
    {artifact} and stop {villain} once and for all. By their side was 
    {sidekick}, a fierce warrior whose skill with a {noun} was 
    unmatched.

    Armed with the {weapon}, a blade forged from the last reserves of 
    {substance} left in the shattered kingdom, {character} fought 
    their way through hordes of monstrous {creature}s. The ground was 
    blackened, and the sky above was a constant {color}, the land itself 
    corrupted by {villain}'s magic.

    As they neared {villain}'s throne, the air grew thick with 
    malevolent energy. {character} used their ability to {ability} to 
    evade the worst of the traps that lined the path, but it was clear 
    that their strength was waning.

    In the final battle, {villain} unleashed all the power of the 
    {artifact}, turning the very air into a weapon. But with a mighty 
    strike, {character} shattered the {artifact}, and {villain} fell 
    to their knees, defeated at last.

    The kingdom of {realm} had been saved, but it was a hollow victory. 
    The land had been scarred beyond repair, and the people would 
    never forget the horrors that had been unleashed. {character} and 
    {sidekick} returned to the remains of their home, where they ate 
    a somber meal of {food} and {substance}, knowing that the light 
    of the kingdom would never shine as brightly again."""
),

'p_story19': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """In the realm of {realm}, the sun had not risen in over a hundred 
    years. The land had been cursed by {villain}, who used the power of 
    the {artifact} to plunge the world into eternal darkness. The 
    people lived in fear of the {creature}s that roamed the night, 
    their eyes glowing with a {color} hue as they hunted their prey.

    {character}, the last of the lightbringers, had been sent on a 
    desperate mission—{quest}—to recover the {artifact} and restore the 
    sun to the sky. With their faithful sidekick, {sidekick}, they 
    ventured into the heart of {realm}, where the darkness was 
    thickest, and the creatures most dangerous.

    Armed with the {weapon}, a blade forged from the rarest {substance}, 
    {character} cut through the hordes of monsters that blocked their 
    path. {sidekick}, wielding a sacred {noun}, defended them from 
    ambushes, while {character} used their ability to {ability} to 
    slip past the worst of the dangers.

    In the final battle, {villain} stood atop a mountain of bones, 
    their eyes glowing with dark power. They called upon the power of 
    the {artifact} to strike {character} down, but {character} fought 
    back with all their strength. With one final {verb}, they struck 
    {villain} down, shattering the {artifact} and breaking the curse.

    The sun rose for the first time in a century, and the people of 
    {realm} rejoiced. But {character} and {sidekick} could not shake 
    the feeling that the darkness still lingered within them. As they 
    sat down to eat a simple meal of {food} and {substance}, they knew 
    that the night would never fully leave their hearts."""
),

'p_story20': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """The sins of the past had come back to haunt {realm}, and at the 
    center of it all was {villain}, who had found the cursed {artifact}. 
    With it, they could summon the spirits of long-dead {creature}s to 
    wreak havoc upon the world.

    {character}, a warrior with a troubled past, was called upon to 
    embark on a dangerous quest—{quest}—to stop {villain} before it was 
    too late. With their loyal sidekick, {sidekick}, they ventured into 
    the heart of {realm}, armed with the {weapon}, a blade forged from 
    the corrupted essence of {substance}.

    The journey was fraught with danger, as the spirits of the dead 
    rose to challenge them at every turn. {character} used their 
    ability to {ability} to navigate the treacherous terrain, while 
    {sidekick} fought off the spirits with a blessed {noun}.

    In the final confrontation, {villain} called upon the sins of the 
    past to strike {character} down, but {character} fought back with 
    all their might. The battle was fierce, but in the end, {character} 
    struck down {villain}, shattering the {artifact} and breaking the 
    curse.

    The spirits were laid to rest, but the sins of the past still 
    lingered in {character}'s heart. As they sat down to eat a meal of 
    {food} and {substance}, they could not shake the feeling that they 
    would never truly be free of the darkness that had followed them 
    through the halls of the dead."""
),

'p_story21': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """In the {adjective} reaches of {realm}, a great darkness stirred. 
    Legends spoke of a chasm called the Devouring Abyss, where the 
    malevolent {villain} had begun harnessing the power of the 
    {artifact} to raise an army of ancient {creature}s. If left 
    unchecked, the world would soon be overrun by nightmares. 

    {character} was chosen for the quest—{quest}—to stop {villain}. 
    With their sidekick, {sidekick}, by their side, they embarked on 
    a treacherous journey. Armed with the {weapon}, a blade that pulsed 
    with the cursed essence of {substance}, {character} ventured into 
    the abyss.

    The darkness was overwhelming. The walls of the chasm whispered 
    the voices of the damned, and monstrous {creature}s lurked in every 
    shadow. {character}'s ability to {ability} allowed them to stay one 
    step ahead, though every passing moment brought them closer to 
    despair. {sidekick}, wielding a mighty {noun}, struck down enemies 
    that dared to challenge them.

    When they reached {villain}, the final battle began. The air 
    crackled with dark magic, turning a sickly {color}, and the abyss 
    itself seemed to hunger for their souls. But {character} fought 
    bravely, using their weapon to {verb} through the darkness and 
    destroy {villain} once and for all.

    Though the abyss was silenced, its void lingered in {character}'s 
    heart. Even as they returned to {realm} and sat down to a meal of 
    {food} and {substance}, they felt a chill that could never be 
    warmed by victory."""
),

'p_story22': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """In the forgotten kingdom of {realm}, a curse lay upon the land, 
    woven by the dark and terrible {villain}, known as the Witch King. 
    The skies burned a permanent {color}, and the people were plagued by 
    foul {creature}s that rose from the earth itself. To break the curse, 
    {character} was sent on a perilous quest—{quest}—to retrieve the 
    {artifact} from the depths of the Witch King's lair.

    {sidekick}, ever faithful, joined {character} on this dark journey, 
    bearing a sacred {noun} that could ward off the creatures of the 
    night. {character} wielded the ancient {weapon}, a blade that 
    radiated the essence of {substance}, powerful enough to cut through 
    the very fabric of curses.

    As they ventured deeper into {realm}, the Witch King's magic 
    twisted reality itself. {character}'s ability to {ability} became 
    their only defense against illusions and deadly traps, but the 
    further they went, the more their minds twisted with fear.

    When they finally faced {villain}, the battle was long and brutal. 
    The air was thick with darkness, and every strike seemed to sap 
    their strength. But {sidekick}'s courage and {character}'s sheer 
    willpower won out. The {artifact} was reclaimed, and with it, 
    the curse was broken.

    However, the cost was high. Though the kingdom was free, {character} 
    and {sidekick} could never forget the horrors they had seen. They 
    returned to a somber meal of {food} and {substance}, knowing that 
    the Witch King's legacy would haunt them forever."""
),

'p_story23': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """The city of {realm} had long been abandoned, its streets 
    suffocated by the presence of a curse known as Evernight. The 
    sun had not risen in years, and the land was haunted by spectral 
    {creature}s that roamed its desolate alleys. {character} had been 
    tasked with a deadly mission—{quest}—to retrieve the {artifact} 
    that {villain} used to maintain the endless night.

    With {sidekick}, a hunter trained in the arts of darkness, 
    {character} entered the city, armed with the {weapon}, a weapon 
    said to be forged from the crystallized {substance} of fallen stars. 
    Together, they moved silently through the dead streets, using 
    {character}'s ability to {ability} to avoid being detected by the 
    lurking horrors.

    The shadows thickened as they ventured deeper, and the air turned 
    an unnatural {color}. Spectral {creature}s clawed at their minds, 
    and the city itself seemed to bend reality around them. 
    {sidekick}'s {noun} glowed faintly, pushing back the darkness 
    wherever they went.

    When they finally reached {villain}, the battle for Evernight began. 
    The air crackled with dark power as {villain} summoned nightmares 
    to strike at them, but {character} pressed on. With a final 
    {verb}, {villain} was defeated, and the {artifact} was shattered, 
    allowing the sun to rise once more.

    As light flooded the city for the first time in years, {character} 
    and {sidekick} sat in a crumbling hall, sharing a simple meal of 
    {food} and {substance}. But neither of them could forget the 
    shadows that still clung to their souls, knowing that Evernight 
    would never truly leave them."""
),

'p_story24': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """Deep beneath the earth, in a place forgotten by time, lay the 
    Tomb of Broken Souls. It was said that no one who entered its 
    cursed halls ever returned whole. {villain} had gone there in search 
    of the {artifact}, and now {character} had no choice but to follow 
    on a quest known as {quest}.

    With their sidekick, {sidekick}, {character} descended into the tomb, 
    carrying the {weapon}, a sword infused with the dark magic of 
    {substance}, powerful enough to cut through even the strongest 
    curses. The tomb was filled with the twisted souls of the damned, 
    their faces contorted in eternal agony. {character}'s ability to 
    {ability} allowed them to navigate the maze of death traps, but 
    the further they went, the more the tomb sapped their strength.

    As they reached the heart of the tomb, they found {villain}, who had 
    already begun to awaken the {creature}s that guarded the {artifact}. 
    The air was thick with death, and the walls seemed to bleed with a 
    {color} ichor. {sidekick} fought valiantly with their {noun}, but 
    it was only through sheer determination that {character} managed to 
    {verb} their way to {villain}.

    The battle was fierce, but in the end, {villain} fell, and the 
    {artifact} was sealed away. However, the tomb's influence could 
    not be entirely undone. As they left the cursed halls, {character} 
    and {sidekick} knew that a part of their souls would always remain 
    trapped in the tomb.

    They returned to the surface and shared a quiet meal of {food} and 
    {substance}, their hearts heavy with the weight of the broken souls 
    they had left behind."""
),

'p_story25': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """The once fertile lands of {realm} had become a poisoned wasteland, 
    its rivers turned to black sludge and its forests decayed to ash. 
    The cause of this blight was {villain}, who had discovered the 
    {artifact}—an ancient relic of untold power—and was using it to 
    drain the life force from the land itself.

    {character} had been sent on a desperate mission—{quest}—to stop 
    {villain} before the entire world was consumed. With {sidekick}, 
    their closest ally, they set off across the poisoned lands, 
    armed with the {weapon}, a weapon forged from the last pure 
    remnants of {substance}. Every step was dangerous, for the air 
    itself had become toxic, and foul {creature}s stalked them at 
    every turn.

    {character}'s ability to {ability} allowed them to press on, even 
    as the poison sapped their strength. The sky above had turned a 
    sickly {color}, and the land beneath their feet crumbled with each 
    step. But {sidekick} fought bravely, wielding a {noun} that cut 
    through the foul creatures with ease.

    When they finally reached {villain}, the battle was brutal. The 
    poison in the air made every breath a struggle, and the ground 
    itself seemed to rise up against them. But with a final, desperate 
    strike, {character} managed to {verb} through {villain}'s defenses 
    and shatter the {artifact}, breaking the curse that had poisoned 
    the land.

    Though the land would eventually heal, {character} and {sidekick} 
    knew that the poison had left its mark on them as well. They sat 
    down to a meal of {food} and {substance}, but the taste was bitter, 
    and they knew that the poisoned lands would haunt them forever."""
),

'p_story26': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """The realm of {realm} was a place where even the bravest feared to 
    tread. At its center was a void, a black hole that seemed to pull 
    everything into its endless depths. {villain} had gone there, 
    seeking the {artifact}, an object that was said to hold the power 
    of creation and destruction. If they succeeded, the world would be 
    lost to the void.

    {character} had been chosen to stop them, to undertake the 
    impossible quest—{quest}—and retrieve the {artifact}. With their 
    sidekick, {sidekick}, they ventured into the heart of the void, 
    armed with the {weapon}, a blade that shimmered with the 
    iridescent glow of {substance}.

    As they neared the center, the very fabric of reality seemed to 
    break apart. The void pulled at their minds, twisting their 
    thoughts, and monstrous {creature}s made of pure darkness lunged 
    at them from the shadows. {character}'s ability to {ability} kept 
    them grounded, but the void's pull was relentless.

    When they finally confronted {villain}, the air turned an eerie 
    {color}, and the void seemed to hunger for their souls. The battle 
    was fierce, but with a final {verb}, {character} struck down 
    {villain}, and the void began to close in on itself.

    They escaped just in time, but the void had left its mark on them. 
    Though they had succeeded in their quest, they knew that part of 
    them had been lost to the endless darkness. As they sat down to 
    eat a meal of {food} and {substance}, they could not shake the 
    feeling that the void still watched them from the shadows."""
),

'p_story27': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """The land of {realm} had long been cursed by a great serpent that 
    slumbered beneath the earth, waiting to rise and devour the world. 
    {villain} had found a way to awaken it, using the power of the 
    {artifact} to control the beast. {character} had no choice but to 
    embark on a dangerous quest—{quest}—to stop them.

    Accompanied by their sidekick, {sidekick}, {character} journeyed 
    into the serpent's domain, armed with the {weapon}, a weapon 
    forged from the venom of the great beast itself, and infused with 
    the magic of {substance}. Every step was treacherous, as the land 
    twisted and shifted beneath them, and {creature}s born from the 
    serpent's curse rose to block their path.

    {character}'s ability to {ability} helped them stay ahead of the 
    serpent's minions, while {sidekick} fought them off with a 
    blessed {noun}. But as they neared the heart of the serpent's 
    lair, the air turned {color}, and they could feel the great beast 
    stirring beneath their feet.

    The final battle was fought in the serpent's very heart, where 
    {villain} stood, controlling the beast with the power of the 
    {artifact}. The serpent struck at them with unimaginable fury, 
    but {character} managed to {verb} through its defenses, striking 
    down {villain} and breaking the curse.

    Though the serpent was defeated, the curse still lingered in the 
    land, and {character} knew that it would never truly be free. 
    As they sat down to eat a meal of {food} and {substance}, they 
    could feel the serpent's venom in their veins, a reminder of 
    the darkness they had faced."""
),

'p_story28': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """A terrible plague had swept across {realm}, turning its people 
    into twisted, shadowy {creature}s that roamed the land, 
    mindlessly hunting the living. The source of this plague was 
    {villain}, who had found the {artifact} and used it to unleash the 
    shadow creatures upon the world.

    {character}, a warrior with a dark past, had been sent on a 
    desperate mission—{quest}—to stop {villain} before the plague 
    consumed everything. With {sidekick}, their trusted companion, 
    {character} ventured into the heart of the plague-ridden land, 
    armed with the {weapon}, a weapon forged from the purest essence 
    of {substance}.

    As they journeyed deeper into the shadows, they were attacked by 
    wave after wave of {creature}s, their eyes glowing with a 
    sickly {color} light. {character}'s ability to {ability} allowed 
    them to stay ahead of the creatures, while {sidekick} fought them 
    off with a holy {noun}.

    When they finally reached {villain}, the air was thick with the 
    plague, and the very ground seemed to writhe beneath their feet. 
    The battle was fierce, and every blow seemed to sap their strength, 
    but {character} pressed on. With a final, desperate {verb}, they 
    struck down {villain} and destroyed the {artifact}, breaking the 
    curse.

    Though the plague was ended, its scars remained. {character} and 
    {sidekick} returned to a land forever changed by the darkness that 
    had swept through it. As they sat down to eat a meal of {food} and 
    {substance}, they knew that the shadow would never truly leave 
    them."""
),

'p_story29': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """At the heart of {realm}, there was a throne made of bones, where 
    {villain} sat in dark triumph. Using the {artifact}, they had 
    summoned legions of {creature}s to their side, and now the land 
    was ruled by death itself. {character} had been sent on a grim 
    mission—{quest}—to destroy {villain} and take the {artifact} 
    before it was too late.

    With {sidekick} by their side, {character} ventured into the land 
    of bones, armed with the {weapon}, a weapon forged from the 
    bones of fallen warriors and infused with the power of {substance}. 
    The air was thick with decay, and the ground crunched beneath their 
    feet with every step. 

    {character}'s ability to {ability} allowed them to avoid the worst 
    of the traps, but the path was still treacherous. {creature}s rose 
    from the ground to block their way, their eyes glowing a deep 
    {color}. {sidekick} fought them off with a sacred {noun}, while 
    {character} pressed forward toward the throne.

    The final battle took place in the shadow of the throne, where 
    {villain} commanded the dead to strike at them. The air crackled 
    with dark power, and every blow seemed to drain their strength, 
    but {character} fought on. With a final, desperate {verb}, they 
    struck down {villain} and shattered the {artifact}, bringing an 
    end to the reign of bones.

    Though the dead had been laid to rest, the memory of the throne 
    still lingered in their minds. {character} and {sidekick} returned 
    to the land of the living, but the sight of bones still haunted 
    their dreams. As they sat down to eat a meal of {food} and 
    {substance}, they knew that the throne of bones would never truly 
    leave them."""
),

'p_story30': ShadowHunterStory(
    ["character", "sidekick", "villain", "weapon", "ability", 
     "substance", "color", "realm", "food", "quest", "adjective", 
     "verb", "noun", "creature", "artifact"],
    """The Forest of Forgotten Souls was a place where no one entered 
    willingly. It was said that the souls of the dead lingered there, 
    trapped between life and death, and that anyone who entered would 
    lose their way forever. {villain} had gone there, seeking the 
    {artifact}, an object of unimaginable power that could control 
    the spirits of the dead. 

    {character} had no choice but to follow, embarking on the 
    dangerous quest—{quest}—with their sidekick, {sidekick}, by their 
    side. Armed with the {weapon}, a blade infused with the essence 
    of {substance}, {character} ventured into the forest, where the 
    very trees seemed to whisper the names of the dead.

    As they moved deeper into the forest, they were attacked by 
    {creature}s, spirits twisted by the power of the {artifact}. Their 
    eyes glowed with a {color} light, and their voices echoed through 
    the trees, begging for release. {character}'s ability to {ability} 
    helped them navigate the maze of the forest, while {sidekick} 
    fought off the spirits with a blessed {noun}.

    When they finally reached {villain}, the battle was fought in the 
    heart of the forest, where the spirits screamed in agony. 
    {villain} used the {artifact} to command the spirits to attack, 
    but {character} pressed on. With a final {verb}, they struck 
    {villain} down, shattering the {artifact} and freeing the souls of 
    the dead.

    Though the spirits were freed, {character} and {sidekick} knew that 
    the forest would always haunt them. As they sat down to eat a meal 
    of {food} and {substance}, they could still hear the whispers of 
    the souls that had been left behind, and they knew that the 
    Forest of Forgotten Souls would never truly release them."""
),

}