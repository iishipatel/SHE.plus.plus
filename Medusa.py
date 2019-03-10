from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
import string
family={"mom":"mom","dad":"dad","moth":"mother","fath":"father","sibl":"sibling","sist":"sister","broth":"brother","aunt":"aunt","unc":"uncle"}
marr={"husband","boyfriend","girlfriend"}
work={"colleagu":"colleague","boss":"boss","employ":"employee"}
ls=LancasterStemmer()
physical=["hurt","beat","hit"]
sex=["rap","sex","forc","inappropry"]
money=["money", 'fin','monet']
society=["socy","friend", "neigbo", "neighb","reput"]
abuse=["phys","sex"]
extra={"friend":"friend","neighbo":"neighbour","neighb":"neighbor"}
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

def report(relation):
    print("MEDUSA: What is the reason?")
    reason=token_gen(input('USER: '))
    for r in reason:
        if r in money:
            print("There are several NGOs in the country who will provide you with a safer functional home away from your abuser. Don't let the money stop you from escaping the dangerous conditions that you are living in")
            break
        elif r in family or r in marr:
            print("Your "+relation+" either does not understand the pain they are inflicting upon you or they do not care. You deserve a life much better than that. Please don't let such toxic relationships stop you from leading a safer and happier life")
            break
        elif r in society:
            print("Your life and mental health are more important than anyone else's views. Putting up with abuse not only harms you but will make the abuser fearless and they may abuse someone else, and it will be your silence which lead to another ruined life. Nobody wants to live with that guilt")
            break
                
def physicalabuse(user_input):
    fam=0
    for i in token_gen(user_input):
        if i in family:
            fam_rel=family[i]
            fam=1
            break
        elif i in marr:
            fam_rel=i
            fam=1
    print("MEDUSA: That is terrible. How old are you?")
    if int(input("USER: "))>=18:
        minor=0
    else:
        minor=1
    if(fam==0 ):
        print("What is your relation to them?")
        for i in token_gen(input("USER: ")):
            if i in family:
                fam_rel=family[i]
    print("\nI am so sorry you have to go through such an ordeal. Your situation comes under domestic abuse.")
    if(minor==1):
        print("\nAs a minor, you are a victim of child abuse with your "+fam_rel+" being the abuser. You need to speak up right now. Contact the child helpline: 1098 and report your "+fam_rel+" so that the authorities can take you to a safer environment" )
    else:
        print("You are a victim of domestic abuse, a criminal offense under the Constitution of India")
        print("MEDUSA: Are you ready to report the abuser (yes or no)?")
        rep=input('USER:')
        if(rep!='yes'):
            report(fam_rel)
        print("Report your "+fam_rel+" to the police station immediately at 100. You deserve to live a safer life and the only way to get out of your situation is to put your"+fam_rel+" behind the bars.")

def sexabuse(user_input):
    fam=0
    so=0
    ext=0
    for i in token_gen(user_input):
        if i in family:
            fam_rel=family[i]
            fam=1
            break
        elif i in marr:
            fam_rel=i
            so=1
        elif i in extra:
            fam_rel=i
            ext=1
    print("MEDUSA: That is horrible. How old are you?")
    if(int(input("USER: "))>=18):
        minor=0
    else:
        minor=1
    if(fam==0 and so==0 and ext==0):
        print("How is the abuser related to you?")
        for i in token_gen(input("USER: ")):
            if i in family:
                fam_rel=family[i]
                fam=1
                break
            elif i in marr:
                fam_rel=i
                so=1
            elif i in extra:
                fam_rel=extra[i]
                ext=1            
    for i in token_gen(user_input):
        if minor==1 and fam==1:
            print("MEDUSA: You are a victim of Child Sexual Abuse by a family member, which is incest. You need to report your "+fam_rel+" right now. Call the child helpline at 1098")
            break
        if minor==1 and ext==1:
            print("MEDUSA: You are a victim of Child Sexual Abuse. You need to report your "+fam_rel+" right now. Call the child helpline at 1098")
            break
        elif minor==0 and ext==1:
            print("MEDUSA: You are a victim of Sexual Abuse. Are you ready to report your "+fam_rel+"?")
            if(input("USER: ")!='yes'):
                report(fam_rel)
            else:
                print("MEDUSA: Call the local police station at 100. Report your "+fam_rel+" and get out of the dangerous environment at the earliest")
            break
        elif so==1:
            print("MEDUSA: No matter how your relationship is defined, it is never okay to engage in sexual activity without consent. Are you ready to report your "+fam_rel+"?")
            if(input("USER: ")!='yes'):
                report(fam_rel)
            else:
                print("MEDUSA: Call the local police station at 100. Report your "+fam_rel+" and get out of the dangerous environment at the earliest")
            break

    
    '''
def emoabuse():
def checkabuse():
       '''     
print('MEDUSA: Welcome to Medusa! How may I help you? If you wish to exit type "Bye!" ')
while(True):
    flag=0
    user_input=input('USER: ')
    if(user_input=='Bye!'):
        break
    print(token_gen(user_input))
    for j in abuse:
        if("abus" in token_gen(user_input) and j not in token_gen(user_input)):
            print("MEDUSA: I'm very sorry to hear about this.\n What kind of abuse is this? Are they physically hurting you or sexually, or emotionally manipulating you?" )
            user_input=input("USER: ")
            for i in token_gen(user_input):
                if i=="phys":
                    physicalabuse(user_input)
                    flag=1
                    break
                if i=="sex":
                    sexabuse(user_input)
        if flag==1:
            break
    
    if flag==1:
        continue
    for i in token_gen(user_input):
        for j in physical:
            if(j in token_gen(user_input)):
                physicalabuse(user_input)
                flag=1
                break
        for j in sex:
            if(j in token_gen(user_input)):
                sexabuse(user_input)
                flag=1
                break
        
        if (flag==1):
            break
