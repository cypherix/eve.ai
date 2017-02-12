from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
import os
import re
import time
import string

frameworks=[("php","laravel"),("javascript","nodejs"),("python","django"),("python","data analytics"),("php","codeignite")]
skill_dict=["php","javascript","html","c#","asp.net","java","laravel","nodejs","django","python","ml","c","c++","mysql","mongodb","postgresql","ajax"]
college_dict=[('Sree Chitra Thirunal College Of Engineering Trivandrum',5.0),('University Of California Irwine',5.0),('Harvard University',5.0)]
company_dict=[('Google ',5.0),('Microsoft ',5.0),('TCS ',3.0),('Freshdesk ',4.0)]
start=time.time()
college=""
company=""
c=""
college_score=0.0
company_score=0.0

conclusion2=""



#Location of file
with open('/Users/continuumlabs/Desktop/stanford/resume.txt', 'r') as f:
    
    data=f.read()
### SKILL EXTRACTION AND SCORE GENERATION 
    if re.search(r'(Skills|SKILLS|Technologies|TECHNOLOGIES)((:|\s|-|:-)*)((\r\n|\r|\n)*)((.*?|\r\n|\r|\n)*)([A-z])(:|-|(\n)+]{1,})', data):
        c2=re.search(r'(Skills|SKILLS|Technologies|TECHNOLOGIES)((:|\s|-|:-)*)((\r\n|\r|\n)*)((.*?|\r\n|\r|\n)*)([A-z])(:|-|(\n)+]{1,})', data).group(0)
        c2=c2.lower()
        #print c
        stop_words=set(stopwords.words('english'))
        stop_words=set(string.punctuation)
        resume1=[i for i in wordpunct_tokenize(c2) if i  not in stop_words]
        print "Skills in resume:"
        resume=list(set(resume1))#removes duplicates
        skill_list=[i for i in resume if i in skill_dict] #compare skills in resume and the skill dictionary
        print skill_list
        skill_match=[]

        jd=["javascript","html","ml","php"]#jd
        #print "\nJD skills "
        #print jd
        ##append frameworks to new jd list
        jd1=jd
        for i in range(0,len(jd)):
         for (x,y) in frameworks:
          if(x==jd[i]):
           jd1.append(y)
        #print "JD skills after processing"
        #print jd1
    ##search for skills in the new jd list but use old jd list for score calculation
        for i in range(0,len(jd1)):
            for j in range(0,len(skill_list)):
                if(jd1[i]==skill_list[j]):
                    skill_match.append(skill_list[j])
        print "\nMatching skill set:"
        print skill_match

        #score generation
        len_skill_match=len(skill_match)
        len_skill_list=len(skill_list)
        if(len_skill_list >0):
            Precision=float(len_skill_match)/len_skill_list
        else:
            Precision=0
            
        len_jd=len(jd)
        Recall=float(len_skill_match)/len_jd
        if ((Precision + Recall)!=0):
            skill_score= 2*((Precision*Recall)/(Precision+Recall))
        else:
            skill_score=0
    
        

### CODE ENDS
    #### COLLEGE AND EMAIL EXTRACTION
    #regular expression to find educational institution
    if re.search(r'(Academia|ACADEMIA|Education|EDUCATION)((:|\s|-|:-)*)((\r\n|\r|\n)*)((.*?|\r\n|\r|\n)*)([A-Z]{2,})', data):
        conclusion1 = re.search(r'(Academia|ACADEMIA|Education|EDUCATION)((:|\s|-|:-)*)((\r\n|\r|\n)*)((.*?|\r\n|\r|\n)*)([A-Z]{2,})', data).group(0)
    #regular expression to find work experience
    if re.search(r'(Work Experience|WORK EXPERIENCE)((:|\s|-|:-)*)((\r\n|\r|\n)*)((.*?|\r\n|\r|\n)*)([A-z])(:|-|(\n)+]{1,})', data):
        conclusion2=re.search(r'(Work Experience|WORK EXPERIENCE)((:|\s|-|:-)*)((\r\n|\r|\n)*)((.*?|\r\n|\r|\n)*)([A-z])(:|-|(\n)+]{1,})', data).group(0)
        
    college+=str(conclusion1)
    company+=str(conclusion2)
    c1 =college.split(' ',1)[1]
    if c1[-1]!=".":
        c1+="."  #to determine the end of extracted paragraph(if there is no fullstop)

    c2 =company.split(' ',1)[1]
    if c2[-1]!=".":
        c2+="."  #to determine the end of extracted paragraph(if there is no fullstop)

 
    f.seek(0,0) #point to beginning of file
    firstNlines=f.readlines()[0:5]#read first 5 lines
    firstNlines= list(map(lambda s: s.strip(), firstNlines))#strip newline characters 
    data_sect2=re.findall(r'[\w\.-]+@[\w\.-]+',data)#email regex
    email=str(data_sect2)  

    def entity_recog(text):
        l=""
        final_list=[] #final list of colleges
        # Change the path according to your system
        stanford_classifier = '/Users/continuumlabs/Desktop/stanford/stanford-ner-2016-10-31/classifiers/english.all.3class.distsim.crf.ser.gz'
        stanford_ner_path = '/Users/continuumlabs/Desktop/stanford/stanford-ner-2016-10-31/stanford-ner.jar'

        # Creating Tagger Object
        st = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')

        tokenized_text = word_tokenize(text)
        classified_text = st.tag(tokenized_text)
        for sublist in classified_text:
            if sublist[1]=='ORGANIZATION':
                l+=str(sublist[0])
                l+=" "
            elif sublist[1]=='LOCATION':
                l+=str(sublist[0])
                        
            elif sublist[0]=='.':
                final_list.append(l)
                l=""
        final_list=list(filter(None,final_list))
        return final_list

    college_list=entity_recog(c1)
    company_list=entity_recog(c2)
    for i in range(0,len(college_list)):
        for (x,y) in college_dict:
            if(x==college_list[i]):
                college_score=float(y)+college_score

 
    for i in range(0,len(company_list)):
        for (x,y) in company_dict:
            if(x==company_list[i]):
                company_score=float(y)+company_score

    company_score=(10*company_score)/len(company_list)
    college_score=(4*college_score)/len(college_list)
    skill_score=20*skill_score
    total_score=company_score+college_score+skill_score
 
 
    
print "Extracted Details:"          
print college_score
print company_score
#print (firstNlines)
print email
print "\nSCORE"
print skill_score#percent
print "Total Score" #out of 90
print total_score
#Average runtime:11.65
print time.time()-start



