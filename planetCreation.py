import os
import random as rnd
import time
COLORS = ["Gray","Brown","Light Brown","Light Gray","Dark Red", "Navy Blue","Light Yellow","Dark Green","Dark Blue"]
STAR_COLORS = ["Yellow", "Light Blue", "Blue","Red","Dark Red","White"]

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
PART_ONE_NAME = [
    # Original
    "Kalmara", "Malara", "Aegeanon", "Posideon", "Hercules", 
    "Hetelo", "Oceanus", "Vulcan", "Umaara",
    
    # Mythological & Ancient Gods
    "Astraea", "Hyperion", "Osiris", "Tiamat", "Elysium", 
    "Ares", "Minerva", "Triton", "Zephyros", "Chronos",
    
    # Sci-Fi & Alien
    "Xylar", "Zanthos", "Vaelen", "Krynn", "Nexor", 
    "Theron", "Vorath", "Drakon", "Zorax", "Kaelis", 
    "Qaldor", "Xylo", "Vaelis",
    
    # Celestial & World-Building
    "Orion", "Lyra", "Solaria", "Zenobia", "Kepler", 
    "Eldoria", "Cygnus", "Andromeda", "Caelum", "Vesper", 
    "Oberon",
    
    # Human & Classical
    "Aurelius", "Cassian", "Seraphina", "Valerius", "Leonidas", 
    "Alexander", "Balthazar", "Kaelen",
    
]
PART_TWO_NAME = [
    # Original
    "Mysara", "Canador", "Infernius", "Beelzenol", "Maal", 
    "Vaalcanus", "Mooluna", "Amcara", "Kemnus", "Xenona", 
    "Dromedala", "Kazaralax",
    
    # Dark & Fiery / Infernal
    "Ignis", "Pyroth", "Ashakar", "Brimstone", "Volcanis", 
    "Malakor", "Voros", "Obsidian", "Scorchia", "Netheron",
    
    # Deep Alien / Cosmic
    "Zulra", "Xanthos", "Vectis", "Krytos", "Vortex", 
    "Gorgon", "Phobos", "Umbra", "Nadir", "Acheron", 
    "Xylos", "Vanguard",
    
    # Planet & World Components
    "Lunaris", "Astral", "Solis", "Terran", "Verdant", 
    "Eclipsis", "Nova", "Nebula", "Corona", "Penumbris", 
    "Abyssus",
    
    # Exotic & Ancient Titles
    "Mortis", "Valakor", "Zul'Amon", "Dreadion", "Kazador", 
    "Vexis", "Xerxes", "Tenebris"
]
MOON_SUFFIX = ["Prime","Delta","Epsilon","Alpha","Beta","Sigma","Yotta"]
PREFIXES = ["Ocean","Har","Xeno","Melar","Baal","Mel","Aeag","Meka","Funa","Aieona","Strapat","Komala","Hadeo","Jaurna","Eakla","Kakal","Togo","Yama","Shizen","Aeina","Meina","Lael","Tomo","Shigi","Ramha","Sri","Prad","Anu","Upa","Gan"]
FIXES = ["hex","ra","nol","hadeo","oelio","-Lokama","malk","shama","terg","minid","-Ommol","mesa","-Olok","jsa","sama","iols","biol","kyu","ram","-Kyua","meiama"]
SUFFIXES = ["us","kar","ara","rus","ol","me","oko","emon","pok","malak","zar","varab","burg","verk","cozza","perla","eladus","ania","efernia","koona","haela","looga","gachi","tama","yama","ram","wala","aayi","ma","ka","rala","anna","esh"]
MAIN_TYPES = ["Gas Giant","Terrestrial Planet","Moon","Star", "Captured Asteroid"]
SUBTYPES = {
    "Sol Sized Star":["Main Sequence","Yellow Dwarf", "Orange Dwarf"],
    "Smaller Stars":["Red Dwarf","White Dwarf","Black Dwarf"],
    "Larger Stars": ["Red Giant","Blue Giant", "Orange Giant"],
    "Largest Stars":["Red Hypergiant","Blue Hypergiant","Quasi-Star"],
    "Terrestrial Planet":["Ocean Planet","Desert World", "Ice World","Supercritical Planet", "Venusian Planet"],
    "Gas Giant":["Ice Giant", "Hot Jupiter", "Lukewarm Giant"],
    "Larger Giant":["Gas Hypergiant","Brown Dwarf"],
    "Moon":["Barren Moon","Cryovolcanic Moon","Volcanic Moon","Cracked Moon"]


}

# Planet Class
class Planet:
    def __init__(self,name,typePl,radius,color,subtype):
        self.typePl = typePl
        self.radius = radius
        self.color = color
        self.subtype = subtype
        self.name = name
        
    def state(self):
        
        return f"{self.name} : Type: {self.typePl} ({self.subtype}), Radius: {self.radius:,}km, Color: {self.color}"












def GRIFL(item_list):
    return item_list[rnd.randint(0,len(item_list) - 1)]

# Generate Functions
def GenerateBody(forcedtype):
    if forcedtype:
    # Type Generation
        typeGen = forcedtype 
    else:
        typeGen = GRIFL(MAIN_TYPES)
    # Radius Generation
    if typeGen == "Gas Giant":
        radius = rnd.randint(50000,400000)
        if radius < 200000:
            subtypes = GRIFL(SUBTYPES["Gas Giant"])
        else:
            subtypes = GRIFL(SUBTYPES["Larger Giant"])



    elif typeGen == "Captured Asteroid":
        radius = rnd.randint(5,200)   
        subtypes= "Captured Asteroid" 
    elif typeGen == "Terrestrial Planet":
        radius = rnd.randint(2000,11000)
        subtypes = GRIFL(SUBTYPES["Terrestrial Planet"])
    elif typeGen == "Moon":
        radius = rnd.randint(10,3000)
        if radius >= 200:
            subtypes = GRIFL(SUBTYPES["Moon"])
        else:
            subtypes = "Captured Asteroid"
    elif typeGen == "Star":
        radius = rnd.randint(60000,1500000000)
        if radius > 1000000000:
            subtypes = GRIFL(SUBTYPES["Largest Stars"])
        elif radius < 1000000000 and radius > 70000000:
            subtypes = GRIFL(SUBTYPES["Larger Stars"])
        elif radius < 70000000 and radius > 300000:
            subtypes = GRIFL(SUBTYPES["Sol Sized Star"])
        else:
            subtypes = GRIFL(SUBTYPES["Smaller Stars"])
    
    # Color Generation
    color = ""
    if typeGen == "Star":
        if subtypes in ("Red Dwarf", "Red Giant", "Red Hypergiant"):
            color = "Red"
        elif subtypes == "Yellow Dwarf":
            color = "Yellow"
        elif subtypes in ("Orange Dwarf", "Orange Giant"):
            color = "Orange"
        elif subtypes == "White Dwarf":
            color = "White"
        elif subtypes in ("Blue Giant", "Blue Hypergiant"):
            color = "Light Blue"
        elif subtypes == "Black Dwarf":
            color = "Black"
        else:
            color = GRIFL(STAR_COLORS)
    else:
        color = GRIFL(COLORS)
    # Name Generation
    midfixChance = rnd.randint(1,3)
    if midfixChance == 1:
        if typeGen in ("Moon", "Captured Asteroid"):
            name = f"{GRIFL(PREFIXES)}{GRIFL(FIXES)}{GRIFL(SUFFIXES)} {GRIFL(MOON_SUFFIX)}"
        else:
            name = f"{GRIFL(PREFIXES)}{GRIFL(FIXES)}{GRIFL(SUFFIXES)}"
    else:
        if typeGen in ("Moon", "Captured Asteroid"):
            name = f"{GRIFL(PREFIXES)}{GRIFL(SUFFIXES)} {GRIFL(MOON_SUFFIX)}"
        else:
            name = f"{GRIFL(PREFIXES)}{GRIFL(SUFFIXES)}"
    return name,typeGen,radius,color,subtypes

    
def GenerateSector(amounts):
    time.sleep(1)
    print(f"\n====== SECTOR GENERATED: {rnd.randint(1,99)}{GRIFL(ALPHABET).upper()} ======")
    for i in range(amounts):
        time.sleep(0.3)
        GenerateSystem(False,0)
    print(f"\n===============================")
def WriteSectorToFile(amounts):
    sectorName = f"{rnd.randint(1,99)}{GRIFL(ALPHABET).upper()}"
    os.makedirs(os.path.join("SectorCreator","sector"), exist_ok=True)
    with open(f"SectorCreator\sector\{sectorName}.txt","w") as file:
        print(f"\n====== SECTOR GENERATED: {sectorName} ======")
        for i in range(amounts):
            GenerateSystem(True,file)
        file.write(f"\n===============================")




def GenerateSystem(isWritingFile,file):
    star = Planet(*GenerateBody('Star'))

    if isWritingFile: file.write(f"""\n-------{star.name.upper()} SYSTEM------- 
              \n{star.state()}""")
    else: print(f"""\n-------{star.name.upper()} SYSTEM------- 
              \n{star.state()}""")
        
    planetAmount = rnd.randint(1,7)
    # Planet and Moon Gen
    for i in range(planetAmount):
        typeOfPlanet = rnd.randint(1,3)
        if typeOfPlanet == 1:
            planet = Planet(*GenerateBody('Terrestrial Planet'))

            if isWritingFile: file.write(f"\n-- {planet.state()}")
            else: print(f"\n-- {planet.state()}")

            moonAmnt = rnd.randint(0,4)
            for i in range(moonAmnt):
                moon = Planet(*GenerateBody('Moon'))
                if isWritingFile: file.write(f"\n---- {moon.state()}") 
                else: print(f"\n---- {moon.state()}")
        else:
            capturedAsteroidCount = 0
            planet = Planet(*GenerateBody('Gas Giant'))
            if isWritingFile: file.write(f"\n-- {planet.state()}")
            else: print(f"\n-- {planet.state()}")
            moonAmnt = rnd.randint(0,90)
            moonAmntTillAst = rnd.randint(5,10)
            for _ in range(moonAmnt):
                if _ > moonAmntTillAst:
                    
                    capturedAsteroidCount += 1
                else:
                    moon = Planet(*GenerateBody('Moon'))
                    if isWritingFile: file.write(f"\n---- {moon.state()}") 
                    else: print(f"\n---- {moon.state()}")
                
            if isWritingFile: file.write(f"\n---------- And {capturedAsteroidCount} captured asteroids")
            else: print(f"\n---------- And {capturedAsteroidCount} captured asteroids")

WriteSectorToFile(200)

