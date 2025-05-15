#!/usr/bin/python3
print("Content-Type: text/html\n\n")

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

#What I'm doing: line plot
#Ideas: __ lines, one graph
#   Total incidents per year
#   Average incidents per year
#   Victims per year
#   Offenders per year

#TODO: test multiple lines one graph (just do multiple plt.pltot()s? and then multiple legen things? lowk idk)
#Globals
indent = "    "
lineBreak = "\n<br>"
newLine = '''
'''
yearFreq = {}
kemalOsis = 235824331
emmaosis = 0
stellaOSIS = 0
#Multiline for HTML Webpages, it gets replaced by the actual content by certain functions
pageMultiline = '''
<!DOCTYPE html>
<html>
    <head> _HEAD_
    </head>
    <body>
    _BODY_
    </body>
</html>
'''


#Helper Functions (copied from my pythonFuncs file)

#readCSV(path, rotate) -> list
#path -> string
#rotate -> int
#Reads a CSV file and returns a list of lists, where each inner list is a row in the CSV file.
def readCSV(path: str = "",
            rotate: int = 0) -> list:
    with open(path, "r") as file:
        table = [row.split(",") for row in file.read().split("\n")]
    if rotate > 0:
        return myRot90(table, rotate)
    else:
        return table
	
#writePage(path, content) -> None
#page -> string
#content -> string
#Writes the content to the specified path, creating a new file if it doesn't exist.
#If the file already exists, it will be overwritten.
def writePage(path, content):
    with open(path, "w") as file:
        file.write(content)

#mean(vals: tuple = ()) -> float
#vals -> tuple of numbers
#Returns the mean of the numbers in vals.
#If vals is empty, it will return 0.0.
def mean(vals: tuple = ()) -> float:
    if len(vals) == 0:
        return 0.0
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
def myRot90(array: list = [[]],
            numTimes: int = 1,
            axes: list = []) -> list:
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
def makePage(head:dict = {"title": "title",
                          "description": "description",
                          "keywords": "keywords",
                          "author": "author"},
             body:list = ["<p> Body Element 1</p>", "<p> Body Element 2</p>"]) -> str:
    headContent = f'''<title>{head["title"]}</title>
        <link rel="stylesheet" href="CSS/DPStyle.css">
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

#Print home page
print(makePage(head = {
    "title": "Hate Crimes in the US",
    "description": "A website exploring hate crimes in the US from 2010 to 2022.",
    "keywords": "data, python, hate crimes, analysis, trends, matplotlib, graph",
    "author": ""},
    body = [["<h1>Some Text</h1>"],
        ["Table of Data?"],]))

#Write to the files:
writePage(f"HTML/{kemalOsis}.html",makePage(head = {
    "title": "General Trends and Analysis of Hate Crimes in the US",
    "description": "A graph showing the trends and analysis of hate crimes in the US.",
    "keywords": "data, python, hate crimes, analysis, trends, matplotlib, graph",
    "author": "Kemal Cater"},
    body = [["<h1>General Trends and Analysis of Hate Crimes in the US</h1>"],
        ["<img src='IMG/incidentsPerYearGraph.png' alt='Graph of Hate Crimes in the US'>"],]))
writePage(f"HTML/{emmaosis}.html", makePage())
writePage(f"HTML/{stellaOSIS}.html", makePage())