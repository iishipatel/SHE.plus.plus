from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer
import sys
family={"mom":"mom","dad":"dad","moth":"mother","fath":"father","sibl":"sibling","sist":"sister","broth":"brother","aunt":"aunt","unc":"uncle"}
marr={"husband","boyfriend","girlfriend"}
work={"colleagu":"colleague","boss":"boss","employ":"employee"}
ls=LancasterStemmer()
physical=["hurt","beat","hit","phys"]
sex=["rap","sex","forc","inappropry","touch"]
emo=["curs","scream","shout"]
mental_issues=["depress","sad", "upset","anxy","scar","traum"]
money=["money", 'fin','monet']
society=["socy","friend", "neigbo", "neighb","reput"]
abuse=["phys","sex"]
misc=["harass","bul","tort","troubl", "teas"]
leave=["thank",'bye',"no"]
extra={"friend":"friend","neighbo":"neighbour","neighb":"neighbor"}                    

def psycho_help(user_input):
    print("\nMEDUSA: I hate that you're feeling that way. What happened?")
    response=input("USER: ")
    check_abuse(response)

def token_gen(user_input):
    words=word_tokenize(user_input)
    stopWords=list(stopwords.words('english'))
    stopWords.remove("no")
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
            print("MEDUSA: There are several NGOs in the country who will provide you with a safer functional home away from your abuser. Don't let the money stop you from escaping the dangerous conditions that you are living in")
            break
        elif r in family or r in marr:
            print("MEDUSA: Your "+relation+" either does not understand the pain they are inflicting upon you or they do not care. You deserve a life much better than that. Please don't let such toxic relationships stop you from leading a safer and happier life")
            break
        elif r in society:
            print("MEDUSA: Your life and mental health are more important than anyone else's views. Putting up with abuse not only harms you but will make the abuser fearless and they may abuse someone else, and it will be your silence which lead to another ruined life. Nobody wants to live with that guilt")
            break
    return 0
                
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
        print("MEDUSA: What is your relation to them?")
        for i in token_gen(input("USER: ")):
            if i in family:
                fam_rel=family[i]
    print("MEDUSA: I am so sorry you have to go through such an ordeal. Your situation comes under domestic abuse.")
    if(minor==1):
        print("MEDUSA: As a minor, you are a victim of child abuse with your "+fam_rel+" being the abuser. You need to speak up right now. Contact the child helpline: 1098 and report your "+fam_rel+" so that the authorities can take you to a safer environment" )
    else:
        print("MEDUSA: You are a victim of domestic abuse, a criminal offense under the Constitution of India")
        print("MEDUSA: Are you ready to report the abuser (yes or no)?")
        rep=input('USER:')
        if(rep!='yes'):
            report(fam_rel)
        print("MEDUSA: Report your "+fam_rel+" to the police station immediately at 100. You deserve to live a safer life and the only way to get out of your situation is to put your"+fam_rel+" behind the bars.")
    print("Do you have any further queries?")
    check_abuse(input("USER: "))

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
        print("MEDUSA: How is the abuser related to you?")
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
            print("MEDUSA: You are a victim of Child Sexual Abuse by a family member. You need to report your "+fam_rel+" right now. Call the child helpline at 1098")
            break
        if minor==1 and ext==1:
            print("MEDUSA: You are a victim of Child Sexual Abuse. You need to report your "+fam_rel+" right now. Call the child helpline at 1098")
            break
        elif minor==0 and ext==1:
            print("MEDUSA: You are a victim of Sexual Abuse. Are you ready to report your "+fam_rel+"?")
            if(input("USER: ")!='yes'):
                report(fam_rel)
            print("MEDUSA: Call the local police station at 100. Report your "+fam_rel+" and get out of the dangerous environment at the earliest")
            break
        elif minor==0 and fam==1:
            print("MEDUSA: You are a victim of Sexual Abuse by a family member. Are you ready to report your "+fam_rel+"?")
            if(input("USER: ")!='yes'):
                report(fam_rel)
            print("MEDUSA: Call the local police station at 100. Report your "+fam_rel+" and get out of the dangerous environment at the earliest")
            break
        elif so==1:
            print("MEDUSA: No matter how your relationship is defined, it is never okay to engage in sexual activity without consent. Are you ready to report your "+fam_rel+"?")
            if(input("USER: ")!='yes'):
                report(fam_rel)
            print("MEDUSA: Call the local police station at 100. Report your "+fam_rel+" and get out of the dangerous environment at the earliest")
            break
    print("Do you have any further queries?")
    check_abuse(input("USER: "))

def emoabuse(user_input):
    fam=0
    career=0
    married=0
    print("MEDUSA: How old are you?")
    if(int(input("USER: "))>=18):
        minor=0
    else:
        minor=1
    for i in user_input:
        if i in family:
            fam_rel=family[i]
            fam=1
            break
        elif i in work:
            fam_rel=i
            career=1
            break
        elif i in marr:
            fam_rel=marr[i]
            married=1
            break
    if(fam==0 and married==0 and career==0):
        print("MEDUSA: How is the abuser related to you?")
        for i in token_gen(input("USER: ")):
            if i in family:
                fam_rel=family[i]
                fam=1
                break
            elif i in work:
                fam_rel=i
                career=1
                break
            elif i in marr:
                fam_rel=marr[i]
                married=1
                break
    print("MEDUSA: Your mental health is very important. Without a healthy mind you can never truly live a healthy life. Have you ever talked to your "+fam_rel+" regarding their effect on you?")
    if(input("USER: ")=='yes'):
        print("MEDUSA: Very well. Since their attitude hasn't changed, you need to take matters into your own hand.")
        print("MEDUSA: How would you describe your mental condition?")
        mental_state=input("USER: ")
        for token in token_gen(mental_state):
            if token in mental_issues:
                psycho_help(mental_state)
                break
    print("Do you have any further queries?")
    check_abuse(input("USER: ")    )
    
 
 
def check_abuse(user_input):
    tokens=token_gen(user_input)
    flag=0
    for token in tokens:
        if token=="yes":
            print("MEDUSA: How can I help you?")
            check_abuse(input("USER: "))
            flag=1
        if token in physical:
            physicalabuse(user_input)
            flag=1
        if token in sex:
            sexabuse(user_input)
            flag=1
        if token in emo:
            emoabuse(user_input)
            flag=1
        if token in mental_issues:
            psycho_help(user_input)
            flag=1
        if token in misc:
            print("MEDUSA: I am sorry to hear that, but could you be more specific?")
            flag=1
        if token in leave:
            print("\nMEDUSA: Thank you for using Medusa. And remember, stay strong :)")
            return 1
            flag=1
    if(flag!=1):
        print("I could not understand you. Could you repeat please?")
        return 2
        
    
print('MEDUSA: Welcome to Medusa! How may I help you? If you wish to exit type "bye" ')
x=0
while(x!=1):
     user_input=(input("USER: "))
     if(user_input.lower()=='bye'):
         break
     x=check_abuse(user_input)
     if x==1:
         break
     if x==2:
         continue
     
