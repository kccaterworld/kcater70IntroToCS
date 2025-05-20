wordFreq = {
        
    }

wordsToAdd = ["test","Hello","fish","bacon","bacon","fish","at","bacon","bacon",
              "fish","kevin",'test',"Hello","fish","bacon","bacon","fish","at",
              "bacon","kevin","bacon","kevin","bacon"]
#Write loop here!
def freqWords(data):
    for word in data:
        if word in wordFreq:
            wordFreq[word] += 1
        else:
            wordFreq[word] = 1
    return wordFreq

newWordList = []
def processWordies(wordLists):
    newWordList = []
    for item in wordLists:
        newWordList.append(item.strip(" .,?!;:\n"))
    return newWordList

with open("/home/students/odd/2027/kcater70/Documents/Text1.txt","r") as Text1:
    Text1 = Text1.read()
    
with open("/home/students/odd/2027/kcater70/Documents/Text2.txt","r") as Text2:
    Text2 = Text2.read()
    
with open("/home/students/odd/2027/kcater70/Documents/Text3.txt","r") as Text3:
    Text3 = Text3.read()

def tallyText(string):
    return freqWords(processWordies(string.split(" ")))

#print(Text1, Text2, Text3)
print(tallyText(Text1))
print(tallyText(Text2))
print(tallyText(Text3))