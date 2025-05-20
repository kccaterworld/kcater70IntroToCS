#imports
import random

#HTML skeleton
indent = "    "
lineBreak = "\n<br>"
newLine = '''
'''
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


#randomList(start,end,length) -> list
#start -> int
#end -> int
#length -> int
#creates list of length number values between values start and end
def randomList(start,end,length):
    list = []
    for i in range(length):
        list += [random.randint(start,end)]
    return list

#stripInner(list,item) -> list
def stripInner(text,item):
    data = list(text)
    for thing in item:
        while thing in data:
            data.remove(thing)
    return " ".join(data)

#makehead(title,css) -> string
#title -> string
#css -> list of lists, optimized for buildCSSBlock()
def genTitle(title):
    return f'''\n\t<title> {title} </title>'''


def buildMeta(charset,description,keywords,author,viewport):
   return f'''\t<meta charset="{charset}">
    \t<meta name="description" content="{description}">
    \t<meta name="keywords" content="{keywords}">
    \t<meta name="author" content="{author}">
    \t<meta name="viewport" content="{viewport}">'''

#buildCSSBlock(cssElement,cssProperty,cssValue) -> string
#cssElement -> string
#cssProperty -> string
#cssValue -> string
#Creates a CSS block for element(s) cssElement, with respective properties and values.
#If inputs are invalid it will not render
def buildCSSBlock(cssElement,cssProperty,cssValue):
    cssMultiline = '''_ELEMENT_ {
        _PROPERTIES_
	}
	'''
    properties = ""
    cssMultiline = cssMultiline.replace("_ELEMENT_",cssElement)
    for i in range(len(cssProperty)):
        properties += f"    " + cssProperty[i] + ":" + cssValue[i] + ";"
    cssMultiline = cssMultiline.replace("_PROPERTIES_",properties)
    return cssMultiline

#buildCSSFull() -> string
def buildCSSFull():
    cssFull = ""
    cssFull += buildCSSBlock("Example Tag",["Example Property"],["Example Value"])
    return cssFull


def buildHeadLinks(rel,type,href):
    return f'''\t<link rel="{rel}" type="{type}" href="{href}">'''

#buildHeader(tag,content,*styles) -> string
#tag -> string
#content -> string
#*styles -> list of lists optimized for buildCSSBlock()
#Generates a simple HTML block (generalized version of makePara)
def buildHeader(tag,content):
    return f'''\t<{tag}> {str(content)} </{tag}>'''

#buildPara(text) -> string
#text -> string
#Generates an HTML paragraph with conents text
def buildPara(text):
    return f"\n\t<p> {str(text)} </p>" 


def buildLink(ref,content,newTab: bool):
    if newTab == True:
        nT = '''target="_blank"'''
    elif newTab == False:
        nT = ''''''
    else:
        nT = ''''''
    return f'''\n\t<a href="https://www.{ref}" {nT}> {content} </a>'''

#buildTable(caption,header,body,footer) -> string
#caption -> string
#header -> list of lists
#body -> list of lists
#footer -> list of lists
#Creates HTML table with caption Caption, using header, body, and footer as such.
#header, body, footer: main list is all data, each inner list is a row, each list value is a collumn for that row
def buildTable(caption: str = "Table",
               header:list[list[str]] = [[""],[""]],
               body:list[list[str]] = [[""],[""]],
               footer:list[list[str]] = [[""],[""]]):
            multHead = ""
            multBody = ""
            multFoot = ""
            for item in header:
                multHead += "\t<tr>"
                for cell in item:
                    multHead += "<th>" + str(cell) + "</th>"
                multHead += "</tr>"
            for item in body:
                multBody += "\t<tr>"
                for cell in item:
                    multBody += "<td>" + str(cell) + "</td>"
                multBody += "</tr>"
            for item in footer:
                multFoot += "\t<tr>"
                for cell in item:
                    multFoot += "<td>" + str(cell) + "</td>"
                multFoot += "</tr>"
            return f'''\n\t<table>
            <caption> {caption} </caption>
            <thead>
                {multHead}
            </thead>
            <tbody>
                {multBody}
            </tbody>
            <tfoot>
                {multFoot}
            </tfoot>
        </table>\n'''

#randomTableOfRandomness(rows,collumns) -> list
#rows -> int
#collumns -> int
#creates makeTable() input for rows Rows abd collumns Collumns. Every cell contains a random number between -100 and 100
def randomTableOfRandomness(rows,collumns):
    caption = "The Random Table"
    header = []
    body = []
    footer = []
    for i in range(random.randint(1,5)):    
        header.append(randomList(-100,100,collumns))
    for i in range(random.randint(1,5)):    
        footer.append(randomList(-100,100,collumns))
    for i in range(rows):
        body.append(randomList(-100,100,collumns))
    return buildTable(caption,header,body,footer)

#buildList(title,items,type) -> string
#title -> string
#items -> list
#type -> string
#creates HTML list of specified type using title Title, containing item list entries
def buildList(title,items,type):
    list = '\n\t<'+type+'> ' +  str(title)
    for i in range(len(items)):
        list += '\n\t    <li> ' + str(items[i]) + '</li>'
    list += '\n\t</'+type+'>'
    return list

#genPageHead() -> string
def genPageHead():
    pageHead = ""
    #Example of how to add to pageHead
    pageHead += ""
    #Example title and CSS commands (IMPORTANT)
    pageHead += genTitle("Example Title")
    #Adding meta tags (IMPORTANT)
    pageHead += indent + newLine + buildMeta("UFT-8","Example Description","Example Keywords","Example Author","width=device-width, initial-scale=1.0",)
    #Adding links (IMPORTANT)
    pageHead += indent + newLine + buildHeadLinks("stylesheet","text/css","style.css")
    pageHead += indent + newLine + buildHeadLinks("icon","image/x-icon","favicon.ico")    
    return pageHead

#genPageBody() -> string
def genPageBody():
    pageBody = ""
    #Example of how to add to pageBody (include newLine)
    pageBody += ""
    #Example Header
    pageBody += buildHeader("h1","Example Header!")
    pageBody += buildLink("youtube.com","Youtube",True)
    #Example Paragraph
    pageBody += newLine + buildPara("HIIIIIII")
    #Example table of how rows and collumns work in each section. (SECTION)(ROWNUM)(COLNUM) SECTION: [H(header),B(body),F(footer)]
    pageBody += newLine + buildTable("Example Table",[["HR1C1","HR1C2"],["HR2C1","HR2C2"]],[["BR1C1","BR1C2"],["BR2C1","BR2C2"]],[["FR1C1","FR1C2"],["FR2C1","FR2C2"]])
    #Example lists
    pageBody += buildList("Example Ordered List",["First","Second","Third"],"ol")
    pageBody += newLine + buildList("Example Unordered List",["Item","Item","Item"],"ul")
    return pageBody

def genPage():
    MPage = pageMultiline.replace("_HEAD_",genPageHead())
    MPage = MPage.replace("_BODY_",genPageBody())
    return MPage



print(genPage())