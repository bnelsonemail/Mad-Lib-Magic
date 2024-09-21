"""Madlibs Superhero Stories."""


class SuperheroStory:
    """A Mad Libs Superhero Story.

    To create a Superhero story, pass a list of prompts and the text
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
    
    
# Collection of Superhero Themed Stories
SuperheroStories = {
    'p_story1': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower",
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The legendary {character} and their trusted sidekick {sidekick}
        were on a quest to {quest} to save the world from the evil {villain}. The 
        villain had acquired a dangerous {substance}, which was glowing 
        an eerie {color}, threatening to destroy the entire {location}. 
        Armed with only their {weapon} and the incredible ability to 
        {superpower}, {character} knew time was running out. As they raced 
        through the {adjective} streets, dodging wild {creature}s, 
        {character} felt a pang of hunger and grabbed a {food} from a nearby 
        vendor. "No time for a break!" exclaimed {sidekick}, but {character} 
        knew they would need their energy for the final battle. With one last 
        {verb}, they approached {villain}'s lair, knowing that their 
        {identity} must remain a secret until the end."""
    ),
    'p_story2': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """In the heart of {location}, the fearless hero {character} and 
        their loyal sidekick {sidekick} embarked on their most dangerous 
        quest to {quest} yet. The notorious {villain} had stolen the powerful 
        {substance}, a rare material that gleamed with an unnatural 
        {color}. With only their trusty {weapon} and the ability to 
        {superpower}, {character} knew they had to act fast. The streets 
        were crawling with {adjective} {creature}s, making every step 
        treacherous. "We have to stay focused," {sidekick} muttered, 
        dodging a flying {noun}. As they moved closer to {villain}'s 
        lair, the scent of {food} filled the air, tempting them, but 
        {character} refused to be distracted. One final {verb}, and they 
        would face their ultimate nemesis. Could their true {identity} 
        remain hidden for much longer?"""
    ),
    'p_story3': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """Deep within the {location}, {character} and {sidekick} prepared 
        for the greatest quest to {quest} of their lives. The wicked {villain} had 
        concocted a plan to use a dangerous {substance} to destroy the city. 
        This substance, glowing with a vibrant {color}, was hidden within 
        a secret bunker. Armed with the {weapon} and the ability to 
        {superpower}, {character} knew this would not be an easy fight. 
        They faced {adjective} obstacles, including monstrous {creature}s 
        and traps set by {villain}. As they made their way through, the 
        smell of {food} wafted through the air. "Not now!" {character} 
        yelled as {sidekick} reached for a bite. With one last effort, 
        they {verb} toward {villain}, ready to confront them, but the 
        truth of {character}'s {identity} was close to being revealed."""
    ),
    'p_story4': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """In the desolate {location}, {character} and {sidekick} were on 
        a mission to stop the devious {villain}. The villain had stolen 
        a potent {substance} known for its {color} hue, threatening to 
        unleash it on the world. With only their {weapon} in hand and 
        the power to {superpower}, they had no time to waste. As they 
        ventured through {adjective} terrain, they encountered ferocious 
        {creature}s guarding the path. A quick {verb} and they moved 
        forward, but {sidekick} couldn't resist the allure of {food} 
        nearby. "Stay focused!" warned {character}, knowing their quest to {quest} 
        depended on it. The final battle with {villain} loomed, but 
        could they protect {character}'s secret {identity}?"""
    ),
    'p_story5': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The {adjective} city of {location} was under siege. {character} 
        and {sidekick} were the only hope. {villain} had gained control of 
        a mysterious {substance}, a {color} element that could destroy 
        everything. With the {weapon} in hand and the power to 
        {superpower}, {character} was ready to stop {villain}. The journey 
        was dangerous, full of {creature}s that roamed the streets. As 
        they pressed on, they couldn't help but notice the delicious 
        scent of {food} coming from nearby. "We don't have time for that!" 
        {sidekick} exclaimed, though their stomach growled. With a mighty 
        {verb}, they made it to {villain}'s lair, but keeping {character}'s 
        {identity} safe and to complete their quest to {quest} was becoming more
        challenging."""
    ),
    'p_story6': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """{character} and their brave sidekick {sidekick} found themselves 
        on a quest to {quest} in the middle of the {adjective} {location}. The evil 
        {villain} had hidden a dangerous {substance} with a glowing {color} 
        deep within a labyrinth guarded by terrifying {creature}s. Armed 
        with their {weapon} and the ability to {superpower}, they pushed 
        forward, despite {sidekick}'s distractions with the local {food}. 
        They had to {verb} quickly before {villain} unleashed their plan. 
        But there was one risk: would {character}'s secret {identity} be 
        exposed in the process?"""
    ),
    'p_story7': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """On a {adjective} day in {location}, {character} and {sidekick} 
        embarked on their latest quest to {quest}. {villain} had stolen the {substance} 
        that glowed {color} under the moonlight. With their trusted {weapon} 
        and the power to {superpower}, they were the only ones who could 
        stop this madness. The journey was full of monstrous {creature}s 
        and obstacles at every turn. As they reached the final leg, 
        {sidekick}'s hunger took over and they stopped for {food}. "No time!" 
        shouted {character}. With a final {verb}, they stormed into 
        {villain}'s lair, but could they keep their {identity} hidden?"""
    ),
    'p_story8': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The sky over {location} was {adjective}, and the air smelled of 
        danger. {character} and {sidekick} were on a quest to {quest} to stop 
        {villain}, who had found the elusive {substance} that emitted a 
        dangerous {color} glow. Armed with their legendary {weapon} and 
        the ability to {superpower}, they ventured through fields filled 
        with hostile {creature}s. As they approached the lair, {sidekick} 
        couldn't resist the smell of {food} from a nearby stand. "Stay 
        focused!" {character} said, knowing that only one {verb} remained 
        between them and victory. But their secret {identity} was hanging 
        by a thread."""
    ),
    'p_story9': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """Far away in the {adjective} land of {location}, {character} and 
        {sidekick} faced their toughest quest to {quest} yet. The villainous {villain} 
        had discovered a {substance} of unimaginable power, shining in a 
        strange {color}. With their {weapon} in hand and their ability to 
        {superpower}, they battled through hordes of {creature}s to reach 
        {villain}'s fortress. Along the way, {sidekick} couldn't help but 
        grab a {food}, despite the urgency. One swift {verb}, and they would 
        confront their enemy. But {character} knew that protecting their 
        {identity} was the real challenge."""
    ),
    'p_story10': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """In a {adjective} world of chaos, only {character} and their 
        sidekick {sidekick} could complete the quest to {quest}. {villain} had 
        stolen the precious {substance} that glowed with a {color} light. 
        Armed with a {weapon} and the power to {superpower}, they had to 
        save {location}. The land was crawling with {creature}s, and the 
        delicious smell of {food} filled the air, but there was no time 
        for distraction. A single {verb} could save the day, but could 
        {character} keep their {identity} hidden from the world?"""
    ),
    
    'p_story11': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The sky over {location} was shrouded in a {adjective} mist as 
        {character} and {sidekick} tracked {villain}. The villain had 
        harnessed a deadly {substance}, glowing with an unnatural 
        {color}, capable of destroying everything. With only their 
        {weapon} and their ability to {superpower}, {character} felt the 
        crushing weight of their quest to {quest}. The once lively streets now 
        crawled with monstrous {creature}s. As they pressed on, the scent 
        of decayed {food} filled the air. "We must keep moving," 
        {sidekick} urged. One last {verb} would bring them face to face 
        with {villain}, but could {character} keep their dark {identity} 
        hidden in time to save the city?"""
    ),
    'p_story12': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """In the shadowy underbelly of {location}, {character} and their 
        silent sidekick {sidekick} hunted the notorious {villain}, who 
        had stolen a rare {substance}, a toxic material that shimmered 
        {color}. Armed with the cursed {weapon} and the ability to 
        {superpower}, {character} knew they were running out of time. 
        Their quest to {quest} to stop {villain} felt like a descent into madness. 
        They stumbled over the bodies of {creature}s, victims of 
        {villain}'s cruel experiment. The stench of rotten {food} filled 
        their lungs. "No rest now," whispered {sidekick}, and with one 
        final {verb}, they reached {villain}'s lair. But the secret of 
        {character}'s {identity} was unraveling faster than they could 
        contain it."""
    ),
    'p_story13': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The once bustling {location} had become a {adjective} wasteland. 
        {character} and {sidekick} prowled the streets, haunted by the 
        relentless hunt for {villain}. The villain had unlocked the 
        potential of the deadly {substance}, a glowing {color} nightmare 
        that seeped into every crack. Armed with the cursed {weapon}, 
        {character} fought off the vicious {creature}s that had begun to 
        infest the city. Their quest to {quest} had become a twisted obsession. 
        The smell of rotting {food} was inescapable. "We have to 
        {verb}," said {sidekick}, but {character} knew that to end this, 
        they would have to confront their darkest secret: their own 
        {identity}.”"""
    ),
    'p_story14': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The eerie silence of {location} was broken by the screams of 
        {creature}s as {character} and {sidekick} pursued {villain}. 
        The villain had acquired a dark {substance}, a poisonous material 
        with a {color} glow that threatened to consume everything. 
        Armed with the cursed {weapon} and the ability to {superpower}, 
        {character} could feel the toll of the quest to {quest}. The streets 
        reeked of spoiled {food}. As they neared the heart of 
        {villain}'s domain, {sidekick} whispered, "There’s no turning 
        back." With a final {verb}, they faced their enemy, knowing 
        that {character}'s own {identity} could lead them down the same 
        dark path as {villain}."""
    ),
    'p_story15': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The {adjective} city of {location} was a broken ruin. 
        {character} and {sidekick} were on a mission to stop 
        {villain} from unleashing the full power of a dangerous 
        {substance}, an oily {color} liquid that corrupted everything 
        it touched. The weight of their quest to {quest} grew heavier as the 
        world crumbled around them. With their {weapon} and the ability 
        to {superpower}, they fought through {creature}s driven mad by 
        the substance. As the scent of charred {food} filled the air, 
        {sidekick} whispered, "This might be the end." But with one last 
        {verb}, {character} faced the villain. The darkest part of 
        themselves—{identity}—was ready to be unleashed."""
    ),
    'p_story16': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """In the forsaken {location}, {character} stood alongside 
        {sidekick}, staring into the abyss where {villain} lurked. 
        The villain had created a devastating weapon using a rare 
        {substance}, which pulsated with a sickly {color}. With the 
        {weapon} in hand and the ability to {superpower}, 
        {character} knew they were outmatched. Their quest to {quest} felt more 
        like a slow march to oblivion. {creature}s wandered the ruined 
        streets, the air thick with the scent of spoiled {food}. "We 
        have to keep going," {sidekick} murmured. One last desperate 
        {verb} would bring them to {villain}, but the true cost might 
        be exposing {character}'s {identity} and losing everything."""
    ),
    'p_story17': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """Beneath the blackened skies of {location}, {character} and 
        {sidekick} raced against time. {villain} had harnessed a dark 
        {substance}, a foul material that oozed {color} and threatened 
        to devour the city. With the {weapon} in hand and the power to 
        {superpower}, {character} faced unspeakable horrors in their 
        quest to {quest}. The streets were filled with the mutated {creature}s, 
        victims of the substance. The smell of rancid {food} hung in 
        the air. As they prepared for the final confrontation, 
        {sidekick} whispered, "We can't win." With a single {verb}, 
        {character} would face the truth—both about {villain}, and their 
        own {identity}."""
    ),
    'p_story18': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """In the {adjective} depths of {location}, {character} and 
        {sidekick} pursued {villain}, who had discovered a terrifying 
        {substance}, a {color} element capable of unspeakable destruction. 
        With only their {weapon} and their ability to {superpower}, 
        {character} fought through {creature}s twisted by the substance. 
        The path was lined with decayed {food} and broken dreams. "This 
        is a one-way trip," {sidekick} whispered, the weight of the 
        quest to {quest} becoming unbearable. One final {verb}, and {character} 
        would face their greatest enemy. But the cost of hiding their 
        {identity} might be too high this time."""
    ),
    'p_story19': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """A shadow fell over {location}, the land poisoned by a 
        {color} {substance} unleashed by {villain}. {character} and 
        {sidekick} embarked on a grim quest to {quest} to stop them. Armed with 
        a cursed {weapon} and the ability to {superpower}, the duo faced 
        {adjective} horrors. The smell of decaying {food} filled the air 
        as they fought off crazed {creature}s. "The darkness is 
        spreading," {sidekick} said quietly. One final {verb}, and they 
        would confront {villain}, but {character}'s hidden {identity} 
        might prove the real undoing of their mission."""
    ),
    'p_story20': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The once vibrant {location} was now a {adjective} shell of 
        itself. {villain} had released a {substance} that burned 
        {color} in the sky, destroying everything it touched. 
        {character} and {sidekick}, armed with a cursed {weapon} and 
        the ability to {superpower}, knew this quest to {quest} would be their 
        last. The land was filled with twisted {creature}s and the 
        scent of burning {food}. "We're out of time," {sidekick} 
        muttered. With one final {verb}, they rushed into battle, 
        knowing that {character}'s {identity} would either save or 
        doom them all."""
    ),
    'p_story21': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """In the heart of the crumbling {location}, {character} and 
        {sidekick} faced {villain}, who had used the forbidden 
        {substance}, a {color} elixir that corrupted all it touched. 
        With their cursed {weapon} and the power to {superpower}, 
        {character} knew their quest to {quest} was nearing its end. The streets 
        were filled with broken {noun}s and dying {creature}s. The 
        smell of burned {food} was overpowering. "No turning back," 
        {sidekick} whispered. With a final {verb}, {character} stepped 
        forward, the truth of their {identity} waiting in the shadows."""
    ),
    
    'p_story22': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """In the desolate wasteland of {location}, {character} and 
        {sidekick} stalked {villain}. The villain had harnessed a 
        deadly {substance}, glowing with a sickly {color}. With their 
        cursed {weapon} and the power to {superpower}, {character} knew 
        their quest to {quest} would not end in victory. {creature}s roamed the 
        streets, driven mad by the toxin. As the stench of decaying 
        {food} filled the air, {sidekick} muttered, "We're too late." 
        A final {verb} brought them to {villain}, but the truth of 
        {character}'s {identity} was about to come to light in the 
        darkest way possible."""
    ),
    'p_story23': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """In the shadowed depths of {location}, {character} and {sidekick} 
        faced the inevitable. {villain} had created a weapon from a 
        twisted {substance}, glowing {color} and deadly. Armed with only 
        their {weapon} and the ability to {superpower}, {character} was 
        ready to embrace the darkness of their quest to {quest}. The once familiar 
        streets were filled with {creature}s warped by the toxin, the 
        air heavy with the smell of rotting {food}. "There's no going 
        back," {sidekick} said softly. With a last {verb}, they reached 
        {villain}'s stronghold, but would {character}'s hidden {identity} 
        survive the final blow?"""
    ),
    'p_story24': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The {adjective} ruins of {location} were all that remained 
        after {villain} released the {substance}. The {color} fog hung 
        in the air, as {character} and {sidekick} prepared for their 
        final quest to {quest}. Armed with the {weapon} and the power to 
        {superpower}, {character} felt the burden of their secret 
        {identity} weighing them down. The streets crawled with 
        mindless {creature}s, drawn to the deadly glow. The stench of 
        decayed {food} was suffocating. "This is the end," {sidekick} 
        muttered. One last {verb}, and they would face {villain}, 
        knowing there might be no return from this darkness."""
    ),
    'p_story25': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """In the {adjective} streets of {location}, {character} and 
        {sidekick} fought their way through a city in ruins. 
        {villain}'s {substance}, a glowing {color} liquid, had poisoned 
        the land. With their {weapon} and the ability to {superpower}, 
        {character} knew they had little time left to stop the spread. 
        Their quest to {quest} had become a desperate battle against the {creature}s 
        mutated by the substance. The smell of burning {food} lingered 
        in the air. "There's no time for rest," {sidekick} warned. With 
        a final {verb}, they closed in on {villain}, but the truth of 
        {character}'s {identity} might be their undoing."""
    ),
    'p_story26': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The night was {adjective} and the air in {location} was thick 
        with fear. {villain} had unleashed a dangerous {substance}, 
        glowing a poisonous {color}. {character}, armed with a cursed 
        {weapon}, and {sidekick}, their silent partner, embarked on 
        their final quest to {quest}. The {creature}s that once roamed freely 
        now writhed in agony, twisted by the toxin. The scent of decayed 
        {food} was inescapable. With a single {verb}, they moved toward 
        {villain}'s lair, knowing that the darkest secret of all— 
        {character}'s {identity}—was about to be revealed."""
    ),
    'p_story27': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """In the heart of {location}, {villain} was waiting, surrounded 
        by the {color} glow of the {substance}. {character} and {sidekick} 
        pushed forward, their quest to {quest} hanging in the balance. The land 
        had been devastated, filled with {creature}s born from the 
        toxic mist. Armed with a cursed {weapon} and the power to 
        {superpower}, {character} felt the weight of their secret 
        {identity} closing in. The smell of spoiled {food} filled their 
        lungs as they approached the final showdown. "It's now or never," 
        {sidekick} whispered. A final {verb}, and they would face the 
        evil that awaited them."""
    ),
    'p_story28': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """Beneath the {adjective} skies of {location}, {character} and 
        {sidekick} braced for their final confrontation with {villain}. 
        The villain had created a devastating weapon using the cursed 
        {substance}, a {color} liquid capable of consuming life itself. 
        With their {weapon} in hand and the ability to {superpower}, 
        {character} moved through the desolate streets, stepping over 
        the remains of {creature}s. The scent of burnt {food} clung to 
        them as they approached {villain}'s lair. "This is it," 
        {sidekick} whispered. With a last {verb}, they prepared to face 
        the end, unsure if {character}'s {identity} would survive the 
        battle ahead."""
    ),
    'p_story29': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The city of {location} had become a {adjective} wasteland 
        after {villain} released the {substance}. {character} and 
        {sidekick} stood in the shadow of {villain}'s fortress, their 
        quest to {quest} nearing its bitter end. Armed with the {weapon} and 
        the ability to {superpower}, {character} could feel the 
        creeping influence of the {color} substance. The streets were 
        littered with {creature}s, the air thick with the stench of 
        rotting {food}. "This is our last chance," {sidekick} warned. 
        One final {verb}, and they would confront their greatest foe, 
        but the truth of {character}'s {identity} was a threat all its 
        own."""
    ),
    'p_story30': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The air in {location} was toxic, filled with the deadly fumes 
        of the {substance} {villain} had unleashed. {character} and 
        {sidekick} moved through the {adjective} streets, the glow of 
        the {color} substance lighting their path. Their quest to {quest} was 
        almost over, but the weight of it was crushing. Armed with the 
        cursed {weapon}, {character} could feel their grip on reality 
        slipping. The stench of burned {food} and the cries of 
        mutated {creature}s filled the air. "We have no choice," 
        {sidekick} murmured. A final {verb}, and they would reach 
        {villain}, but the truth of {character}'s {identity} might be 
        their undoing."""
    ),
    'p_story31': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """In the {adjective} darkness of {location}, {character} and 
        {sidekick} faced a grim choice. {villain}'s {substance}, a 
        glowing {color} liquid, had poisoned the land and twisted the 
        minds of the {creature}s that once lived there. With their 
        {weapon} and the power to {superpower}, {character} knew they 
        were on a path of no return. The smell of rotting {food} filled 
        their senses as they approached {villain}'s lair. "We can't 
        hesitate now," {sidekick} said softly. With a final {verb}, 
        {character} confronted their greatest enemy, but it was their 
        {identity} that would be tested most of all."""
    ),
    'p_story32': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The {adjective} city of {location} was dying. {villain}'s 
        {substance}, a glowing {color} material, had seeped into 
        every corner, warping everything it touched. {character} and 
        {sidekick} moved through the desolation, their quest to {quest} to 
        stop the madness close to failure. Armed with the {weapon} 
        and the ability to {superpower}, they fought their way through 
        the {creature}s created by the substance. The stench of 
        burnt {food} filled the air. "We're running out of time," 
        {sidekick} warned. One last {verb}, and they would face 
        {villain}, but the real challenge would be protecting 
        {character}'s hidden {identity}."""
    ),
    
    'p_story33': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """In the {adjective} alleys of {location}, {character} and {sidekick} 
        hunted the elusive {villain}, who had perfected a toxic {substance} 
        that gleamed {color} under the streetlights. Armed with a cursed 
        {weapon} and the power to {superpower}, {character} pushed forward, 
        knowing their quest to {quest} was becoming more hopeless with each step. 
        The streets were overrun with mutated {creature}s, and the smell of 
        decayed {food} was suffocating. "Time is running out," {sidekick} 
        whispered. With one final {verb}, they would confront {villain}, but 
        keeping {character}'s true {identity} hidden would be a dangerous task."""
    ),
    'p_story34': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The storm over {location} raged on as {character} and {sidekick} 
        ventured deeper into the {adjective} ruins. {villain} had crafted a 
        deadly {substance} that shimmered {color} in the darkness, a weapon 
        capable of destroying everything. Armed with their {weapon} and the 
        ability to {superpower}, {character} knew their quest to {quest} would cost 
        them dearly. The once peaceful land was now crawling with {creature}s, 
        and the scent of rotting {food} filled their lungs. "This is a trap," 
        {sidekick} warned. But with a final {verb}, they moved closer to 
        {villain}, knowing that revealing {character}'s {identity} could be 
        their final mistake."""
    ),
    'p_story35': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The once {adjective} paradise of {location} had become a nightmare, 
        ravaged by the {substance} that {villain} unleashed. The {color} 
        taint had spread, warping both land and life. {character} and 
        {sidekick}, armed with the {weapon} and the power to {superpower}, 
        pressed on in their quest to {quest} to stop the madness. The streets were 
        filled with the cries of twisted {creature}s, and the scent of 
        rancid {food} clung to the air. "We may not survive this," 
        {sidekick} muttered. A final {verb} brought them face to face with 
        {villain}, but the real danger lay in {character}'s own {identity}.” """
    ),
    'p_story36': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The darkened streets of {location} echoed with the screams of 
        those who had been affected by the {substance} {villain} released. 
        {character}, alongside {sidekick}, moved through the {adjective} 
        wasteland with their {weapon}, knowing the power to {superpower} 
        might not be enough. The {color} glow of the toxin filled the air, 
        and the smell of spoiled {food} made them gag. "This place is dead," 
        {sidekick} whispered. Their quest to {quest} was now a battle of survival 
        as mutated {creature}s hunted them. With a final {verb}, they faced 
        {villain}, but could {character} keep their hidden {identity} safe?” """
    ),
    'p_story37': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The crumbling walls of {location} stood silent as {character} and 
        {sidekick} tracked {villain} through the {adjective} ruins. {villain} 
        had discovered a {substance}, a glowing {color} liquid that could 
        destroy worlds. With the cursed {weapon} in hand and the ability to 
        {superpower}, {character} knew they were outmatched, but the quest to {quest} 
        had to go on. The streets were filled with twisted {creature}s, and 
        the smell of burnt {food} lingered in the air. "We won't make it," 
        {sidekick} warned. With a final {verb}, they faced {villain}, but 
        the truth of {character}'s {identity} could shatter everything.” """
    ),
    'p_story38': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """In the dead of night, {character} and {sidekick} moved through 
        the {adjective} forest of {location}, searching for {villain}. The 
        villain had unleashed a deadly {substance}, a {color} toxin that 
        had spread through the air, twisting the land and the creatures 
        that lived there. With the {weapon} in hand and the power to 
        {superpower}, {character} led the charge, knowing this quest to {quest} was 
        likely to end in death. The scent of decaying {food} filled their 
        lungs. "We're running out of time," {sidekick} murmured. With one 
        last {verb}, they reached {villain}, but could {character}'s 
        {identity} survive the coming storm?” """
    ),
    'p_story39': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The {adjective} streets of {location} were filled with terror 
        as {character} and {sidekick} chased {villain} through the 
        wreckage. {villain} had created a deadly {substance} with a 
        strange {color} glow, and it was spreading fast. Armed with 
        their cursed {weapon} and the ability to {superpower}, 
        {character} knew the quest to {quest} to stop this destruction was 
        hopeless. The land was overrun by {creature}s, and the stench 
        of charred {food} hung in the air. "This is the end," {sidekick} 
        said quietly. With one final {verb}, they prepared to face 
        {villain}, but {character}'s hidden {identity} might be their 
        true undoing."""
    ),
    'p_story40': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The horizon over {location} was {adjective}, dark clouds 
        looming as {character} and {sidekick} followed the trail of 
        {villain}. The villain had weaponized a {substance}, its 
        {color} glow poisoning everything it touched. Armed with a 
        {weapon} and the power to {superpower}, {character} knew they 
        were walking into a death trap. The stench of decayed {food} 
        filled their senses as {creature}s writhed in the streets. 
        "There's no turning back," {sidekick} said. With a last 
        desperate {verb}, they reached {villain}'s lair, but the cost 
        might be revealing {character}'s true {identity}.” """
    ),
    'p_story41': SuperheroStory(
        ["character", "sidekick", "villain", "weapon", "superpower", 
         "substance", "color", "location", "food", "quest", "adjective", 
         "verb", "noun", "creature", "identity"],
        """The {adjective} streets of {location} echoed with the screams 
        of those touched by {villain}'s {substance}. The glowing {color} 
        mist twisted everything in its path, turning the city into a 
        nightmare. {character} and {sidekick}, armed with the cursed 
        {weapon} and the power to {superpower}, raced against time. Their 
        quest to {quest} had become a race for survival, with {creature}s lurking 
        around every corner. The stench of decaying {food} was overpowering. 
        "We can't stop now," {sidekick} whispered. With one final {verb}, 
        they moved toward the villain’s lair, knowing that {character}'s 
        secret {identity} could cost them everything.” """
    ),
}