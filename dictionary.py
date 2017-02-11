import nltk.corpus
from nltk.corpus import wordnet
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string


university=("I have graduated from University of Illinois-Urbana-Champaign")

#Dictionary containing universities' ratings

exDict={"Carnegie Mellon University":5.0,"Massachusetts Institute of Technology":5.0,"Stanford University":5.0,"University of California-Berkeley":5.0,"University of Illinois-Urbana-Champaign":4.6,"Cornell University":4.5,"University of Washington":4.5,"Princeton University":4.4,"Georgia Institute of Technology":4.3,"University of Texas-Austin":4.3,"California Institute of Technolgy":4.2,
      "University of Wisconsin-Madison":4.2,"University of California-Los Angeles":4.1,"University of Michigan-Ann Arbor":4.1,"Columbia University":4.0,"University of California-SanDiego":4.0,"University of Maryland—​College Park":4.0,
      "Harvard University":3.9,"University of Pennsylvania":3.8,"Brown University":3.7,"Purdue University-West Lafayette":3.7,"Rice University":3.7,"University of Southern California":3.7,"Yale University":3.7,"Duke University":3.6,"University of Massachusetts-Amherst":3.6,"University of North Carolina-Chapel Hill":3.6,"Johns Hopkins University":3.5,"New York University":3.4,"Pennsylvania State University-University Park":3.4,
      "University of California-Irvine":3.4,"University of Minnesota-Twin Cities":3.4,"University of Virginia":3.4,"Northwestern University":3.3,"Ohio State University":3.3,"Rutgers , The State University of New Jersey-New Brunswick":3.3,"University of California-Davis":3.3,"University of California-Santa Barbara":3.3,"University of Chicago":3.3,"Dartmouth College":3.1,"Stony Brook University-SUNY":3.1,
      "Texas A & M University-College Station":3.1,"University of Arizona":3.1,"University of Colarado-Boulder":3.1,"University of Utah":3.1,"Virginia Tech":3.1,"Washington University St. Louis":3.1,"Arizona State University":3.0}

stop_words=set(stopwords.words('english'))

words=word_tokenize(university)

filtered_sentence=[]

stop_words.remove("of")


# Remove stop words

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

list1=[]  
     
print(filtered_sentence)
for word in filtered_sentence:
    if word[0].isupper() or word=='of' or word=="," or word=="&":
        list1.append(word)
list1.remove("I")
x=" ".join(list1)
#print(x)
print(exDict[x])
