import textcl
import dictionary
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
import apiai,itertools
import json,re

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

        """API.AI Caller Function"""
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
                    return 0,0,0
        

        """degree extraction"""
        def email_recog(self,text):
   
                    email=re.findall(r'[\w\.-]+@[\w\.-]+',text)#email regex
                    email=str(email)
                    return email


        """degree extraction"""
        def degree_recog(self,text):
                
                    if re.findall(r'\b(([\w]+[.][\w]+)([.][\w])*)',text):
                                degree=re.findall(r'\b(([\w]+[.][\w]+)([.][\w])*)',text)
                                degree=map(list,degree)
                                degree1=filter(None,list(set(itertools.chain.from_iterable(degree))))
                                return degree1


        """college identification and score generation"""
        def college_recog(self,text):
                
                    college_list=self.entity_recog(text)
                    college_score=0.0
                    final_col_list=[]
                    if(college_list):
                            
                            for i in range(0,len(college_list)):
                                for (x,y) in dictionary.college_dict:
                                    if(college_list[i]==x):
                                        college_score=float(y)+college_score
                                        final_col_list.append(x)
                            college_score=(4*college_score)/len(final_col_list) #Logical error
                            return final_col_list,college_score

        """work experience identification and score generation"""   
        def work_recog(self,text):
                
                    print text
                    company_score=0.0
                    if(text):
                                comp,job,dur= self.APII(text)
                                #company_list=entity_recog(work)
                                for i in range(0,len(comp)):
                                 for (x,y) in dictionary.company_dict:
                                    if(x==comp[i]):
                                      company_score=float(y)+company_score
                                      samp=dur[i]['amount'] #BUGS
                                        
                                      if (samp<2):
                                          dur_score=1
                                      elif (samp >=2 and samp< 5):
                                          dur_score=2
                                      elif (samp >= 5 and samp< 7):
                                        dur_score=3
                                      elif (samp >=7 and samp< 9):
                                        dur_score=4
                                      elif (samp>=9):
                                        dur_score=5
                                      else:
                                        dur_score=1
                                      #print "duration score"
                                      #print dur_score
                                      #print dur[i]
                                      company_score=company_score +float(dur_score)
                                     
                                #print company_score
                                company_score=(5*company_score)/len(comp)
                                return company_score,comp,job,dur
                        

            
with open('/Users/continuumlabs/Desktop/stanford/rohit.txt', 'r') as f:
            
            data=f.read().splitlines()
            data = list(filter(None, data))
            data1=' '.join(data)
            #print data1
            work,edu,trivial=textcl.classify(data)
            work=" ".join(work)
            edu=" ".join(edu)
            trivial=" ".join(trivial)
            """name recognition"""
            f.seek(0,0)
            firstNlines=f.readlines()[0:1]#read first line
            firstNlines= list(map(lambda s: s.strip(), firstNlines))#strip newline characters
            name=" ".join(firstNlines)

            e=eve()
            email1= e.email_recog(trivial)
            degree1=e.degree_recog(edu)
            if(work):
                    company_score1,company,job,duration=e.work_recog(work)
            else:
                    company_score1=0
                    company=0
                    job=0
                    duration=0
            final_col_list1,college_score1=e.college_recog(edu)
            
            print "EXTRACTED DETAILS"
            print name
            print email1
            print final_col_list1
            print degree1
            print college_score1
            print company
            print job
            print duration
            print company_score1
            print "work experience"
            print work
            #print comp,job,dur
            print "education"
            print edu
            #print college_list1
            print "Trivial"
            print trivial
            
            
            
           

