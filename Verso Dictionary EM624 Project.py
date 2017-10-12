#Aurthor: Kishan J
#This is a script for verso dictionary proto type:A reverse dictionary.



#Importing the required data packages
import nltk, json, itertools
from nltk.corpus import wordnet

#Creating empty dictionary and a list for nouns

wordDict = {}
nouns = []

#Defining a fucntion for taking out nouns into a list
def returnNouns(inputString):
    tokens = nltk.word_tokenize(inputString)
    return list(set([word for word, pos in nltk.pos_tag(tokens) if pos.startswith('NN')]))

#Defining a fuction for calculating similarity between wnons
def findSimilarity(word1, word2):
    try:    
        w1 = wordnet.synset(word1 + '.n.01')
        w2 = wordnet.synset(word2 + '.n.01')
        #print w1, w2

        return w1.wup_similarity(w2)
    except:
        return 0
        print 'error occured'
    
#Defining a fuction for comapring the similarities and returning the max key as an out put word fir the input phrase   
def compaire():
    userInput = raw_input('Please enter a phrase which is defination for something: ')
    userInputTokenList = returnNouns(userInput)
    
    with open('wordDict.json', 'r') as wordDict:
        wordDictData = json.load(wordDict)
    result = 0
    resultKey = ''
    for key in wordDictData.keys():
# to calculate the Cartetian product of the nouns from user Input and nouns form the wordlist  and Returns list of Tuples       
        combinedList = list(itertools.product(wordDictData[key], userInputTokenList)) 
        
        count = 1
        maxSimilarity = 0        
        for tup in combinedList:
            if len(tup) == 2:
                maxSimilarity += findSimilarity(tup[0], tup[1])
                count += 1
        
        result = max(maxSimilarity / count, result)
        if result == maxSimilarity / count:
            resultKey = key
    return (resultKey, result)

finalResult = compaire()

#Printing the final result and similarity into percentages

print '\nThe closest meaning of the phrase is ' + str(finalResult[0]).upper() + ' with similarity of ' + str(finalResult[1] * 100)[:5] + '%'
    

#Thank you

    

    
    
    
    
    
    
    
