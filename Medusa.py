from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
import string

ls=LancasterStemmer()

def token_gen(user_input):
    words=word_tokenize(user_input)
    stopWords=list(stopwords.words('English'))
    clean_input=[]
    for w in words: 
        if w not in stopWords:
            clean_input.append(ls.stem(w))
    cleaner=[]
    for w in clean_input:
        if w not in '!,."?':
            cleaner.append(w)
    return cleaner
            

flag=True
print('Medusa: Welcome to Medusa! How may I help you? If you wish to exit type "Bye!" ')
while(flag==True):
    user_input=input('User: ')
    if(user_input!='Bye!'):
        print(token_gen(user_input))
        flag=False
        
