#!/usr/bin/python3
print("Content-Type: text/html\n\n")


with open("/home/students/odd/2027/kcater70/Documents/Code/Python/pokemon/pokemon.csv", "r") as pokeRawData:
    pokeRawData = pokeRawData.read()
    pokeDataSplit = pokeRawData.split("\n")
    pokeData = []
    for item in pokeDataSplit:
        pokeData.append(item.split(","))

#buildTable(caption,header,body,footer) -> string
#caption -> string
#header -> list of lists
#body -> list of lists
#footer -> list of lists
#Creates HTML table with caption Caption, using header, body, and footer as such.
#header, body, footer: main list is all data, each inner list is a row, each list value is a collumn for that row
def buildTable(caption,header,body,footer):
            tableMultiline = '''\n\t<table>
            <caption> _CAPTION_ </caption>
            <thead> _HEAD_
            </thead>
            <tbody> _BODY_
            </tbody>
            <tfoot> _FOOT_
            </tfoot>
        </table>\n'''
            multHead = ""
            multBody = ""
            multFoot = ""
            for item in header:
                multHead += "\n\t\t<tr>"
                for cell in item:
                    multHead += "<th>" + str(cell) + "</th>"
                multHead += "</tr>"
            for item in body:
                multBody += "\n\t\t<tr>"
                for cell in item:
                    multBody += "<td>" + str(cell) + "</td>"
                multBody += "</tr>"
            for item in footer:
                multFoot += "\n\t\t<tr>"
                for cell in item:
                    multFoot += "<td>" + str(cell) + "</td>"
                multFoot += "</tr>"
            tableMultiline = tableMultiline.replace("_CAPTION_",caption)
            tableMultiline = tableMultiline.replace("_HEAD_",multHead)
            tableMultiline = tableMultiline.replace("_BODY_",multBody)
            tableMultiline = tableMultiline.replace("_FOOT_",multFoot)
            return tableMultiline

print(buildTable("Pokemon",[pokeData[1]],[pokeData[2:]],[]))
