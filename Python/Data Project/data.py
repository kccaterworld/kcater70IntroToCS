#!/usr/bin/python3
print("Content-Type: text/html\n\n")

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import random


#Globals
indent = "    "
lineBreak = "\n<br>"
newLine = '''
'''
yearFreq = {}
kemalOSIS = "235824331"
emmaOSIS = "227178217"
stellaOSIS = "239363948"
#Multiline for HTML Webpages, it gets replaced by the actual content by certain functions
site = '''<!DOCTYPE html>
<html>
    <head>
        <title>?TITLE?</title>
        <link rel="stylesheet" href="../CSS/DPStyle.css">
        <meta name="viewport" content="width=device-width, initial-scale=1">  
    </head>
    <body>
        ?NAV?
        ?BODY?
    </body>
</html>'''

#Helper Functions (copied from my pythonFuncs file)


#Function to make header in HTML website
def makeHeader(h,num):
   return "<h"+str(num)+">"+str(h)+"</h"+str(num)+">\n"

#Function to make a Paragraph in HTML website
def makeParagraph(p):
    global indent
    return indent + "<p>"+str(p)+"</p>\n"


def navbar():
    nav = f'''
    <nav>
    <ol>
        <li><a href="../data.py">Home Page</a></li>
        <li><a href="HTML/{kemalOSIS}.html">Hate Crimes through the years</a></li>
        <li><a href="HTML/{emmaOSIS}.html">Race</a></li>
        <li><a href="HTML/{stellaOSIS}.html">Religion</a></li>
      </ol>
    </nav>
    '''
    return nav.strip()

#readCSV(path, rotate) -> list
#path -> string
#rotate -> int
#Reads a CSV file and returns a list of lists, where each inner list is a row in the CSV file.
def readCSV(path: str = "",
            rotate: int = 0):
    with open(path, "r") as file:
        table = [row.split(",") for row in file.read().split("\n")]
        return myRot90(table, rotate)

#writePage(path, content) -> None
#page -> string
#content -> string
#Writes the content to the specified path, creating a new file if it doesn't exist.
#If the file already exists, it will be overwritten.
def writePage(path: str, content: str = "") -> None:
    with open(path, "w") as file:
        file.write(content)

#mean(vals: tuple = ()) -> float
#vals -> tuple of numbers
#Returns the mean of the numbers in vals.
#If vals is empty, it will return 0.0.
def mean(vals: tuple = ()) -> float:
    if len(vals) == 1:
        return float(vals[0])
    sum = 0
    for number in vals:
        sum += number
    return float(sum / len(vals))

#myRot90(array: list = [[]],
#        numTimes: int = 1,
#        axes: list = []) -> list
#array -> list of lists
#numTimes -> int
#axes -> list of ints
#Rotates the array 90 degrees counter-clockwise numTimes times.
#If numTimes is 0, it will return the original array.
#If numTimes is 1, it will return the array rotated 90 degrees counter-clockwise.
def myRot90(array: list[list[str]] | list[list[int]] = [[]],
            numTimes: int = 1,
            axes: list[int] = []):
    if numTimes == 0:
        return array
    if numTimes == 1:
        return [list(row) for row in zip(*array)]
    else:
        myRot90([list(row) for row in zip(*array)], numTimes - 1, axes)

def freqYears(data):
    for year in data:
        if year in yearFreq:
            yearFreq[year] += 1
        else:
            yearFreq[year] = 1
    return yearFreq

#makePage(head, body) -> str
#head -> dict
#body -> list
#head should be a dict of a certain shape, with the keys "title", "description", "keywords", and "author".
#body should be a list of strings, which will be the body of the HTML page.
#Each string in body should be a valid HTML element.
def makePage(head:dict = {"title": "Title",
                          "description": "description",
                          "keywords": "keywords",
                          "author": "author",
                          "stylesheet": "style.css"},
             body:list = ["<p> Body Element 1</p>", "<p> Body Element 2</p>"]) -> str:
    headContent = f'''<title>{head["title"]}</title>
        <link rel="stylesheet" href="{head["stylesheet"]}">
        <meta name="description" content="{head["description"]}">
        <meta name="keywords" content="{head["keywords"]}">
        <meta name="author" content="{head["author"]}">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">'''
    bodyContent = "".join([element  + "\n\t\t" for element in body])
    return f'''
<!DOCTYPE html>
<html>
    <head>
        {headContent}
    </head>
    <body>
        {bodyContent}
    </body>
</html>
'''


#Main Program
#Read the CSV
dataList = readCSV("hatecrimes.csv")[0:-1]

###########################################################################################################################
# K. Cater - General trends of hate crimes in the US
###########################################################################################################################

#Make a list of the years:
yearsList = sorted(list({row[1] for row in dataList}), reverse = True)[1:]
#Define Axis Lists
freqYears([row[1] for row in dataList[1:]])
xAxis = [int(year) for year in yearsList]
totIncsYAxis = [sum([int(row[41]) for row in dataList if row[1] == year]) for year in yearsList]
avgIncsYAxis = [round((totIncsYAxis[yearsList.index(year)] / yearFreq[year]),2) for year in yearsList]
totVicsYAxis = [sum([int(row[42]) for row in dataList if row[1] == year]) for year in yearsList]
totOffsYAxis = [sum([int(row[43]) for row in dataList if row[1] == year]) for year in yearsList]
yTicks = range(int(min([min(yAxis) for yAxis in [totIncsYAxis, avgIncsYAxis, totVicsYAxis, totOffsYAxis]])),max([max(yAxis) for yAxis in [totIncsYAxis, avgIncsYAxis, totVicsYAxis, totOffsYAxis]]))
#Total Incidents Per Year
plt.figure(figsize=(15, 8))
plt.plot(xAxis,
         totIncsYAxis,
         color="black",
         marker="",
         linestyle="-",
         markersize=1,
         label="Total Incidents Per Year",
         alpha=1,
         linewidth=2,
         markeredgecolor="black",
         markeredgewidth=2,
         markerfacecolor="black")
#Average County Incidents per Year
plt.plot(xAxis,
         avgIncsYAxis,
         color="blue",
         marker="",
         linestyle="-",
         markersize=1,
         label="Average Incidents Per Year",
         alpha=1,
         linewidth=2,
         markeredgecolor="black",
         markeredgewidth=2,
         markerfacecolor="black")
#Total Victims Per Year
plt.plot(xAxis,
         totVicsYAxis,
         color="red",
         marker="",
         linestyle="-",
         markersize=1,
         label="Total Victims Per Year",
         alpha=1,
         linewidth=2,
         markeredgecolor="black",
         markeredgewidth=2,
         markerfacecolor="black")
#Total Offenders Per Year
plt.plot(xAxis,
         totOffsYAxis,
         color="green",
         marker="",
         linestyle="-",
         markersize=1,
         label="Total Offenders Per Year",
         alpha=1,
         linewidth=2,
         markeredgecolor="black",
         markeredgewidth=2,
         markerfacecolor="black")
#Plot stuff
plt.title("Title")
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
plt.xticks(xAxis, rotation=45, ha='right')
plt.yticks(yTicks, rotation=0, ha='right')
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.gca().yaxis.set_major_locator(MultipleLocator(20))
plt.gca().set_aspect('auto', adjustable='box')
plt.savefig("IMG/incidentsPerYearGraph.png")
plt.clf()


###########################################################################################################################
# E. Ching - Bar graph illustrating hate crimes based on race
###########################################################################################################################

def race():
    global dataList
    white = 0
    black = 0
    native = 0
    asian = 0
    hawaiian = 0
    multi = 0
    for row in dataList[1:]:
        white += int(row[8])
        black += int(row[9])
        native += int(row[10])
        asian += int(row[11])
        hawaiian += int(row[12])
        multi += int(row[13])
    stats = [white, black, native, asian, hawaiian, multi]
    races = []
    options = []
    for header in dataList[0]:
        races.append(header)
    for i in range(8, 14):
        options.append(races[i])
    plt.figure(figsize=(20, 10))
    plt.bar(options, stats)
    plt.ylabel("total number of reported crimes")
    plt.xlabel("crime against race")
    plt.title("hate crimes based on race in New York (2010 - 2022)")
    plt.savefig("IMG/bar_race.png")

# Generate data and chart
race()

# Build HTML content
site = site.replace("?NAV?", navbar().replace("HTML/", ""))
site = site.replace("?STYLE?", "http://marge.stuy.edu/~eching70/DataProject/CSS/DPStyle.css")
race_page = site.replace("?TITLE?", "Race")

body = makeHeader("Correlation between Race and Crime", 1)
body += makeParagraph("Hate crimes based on race have and continue to reflect racism, implicit bias, and social tensions that disproportionately target certain groups. This graph illustrates reported hate crimes in New York from 2010 to 2022, broken down by race.")
body += indent * 2 + "<img src='../IMG/bar_race.png' alt='race plot'>\n"
body += makeParagraph("hi")
body = body.strip()
race_page = race_page.replace("?BODY?", body)
writePage(f"HTML/{emmaOSIS}.html", race_page)


###########################################################################################################################
# S. Kubersky - Pie graph illustrating trends of religion based hate crimes
###########################################################################################################################

def religionGraph():
    data = dataList[0]
    mylabels = data[15:23]
    jewish = 0
    catholic = 0
    protestant = 0
    islamic = 0
    multiple = 0
    atheism = 0
    religion = 0
    other = 0
    for row in dataList[1:]:
        jewish += int(row[15])
        catholic += int(row[16])
        protestant += int(row[17])
        islamic += int(row[18])
        multiple += int(row[19])
        atheism += int(row[20])
        religion += int(row[21])
        other += int(row[22])
    raw = [jewish, catholic, protestant, islamic, multiple, atheism, religion, other]
    total = 0
    for i in raw:
        total += i
    percentage = []
    for i in raw:
        percent = (i / total) * 100
        percentage.append(percent)
    colors = ['gold', 'lightskyblue', 'yellowgreen', 'dodgerblue', 'lightcoral', 'coral', 'cornflowerblue', 'yellow']
    myexplode = [0, 0, 0, 0, .5, 0, .5, 0]
    plt.figure(figsize=(20, 10))
    plt.pie(percentage, labels=mylabels, colors=colors, explode = myexplode)
    plt.legend(title = "Relgions:", loc='lower left')
    plt.title('Hate Crimes in New York State By Religion')
    plt.savefig("IMG/ReligionPlot.png")

religionGraph()

def genReligionBody():
	body = makeHeader("Correlation Between Religion, in Hate Crime Statistics", 1)
	body += makeParagraph("This shows how in New York State there is an issue with anti-semitism ")
	body += indent*2 + '''<img src="../IMG/ReligionPlot.png" alt="Religion">'''
	body =  body.strip()
	return body

religionGraph()

religionpage = site.replace("?TITLE?", "The Corrolation Between Hate Crimes and Religion")
religionpage = religionpage.replace("?NAV?", navbar().replace("HTML/", ""))
religionpage = religionpage.replace("?BODY?", genReligionBody())
writePage(f"HTML/{stellaOSIS}.html", religionpage)


#Print home page
print(makePage(head = {"title": "Hate Crimes in the US",
    "description": "A website exploring hate crimes in the US from 2010 to 2022.",
    "keywords": "data, python, hate crimes, analysis, trends, matplotlib, graph",
    "author": "",
    "stylesheet": "CSS/DPStyle.css"},
    body = [navbar().replace("../", ""),
        "<h1>Hate Crimes across NYS Counties</h1>",
        f'''<a href="HTML/{kemalOSIS}.html">General Trends and Analysis of Hate Crimes in the US</a>''',
        f'''<a href="HTML/{emmaOSIS}.html">EMMA TEXT</a>''',
        f'''<a href="HTML/{stellaOSIS}.html">STELLA TEXT</a>''']))

#Write to the files:
writePage(f"HTML/{kemalOSIS}.html",makePage(head = {"title": "General Trends and Analysis of Hate Crimes in the US",
    "description": "A graph showing the trends and analysis of hate crimes in the US.",
    "keywords": "data, python, hate crimes, analysis, trends, matplotlib, graph",
    "author": "Kemal Cater",
    "stylesheet": "../CSS/DPStyle.css"},
    body = [navbar().replace("HTML/", ""),
        "<h1>General Trends and Analysis of Hate Crimes in the US</h1>",
        "<img src='../IMG/incidentsPerYearGraph.png' alt='Graph of Hate Crimes in the US'>"]))