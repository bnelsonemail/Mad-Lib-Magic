"""Madlibs Detective Stories."""


class BiblicalStory:
    """A Mad Libs Biblical Story.

    To create a Biblical story, pass a list of prompts and the text
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
    
    
# Collection of Biblical Themed Stories
BiblicalStories = {
    'p_story1': BiblicalStory(
        ["character-male", "character-female", "miracle", "weapon", "emotion", "object",
         "color", "location", "food", "quest", "adjective", "verb", "noun",
         "creature", "weather", "commandment"],
        """Jesus and {character-male} were walking near {location} when a great 
        {miracle} occurred. The {weather} changed, and the sky turned {color}. 
        Suddenly, a {creature} appeared. {character-male} instinctively reached 
        for his {weapon}, but Jesus, filled with {emotion}, told him to stay 
        calm. Instead, Jesus performed the {miracle} using only a {object}. 
        They continued their {quest}, grateful for God's {adjective} power. 
        When they arrived at their destination, they shared a meal of {food} 
        and gave thanks. Jesus reminded them of the {commandment} and told 
        them to {verb} with all their hearts. The people praised God, thanking 
        Him for His {noun}."""
    ),

    'p_story2': BiblicalStory(
        ["character-female", "miracle", "weapon", "object", "location", 
         "emotion", "creature", "weather", "food", "verb", "quest", "color", 
         "adjective", "noun", "commandment"],
        """One day, {character-female} was traveling through {location} when 
        she encountered a {creature}. Frightened, she felt {emotion}, but then 
        remembered the stories of Jesus performing miracles. She prayed, and 
        suddenly a {miracle} happened. The {weather} cleared, and the sky 
        turned {color}. She saw an {object} lying on the ground and realized 
        it was a sign. She completed her {quest} by picking up the {object} 
        and bringing it back to her village. When she returned, the people 
        celebrated with a feast of {food}, and they all remembered to {verb} 
        and follow the {commandment}. The {adjective} moment brought them 
        closer to God, and they rejoiced in His {noun}."""
    ),

    'p_story3': BiblicalStory(
        ["character-male", "miracle", "location", "weapon", "emotion", 
         "creature", "weather", "object", "food", "quest", "color", "verb", 
         "adjective", "noun", "commandment"],
        """{character-male} was on his way to {location} when a terrible storm 
        arose. The sky turned {color}, and he felt {emotion} as a giant 
        {creature} appeared before him. Just when he thought all hope was lost, 
        Jesus appeared and performed a great {miracle}. The {creature} fled, 
        and the storm subsided. Grateful, {character-male} continued his 
        {quest}, finding a {object} that reminded him of God's {adjective} 
        power. He returned home and shared his story over a meal of {food}, 
        reminding everyone to {verb} and keep the {commandment}. The village 
        praised God for His {noun}, and their faith grew stronger."""
    ),

    'p_story4': BiblicalStory(
        ["character-female", "location", "miracle", "weapon", "object", 
         "creature", "food", "emotion", "verb", "weather", "color", 
         "commandment", "adjective", "quest", "noun"],
        """Jesus and {character-female} were traveling through {location} when 
        they encountered a fierce {creature}. {character-female} felt {emotion} 
        and reached for her {weapon}, but Jesus stopped her. Instead, He 
        performed a {miracle}, calming the {creature}. The sky cleared, and the 
        {weather} turned calm and {color}. Jesus picked up a {object} and 
        handed it to her as a reminder of God's {adjective} love. Together, 
        they completed their {quest} and shared a meal of {food}. Jesus spoke 
        of the {commandment} and urged them all to {verb} with faith. The day 
        ended with praises for God's {noun}, and the people were blessed."""
    ),

    'p_story5': BiblicalStory(
        ["character-male", "character-female", "miracle", "location", "weapon", 
         "creature", "emotion", "food", "weather", "object", "verb", "quest", 
         "color", "adjective", "noun", "commandment"],
        """While Jesus was teaching near {location}, {character-male} and 
        {character-female} came forward seeking help. They had encountered a 
        {creature} and were filled with {emotion}. Jesus listened and, with 
        great compassion, performed a {miracle}, saving them from their fear. 
        The {weather} shifted, and the sky turned {color}. In gratitude, they 
        continued their {quest}, finding a {object} along the way. They shared 
        a meal of {food}, and Jesus reminded them to {verb} with all their 
        strength, following the {commandment}. The people praised God for His 
        {adjective} love, and the {noun} of the day was remembered by all."""
    ),

    'p_story6': BiblicalStory(
        ["character-male", "location", "miracle", "creature", "weapon", 
         "emotion", "object", "food", "weather", "verb", "quest", "color", 
         "adjective", "commandment", "noun"],
        """{character-male} was walking along the road to {location}, when 
        suddenly a {creature} appeared from the shadows. He felt {emotion}, 
        gripping his {weapon}, but Jesus appeared and performed a {miracle}. 
        The {creature} fled, and {character-male} found a {object} nearby as a 
        reminder of the event. He continued his {quest}, and when he arrived, 
        he shared a meal of {food} with the people. The {weather} turned calm, 
        and they all praised God for His {adjective} work. Jesus reminded them 
        to {verb} and to follow the {commandment}. The village celebrated the 
        {noun} of the day and grew stronger in their faith."""
    ),

    'p_story7': BiblicalStory(
        ["character-female", "location", "miracle", "weapon", "object", 
         "creature", "food", "emotion", "verb", "weather", "color", 
         "adjective", "noun", "quest", "commandment"],
        """{character-female} was traveling to {location}, where she hoped to 
        complete a {quest}. Along the way, she encountered a {creature} that 
        filled her with {emotion}. Reaching for her {weapon}, she prayed for 
        guidance. Suddenly, Jesus appeared and performed a {miracle}, and the 
        {creature} disappeared. The sky turned {color}, and the {weather} 
        became calm. She continued on her journey and found a {object} that 
        reminded her of God's {adjective} grace. When she arrived, she shared 
        a meal of {food} with the people and reminded them to {verb} the 
        {commandment}. The {noun} of the day was a blessing to all, and they 
        gave thanks to God."""
    ),

    'p_story8': BiblicalStory(
        ["character-male", "miracle", "location", "weapon", "creature", "food", 
         "emotion", "verb", "object", "quest", "weather", "color", "adjective", 
         "noun", "commandment"],
        """{character-male} was on a journey to {location}, where he hoped to 
        find peace. However, as he walked, a fierce {creature} emerged, and he 
        felt great {emotion}. Reaching for his {weapon}, he prepared to defend 
        himself, but Jesus appeared and performed a {miracle}, calming the 
        {creature}. The {weather} cleared, and the sky turned {color}. 
        Grateful, {character-male} found a {object} as a sign of God's presence 
        and completed his {quest}. When he returned, he shared a meal of {food} 
        with his people and reminded them to {verb} the {commandment}. The 
        {adjective} {noun} of the day brought joy to all, and they praised God."""
    ),

    'p_story9': BiblicalStory(
        ["character-female", "miracle", "location", "creature", "weapon", 
         "emotion", "food", "object", "verb", "quest", "weather", "color", 
         "adjective", "noun", "commandment"],
        """{character-female} was walking near {location} when a great storm 
        arose. The {weather} turned violent, and a {creature} appeared. Filled 
        with {emotion}, she reached for her {weapon}, but Jesus appeared and 
        performed a {miracle}. The storm stopped, and the sky turned {color}. 
        As a sign of God's grace, she found a {object} on the ground and 
        completed her {quest}. When she returned home, she shared a meal of 
        {food} with her family and reminded them to {verb} the {commandment}. 
        The {adjective} {noun} of the day was a reminder of God's protection."""
    ),

    'p_story10': BiblicalStory(
        ["character-male", "character-female", "miracle", "location", "weapon", 
         "object", "creature", "food", "weather", "emotion", "verb", "quest", 
         "color", "adjective", "noun", "commandment"],
        """As Jesus and {character-male} traveled to {location}, they met 
        {character-female} along the way. Together, they witnessed a {miracle}, 
        as Jesus calmed a {creature} that had been terrorizing the village. 
        They felt {emotion} and continued their {quest}. The {weather} turned 
        pleasant, and the sky became {color}. Along the road, they found a 
        {object} and knew it was a sign of God's {adjective} love. They shared 
        a meal of {food} and praised God. Jesus reminded them to {verb} and 
        keep the {commandment}, for the {noun} of the day was God's blessing."""
    ),
    
    'p_story11': BiblicalStory(
        ["character-male", "character-female", "miracle", "weapon", "emotion", 
         "object", "color", "location", "food", "quest", "adjective", "verb", 
         "noun", "creature", "weather", "commandment"],
        """While Jesus was teaching in {location}, He was approached by 
        {character-male} and {character-female}, who had been traveling for 
        days. They were seeking Jesus because they had heard of the many 
        {miracle}s He had performed. Their hearts were full of {emotion}, 
        hoping for a miracle of their own. In their hands, they carried a 
        {object}, which they believed held significance. When they arrived, 
        they saw a {creature} that appeared out of nowhere, causing the people 
        to panic. As the {weather} turned dark and the sky became {color}, 
        {character-male} reached for his {weapon}, prepared to defend the 
        crowd. But Jesus, with a calm voice, told him to {verb}. Jesus then 
        lifted His hands and performed a great {miracle}, causing the 
        {creature} to retreat and the weather to clear. The people were amazed 
        and praised God. Afterward, Jesus invited them to share a meal of 
        {food}. During the meal, Jesus reminded them of the importance of 
        keeping the {commandment}, for it was through obedience to God that 
        blessings would continue to flow. As they continued their {quest}, 
        they knew that the day had been marked by God's {adjective} presence, 
        and the {noun} they had carried became a symbol of their faith."""
    ),

    'p_story12': BiblicalStory(
        ["character-male", "character-female", "location", "miracle", "creature", 
         "emotion", "food", "verb", "weather", "weapon", "object", "quest", 
         "color", "adjective", "noun", "commandment"],
        """One day, {character-male} and {character-female} set out on a 
        journey to {location}. They were determined to find Jesus, for they 
        had heard of His ability to perform great miracles. Along their way, 
        they encountered a fierce {creature}. Filled with {emotion}, 
        {character-female} was tempted to turn back. But {character-male}, 
        filled with faith, encouraged her to press on. The {weather} began to 
        worsen, and soon the skies turned {color}. As the storm raged, Jesus 
        appeared before them and performed a {miracle}, calming the {creature} 
        and bringing peace to the land. Relieved, they continued on their 
        {quest}. They found a {object} lying along the path, and they took it 
        as a sign of God's guidance. When they reached their destination, they 
        shared a meal of {food}, and Jesus reminded them to {verb} and honor 
        the {commandment}, for God's ways were always {adjective}. The 
        {noun} they found became a testimony of their journey and God's 
        protection over them."""
    ),

    'p_story13': BiblicalStory(
        ["character-male", "character-female", "miracle", "location", "weapon", 
         "emotion", "object", "color", "weather", "food", "creature", "verb", 
         "quest", "adjective", "noun", "commandment"],
        """Jesus, {character-male}, and {character-female} were walking toward 
        {location} when they were confronted by a massive {creature}. The 
        creature stood in their path, roaring fiercely as the {weather} turned 
        ominous. {character-female} felt {emotion}, and {character-male} 
        instinctively reached for his {weapon}, but Jesus told him to stay his 
        hand. Jesus performed a {miracle}, calming the creature and causing 
        the skies to turn {color}. As they continued their {quest}, they found 
        a {object} lying on the ground. They picked it up, knowing it was a 
        sign from God. When they reached their destination, they shared a meal 
        of {food} with the people, praising God's {adjective} power. Jesus 
        reminded them to {verb} and always honor the {commandment}, for their 
        faith had brought them through. The {noun} they carried would forever 
        remind them of this day of divine intervention."""
    ),

    'p_story14': BiblicalStory(
        ["character-male", "location", "miracle", "creature", "weapon", "emotion", 
         "object", "food", "verb", "color", "weather", "quest", "adjective", 
         "noun", "commandment"],
        """{character-male} set out for {location} with great anticipation. He 
        had heard that Jesus would be there, performing miracles and teaching 
        the people. As {character-male} traveled, the {weather} turned, and he 
        found himself caught in a terrible storm. The sky darkened to a deep 
        {color}, and suddenly a {creature} emerged from the shadows. 
        {character-male} felt {emotion} but remembered the stories of Jesus 
        calming storms and healing the sick. He reached for his {weapon} to 
        defend himself, but before he could act, Jesus appeared and performed 
        a {miracle}, causing the {creature} to disappear and the storm to 
        cease. As the sky cleared, {character-male} found a {object} on the 
        ground, which he took as a sign of God's protection. He continued on 
        his {quest}, finally reaching {location}. There, he shared a meal of 
        {food} with the people and praised God for His {adjective} works. 
        Jesus reminded them all to {verb} and keep the {commandment}, for God 
        was always with them. The {noun} he carried became a symbol of his 
        faith, and he shared the story with all who would listen."""
    ),

    'p_story15': BiblicalStory(
        ["character-male", "character-female", "miracle", "location", "creature", 
         "emotion", "weapon", "object", "food", "weather", "verb", "quest", 
         "color", "adjective", "noun", "commandment"],
        """Jesus and His disciples, including {character-male} and 
        {character-female}, were making their way toward {location}. Along the 
        road, a {creature} appeared, blocking their path. The skies grew dark, 
        and the {weather} became tumultuous. {character-male} and 
        {character-female} felt {emotion} as they reached for their {weapon}s. 
        But Jesus, knowing their hearts, told them to wait. He performed a 
        {miracle}, calming both the storm and the creature, causing it to move 
        aside. They continued their {quest} and soon found a {object} lying 
        on the ground. They took it with them, recognizing it as a sign from 
        God. Upon reaching their destination, they shared a meal of {food} 
        with the people, and Jesus reminded them all to {verb} the 
        {commandment}. God's {adjective} power was evident throughout the 
        journey, and the {noun} they found became a treasured symbol of God's 
        provision. The people rejoiced, knowing they had been blessed by the 
        presence of Jesus Himself."""
    ),

    'p_story16': BiblicalStory(
        ["character-male", "location", "miracle", "creature", "weapon", "emotion", 
         "object", "food", "weather", "verb", "quest", "color", "adjective", 
         "noun", "commandment"],
        """{character-male} was a humble man who lived in a small village near 
        {location}. One day, he heard that Jesus would be passing through, so 
        he set out to see Him. Along the way, he encountered a terrifying 
        {creature} that blocked his path. Filled with {emotion}, he reached 
        for his {weapon}, but something stopped him. He remembered hearing 
        about Jesus’ miracles and decided to pray instead. As he did, Jesus 
        appeared and performed a {miracle}, calming the {creature} and 
        clearing the skies, which had turned a dark {color}. The {weather} 
        became peaceful once again. {character-male} continued his {quest}, 
        finding a {object} on the side of the road, which he took as a sign of 
        God's grace. When he reached his destination, he shared a meal of 
        {food} with others who had come to see Jesus. Afterward, Jesus reminded 
        them to {verb} and keep the {commandment}. The {noun} that 
        {character-male} found became a symbol of his journey, and he returned 
        home with a renewed faith in God's {adjective} power."""
    ),

    'p_story17': BiblicalStory(
        ["character-male", "location", "miracle", "weapon", "creature", "food", 
         "emotion", "object", "weather", "verb", "quest", "color", "adjective", 
         "noun", "commandment"],
        """{character-male} had heard that Jesus was performing miracles in 
        {location}, and he decided to travel there in hopes of seeing one for 
        himself. Along the way, he encountered a vicious {creature} that 
        blocked his path. The skies turned {color}, and the {weather} became 
        stormy. {character-male} felt {emotion}, but instead of reaching for 
        his {weapon}, he prayed for protection. Suddenly, Jesus appeared and 
        performed a {miracle}, calming the storm and causing the creature to 
        flee. Relieved, {character-male} continued on his {quest}. He found a 
        {object} on the ground, which he knew was a sign from God. When he 
        reached {location}, he shared a meal of {food} with the people there. 
        Jesus reminded them all to {verb} and keep the {commandment}. The 
        {adjective} day ended with {character-male} returning home, carrying 
        the {noun} as a symbol of God's protection and grace."""
    ),

    'p_story18': BiblicalStory(
        ["character-female", "location", "miracle", "weapon", "creature", "food", 
         "emotion", "object", "weather", "verb", "quest", "color", "adjective", 
         "noun", "commandment"],
        """{character-female} had been searching for Jesus for many days. She 
        had heard He was near {location}, performing miracles. Determined, she 
        set out on her {quest}. As she walked, a fierce {creature} appeared 
        before her, and the skies turned {color}. The {weather} grew dark, and 
        she felt {emotion}. She reached for her {weapon}, but before she could 
        act, Jesus appeared and performed a {miracle}. The creature vanished, 
        and the skies cleared. As a sign of God's presence, she found a 
        {object} on the ground. When she arrived at her destination, she 
        shared a meal of {food} with the people. Jesus reminded them to {verb} 
        and honor the {commandment}, for God's ways were always {adjective}. 
        The {noun} she found became a symbol of her faith and courage, and she 
        returned home knowing that God had been with her throughout her 
        journey."""
    ),

    'p_story19': BiblicalStory(
        ["character-male", "location", "miracle", "creature", "weapon", "object", 
         "emotion", "food", "weather", "verb", "quest", "color", "adjective", 
         "noun", "commandment"],
        """{character-male} set out from his home near {location}, seeking 
        Jesus. As he traveled, he encountered a terrifying {creature} that 
        blocked his path. The sky turned {color}, and the {weather} grew 
        stormy. Feeling {emotion}, {character-male} reached for his {weapon}, 
        but he remembered to pray instead. Jesus appeared and performed a 
        {miracle}, calming the {creature} and restoring peace to the land. As 
        the sky cleared, {character-male} found a {object} lying on the 
        ground, which he took as a sign from God. He continued his {quest}, 
        and when he reached his destination, he shared a meal of {food} with 
        the people. Jesus reminded them all to {verb} and keep the 
        {commandment}, for God's protection was always with them. The 
        {adjective} day ended with {character-male} returning home, carrying 
        the {noun} as a symbol of God's grace and protection."""
    ),

    'p_story20': BiblicalStory(
        ["character-female", "location", "miracle", "creature", "emotion", 
         "weapon", "object", "food", "weather", "verb", "quest", "color", 
         "adjective", "noun", "commandment"],
        """{character-female} was traveling to {location} in search of Jesus, 
        hoping to witness a miracle. As she walked, a large {creature} appeared 
        before her, blocking her path. The skies turned {color}, and the 
        {weather} became turbulent. Filled with {emotion}, she reached for her 
        {weapon}, but then she remembered the stories of Jesus calming storms 
        and healing the sick. She prayed, and suddenly Jesus appeared and 
        performed a {miracle}. The {creature} disappeared, and the skies 
        cleared. As a sign of God's grace, she found a {object} on the ground. 
        She continued her {quest} and reached {location}, where she shared a 
        meal of {food} with the people. Jesus reminded them all to {verb} and 
        keep the {commandment}, for God's protection was always with them. 
        The {adjective} day ended with {character-female} carrying the {noun} 
        back home as a symbol of God's grace and provision."""
    ),
    
    'p_story21': BiblicalStory(
        ["character-male", "character-female", "miracle", "weapon", "emotion", 
         "object", "color", "location", "food", "quest", "adjective", "verb", 
         "noun", "creature", "weather", "commandment"],
        """Jesus sat by the shore of {location}, teaching the people in parables. 
        {character-male} and {character-female} listened as Jesus spoke of the 
        Parable of the Sower. He explained how some seeds fell on rocky ground 
        while others fell on fertile soil. Later, as they traveled, they 
        encountered a {creature}. Filled with {emotion}, {character-male} 
        reached for his {weapon}. But Jesus calmed them with a {miracle}. 
        The {weather} shifted, and the skies turned {color}. In their journey, 
        they found a {object}, which Jesus used as a lesson on faith. They 
        completed their {quest}, sharing a meal of {food}, and Jesus reminded 
        them to {verb} the {commandment}. God's {adjective} power became a 
        beacon of hope for them. The people praised God for His {noun}."""
    ),

    'p_story22': BiblicalStory(
        ["character-male", "location", "miracle", "creature", "weapon", "object", 
         "food", "emotion", "verb", "weather", "color", "quest", "adjective", 
         "noun", "commandment"],
        """One day, Jesus and {character-male} entered {location}, where the 
        people gathered to hear the Parable of the Lost Sheep. As Jesus spoke 
        of a shepherd who left ninety-nine sheep to find one lost, a great 
        {creature} appeared from the distance. The people felt {emotion}, but 
        Jesus performed a {miracle}, calming the creature. The skies turned 
        {color}, and the {weather} became peaceful. As they walked, 
        {character-male} found a {object} on the path, which Jesus used to 
        teach the crowd about God's love. They shared a meal of {food}, and 
        Jesus reminded them to {verb} the {commandment}, for God's grace was 
        {adjective}. The {noun} they found became a symbol of their faith in 
        God, and the crowd left praising His name."""
    ),

    'p_story23': BiblicalStory(
        ["character-male", "character-female", "miracle", "location", "creature", 
         "emotion", "weapon", "object", "food", "weather", "verb", "color", 
         "quest", "adjective", "noun", "commandment"],
        """As Jesus taught in {location}, He shared the Parable of the Good 
        Samaritan. He explained how a traveler was beaten and left by the road, 
        but a Samaritan showed mercy. Later, {character-male} and 
        {character-female} encountered a {creature} as they traveled on their 
        {quest}. The skies turned {color}, and {emotion} filled their hearts. 
        {character-male} reached for his {weapon}, but Jesus performed a 
        {miracle}, bringing peace. They found a {object} on the path, which 
        Jesus used as a reminder of mercy and compassion. They shared a meal 
        of {food} and praised God's {adjective} grace. Jesus reminded them to 
        {verb} the {commandment}, for love was greater than all. The {noun} 
        became a lasting reminder of their journey of faith."""
    ),

    'p_story24': BiblicalStory(
        ["character-male", "miracle", "location", "creature", "emotion", "weapon", 
         "object", "food", "weather", "verb", "quest", "color", "adjective", 
         "noun", "commandment"],
        """Jesus and {character-male} walked toward {location}, where a great 
        crowd awaited His teaching. Jesus spoke to them in the Parable of the 
        Mustard Seed, explaining how even the smallest seed can grow into the 
        largest tree. As they journeyed, a fierce {creature} blocked their 
        path. The skies turned {color}, and {character-male} felt {emotion}. 
        He reached for his {weapon}, but Jesus calmed him and performed a 
        {miracle}. They found a {object} along the road, which Jesus used as 
        a lesson about faith. They shared a meal of {food}, and Jesus reminded 
        them to {verb} and keep the {commandment}. The {adjective} skies 
        cleared, and they completed their {quest}. The {noun} they carried 
        became a reminder of God's unfailing love and power."""
    ),

    'p_story25': BiblicalStory(
        ["character-female", "location", "miracle", "creature", "weapon", 
         "emotion", "object", "food", "weather", "verb", "quest", "color", 
         "adjective", "noun", "commandment"],
        """As {character-female} walked with Jesus toward {location}, she 
        listened as He told the Parable of the Prodigal Son. He spoke of a 
        father who rejoiced when his wayward son returned home. They continued 
        their {quest}, and suddenly, a large {creature} appeared. The skies 
        turned {color}, and {character-female} felt {emotion}. She reached for 
        her {weapon}, but Jesus performed a {miracle}, calming the creature. 
        They found a {object} along the road, which Jesus used to remind them 
        of God's forgiveness. They shared a meal of {food}, and Jesus reminded 
        them to {verb} and follow the {commandment}, for God’s love was 
        {adjective}. The {noun} they carried became a symbol of redemption and 
        grace, and the people gave thanks to God."""
    ),

    'p_story26': BiblicalStory(
        ["character-male", "miracle", "location", "creature", "emotion", "weapon", 
         "object", "food", "weather", "verb", "quest", "color", "adjective", 
         "noun", "commandment"],
        """Jesus and {character-male} arrived in {location}, where He shared the 
        Parable of the Talents with the crowd. He taught how each person is 
        entrusted with gifts and how they should be used wisely. As they 
        traveled, a dangerous {creature} appeared. The skies turned {color}, 
        and {character-male} felt {emotion}. He reached for his {weapon}, but 
        Jesus performed a {miracle}, calming the storm and the creature. They 
        found a {object} on their path, which Jesus used to remind them to use 
        their talents for God's glory. They shared a meal of {food}, and Jesus 
        urged them to {verb} and keep the {commandment}. The people praised 
        God's {adjective} power, and the {noun} they carried became a reminder 
        of their call to serve God faithfully."""
    ),

    'p_story27': BiblicalStory(
        ["character-male", "character-female", "miracle", "location", "creature", 
         "emotion", "weapon", "object", "food", "weather", "verb", "quest", 
         "color", "adjective", "noun", "commandment"],
        """As Jesus and His disciples, including {character-male} and 
        {character-female}, approached {location}, He told the Parable of the 
        Wise and Foolish Builders. He explained how those who build their 
        lives on God's Word are like a wise man who built his house on a rock. 
        Soon after, they encountered a terrifying {creature}. The skies turned 
        {color}, and {emotion} filled their hearts. {character-male} reached 
        for his {weapon}, but Jesus performed a {miracle}, calming the creature 
        and bringing peace. They found a {object} along the road, which Jesus 
        used to remind them of God's firm foundation. They shared a meal of 
        {food} and continued their {quest}. Jesus reminded them to {verb} the 
        {commandment}, for God's ways were {adjective}. The {noun} they found 
        became a symbol of God's protection and guidance."""
    ),

    'p_story28': BiblicalStory(
        ["character-male", "location", "miracle", "creature", "emotion", "weapon", 
         "object", "food", "weather", "verb", "quest", "color", "adjective", 
         "noun", "commandment"],
        """As Jesus and {character-male} traveled toward {location}, Jesus 
        taught the people the Parable of the Rich Fool. He warned them not to 
        store up treasures for themselves but to be rich toward God. As they 
        walked, a great {creature} appeared, and the skies turned {color}. 
        {character-male} felt {emotion} as he reached for his {weapon}, but 
        Jesus performed a {miracle}, calming the creature and clearing the 
        skies. They found a {object} along their path, which Jesus used to 
        remind the people of God’s providence. They shared a meal of {food}, 
        and Jesus urged them to {verb} and keep the {commandment}. The 
        {adjective} day ended with the people praising God's {noun} and 
        thanking Him for His faithfulness."""
    ),

    'p_story29': BiblicalStory(
        ["character-female", "location", "miracle", "creature", "emotion", "weapon", 
         "object", "food", "weather", "verb", "quest", "color", "adjective", 
         "noun", "commandment"],
        """{character-female} followed Jesus to {location}, where He shared the 
        Parable of the Vineyard Workers. He taught about the generosity of God, 
        who gives the same reward to all who serve Him, regardless of when 
        they started. As they traveled, they encountered a fierce {creature}, 
        and the skies turned {color}. {character-female} felt {emotion}, but 
        instead of reaching for her {weapon}, she prayed. Jesus performed a 
        {miracle}, calming the creature and the storm. They found a {object} 
        along their path, which Jesus used to teach about God’s generosity. 
        They shared a meal of {food}, and Jesus reminded them to {verb} and 
        follow the {commandment}, for God’s ways were {adjective}. The {noun} 
        they carried became a lasting symbol of God's grace and love."""
    ),

    'p_story30': BiblicalStory(
        ["character-male", "location", "miracle", "creature", "emotion", "weapon", 
         "object", "food", "weather", "verb", "quest", "color", "adjective", 
         "noun", "commandment"],
        """As {character-male} walked with Jesus toward {location}, he listened 
        as Jesus shared the Parable of the Pharisee and the Tax Collector. He 
        taught how humility is key in the eyes of God. Soon after, they 
        encountered a dangerous {creature}. The skies turned {color}, and 
        {character-male} felt {emotion}. He reached for his {weapon}, but 
        Jesus performed a {miracle}, bringing peace. They found a {object} 
        along the road, which Jesus used to remind them of the importance of 
        humility. They shared a meal of {food}, and Jesus reminded them to 
        {verb} and keep the {commandment}, for God's ways were {adjective}. 
        The {noun} became a powerful symbol of humility and grace, reminding 
        them to always trust in God."""
    ),
    
    'p_story31': BiblicalStory(
        ["character-male", "character-female", "miracle", "weapon", "emotion", 
         "object", "color", "location", "food", "quest", "adjective", "verb", 
         "noun", "creature", "weather", "commandment"],
        """On the night of the Passover, Jesus gathered with His disciples, 
        including {character-male} and {character-female}, in the upper room 
        in {location}. They shared the Last Supper, where Jesus broke bread and 
        passed a cup of {food}, saying, "This is my body and my blood." 
        {character-male} felt a deep {emotion} as Jesus spoke of His coming 
        sacrifice. After the meal, they went to the Garden of Gethsemane to 
        pray. The night was {color}, and the {weather} was tense. Suddenly, a 
        group of soldiers appeared with swords and {weapon}s, and Jesus was 
        arrested. {character-female} watched in sorrow as Jesus was led away, 
        knowing His {quest} was nearing its darkest hour. Yet, Jesus reminded 
        them to keep the {commandment} and trust in God's {adjective} plan. 
        The {noun} of that night would forever be remembered as the beginning 
        of the ultimate sacrifice."""
    ),

    'p_story32': BiblicalStory(
        ["character-male", "character-female", "location", "miracle", "creature", 
         "emotion", "food", "verb", "weather", "weapon", "object", "quest", 
         "color", "adjective", "noun", "commandment"],
        """As Jesus was brought before Pontius Pilate at {location}, He stood 
        silently while the crowd called for His crucifixion. {character-male} 
        and {character-female} were among the onlookers, filled with 
        {emotion}. The sky grew dark, and the {weather} became ominous as Jesus 
        carried His cross. Along the way, they saw Him stumble, and a man named 
        Simon was called to help carry the {object}. They followed Jesus to 
        Golgotha, where He was nailed to the cross. The {color} sky and 
        {adjective} winds marked the sadness of the day. Even in this moment, 
        Jesus performed a {miracle} of forgiveness, asking His Father to forgive 
        those who crucified Him. As they watched, they were reminded to {verb} 
        and follow the {commandment}, for the {noun} of that day would change 
        the world forever."""
    ),

    'p_story33': BiblicalStory(
        ["character-male", "miracle", "location", "weapon", "creature", 
         "emotion", "object", "food", "weather", "verb", "quest", "color", 
         "adjective", "noun", "commandment"],
        """After Jesus was crucified, He was laid in a tomb at {location}, and a 
        large stone was rolled in front of the entrance. {character-male} stood 
        nearby, filled with {emotion}. The {weather} was still, and the 
        {creature}s of the night made no sound. On the third day, Mary Magdalene 
        came to the tomb and found the stone rolled away. Jesus had risen! An 
        angel appeared, dressed in {color}, and said, "Why do you look for the 
        living among the dead?" The miracle of the resurrection had occurred. 
        {character-male} rejoiced and ran to tell the others. He remembered to 
        {verb} the {commandment} and share the good news. The {object} he found 
        at the tomb became a reminder of that {adjective} day, and the 
        {noun} of the resurrection filled his heart with hope."""
    ),

    'p_story34': BiblicalStory(
        ["character-female", "miracle", "location", "creature", "emotion", 
         "weapon", "object", "food", "weather", "verb", "quest", "color", 
         "adjective", "noun", "commandment"],
        """Early on the morning of the resurrection, {character-female} went to 
        the tomb at {location}. The sky was {color}, and the {weather} was 
        peaceful. She was filled with {emotion} as she approached the entrance, 
        expecting to find the tomb sealed. Instead, she saw an angel who told 
        her, "He is not here; He has risen!" The stone had been rolled away, and 
        Jesus had conquered death. She remembered the words of Jesus and the 
        {commandment} He had given them. She ran to tell the disciples the good 
        news, her heart filled with {adjective} joy. Along the way, she found a 
        {object}, which reminded her of the miracle she had witnessed. They all 
        gathered and shared a meal of {food}, celebrating the {noun} of the 
        resurrection, knowing that their {quest} had only just begun."""
    ),

    'p_story35': BiblicalStory(
        ["character-male", "character-female", "miracle", "location", "creature", 
         "emotion", "weapon", "object", "food", "weather", "verb", "quest", 
         "color", "adjective", "noun", "commandment"],
        """After the resurrection, Jesus appeared to His disciples in {location}. 
        {character-male} and {character-female} were among them, their hearts 
        filled with {emotion}. Jesus showed them His hands and side, proving 
        that He had truly risen. They were amazed at the {miracle} before them. 
        He spoke to them about forgiveness and love, urging them to {verb} and 
        keep the {commandment}. As they listened, the {weather} grew calm, and 
        the sky turned {color}. They found a {object} nearby, which Jesus used 
        to teach them about faith. Together, they shared a meal of {food}, and 
        the {noun} of that day became a symbol of their {adjective} faith in 
        the risen Lord. Their {quest} to spread the gospel had begun, and they 
        went forth with renewed strength and purpose."""
    ),

    'p_story36': BiblicalStory(
        ["character-female", "location", "miracle", "creature", "emotion", 
         "weapon", "object", "food", "weather", "verb", "quest", "color", 
         "adjective", "noun", "commandment"],
        """Three days after the crucifixion, {character-female} came to the tomb 
        at {location}. The stone had been rolled away, and the body of Jesus was 
        gone. Filled with {emotion}, she stood weeping when a {creature} 
        appeared beside her. "Why are you crying?" asked the voice. She turned 
        and saw Jesus, alive and risen! It was a {miracle}, and her heart 
        rejoiced. She ran to tell the disciples the good news. The {weather} 
        brightened, and the sky turned {color}. Along her path, she found a 
        {object}, which reminded her of the resurrection. They gathered together 
        and shared a meal of {food}, praising God for His {adjective} power. 
        Jesus reminded them to {verb} and follow the {commandment}, for their 
        {quest} to spread the gospel had just begun. The {noun} of that day 
        would be remembered forever as a sign of hope and victory over death."""
    ),

    'p_story37': BiblicalStory(
        ["character-male", "location", "miracle", "creature", "emotion", 
         "weapon", "object", "food", "weather", "verb", "quest", "color", 
         "adjective", "noun", "commandment"],
        """On the morning of the resurrection, {character-male} walked to the 
        tomb at {location}, where the body of Jesus had been laid. As he 
        approached, he saw that the stone had been rolled away. His heart 
        filled with {emotion}, he stepped inside and saw an angel, who told him 
        that Jesus had risen. The {weather} was calm, and the sky turned 
        {color} as the angel reminded him of Jesus' words. He found a {object} 
        near the entrance, which became a symbol of the {miracle} he had 
        witnessed. He ran to tell the others, sharing the good news over a meal 
        of {food}. Together, they praised God's {adjective} power and vowed to 
        {verb} and keep the {commandment}. The {noun} of that day became a 
        reminder of the victory of Christ and the beginning of their {quest} to 
        spread the gospel throughout the world."""
    ),

    'p_story38': BiblicalStory(
        ["character-female", "location", "miracle", "creature", "emotion", 
         "weapon", "object", "food", "weather", "verb", "quest", "color", 
         "adjective", "noun", "commandment"],
        """After the crucifixion, {character-female} went to {location} with 
        spices to anoint the body of Jesus. She arrived early in the morning, 
        and the {weather} was still. As she approached the tomb, she noticed 
        the stone had been rolled away. Filled with {emotion}, she looked 
        inside and saw an angel who told her, "He is not here; He has risen!" 
        Overcome with joy, she found a {object} in the tomb, a reminder of the 
        {miracle} that had taken place. She hurried back to the disciples to 
        share the news. Together, they shared a meal of {food}, marveling at 
        God's {adjective} power. Jesus appeared to them, reminding them to 
        {verb} and keep the {commandment}. The {noun} of the resurrection 
        became a symbol of their faith and a source of strength for their 
        {quest} to proclaim the gospel to all nations."""
    ),

    'p_story39': BiblicalStory(
        ["character-male", "location", "miracle", "creature", "emotion", 
         "weapon", "object", "food", "weather", "verb", "quest", "color", 
         "adjective", "noun", "commandment"],
        """{character-male} stood at the foot of the cross in {location}, 
        watching as Jesus took His last breath. The skies turned {color}, and 
        the {weather} grew dark. Filled with {emotion}, he wept for the loss of 
        the Savior. Three days later, he came to the tomb and found the stone 
        rolled away. The miracle of the resurrection had occurred. An angel 
        appeared, dressed in {color}, and said, "He is not here; He has risen!" 
        {character-male} found a {object} in the tomb, which became a symbol of 
        his faith. He shared the good news with the others, and together they 
        shared a meal of {food}. Jesus appeared to them, reminding them to 
        {verb} and keep the {commandment}. The {adjective} day marked the 
        beginning of their {quest} to spread the gospel, and the {noun} they 
        found became a powerful reminder of God's victory over death."""
    ),

    'p_story40': BiblicalStory(
        ["character-male", "character-female", "location", "miracle", 
         "creature", "emotion", "weapon", "object", "food", "weather", "verb", 
         "quest", "color", "adjective", "noun", "commandment"],
        """As the sun rose on the morning of the third day, {character-male} and 
        {character-female} went to the tomb at {location}, their hearts heavy 
        with {emotion}. When they arrived, they found the stone had been rolled 
        away. The tomb was empty. An angel appeared and told them that Jesus 
        had risen from the dead. Overcome with joy, they found a {object} in 
        the tomb, a reminder of the {miracle} they had witnessed. The {weather} 
        brightened, and the sky turned {color}. They ran to tell the disciples, 
        sharing a meal of {food} in celebration. Jesus appeared to them, 
        reminding them to {verb} and keep the {commandment}, for their 
        {quest} to spread the gospel had begun. The {noun} they carried became 
        a symbol of hope and God's {adjective} love for all mankind."""
    ),
}