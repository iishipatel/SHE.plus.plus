from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
import string
family={"mom":"mom","dad":"dad","moth":"mother","fath":"father","sibl":"sibling","sist":"sister","broth":"brother","aunt":"aunt","unc":"uncle","boyfriend":"boyfriend","girlfriend":"girlfriend"}
ls=LancasterStemmer()
physical=["hurt","beat","hit"]
def token_gen(user_input):
    words=word_tokenize(user_input)
    stopWords=list(stopwords.words('english'))
    clean_input=[]
    for w in words: 
        if w not in stopWords:
            clean_input.append(ls.stem(w))
    cleaner=[]
    for w in clean_input:
        if w not in '!,."?':
            cleaner.append(w)
    return cleaner


def physicalabuse():
    print("MEDUSA: Okay. What is your age?")
    if int(input("USER: "))>=18:
        print("What is your relation to them?")
        for i in token_gen(input("USER: ")):
            if i in family:
                print("\nOkay so your " + family[i]+" is physically abusing you. This comes under Domestic Abuse.")
        
    '''
def sexabuse():
def emoabuse():
def checkabuse():

       '''     
print('MEDUSA: Welcome to Medusa! How may I help you? If you wish to exit type "Bye!" ')
while(True):
    user_input=input('USER: ')
    if(user_input=='Bye!'):
        break
    print(token_gen(user_input))
    if("abus" in token_gen(user_input) and "phys" not in token_gen(user_input)):
        print("MEDUSA: I'm very sorry to hear about this.\n What kind of abuse is this? Are they physically hurting you or sexually, or emotionally manipulating you?" )
        for i in token_gen(input("USER: ")):
            if i=="phys":
                physicalabuse()
                break
        continue
    for i in token_gen(user_input):
        for j in physical:
            if(j in token_gen(user_input)):
                physicalabuse()
                break
    continue
    
