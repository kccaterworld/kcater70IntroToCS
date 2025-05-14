#! /usr/bin/python3
print("Content-Type: text/html\n\n")

#globals
#top 10, fill it out
top10 = ["Squirtle","Bulbasaur","Charizard","Beedrill","Rattata","Ninetales","Meowth","Graveler","Farfetch'd","Gyarados"]
reasons = ["","","","","","","","","",""]
#globals for meta tag, fill them out, leave f-strings in
author = "" #TODO: put your name here
homeDescription = "" #TODO: Fill this out
homeKeywords = "" #TODO: Fill this out
topTenDescription = "" #TODO: Fill this out
topTenKeywords = "" #TODO: Fill this out
allPokemonDescription = "" #TODO: Fill this out
allPokemonKeywords = "" #TODO: Fill this out
#page variables
homeHeader = "" #Put what you want in your h1 tag here
homeBody = '''
''' #TODO: Put the body of your home page here, theres a spot for an image lower down
pokeStyles = '''
''' #TODO FILL THIS WITH CSS IF U WANNA OTHERWISE WRITE IT MANUALLY AND DELET THE LAST LINE

navbar = '''<div class="navbar">
	<!-- Navbar -->
	<nav>
	    <ol>
	        <!-- Home page -->
	        <li id="navbarHome" class="navbarHomeItem"><a href="../makePokedexv1.py" id="homeLink">Home</a></li>
	        <!-- Dropdown menu for types pages -->
            <li id="navbarPagesDropdown" class="navbarItem">Types
                <ul>
                    <!-- Type pages -->
                    <li style="border-radius: 0px 15px 0px 0px;"><a href="HTML/bug.html" class="pagesLink">Bug Types</a></li>
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
	</nav>'''

##helper functions

#make table function
def html_table(header,table):
    html = '\t\t<table border="1">\n'
    html += "\t\t<table>\n\t\t\t<tr>"
    for item in header:
        html += f"<th>{item}</th>"
    html += "</tr>\n"
    for row in table:
        html += '\t\t\t<tr>'
        for cell in row:
            html += f'<td>{cell}</td>'
        html += '</tr>\n'
    html += '\t\t</table>'
    return html

#generate page bodies
def genHomePage():
    body = navbar.replace("../","")
    body += f"<h1>{homeHeader}</h1>"
    body += f"<p>{homeBody}</p>"
    body += "" #TODO ADD ANY IMAGES HERE IF U WANNA
    return body

def genAllPokemon():
    body = navbar.replace("HTML/","")
    body += "<h1>All Pokemon</h1>\n" #TODO change it if you want to
    body += html_table(pokeData[0],pokeData[1:])
    return body

def genTop10():
    body = navbar.replace("HTML/","")
    body += "<h1>Top 10</h1>"
    top10List = [row for row in pokeData[1:] if len(row) > 0 and row[3].strip() in top10]
    for row in top10List:
        row.append(reasons[top10List.index(row)])
    body += html_table(pokeData[0] + ["Reasons"],top10List)
    return body

def genType(type):
    body = navbar.replace("HTML/","")
    body += f"<h1>{type.title()} Type Pokemon</h1>"
    body += html_table([pokeData[0]],[row for row in pokeData if type.lower() in [type_.lower() for type_ in row[4:6]]])
    body += ""
    return body

#makePage(title,body)
def makePage(title:str,body:str,description:str = "",keywords:str = ""):
    return f'''<!DOCTYPE HTML>
<html>
    <head>
        <title>{title}</title>
        <link rel="stylesheet" href="pokeStyles.css">
        <meta charset="UFT-8">
        <meta name="description" content="{description}">
        <meta name="keywords" content="{keywords}">
        <meta name="author" content="{author}">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        {body}
    </body>
</html>'''

#writePage(path, content)
def writePage(path,content):
    file = open(path, "w")
    file.write(content)
    file.close()

#load csv and split it into makeTable format
with open("pokemon.csv","r") as pokeData:
    pokeData = pokeData.read()
    pokeData = pokeData.split("\n")
    pokeData = [item.split(",") for item in pokeData]
    pokeData = pokeData[0:-1]

#add images to the table 
pokeData[0].insert(1,"Front")
pokeData[0].insert(2,"Back")
for row in pokeData[1:]:
    row.insert(1,f'''<img src="../img/front/{row[0]}.png">''')
    row.insert(2,f'''<img src="../img/back/{row[0]}.png">''')

#make typesList (a list of the types) from the table
typesList = sorted(list({cell for row in pokeData[1:] for cell in row[4:6] if cell}))
print(typesList)
print(len(typesList))

#printing home page
print(makePage("Home",genHomePage(),homeDescription,homeKeywords))
print("Go 8")

#making the pages
writePage("HTML/top10.html",makePage("Top 10",genTop10(),topTenDescription,topTenKeywords))
writePage("HTML/allPokemon.html", makePage("All Pokemon",genAllPokemon(),allPokemonDescription,allPokemonKeywords))
for type in typesList:
    writePage(f"HTML/{type}.html",makePage(f"{type.title()} Types",genType(type),f'''{type} page''',f'''{type}, pokemon, etc.'''))
writePage("CSS/pokeStyle.css",pokeStyles)