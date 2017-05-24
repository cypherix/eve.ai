import textcl
import skillcl
import dictionary
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
import apiai,itertools
import json,re
from nltk.tokenize import sent_tokenize
from collections import defaultdict
from string import punctuation
from heapq import nlargest
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import github_scrapper
import string
from nameparser import HumanName
from collections import OrderedDict

class FrequencySummarizer:
                  def __init__(self, min_cut=0.1, max_cut=0.9):
                    """
                     Initilize the text summarizer.
                     Words that have a frequency term lower than min_cut 
                     or higer than max_cut will be ignored.
                    """
                    self._min_cut = min_cut
                    self._max_cut = max_cut 
                    self._stopwords = set(stopwords.words('english') + list(punctuation))

                  def _compute_frequencies(self, word_sent):
                    """ 
                      Compute the frequency of each of word.
                      Input: 
                       word_sent, a list of sentences already tokenized.
                      Output: 
                       freq, a dictionary where freq[w] is the frequency of w.
                    """
                    freq = defaultdict(int)
                    for s in word_sent:
                      for word in s:
                        if word not in self._stopwords:
                          freq[word] += 1
                    # frequencies normalization and fitering
                    m = float(max(freq.values()))
                    for w in freq.keys():
                      freq[w] = freq[w]/m
                      if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
                        del freq[w]
                    return freq

                  def summarize(self, text, n):
                    """
                      Return a list of n sentences 
                      which represent the summary of text.
                    """
                    sents = sent_tokenize(text)
                    assert n <= len(sents)
                    word_sent = [word_tokenize(s.lower()) for s in sents]
                    self._freq = self._compute_frequencies(word_sent)
                    ranking = defaultdict(int)
                    for i,sent in enumerate(word_sent):
                      for w in sent:
                        if w in self._freq:
                          ranking[i] += self._freq[w]
                    sents_idx = self._rank(ranking, n)    
                    return [sents[j] for j in sents_idx]

                  def _rank(self, ranking, n):
                    """ return the first n sentences with highest ranking """
                    return nlargest(n, ranking, key=ranking.get)

class eve:
               
        """NER Function"""
        def entity_recog(self,text):
                l=""
                name=[]
                final_list=[] #final list of colleges
                # Change the path according to your system
                stanford_classifier = '/Users/continuumlabs/Desktop/stanford/stanford-ner-2016-10-31/classifiers/english.all.3class.distsim.crf.ser.gz'
                stanford_ner_path = '/Users/continuumlabs/Desktop/stanford/stanford-ner-2016-10-31/stanford-ner.jar'

                # Creating Tagger Object
                st = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')

                tokenized_text = word_tokenize(text)
                classified_text = st.tag(tokenized_text)
                #print classified_text
                
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
                #print final_list
                return final_list

        """Not Used Anymore!!!!
        API.AI Caller Function
        def APII(self,text):
            CLIENT_ACCESS_TOKEN = 'ed1ad45b4498400bad421d21091a8065'
            ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

            request = ai.text_request()

            request.lang = 'en'  # optional, default value equal 'en'

            #request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

            request.query = text

            response = request.getresponse()
            responsestr = response.read().decode('utf-8')
            response_obj = json.loads(responsestr)
            if(response_obj['result']["metadata"]["intentName"]=='work_exp'):
                    
                    company=response_obj["result"]["parameters"]["company"]
                    duration=response_obj["result"]["parameters"]["duration"]
                    job_title=response_obj["result"]["parameters"]["jobposts"]
                    return company,job_title,duration
            else:
                    return 0,0,0"""
        

        """degree extraction"""
        def email_recog(self,text):
   
                    email=re.findall(r'[\w\.-]+@[\w\.-]+',text)#email regex
                    email=str(email)
                    return email


            
        """phone number extraction"""
        def phone_extract(self, text):
            import re
            f=text
            number=[]
            for line in f:
                x=line
                match=re.findall("[+]\d{12}|\d{10}",x)
                if (match):
                    #print match
                    number.append(match)
                else:
                    match=re.findall("\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}",x)
                    if (match):
                        #print match
                        number.append(match)
            """for i in number:
                for j in i:
                    print j"""
            return number
        
        """degree extraction"""
        def degree_recog(self,text):
            main=text
            course_list=[]
            course1=[]
            degree=[]
            secondary=["College","University","Institute","School"]
            sen=[x for x in main if any(x in y or y in x for y in secondary)]
            #print main
            #print sen
            degree_list1=["BTech","Bachelors","MTech","Masters","MS","BS"]
            f=open('/Users/continuumlabs/Desktop/stanford/Btech.txt','r')
            for line in f:
                course_list.append(line.strip())
            for i in sen:
                temp=0
                stop_words=set(stopwords.words('english'))
                i=i.translate(None, string.punctuation)
                #print i
                list1=[k for k in wordpunct_tokenize(i) if k  not in stop_words]
                #print list1
                for l in list1:
                    for j in degree_list1:
                        c=fuzz.partial_ratio(l,j)
                        #print l,j,c
                        if(c>95):
                           degree.append(j)
                bi_gram=nltk.trigrams(list1)
                for x in bi_gram:
                    test=" ".join(x)
                    for z in course_list:
                        c=fuzz.partial_ratio(test,z)
                        #print test,z,c
                        if(c>temp):
                            temp=c
                            course=z
                course1.append(course)
                
                        
                        
                
            #print degree,course1
            degree_course=zip(degree,course1)
            #print degree_course
            return degree_course
        
        """def skill_validation_engine(self,text1):
                    c2=text1.lower()
                    #print c2
                    stop_words=set(stopwords.words('english'))
                    stop_words=set(string.punctuation)
                    resume1=[i for i in wordpunct_tokenize(c2) if i  not in stop_words]
                    print "Skills in resume:"
                    resume_list=list(set(resume1))#removes duplicates
                    skill_list=[i for i in resume_list if i in dictionary.skill_dict] #compare skills in resume and the skill dictionary
                    print resume_list
                    print "Identified skills"
                    print skill_list
                    print len(skill_list)
                    skill_match=[]

                    jd=["html","ml","php"]#jd
                    print "\nJD skills "
                    print jd
                    len_jd=len(jd)
                    ##append frameworks to new jd list
                    jd1=jd
                    for i in range(0,len(jd)):
                     for (x,y) in dictionary.frameworks:
                      if(x==jd[i]):
                       jd1.append(y)
                    print "JD skills after processing"
                    print jd1
                    print len(jd1)
                ##search for skills in the new jd list but use old jd list for score calculation
                    for i in range(0,len(jd1)):
                        for j in range(0,len(skill_list)):
                            if(jd1[i]==skill_list[j]):
                                skill_match.append(skill_list[j])
                    print "\nMatching skill set:"
                    print skill_match
                    print len(skill_match)

                    #score generation
                    len_skill_match=len(skill_match)
                    len_skill_list=len(skill_list)
                    if(len_skill_list >0):
                        Precision=float(len_skill_match)/len_skill_list
                        print Precision
                    else:
                        Precision=0
                        
                    print len_jd
                    Recall=float(len_skill_match)/len_jd
                    print Recall
                    if ((Precision + Recall)!=0):
                        skill_score= 2*((Precision*Recall)/(Precision+Recall))
                    else:
                        skill_score=0
                    return skill_score """   
            


        """college identification and score generation"""
        def college_recog(self,text):
                
                    college_list=self.entity_recog(text)
                    college_score=0.0
                    final_col_list=[]
                    if(college_list):
                            
                            """for i in range(0,len(college_list)):
                                for (x,y) in dictionary.college_dict:
                                    if(college_list[i]==x):
                                        college_score=float(y)+college_score
                                        final_col_list.append(x)
                            college_score=(4*college_score)/len(final_col_list) #Logical error
                            #return final_col_list,college_score"""
                            secondary=["College","University","Institute","School"]
                            college_list=[x for x in college_list if any(x in y or y in x for y in secondary)]
                            return college_list
                    else:
                        return 0,0

        """work experience identification and score generation"""   
        def work_recog(self,text):
                
                    #print text
                    company_score=0.0
                    company_names=[]
                    company_list2=[]
                    processed_company_list=[]
                    if(text):
                                 
                                #comp,job,dur= self.APII(text)
                                company_list=self.entity_recog(work)
                                for (x,y) in dictionary.company_score:
                                    company_list2.append(x)
                                for i in itertools.product(company_list, company_list2):
                                        company_names.append(i)
                                for (x,y) in company_names:
                                        c=fuzz.partial_ratio(*(x,y))
                                        if(c>90):
                                                processed_company_list.append(y)

                                if(processed_company_list):
                                    
                                    for i in range(0,len(processed_company_list)):
                                     for (x,y) in dictionary.company_score:
                                        if(x==processed_company_list[i]):
                                          company_score=float(y)+company_score
                                    #print company_score
                                    company_score=(10*company_score)/len(processed_company_list)
                                    return company_score,processed_company_list
                                else:
                                    return 0,0
                        

            
with open('/Users/continuumlabs/Desktop/stanford/Livinnatious.txt', 'r') as f:
            
            data=f.read().splitlines()
            data = list(filter(None, data))
            data1=' '.join(data)
            #print data1
            work,edu,trivial=textcl.classify(data)
            skill,trivial2=skillcl.classify(trivial)
            work=" ".join(work)
            edu1=edu
            edu=" ".join(edu)
            trivial=" ".join(trivial)
            skill=" ".join(skill)
            repos,followers,git_url,commits,gitlang=github_scrapper.gitScrape(trivial)
            
            """name recognition"""
            f.seek(0,0)
            firstNlines=f.readlines()[0:1]#read first line
            firstNlines= list(map(lambda s: s.strip(), firstNlines))#strip newline characters
            name=" ".join(firstNlines)
            name=HumanName(name)
   

            e=eve()
            summary=""
            fs = FrequencySummarizer() 
            for s in fs.summarize(data1,5):
                    summary+=s
            
            email1= e.email_recog(trivial)
            number=e.phone_extract(data)
            #skill_score=e.skill_validation_engine(skill)
            email1=''.join(email1)
            if(work):
                    company_score1,company=e.work_recog(work)
            else:
                    company_score1=0
                    company=0
                    job=0
                    duration=0
            #final_col_list1,college_score1=e.college_recog(edu)
            final_col_list=e.college_recog(edu)
            degree1=e.degree_recog(edu1)
            #final_col_list2=','.join(final_col_list1)
            """if(company):
                company=','.join(company)
            if(gitlang):
                gitlang=','.join(gitlang)"""
            
            print "EXTRACTED DETAILS"
            """print name
            print email1
            print final_col_list2
            #print degree1
            print college_score1
            print company
            print company_score1
            print repos,commits,followers,gitlang
            print skill
            print skill_score
            print edu
            print work
            print trivial
            print name.first,name.middle,name.last
            print degree1
            print final_col_list
            print company
            print number
            print email1
            print repos,commits,followers,gitlang
            print summary
            print skill"""

            json_payload={'name':{'first name':name.first,'middle name':name.middle,'last name':name.last},'number':number,'education':{'degree':degree1,'college':final_col_list},'work experience':company,'skills':skill,'github data':{'url':git_url,'followers':followers,'repos':repos,'commits':commits,'languages':gitlang},'resume summary':summary}
            print json_payload
            #print json.dumps(OrderedDict(json_payload))
        

            
            
            
           

