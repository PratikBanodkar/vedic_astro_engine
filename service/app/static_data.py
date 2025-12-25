# service/app/static_data.py

# --- PLANETARY LORDS (Standard Vedic) ---
PLANET_DETAILS = {
    0: {"id": 1, "name": "Sun", "vedic_name": "Surya"},
    1: {"id": 2, "name": "Moon", "vedic_name": "Chandra"},
    2: {"id": 3, "name": "Mars", "vedic_name": "Mangala"},
    3: {"id": 4, "name": "Mercury", "vedic_name": "Budha"},
    4: {"id": 5, "name": "Jupiter", "vedic_name": "Guru"},
    5: {"id": 6, "name": "Saturn", "vedic_name": "Shani"},
    6: {"id": 7, "name": "Venus", "vedic_name": "Shukra"},
    7: {"id": 8, "name": "Rahu", "vedic_name": "Rahu"},
    8: {"id": 9, "name": "Ketu", "vedic_name": "Ketu"},
}

# --- RASI (ZODIAC SIGNS) ---
# Map Index (0-11) to Rasi Name and Lord ID
RASI_DATA = {
    0: {"name": "Mesha", "lord_id": 2, "zodiac_name": "Aries"},
    1: {"name": "Vrishabha", "lord_id": 6, "zodiac_name": "Taurus"},
    2: {"name": "Mithuna", "lord_id": 3, "zodiac_name": "Gemini"},
    3: {"name": "Karka", "lord_id": 1, "zodiac_name": "Cancer"},
    4: {"name": "Simha", "lord_id": 0, "zodiac_name": "Leo"},
    5: {"name": "Kanya", "lord_id": 3, "zodiac_name": "Virgo"},
    6: {"name": "Tula", "lord_id": 6, "zodiac_name": "Libra"},
    7: {"name": "Vrischika", "lord_id": 2, "zodiac_name": "Scorpio"},
    8: {"name": "Dhanu", "lord_id": 4, "zodiac_name": "Sagittarius"},
    9: {"name": "Makara", "lord_id": 5, "zodiac_name": "Capricorn"},
    10: {"name": "Kumbha", "lord_id": 5, "zodiac_name": "Aquarius"},
    11: {"name": "Meena", "lord_id": 4, "zodiac_name": "Pisces"},
}

# --- NAKSHATRA FULL DATA ---
# This matches the Vimshottari Lord sequence: Ketu, Ven, Sun, Mon, Mar, Rah, Jup, Sat, Mer
NAKSHATRA_LORDS_ORDER = [8, 6, 0, 1, 2, 7, 4, 5, 3] 

YOGA_DESCRIPTIONS = {
    "Gajakesari Yoga": """Gajakesari Yoga is one of the most celebrated combinations in Vedic astrology, formed when Jupiter and the Moon are strongly connected through angular positions. This yoga is believed to bless a person with intelligence, good judgment, emotional balance, and a graceful personality. Individuals with this yoga often receive support from influential people and enjoy opportunities that help them grow in life. It brings a natural ability to lead and inspire others while maintaining humility. Professionally, this yoga supports success in learning, finance, leadership, communication, or any field requiring wisdom and clarity. Overall, it gives stability, prosperity, and a positive public image.""",

    "Kedar Yoga": """Kedar Yoga arises when all planets are located across four houses, creating a strong foundation of practicality and focus. This yoga enhances one’s ability to remain disciplined, organized, and committed to long-term goals. People with this yoga usually excel in tasks that require structure, patience, and steady effort rather than impulsive action. They tend to earn respect through sincerity rather than flashy achievements. Due to their stable nature, they become reliable individuals in both personal and professional relationships. This yoga also helps a person recover quickly from difficulties because of their consistent mindset and strong inner discipline.""",

    "Kahal Yoga": """Kahal Yoga is associated with courage, confidence, and strong initiative. It is formed by planetary combinations that amplify determination and the ability to take bold steps when required. Individuals with this yoga often display leadership qualities from a young age and are not afraid to stand up for themselves or for what they believe in. They tend to navigate challenges bravely and emerge stronger from experiences that might overwhelm others. Professionally, this yoga supports success in fields requiring authority, strategy, or independent decision-making. It gives a sense of purpose and the drive to pursue goals despite obstacles.""",

    "Kamal Yoga": """Kamal Yoga, formed when planets occupy all the Kendra houses, is known for creating stability and harmony in one’s life. People with this yoga often enjoy a balanced personal and professional environment, supported by steady progress and strong relationships. This yoga blesses an individual with clarity of mind, emotional grounding, and a peaceful approach to life’s challenges. It can also enhance creativity, nurturing a calm and aesthetically inclined personality. Kamal Yoga brings a sense of security, making the person confident in their abilities and decisions. It is considered a sign of a well-rounded and mature individual.""",

    "Musala Yoga": """Musala Yoga is formed when planets occupy all fixed signs, symbolizing determination, endurance, and a strong sense of loyalty. Individuals with this yoga are known for their ability to stay committed to their goals for long periods, even when progress is slow. They tend to be dependable, grounded, and emotionally stable, often becoming the steady pillar in their families or workplaces. This yoga also gives the strength to withstand emotional or professional pressure with patience and calmness. Such people prefer long-term results over quick gains and generally succeed through perseverance and consistency.""",

    "Raja Yoga": """Raja Yoga is among the most auspicious yogas, signifying authority, accomplishment, and overall prosperity. It forms when beneficial planets strengthen key houses of success, giving the individual opportunities to rise in status and recognition. People with this yoga often receive support from society, mentors, or elders and may occupy influential or respected positions. Raja Yoga enhances decision-making ability, confidence, and the capacity to handle responsibilities smoothly. While it doesn't guarantee overnight success, it ensures that the person is equipped with the qualities needed to achieve lasting growth. This yoga brings dignity, social respect, and a sense of fulfillment.""",

    "Ruchaka Yoga": """Ruchaka Yoga arises when Mars is strongly placed, giving physical strength, vitality, courage, and a proactive mindset. Individuals with this yoga are often energetic, competitive, and naturally inclined to take the lead in challenging situations. They possess a strong sense of justice and stand firm in their beliefs. This yoga is known to produce determined personalities who don’t back down easily and who excel in sports, defense, engineering, or roles requiring disciplined action. It also instills confidence and the ability to rise quickly when faced with obstacles. Overall, it represents dynamic energy and sharp focus.""",

    "Bhadra Yoga": """Bhadra Yoga, formed by a strong Mercury, brings intelligence, sharp memory, wit, and excellent communication skills. Individuals with this yoga are thoughtful, analytical, and quick learners with a natural ability to process information effectively. They often excel in professions involving logic, writing, negotiation, technology, or communication. This yoga enhances adaptability, helping the person manage multiple responsibilities with ease. It also refines speech and interpersonal abilities, allowing them to build harmonious relationships. People with Bhadra Yoga tend to be articulate, clever, and respected for their intellect.""",

    "Hamsa Yoga": """Hamsa Yoga emerges when Jupiter is strongly positioned, blessing the native with wisdom, spirituality, compassion, and emotional depth. People with this yoga possess a calm and generous personality, often guiding others through their knowledge and balanced perspective. They attract respect naturally due to their noble behavior and moral integrity. This yoga promotes good fortune, protection from difficulties, and opportunities for meaningful growth. It also enhances intuition and philosophical understanding, making the person mature beyond their years. Overall, it brings harmony, respect, and inner strength.""",

    "Malavya Yoga": """Malavya Yoga is formed by a powerful Venus, bringing charm, grace, refinement, and a love for beauty and luxury. Individuals with this yoga often have attractive personalities, strong social skills, and a natural ability to form harmonious relationships. They may excel in creative fields, artistic pursuits, or professions that involve aesthetics, luxury, or social interaction. This yoga also brings material comfort, a refined taste, and an appreciation for the finer things in life. It supports emotional harmony, romantic stability, and a pleasant living environment. People with Malavya Yoga are often seen as elegant and charming.""",

    "Sasa Yoga": """Sasa Yoga occurs when Saturn is powerfully placed, creating a personality marked by patience, discipline, resilience, and long-term vision. People with this yoga are capable of handling responsibilities with maturity and often achieve success later in life through consistent effort. They tend to be reliable, organized, and highly determined, even in challenging circumstances. This yoga also grants leadership ability, especially in structured environments or roles requiring strategy and management. Over time, individuals with Sasa Yoga develop strong inner strength and gain respect for their perseverance and dedication.""",
    
    "Sunafa Yoga": """Sunafa Yoga arises when the Moon is supported by benefic planets in the 2nd house from its position. This yoga indicates strong self-reliance, inner confidence, and mental clarity. Individuals with Sunafa Yoga tend to be resourceful, determined, and capable of building their life through consistent effort. Their personality often reflects emotional maturity and practicality in decision-making. They are naturally inclined to build wealth, improve their surroundings, and cultivate independence throughout life.""",

    "Anafa Yoga": """Anafa Yoga forms when planets occupy the 12th house from the Moon. This yoga generally brings a graceful personality, good manners, and a calm, composed mind. Individuals blessed with Anafa Yoga enjoy material comforts, possess artistic inclinations, and attract respect from society. Their intuition and creativity guide them to meaningful achievements. They often have a magnetic charm and emotional depth that help them build strong relationships and social influence.""",

    "Durudhara Yoga": """Durudhara Yoga is formed when both the 2nd and 12th houses from the Moon are occupied by planets. This combination strengthens the native’s ability to manage finances, resources, and relationships effectively. People with Durudhara Yoga lead balanced lives and benefit from stable support systems. They often develop strong interpersonal skills, practical intelligence, and a grounded demeanor. This yoga enhances stability, patience, and the ability to handle responsibilities with confidence.""",

    "Kemadruma Yoga": """Kemadruma Yoga occurs when there are no planets in the 2nd or 12th house from the Moon. Traditionally considered inauspicious, it is said to bring emotional restlessness, loneliness, or fluctuations in mindset. However, modern astrology emphasizes that other planetary strengths can significantly dilute its effects. Individuals with mitigated Kemadruma often develop immense resilience, independence, and inner strength. This yoga ultimately encourages spiritual growth and the ability to rise above early challenges.""",
    
    "Veshi Yoga": """Veshi Yoga forms when planets (except the Moon) occupy the 2nd house from the Sun. This yoga grants strong leadership qualities, ambition, and confidence. People with Veshi Yoga often rise to important roles due to their bold decisions and clarity of purpose. Their personality reflects determination, discipline, and the ability to inspire others. They are usually driven by personal goals and possess a commanding presence that attracts recognition.""",

    "Vaasi Yoga": """Vaasi Yoga occurs when planets (other than the Moon) are placed in the 12th house from the Sun. This yoga brings introspective abilities, spiritual depth, and disciplined thinking. Individuals with Vaasi Yoga excel in areas requiring strategy, creativity, or hidden skills. They approach challenges thoughtfully and possess a unique charm rooted in calmness and inner stability. Such natives often develop strong intuition and a reflective mindset.""",

    "Ubhayachari Yoga": """Ubhayachari Yoga is formed when planets occupy both the 2nd and 12th houses from the Sun. It enhances intelligence, organization, and social presence. Individuals with this yoga often become influential figures due to their balanced perspective and strong decision-making abilities. They enjoy success through consistent effort, adaptability, and a composed attitude. The yoga also indicates resourcefulness and the capacity to navigate life with confidence and clarity.""",

    "Daridra Yoga": """Daridra Yoga traditionally indicates financial instability or hardships, but its effect depends greatly on the overall strength of the horoscope. When present, it may bring phases of hard work and delayed material gains. However, individuals often develop discipline, resilience, and wise resource management as a result. Many rise above early struggles and achieve long-term success due to their determination and perseverance.""",

    "Grahan Yoga": """Grahan Yoga forms when the Sun or Moon is conjunct with Rahu or Ketu, symbolizing eclipsing energy. It can lead to emotional turbulence, heightened sensitivity, or confusion during certain phases of life. With positive planetary support, however, it grants extraordinary psychic ability, intuition, and spiritual depth. Individuals often learn important life lessons early and gradually grow into wise, insightful personalities.""",

    "Shakat Yoga": """Shakat Yoga arises when the Moon is positioned in the 6th, 8th, or 12th house from Jupiter. It is believed to create ups and downs in fortune, bringing periods of progress followed by delays. Despite the inconsistency, people with this yoga develop adaptability, strategy, and patience. They often achieve success later in life through persistence and a strong survival instinct. The yoga ultimately builds inner strength and resilience.""",

    "Chandal Yoga": """Chandal Yoga forms when Jupiter is conjunct with Rahu or Ketu. Traditionally seen as challenging, it may cause unconventional thinking, rebellion, or issues with guidance. However, modern interpretations highlight its potential for sharp intelligence, analytical depth, and fearless questioning of norms. Individuals may become strong thinkers, reformers, or innovators when other planetary influences provide balance.""",

    "Kuja Yoga": """Kuja Yoga, associated with Mars (Manglik influence), affects emotions, relationships, and temperament. While earlier texts emphasized negativity, modern astrology recognizes that compatibility and positive planetary aspects greatly reduce its impact. Individuals with Kuja Yoga often possess immense courage, drive, and leadership ability. Their passionate nature, when channelled properly, leads to major achievements and personal growth.""",

    "Kemdrum Yoga": """Kemdrum Yoga, a variation of lunar affliction, forms when the Moon is isolated without planetary support. It traditionally signifies emotional instability or a lack of material support early in life. Yet many natives grow into strong, self-reliant individuals due to these challenges. With beneficial aspects, they develop deep introspection, maturity, and the ability to navigate life’s complexities with wisdom and confidence.""",
}


from typing import Any
# assume NAKSHATRA_LORDS_ORDER and PLANET_DETAILS are defined elsewhere

def get_nakshatra_details(nk_index: int) -> dict:
    # Calculate Lord based on loop
    lord_id = NAKSHATRA_LORDS_ORDER[nk_index % 9]
    lord = PLANET_DETAILS[lord_id]

    # Base/default template
    details = {
        "id": nk_index + 1,
        "name": "Unknown",
        "lord": lord,
        "syllables": ["?", "?", "?", "?"],
        "info": {
            "deity": "Unknown",
            "ganam": "Unknown",
            "symbol": "Unknown",
            "animal_sign": "Unknown",
            "nadi": "Unknown",
            "color": "Unknown",
            "best_direction": "Unknown",
            "birth_stone": "Unknown",
            "gender": "Unknown",
            "planet": None,
            "enemy_yoni": "Unknown"
        }
    }

    # 0 Ashwini
    if nk_index == 0:
        details.update({
            "name": "Ashwini",
            "syllables": ["Chu", "Che", "Cho", "La"],
            "info": {
                "deity": "Ashwini Kumaras",
                "ganam": "Deva",
                "symbol": "Horse's Head",
                "animal_sign": "Horse",
                "nadi": "Kapha",
                "color": "White",
                "best_direction": "East",
                "birth_stone": "Coral",
                "gender": "Male",
                "planet": "Ketu",
                "enemy_yoni": "Elephant"
            }
        })

    # 1 Bharani
    elif nk_index == 1:
        details.update({
            "name": "Bharani",
            "syllables": ["Li", "Lu", "Le", "Lo"],
            "info": {
                "deity": "Yama",
                "ganam": "Manushya",
                "symbol": "Yoni (receptacle)",
                "animal_sign": "Elephant",
                "nadi": "Pitta",
                "color": "Blood Red",
                "best_direction": "South",
                "birth_stone": "Red Coral",
                "gender": "Female",
                "planet": "Venus",
                "enemy_yoni": "Dog"
            }
        })

    # 2 Krittika
    elif nk_index == 2:
        details.update({
            "name": "Krittika",
            "syllables": ["A", "I", "U", "Ea"],
            "info": {
                "deity": "Agni",
                "ganam": "Rakshasa",
                "symbol": "Knife / Flame",
                "animal_sign": "Goat",
                "nadi": "Kapha",
                "color": "White",
                "best_direction": "East",
                "birth_stone": "Ruby",
                "gender": "Male",
                "planet": "Sun",
                "enemy_yoni": "Mongoose"
            }
        })

    # 3 Rohini
    elif nk_index == 3:
        details.update({
            "name": "Rohini",
            "syllables": ["O", "Va", "Vi", "Vu"],
            "info": {
                "deity": "Brahma",
                "ganam": "Manushya",
                "symbol": "Chariot / Ox",
                "animal_sign": "Ox/Cow",
                "nadi": "Kapha",
                "color": "Red/White",
                "best_direction": "North-East",
                "birth_stone": "Pearl",
                "gender": "Female",
                "planet": "Moon",
                "enemy_yoni": "Horse"
            }
        })

    # 4 Mrigashira
    elif nk_index == 4:
        details.update({
            "name": "Mrigashira",
            "syllables": ["Ve", "Vo", "Ka", "Ki"],
            "info": {
                "deity": "Soma (Chandra)",
                "ganam": "Deva",
                "symbol": "Deer's Head",
                "animal_sign": "Deer",
                "nadi": "Vata",
                "color": "Silver/Grey",
                "best_direction": "North",
                "birth_stone": "Moonstone",
                "gender": "Male",
                "planet": "Mars",
                "enemy_yoni": "Dog"
            }
        })

    # 5 Ardra
    elif nk_index == 5:
        details.update({
            "name": "Ardra",
            "syllables": ["Ku", "Gha", "Nga", "Cha"],
            "info": {
                "deity": "Rudra (Shiva aspect)",
                "ganam": "Manushya",
                "symbol": "Tear Drop / Diamond",
                "animal_sign": "Dog",
                "nadi": "Kapha",
                "color": "Green/Blue",
                "best_direction": "West",
                "birth_stone": "Emerald",
                "gender": "Male",
                "planet": "Rahu",
                "enemy_yoni": "Cat"
            }
        })

    # 6 Punarvasu
    elif nk_index == 6:
        details.update({
            "name": "Punarvasu",
            "syllables": ["Ke", "Ko", "Ha", "Hi"],
            "info": {
                "deity": "Aditi",
                "ganam": "Deva",
                "symbol": "Bow & Quiver",
                "animal_sign": "Cat",
                "nadi": "Vata",
                "color": "White/Gold",
                "best_direction": "North-East",
                "birth_stone": "Topaz",
                "gender": "Male",
                "planet": "Jupiter",
                "enemy_yoni": "Lion"
            }
        })

    # 7 Pushya
    elif nk_index == 7:
        details.update({
            "name": "Pushya",
            "syllables": ["Hu", "He", "Ho", "Da"],
            "info": {
                "deity": "Brihaspati",
                "ganam": "Deva",
                "symbol": "Cow's Udder",
                "animal_sign": "Cow/Sheep",
                "nadi": "Kapha",
                "color": "Yellow",
                "best_direction": "East",
                "birth_stone": "Yellow Sapphire",
                "gender": "Male",
                "planet": "Saturn",
                "enemy_yoni": "Snake"
            }
        })

    # 8 Ashlesha
    elif nk_index == 8:
        details.update({
            "name": "Ashlesha",
            "syllables": ["Di", "Du", "De", "Do"],
            "info": {
                "deity": "Nagas",
                "ganam": "Rakshasa",
                "symbol": "Serpent Coil",
                "animal_sign": "Snake",
                "nadi": "Kapha",
                "color": "Dark/Black",
                "best_direction": "South",
                "birth_stone": "Gomed (Hessonite)",
                "gender": "Female",
                "planet": "Mercury",
                "enemy_yoni": "Cow"
            }
        })

    # 9 Magha
    elif nk_index == 9:
        details.update({
            "name": "Magha",
            "syllables": ["Ma", "Mi", "Mu", "Me"],
            "info": {
                "deity": "Pitrs (Ancestors)",
                "ganam": "Rakshasa",
                "symbol": "Royal Throne",
                "animal_sign": "Rat",
                "nadi": "Kapha",
                "color": "Ivory/White",
                "best_direction": "South-West",
                "birth_stone": "Cat's Eye",
                "gender": "Male",
                "planet": "Ketu",
                "enemy_yoni": "Sheep"
            }
        })

    # 10 Purva Phalguni
    elif nk_index == 10:
        details.update({
            "name": "Purva Phalguni",
            "syllables": ["Mo", "Ta", "Ti", "Tu"],
            "info": {
                "deity": "Bhaga",
                "ganam": "Manushya",
                "symbol": "Hammock / Front legs of bed",
                "animal_sign": "Rat",
                "nadi": "Pitta",
                "color": "Pink",
                "best_direction": "North-West",
                "birth_stone": "Diamond",
                "gender": "Female",
                "planet": "Venus",
                "enemy_yoni": "Cow"
            }
        })

    # 11 Uttara Phalguni
    elif nk_index == 11:
        details.update({
            "name": "Uttara Phalguni",
            "syllables": ["Te", "To", "Pa", "Pi"],
            "info": {
                "deity": "Aryaman",
                "ganam": "Manushya",
                "symbol": "Bed / Four legs of bed",
                "animal_sign": "Cow",
                "nadi": "Pitta",
                "color": "Purple",
                "best_direction": "North",
                "birth_stone": "Blue Sapphire",
                "gender": "Male",
                "planet": "Sun",
                "enemy_yoni": "Rat"
            }
        })

    # 12 Hasta
    elif nk_index == 12:
        details.update({
            "name": "Hasta",
            "syllables": ["Pu", "Sha", "Na", "Tha"],
            "info": {
                "deity": "Savitar",
                "ganam": "Deva",
                "symbol": "Hand",
                "animal_sign": "Buffalo",
                "nadi": "Vata",
                "color": "Green",
                "best_direction": "East",
                "birth_stone": "Emerald",
                "gender": "Female",
                "planet": "Moon",
                "enemy_yoni": "Tiger"
            }
        })

    # 13 Chitra
    elif nk_index == 13:
        details.update({
            "name": "Chitra",
            "syllables": ["Pe", "Po", "Ra", "Re"],
            "info": {
                "deity": "Tvashtar / Vishwakarma",
                "ganam": "Rakshasa",
                "symbol": "Bright Jewel / Pearl",
                "animal_sign": "Tiger",
                "nadi": "Kapha",
                "color": "White/Black",
                "best_direction": "West",
                "birth_stone": "Gomed / Hessonite",
                "gender": "Male",
                "planet": "Mars",
                "enemy_yoni": "Sheep"
            }
        })

    # 14 Swati
    elif nk_index == 14:
        details.update({
            "name": "Swati",
            "syllables": ["Ru", "Re", "Ro", "Ta"],
            "info": {
                "deity": "Vayu",
                "ganam": "Deva",
                "symbol": "Coral / Young Plant Shoot",
                "animal_sign": "Buffalo",
                "nadi": "Kapha",
                "color": "Silver/Green",
                "best_direction": "North-East",
                "birth_stone": "Emerald",
                "gender": "Female",
                "planet": "Rahu",
                "enemy_yoni": "Rat"
            }
        })

    # 15 Vishakha
    elif nk_index == 15:
        details.update({
            "name": "Vishakha",
            "syllables": ["Ti", "Tu", "Te", "To"],
            "info": {
                "deity": "Indra-Agni (dual)",
                "ganam": "Rakshasa",
                "symbol": "Triumphal Arch / Pottery Wheel",
                "animal_sign": "Tiger",
                "nadi": "Kapha",
                "color": "Yellow/Black",
                "best_direction": "East",
                "birth_stone": "Gomed",
                "gender": "Male",
                "planet": "Jupiter",
                "enemy_yoni": "Dog"
            }
        })

    # 16 Anuradha
    elif nk_index == 16:
        details.update({
            "name": "Anuradha",
            "syllables": ["Na", "Ni", "Nu", "Ne"],
            "info": {
                "deity": "Mitra",
                "ganam": "Deva",
                "symbol": "Lotus / Archway",
                "animal_sign": "Deer",
                "nadi": "Vata",
                "color": "Brown/Red",
                "best_direction": "South-East",
                "birth_stone": "Topaz",
                "gender": "Female",
                "planet": "Saturn",
                "enemy_yoni": "Tiger"
            }
        })

    # 17 Jyeshtha
    elif nk_index == 17:
        details.update({
            "name": "Jyeshtha",
            "syllables": ["No", "Ya", "Yi", "Yu"],
            "info": {
                "deity": "Indra",
                "ganam": "Rakshasa",
                "symbol": "Earring / Circular Amulet",
                "animal_sign": "Deer",
                "nadi": "Kapha",
                "color": "Red/Black",
                "best_direction": "South",
                "birth_stone": "Ruby",
                "gender": "Male",
                "planet": "Mercury",
                "enemy_yoni": "Sheep"
            }
        })

    # 18 Moola
    elif nk_index == 18:
        details.update({
            "name": "Moola",
            "syllables": ["Ye", "Yo", "Ba", "Bi"],
            "info": {
                "deity": "Nirrti",
                "ganam": "Rakshasa",
                "symbol": "Roots / Tied Roots",
                "animal_sign": "Dog",
                "nadi": "Vata",
                "color": "Dark Red/Black",
                "best_direction": "North-West",
                "birth_stone": "Garnet",
                "gender": "Male",
                "planet": "Ketu",
                "enemy_yoni": "Cow"
            }
        })

    # 19 Purva Ashadha
    elif nk_index == 19:
        details.update({
            "name": "Purva Ashadha",
            "syllables": ["Bu", "Dha", "Pha", "Da"],
            "info": {
                "deity": "Apah (Water)",
                "ganam": "Manushya",
                "symbol": "Fan / Elephant Tusk",
                "animal_sign": "Monkey",
                "nadi": "Kapha",
                "color": "Blue/Dark Blue",
                "best_direction": "North",
                "birth_stone": "Blue Sapphire",
                "gender": "Female",
                "planet": "Venus",
                "enemy_yoni": "Elephant"
            }
        })

    # 20 Uttara Ashadha
    elif nk_index == 20:
        details.update({
            "name": "Uttara Ashadha",
            "syllables": ["Be", "Bo", "Ja", "Ji"],
            "info": {
                "deity": "Vishwadevas",
                "ganam": "Manushya",
                "symbol": "Elephant Tusk / Moustache",
                "animal_sign": "Mongoose",
                "nadi": "Pitta",
                "color": "Brown",
                "best_direction": "North-East",
                "birth_stone": "Topaz",
                "gender": "Male",
                "planet": "Sun",
                "enemy_yoni": "Dog"
            }
        })

    # 21 Shravana
    elif nk_index == 21:
        details.update({
            "name": "Shravana",
            "syllables": ["Ju", "Je", "Jo", "Kha"],
            "info": {
                "deity": "Vishnu",
                "ganam": "Deva",
                "symbol": "Ear / Three footprints",
                "animal_sign": "Monkey",
                "nadi": "Vata",
                "color": "White",
                "best_direction": "North",
                "birth_stone": "Pearl",
                "gender": "Male",
                "planet": "Moon",
                "enemy_yoni": "Tiger"
            }
        })

    # 22 Dhanishta
    elif nk_index == 22:
        details.update({
            "name": "Dhanishta",
            "syllables": ["Ga", "Gi", "Gu", "Ge"],
            "info": {
                "deity": "Ashta Vasus",
                "ganam": "Rakshasa",
                "symbol": "Drum",
                "animal_sign": "Lion",
                "nadi": "Pitta",
                "color": "Silver",
                "best_direction": "West",
                "birth_stone": "Moonstone",
                "gender": "Male",
                "planet": "Mars",
                "enemy_yoni": "Cow"
            }
        })

    # 23 Shatabhisha
    elif nk_index == 23:
        details.update({
            "name": "Shatabhisha",
            "syllables": ["Go", "Sa", "Si", "Su"],
            "info": {
                "deity": "Varuna",
                "ganam": "Rakshasa",
                "symbol": "Circle / Hundred Physicians",
                "animal_sign": "Horse",
                "nadi": "Vata",
                "color": "Blue",
                "best_direction": "North-West",
                "birth_stone": "Blue Sapphire",
                "gender": "Male",
                "planet": "Rahu",
                "enemy_yoni": "Sheep"
            }
        })

    # 24 Purva Bhadrapada
    elif nk_index == 24:
        details.update({
            "name": "Purva Bhadrapada",
            "syllables": ["Se", "So", "Da", "Di"],
            "info": {
                "deity": "Aja Ekapada",
                "ganam": "Manushya",
                "symbol": "Two-faced man / Funeral cot legs",
                "animal_sign": "Lion",
                "nadi": "Pitta",
                "color": "Silver",
                "best_direction": "South-East",
                "birth_stone": "Moonstone",
                "gender": "Female",
                "planet": "Jupiter",
                "enemy_yoni": "Dog"
            }
        })

    # 25 Uttara Bhadrapada
    elif nk_index == 25:
        details.update({
            "name": "Uttara Bhadrapada",
            "syllables": ["Du", "Tha", "Jha", "Da"],
            "info": {
                "deity": "Ahir Budhnya",
                "ganam": "Manushya",
                "symbol": "Twin / Two back legs of bed",
                "animal_sign": "Cow",
                "nadi": "Pitta",
                "color": "Purple",
                "best_direction": "North",
                "birth_stone": "Blue Sapphire",
                "gender": "Female",
                "planet": "Saturn",
                "enemy_yoni": "Tiger"
            }
        })

    # 26 Revati
    elif nk_index == 26:
        details.update({
            "name": "Revati",
            "syllables": ["De", "Do", "Cha", "Chi"],
            "info": {
                "deity": "Pushan / Revati (sometimes Vishnu)",
                "ganam": "Deva",
                "symbol": "Fish / Drum / Pomegranate",
                "animal_sign": "Sheep / Donkey",
                "nadi": "Kapha",
                "color": "Light Blue",
                "best_direction": "North",
                "birth_stone": "Pearl",
                "gender": "Male",
                "planet": "Mercury",
                "enemy_yoni": "Sheep"
            }
        })

    return details