import textcl
import dictionary
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
import github_scrapper

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
                        else:
                            return 0,0

            """work experience identification and score generation"""   
            def work_recog(self,text):
                    
                        print text
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
                            

                
    with open('/Users/continuumlabs/Desktop/stanford/rohit.txt', 'r') as f:
                
                data=f.read().splitlines()
                data = list(filter(None, data))
                data1=' '.join(data)
                #print data1
                work,edu,trivial=textcl.classify(data)
                work=" ".join(work)
                edu=" ".join(edu)
                trivial=" ".join(trivial)
                repos,followers,git_url,commits,gitlang=github_scrapper.gitScrape(trivial)

                """name recognition"""
                f.seek(0,0)
                firstNlines=f.readlines()[0:1]#read first line
                firstNlines= list(map(lambda s: s.strip(), firstNlines))#strip newline characters
                name=" ".join(firstNlines)

                e=eve()
                summary=""
                fs = FrequencySummarizer() 
                for s in fs.summarize(data1,5):
                        summary+=s
                
                email1= e.email_recog(trivial)
                email1=''.join(email1)
                degree1=e.degree_recog(edu)
                degree1=','.join(degree1)
                if(work):
                        company_score1,company=e.work_recog(work)
                else:
                        company_score1=0
                        company=0
                        job=0
                        duration=0
                final_col_list1,college_score1=e.college_recog(edu)
                final_col_list1=','.join(final_col_list1)
                comapny=','.join(company)
                gitlang=','.join(gitlang)
                
                print "EXTRACTED DETAILS"
                print name
                print email1
                print final_col_list1
                print degree1
                print college_score1
                print company
                print company_score1
                print repos,commits,followers,gitlang

            
            
            
           

