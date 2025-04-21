#! /usr/bin/python3
print("Content-Type: text/html\n\n")

#globals
newLine = "\n"
indent = "  "
nullStr = ""
#top 10, fill it out
top10 = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie"]
reasons = ""
#globals for meta tag, fill them out, leave f-strings in
author = "" #your name here
homeDescription = ""
homeKeywords = ""
topTenDescription = ""
topTenKeywords = ""
allPokemonDescription = ""
allPokemonKeywords = ""
#f-strings will be filled by for loop later
typesDescription = f'''{nullStr}typesList[i]{nullStr} page''' #change as needed
typesKeywords = f'''{nullStr}typesList[i]{nullStr}, pokemon, etc.'''
#page variables
homeHeader = ""
homeBody = ""

##helper functions
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
#print(pokeData)

#make typesList
typesList = sorted(list({cell for row in pokeData[1:] for cell in row[4:6] if cell}))
print(typesList)
print(len(typesList))

#make table function
def html_table(header,table):
    html = '<table border="1">\n'
    html += "<table>\n<tr>"
    for item in header:
        html += f"<th>{item}</th>"
    html += "</tr>\n"
    for row in table:
        html += '<tr>'
        for cell in row:
            html += f'<td>{cell}</td>'
        html += '</tr>\n'
    html += '</table>'
    return html

#generate page bodies
def genHomePage():
    body = f"<h1>{homeHeader}</h1>"
    body += f"<p>{homeBody}</p>"
    body += "" #TODO ADD ANY IMAGES HERE IF U WANNA
    return body

def genAllPokemon():
    body = "<h1>All Pokemon</h1>\n" #TODO change it if you want to
    body += html_table(pokeData[0],pokeData[1:])
    return body

def genTop10():
    body = "<h1>Top 10</h1>"
    top10List = [row for row in pokeData[1:] if len(row) > 0 and row[3].strip() in top10]
    for row in top10List:
        row.append(reasons[top10List.index(row)])
    body += html_table(pokeData[0] + ["Reasons"],)
    return body

def genType(type):
    body = f"<h1>{type.title()} Type Pokemon</h1>"
    body += html_table([pokeData[0]],[pokemon for pokemon in pokeData if type in [type_.lower() for type_ in pokemon]])
    body += ""
    return body

#makePage(title,body)
def makePage(title:str,body:str,description:str = "",keywords:str = ""):
    return f'''
        <!DOCTYPE HTML>
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

#printing home page
print(genHomePage())

#making the pages
writePage("HTML/top10.html",makePage("Top 10",genTop10(),topTenDescription,topTenKeywords))
writePage("HTML/allPokemon.html", genAllPokemon())
for item in typesList:
    writePage(f"HTML/{item}.html",genType(item))