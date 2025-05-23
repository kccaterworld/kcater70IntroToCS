#!/usr/bin/python3
print("Content-Type: text/html\n\n")

#imports
import random
import os
#import cgitb
#cgitb.enable()
#os.chmod("../pokemon", 0o606)
#os.chmod("HTML/", 0o606)
#os.chmod("CSS/", 0o606)
#os.chmod("img", 0o606)
#os.chmod("img/front", 0o606)
#os.chmod("img/back", 0o606)

path="http://marge.stuy.edu/~kcater70/pokemon"
#HTML skeleton
indent = "    "
lineBreak = "\n<br>"
newLine = '''
'''
pageMultiline = '''
<!DOCTYPE html>
<html>
    <head>
        _HEAD_
    </head>
    <body>
        _NAVBAR_
        _BODY_
    </body>
</html>'''

types = {
        
    }
typesStr = ""


#buildPokeNavBar()
def buildPokeNavBar():
    return '''<div class="navbar">
	        <!-- Navbar -->
	        <nav>
	            <ol>
	                <!-- Home page -->
	                <li id="navbarHome" class="navbarHomeItem"><a href="../makePokedex.py" id="homeLink">Home</a></li>
	                <!-- Dropdown menu for types pages -->
                    <li id="navbarPagesDropdown" class="navbarItem">Types
                        <ul>
                            <!-- Type pages -->
                            <li style="border-radius: 0px 15px 0px 0px;"><a href="bug.html" class="pagesLink">Bug Types</a></li>
                            <li><a href="dragon.html" class="pagesLink">Dragon Types</a></li>
                            <li><a href="electric.html" class="pagesLink">Electric Types</a></li>
                            <li><a href="fairy.html" class="pagesLink">Fairy Types</a></li>
                            <li><a href="fighting.html" class="pagesLink">Fighting Types</a></li>
                            <li><a href="fire.html" class="pagesLink">Fire Types</a></li>
                            <li><a href="flying.html" class="pagesLink">Flying Types</a></li>
                            <li><a href="ghost.html" class="pagesLink">Ghost Types</a></li>
                            <li><a href="grass.html" class="pagesLink">Grass Types</a></li>
                            <li><a href="ground.html" class="pagesLink">Ground Types</a></li>
                            <li><a href="ice.html" class="pagesLink">Ice Types</a></li>
                            <li><a href="normal.html" class="pagesLink">Normal Types</a></li>
                            <li><a href="poison.html" class="pagesLink">Poison Types</a></li>
                            <li><a href="psychic.html" class="pagesLink">Psychic Types</a></li>
                            <li><a href="rock.html" class="pagesLink">Rock Types</a></li>
                            <li><a href="steel.html" class="pagesLink">Steel Types</a></li>
                            <li style="padding-bottom: 5px; border-radius: 0px 0px 15px 15px;"><a href="water.html" class="pagesLink">Water Types</a></li>
                        </ul>
                    </li>
                    <li class="navbarBigItem"><a href="../HTML/allpokemon.html">All Pokemon</a></li>
                    <li class="navbarItem"><a href="../HTML/top10.html">My Top 10</a></li>
	            </ol>
	        </nav>
        </div>'''
	
def buildHomeNavBar():
    return '''<div class="navbar">
	        <!-- Navbar -->
	        <nav>
	            <ol>
	                <!-- Home page -->
	                <li id="navbarHome" class="navbarHomeItem"><a href="makePokedex.py" id="homeLink">Home</a></li>
	                <!-- Dropdown menu for types pages -->
                    <li id="navbarPagesDropdown" class="navbarItem"><a style="text-decoration: none;">Types</a>
                        <ul>
                            <!-- Type pages -->
                            <li style="border-radius: 15px 15px 0px 0px;"><a href="HTML/bug.html" class="pagesLink">Bug Types</a></li>
                            <li><a href="HTML/dragon.html" class="pagesLink">Dragon Types</a></li>
                            <li><a href="HTML/electric.html" class="pagesLink">Electric Types</a></li>
                            <li><a href="HTML/fairy.html" class="pagesLink">Fairy Types</a></li>
                            <li><a href="HTML/fighting.html" class="pagesLink">Fighting Types</a></li>
                            <li><a href="HTML/fire.html" class="pagesLink">Fire Types</a></li>
                            <li><a href="HTML/flying.html" class="pagesLink">Flying Types</a></li>
                            <li><a href="HTML/ghost.html" class="pagesLink">Ghost Types</a></li>
                            <li><a href="HTML/grass.html" class="pagesLink">Grass Types</a></li>
                            <li><a href="HTML/ground.html" class="pagesLink">Ground Types</a></li>
                            <li><a href="HTML/ice.html" class="pagesLink">Ice Types</a></li>
                            <li><a href="HTML/normal.html" class="pagesLink">Normal Types</a></li>
                            <li><a href="HTML/poison.html" class="pagesLink">Poison Types</a></li>
                            <li><a href="HTML/psychic.html" class="pagesLink">Psychic Types</a></li>
                            <li><a href="HTML/rock.html" class="pagesLink">Rock Types</a></li>
                            <li><a href="HTML/steel.html" class="pagesLink">Steel Types</a></li>
                            <li style="padding-bottom: 5px; border-radius: 0px 0px 15px 15px;"><a href="HTML/water.html" class="pagesLink">Water Types</a></li>
                        </ul>
                    </li>
                    <li class="navbarBigItem"><a href="HTML/allpokemon.html">All Pokemon</a></li>
                    <li class="navbarItem"><a href="HTML/top10.html">My Top 10</a></li>
	            </ol>
	        </nav>
        </div>'''

def buildLink(ref: str,content: str, newTab: bool = False):
    if newTab == True:
        nT = '''target="_blank"'''
    elif newTab == False:
        nT = ''''''
    else:
        nT = ''''''
    return f'''<a href="{ref}" {nT} style="left: 0;"> {content} </a>'''

#buildTable(caption,header,body,footer) -> string
#caption -> string
#header -> list of lists
#body -> list of lists
#footer -> list of lists
#Creates HTML table with caption Caption, using header, body, and footer as such.
#header, body, footer: main list is all data, each inner list is a row, each list value is a collumn for that row
def buildTable(caption,header,body,footer):
            tableMultiline = f'''\n\t\t<table>
            <caption> <h1>{caption}</h1> </caption>
            <thead> _HEAD_
            </thead>
            <tbody> _BODY_
            </tbody>
            <tfoot> _FOOT_
            </tfoot>
        </table>'''
            multHead = ""
            multBody = ""
            multFoot = ""
            for item in header:
                multHead += "\n\t\t\t\t<tr>"
                for cell in item:
                    multHead += "<th>" + str(cell) + "</th>"
                multHead += "</tr>"
            for item in body:
                multBody += "\n\t\t\t\t<tr>"
                for cell in item:
                    multBody += "<td>" + str(cell) + "</td>"
                multBody += "</tr>"
            for item in footer:
                multFoot += "\n\t\t\t\t<tr>"
                for cell in item:
                    multFoot += "<td>" + str(cell) + "</td>"
                multFoot += "</tr>"
            tableMultiline = tableMultiline.replace("_HEAD_",multHead)
            tableMultiline = tableMultiline.replace("_BODY_",multBody)
            tableMultiline = tableMultiline.replace("_FOOT_",multFoot)
            return tableMultiline


def freqWords(data):
    for word in data:
        if word in types:
            types[word] += 1
        else:
            types[word] = 1
    return types

def processWordies(wordLists):
    newWordList = []
    for item in wordLists:
        newWordList.append(item.strip(" .,?!;:\n"))
    return newWordList

def tallyText(string):
    return freqWords(processWordies(string.split(" ")))


def buildImage(source, alt="Image"):
    return f'''<img src="{source}.png" alt="{alt}">'''


#buildCSSFull() -> string
def buildCSSFull():
    cssFull = ""
    cssFull += "\n/*Navbar font*/"
    cssFull += buildCSSBlock("nav",["font"],["12px Source Sans Pro Topnav, sans-serif"])
    cssFull += "\n/*Giving the tables solid, visible borders.*/"
    cssFull += buildCSSBlock("table, th, td, tr",["border"],["1px solid"])
    cssFull += "\n/*Cool shadow around the table*/"
    cssFull += buildCSSBlock("table",["border-collapse","box-shadow"],["collapse","2px 2px 5px"])
    cssFull += "\n/*Regular table styling*/"
    cssFull += buildCSSBlock("th, td",["padding","text-align"],["2px","center"])
    cssFull += buildCSSBlock("th",["background-color"],["red"])
    cssFull += "\n/*Navbar decor, creating hoverable dropdown, adding colors, hoverable boxes, and changing colors on hover to be more visible*/"
    cssFull += buildCSSBlock("nav a",["color","text-decoration"],["#6fddd2","none"])
    cssFull += buildCSSBlock("nav",["height","margin-top","margin-left","margin-right","background-color","color"],["35px","-8px","-8px","-8px","#413A5E","white"])
    cssFull += buildCSSBlock("nav ol",["padding","margin"],["0px","0px 0px 0px 8px"])
    cssFull += buildCSSBlock("nav li",["height","margin-top","margin-left","margin-right","display","position"],["20px","5px","5px","5px","inline-block","relative"])
    cssFull += buildCSSBlock("nav li#navbarPagesDropdown",["right","width","height","padding-left","border-radius"],["5px","75px","50px","5px","5px 5px 5px 0px"])
    cssFull += buildCSSBlock("nav li#navbarPagesDropdown:hover",["background-color"],["blue"])
    cssFull += buildCSSBlock("a.pagesLink:hover",["background-color"],["blue"])
    cssFull += buildCSSBlock("nav li ul",["display","position","width","top","left","border-radius"],["none","absolute","200px","25px","-10px","0px 25px 25px 25px"])
    cssFull += buildCSSBlock("nav li:hover > ul, nav li:active > ul",["margin-top","display"],["5px","block"])
    cssFull += buildCSSBlock("nav ul",["list-style-type","margin","padding","background-color","border"],["none","10px","0px","blue","1px solid blue"])
    cssFull += buildCSSBlock("nav li ul li",["display","margin","height","width","right"],["block","5px","25px","201.5px","6px"])
    cssFull += buildCSSBlock(".navbarItem",["font-size","height","width","right"],["20px","30px","125px","5px"])
    cssFull += buildCSSBlock(".navbarHomeItem",["font-size","height","width","right"],["20px","30px","75px","5px"])
    cssFull += buildCSSBlock(".navbarBigItem",["font-size","height","width","right"],["20px","30px","150px","5px"])
    cssFull += buildCSSBlock(".navbarItem:hover, .navbarItem:active, .navbarBigItem:hover, .navbarHomeItem:hover",["background-color","border-radius"],["blue","20px"])
    cssFull += buildCSSBlock("nav ol li#navbarPagesDropdown.navbarItem ul li a.pagesLink:hover",["color", "background-color","border-radius"],["green","yellow","5px"])
    cssFull += buildCSSBlock("a",["position","left"],["relative","10px"])
    cssFull += buildCSSBlock("ul li:hover",["background-color"],["yellow"])
    cssFull += "\n/*Coloring the links*/"
    cssFull += buildCSSBlock("#tableTypes",["text-decoration","color"],["none","red"])
    return cssFull[1:]

#buildCSSBlock(cssElement,cssProperty,cssValue) -> string
#cssElement -> string
#cssProperty -> string
#cssValue -> string
#Creates a CSS block for element(s) cssElement, with respective properties and values.
#If inputs are invalid it will not render
def buildCSSBlock(cssElement,cssProperty,cssValue):
    cssMultiline = '''\n_ELEMENT_ {_PROPERTIES_
	}'''
    properties = ""
    cssMultiline = cssMultiline.replace("_ELEMENT_",cssElement)
    for i in range(len(cssProperty)):
        properties += "\n\t" + cssProperty[i] + ": " + cssValue[i] + ";"
    cssMultiline = cssMultiline.replace("_PROPERTIES_",properties)
    return cssMultiline


def buildMeta(charset,description,keywords,author,viewport):
   return f'''\t\t<meta charset="{charset}">
    \t<meta name="description" content="{description}">
    \t<meta name="keywords" content="{keywords}">
    \t<meta name="author" content="{author}">
    \t<meta name="viewport" content="{viewport}">'''

def buildAllPokePara():
    return "\n\t\t<p>Pokemon is a very famous game that I've always enjoyed playing, although I'm not a hardcore player.</p>"

def buildHeadLinks(rel,type,href):
    return f'''\t\t<link rel="{rel}" type="{type}" href="{href}">'''

#makehead(title,css) -> string
#title -> string
#css -> list of lists, optimized for buildCSSBlock()
def titleCSS(title):
    return f'''<title> {title} </title>'''
#genPageHead() -> string
def genAllPokePageHead():
    allPokePageHead = ""
    #Example of how to add to pageHead
    allPokePageHead += ""
    #Example title and CSS commands (IMPORTANT)
    allPokePageHead += titleCSS("Pokemon")
    #Adding meta tags (IMPORTANT)
    allPokePageHead += indent + newLine + buildMeta("UFT-8","Pokemon Website","pokemon, class, data, python","Kemal Cater","width=device-width, initial-scale=1.0",)
    #Adding links (IMPORTANT)
    allPokePageHead += indent + newLine + buildHeadLinks("stylesheet","text/css","../CSS/PokeStyle.css")
    allPokePageHead += indent + newLine + buildHeadLinks("icon","image/x-icon","favicon.ico")
    return allPokePageHead

#genPageBody() -> string
def genAllPokePageBody():
    allPokePageBody = ""
    allPokePageBody += buildPokeNavBar()
    allPokePageBody += buildAllPokePara()
    allPokePageBody += buildTable("All Pokemon",[pokeData[0]],pokeData[1:],[])

    return allPokePageBody

def genPage(path,content):
    #giveFilePerms(path)
    f = open(path, "w")
    f.write(content)
    f.close()




def buildTypeTable(pokeType):
    #bigTypesListForTable = []
    #for item in typesList:
    #    bigTypesListForTable.append([pokemon for pokemon in pokeDataSplit if f"{item}" in [type_.lower() for type_ in pokemon]])
    #print(bigTypesListForTable)
    #for i in range(len(typesList)):
    #    print(buildTable(f"{typesList[i]}",[pokeDataSplit[0]],[bigTypesListForTable[i]],[]))
    return [pokemon for pokemon in pokeData if pokeType in [type_.lower() for type_ in pokemon]]

def buildTypePage(pokeType):
    typeMultiline = '''<!DOCTYPE html>
<html>
    <head>
        _HEAD_
    </head>
    <body>
        _BODY_
    </body>
</html>'''
    typePageBody = ""
    typePageBody += buildPokeNavBar()
    typePageBody += buildTable(f"{pokeType.title()} Type Pokemon",[pokeData[0]],buildTypeTable(pokeType),[])
    typePageHead = ""
    typePageHead += titleCSS(f"{pokeType.title()} Type Pokemon")
    typePageHead += indent + newLine + buildMeta("UFT-8",f"Page for {pokeType} Type Pokemon",f"Pokemon, {pokeType}","Kemal Cater","width=device-width, initial-scale=1.0",)
    typePageHead += indent + newLine + buildHeadLinks("stylesheet","text/css","../CSS/PokeStyle.css")
    #typePageHead += indent + newLine + buildHeadLinks("icon","image/x-icon","favicon.ico")
    typeMultiline = typeMultiline.replace("_HEAD_",typePageHead)
    typeMultiline = typeMultiline.replace("_BODY_",typePageBody)
    return typeMultiline

def genTop10Page():
    top10PageMultiline = '''<!DOCTYPE html>
<html>
    <head>
        _HEAD_
    </head>
    <body>
        _BODY_
    </body>
</html>'''
    top10PageBody = ""
    top10PageBody += buildPokeNavBar()
    top10PageBody += buildTable("My Top 10 Favorite Pokemon",[['#', 'Front Image', 'Back Image', 'Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary', 'Why I Like This Pokemon']],top10Rows,[])
    top10PageHead = ""
    top10PageHead +=  titleCSS("My Top 10 Favorite Pokemon")
    top10PageHead += indent + newLine + buildMeta("UFT-8",f"My favorite pokemon","Pokemon","Kemal Cater","width=device-width, initial-scale=1.0",)
    top10PageHead += indent + newLine + buildHeadLinks("stylesheet","text/css","../CSS/PokeStyle.css")
    top10PageMultiline = top10PageMultiline.replace("_HEAD_",top10PageHead)
    top10PageMultiline = top10PageMultiline.replace("_BODY_",top10PageBody)
    return top10PageMultiline

def genHomePage():
    makePokedexv1PageMultiline = '''<!DOCTYPE html>
<html>
    <head>
        _HEAD_
    </head>
    <body>
        _BODY_
    </body>
</html>'''
    makePokedexv1PageBody = ""
    makePokedexv1PageBody += buildHomeNavBar()
    makePokedexv1PageBody += "\n\t\t<h2>" + introPara + "</h2>"
    makePokedexv1PageBody += "<br>"
    makePokedexv1PageBody += '<img src="img/inteleon.png" alt="Inteleon" width="707" height="707">'
    for i in range(500):
        makePokedexv1PageBody += "\n\t\t<br>"
    makePokedexv1PageBody += "\n\t\t<h1>The minions have a message to the people of Ms. Alonso's class:</h1>"
    makePokedexv1PageBody += "\n\t\t<p>Haiiiiiiiiii</p>\n\t\t<br>"
    makePokedexv1PageBody += '''\n\t\t<img src="../assets/hackinghaha.gif">'''
    makePokedexv1PageHead = ""
    makePokedexv1PageHead +=  titleCSS("Pokemon Home")
    makePokedexv1PageHead += indent + newLine + buildMeta("UFT-8",f"My home page","Pokemon","Kemal Cater","width=device-width, initial-scale=1.0",)
    makePokedexv1PageHead += indent + newLine + buildHeadLinks("stylesheet","text/css","CSS/PokeStyle.css")
    makePokedexv1PageMultiline = makePokedexv1PageMultiline.replace("_HEAD_",makePokedexv1PageHead)
    makePokedexv1PageMultiline = makePokedexv1PageMultiline.replace("_BODY_",makePokedexv1PageBody)
    return makePokedexv1PageMultiline

#Main Prog
with open("pokemon.csv", "r") as pokeRawData:
    pokeRawData = pokeRawData.read()
    pokeDataSplit = pokeRawData.split("\n")
    pokeData = []
    for item in pokeDataSplit:
        pokeData.append(item.split(","))
    pokeData = pokeData[0:-1]

pokeData[0].insert(1,"Back Image")
pokeData[0].insert(1,"Front Image")
for row in pokeData[1:]:
    row.insert(1,buildImage(f"../img/back/{row[0]}"))
    row.insert(1,buildImage(f"../img/front/{row[0]}"))

pokeData[0][4] = buildLink("../HTML","Type 1",True)
pokeData[0][5] = buildLink("../HTML","Type 2",True)
'''for row in pokeData[1:]:
    row[4] = buildLink(ref=f"../HTML/{row[4].lower()}.html",content=f"{row[4]}",newTab=True,styles="text-decoration: none; color: red;",id="tableTypes")
    row[5] = buildLink(f"../HTML/{row[5].lower()}.html",f"{row[5]}",True,styles="text-decoration: none; color: red;",id="tableTypes")'''


typesList = [row[i].lower() for row in pokeData[1:] for i in (4, 5) if row[i]]


for item in pokeData:
    typesStr += item[2] + " " + item[3] + " "

pageMultiline.replace("_NAVBAR",buildPokeNavBar())


allPokePageMultiline = f'''<!DOCTYPE html>
<html>
    <head>{genAllPokePageHead()}
    </head>
    <body>
        {genAllPokePageBody()}
    </body>
</html>
'''

namesList = ["Squirtle","Bulbasaur","Charizard","Beedrill","Rattata","Ninetales","Meowth","Graveler","Farfetch'd","Gyarados"]
top10Rows = [row for row in pokeData[1:] if len(row) > 0 and row[3].strip() in namesList]
reasons = ["I like Bulbasaur because it's just a<br>cute lil dude, chilling out<br>with that bulb on its back.",
           "Call me basic, but Charizard is on here<br>just because it's such an<br>iconic pokemon.",
           "Squirtle is on here just by virtue of<br>being so cute and cuddlable.",
           "I've always loved the character design<br>design of Beedrill, looking<br>so cool, girlbossing around",
           "Rattata is on this list, once again,<br>because it's an absolutely iconic<br>pokemon.",
           "I chose Ninetails because the East Asian<br>legends of different animal<br>spirits are so cool to learn about.",
           "Back when I played the card game, Meowth<br>was one of my first cards, and<br>thus deserved a spot here.",
           "Graveler is here because I still remember<br>how angry my sister used to get<br>fighting them.",
           "Farfetch'd literally just has an awesome<br>name, and it's so cute too.",
           "Once again, Gyarados played an important role<br>in my early plays of Pokemon,<br>and holds a place dear to me."]

for i in range(len(top10Rows)):
    top10Rows[i][0] = str(i + 1)
    top10Rows[i].append(reasons[i])

introPara = "My favorite pokemon ever is Inteleon, from Gen 8. I like Inteleon mostly just because it looks cool (by that I mean that it went on my hear me out cake)."

print(genHomePage())

#Write all other files next
for type in [row[i].lower() for row in pokeData[1:] for i in (4, 5) if row[i]]:
    genPage(f"HTML/{type}.html",buildTypePage(type))

genPage("CSS/PokeStyle.css",buildCSSFull())
genPage("HTML/allpokemon.html",allPokePageMultiline)
genPage("HTML/top10.html",genTop10Page())