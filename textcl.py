import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
stemmer = LancasterStemmer()


# 3 classes of training data
training_data = []
training_data.append({"class":"edu", "sentence":"Bachelors degree Computer Science Indian Institue of Technology,Delhi"})
training_data.append({"class":"edu", "sentence":"Studied BTech Computer Science SCT College of Engineering"})
training_data.append({"class":"edu", "sentence":"MS Mechanical Engineering Rajagiri College of Technology"})
training_data.append({"class":"work", "sentence":"work experience 2 years 4 months"})
training_data.append({"class":"work", "sentence":"Served as Chief Technical Officer at Mindfox for 4 years"})
training_data.append({"class":"work", "sentence":"Worked TCS 5 years  Systems Engineer"})
training_data.append({"class":"work", "sentence":"Mindfox Google Linkedin"})

#New Added




training_data.append({"class":"edu", "sentence":"Bachelor's degree in Computer Science Georgia Institue of Technology- Atlanta,GA"})
training_data.append({"class":"edu", "sentence":"BA (Hons) Graphic Design from University of Birmingham"})
training_data.append({"class":"edu", "sentence":"Diploma in Business Studies Central College Birmingham"})
#training_data.append({"class":"edu", "sentence":"Diploma in Business Studies Central College of Birmiingham"})
#training_data.append({"class":"edu", "sentence":"Higher National Certificate (HNC) in Multimedia"})
#training_data.append({"class":"edu", "sentence":"Hignher National Certificate (HNC) in Multimedia"})
#training_data.append({"class":"edu", "sentence":"Qualification in Computer graphics: 3D Studio, Photoshop, Illustrator IATA (Namur, Belgium)"})
training_data.append({"class":"edu", "sentence":"Qualification in Computer graphics: 3D Studio, Photoshop, Illustrator IATA (Namur, Belgium)"})
training_data.append({"class":"edu", "sentence":"Bachelor of Engineering in Electronics and Communication in April 2003 from Coimbatore Institute of Technology, Coimbatore "})
#training_data.append({"class":"edu", "sentence":"Bachelor of Engineering in Electronics and Communication in April 2003 from Coimbatore Institute of Technology, Coimbatore"})
#training_data.append({"class":"edu", "sentence":"Purdue University College of Technology, Kokomo, In Bachelor of Science in Computer and Information Technology "})
#training_data.append({"class":"edu", "sentence":"Purdue University College of Technology, Kokomo In Bachelor of Science in Computer and Information Technology"})
#training_data.append({"class":"edu", "sentence":"Master's degree , Electronic engineering Military schoo for artillery and air defense (VVUAPVO)"})
#training_data.append({"class":"edu", "sentence":"Master's degree, Electronic engineering Military school for artillery and air defense"})
#training_data.append({"class":"edu", "sentence":"Majoring in Software Engineering (Diploma of Software Engineer) Academy of Management and Computer Training, St-Petersburg, Russia "})
#training_data.append({"class":"edu", "sentence":"Master's Degree in Economics (Russian Diploma of Economist - Organizer) St. Petersburg State Agrarian University, Faculty of Economics, St-Petersburg, Russia"})
#training_data.append({"class":"edu", "sentence":"Continuing Education Courses, University of Missouri at St. Louis"})
#training_data.append({"class":"edu", "sentence":"MSc Design and Digital Media, University of Edinburgh "})
#training_data.append({"class":"edu", "sentence":"Multimedia BA (Hons), Nottingham Trent University"})
#training_data.append({"class":"edu", "sentence":"PhD, School of Pharmacy and Pharmacology, University of Nottingham"})
#training_data.append({"class":"edu", "sentence":"MSc, Biochemical Pharmacology, University of Southampton"})
#training_data.append({"class":"edu", "sentence":"BSc (Hons), Applied Biology, University of Bath"})
#training_data.append({"class":"edu", "sentence":"BSc(Hons) Software Engineering Manchester Metropolitan University "})
#training_data.append({"class":"edu", "sentence":"PgDip Interactive Multimedia  Bath School Of Art And Design "})
#training_data.append({"class":"edu", "sentence":"Bachelor of Technology (Computer Science) National Institute of Technology Raipur"})
#training_data.append({"class":"edu", "sentence":"Seneca College, Toronto, ON Digital Media Arts Diploma Program"})
#training_data.append({"class":"edu", "sentence":"Sheridan College, Oakville, ON Web Design Graduate Certiﬁcate "})
#training_data.append({"class":"edu", "sentence":"Graduated with High Honours - Sheridan College "})



#training_data.append({"class":"work", "sentence":"Circus Strategic Communications Junior Web Developer "})
#training_data.append({"class":"work", "sentence":"Junior Web Developer at Circus Strategic Communication"})
#training_data.append({"class":"work", "sentence":"Pixel Junkie Inc. Web Developer "})
#training_data.append({"class":"work", "sentence":"Web Developer at Pixel Junkie Inc."})
#training_data.append({"class":"work", "sentence":"Digital-Minded Junior Flash Developer "})
#training_data.append({"class":"work", "sentence":"Digital Minded Junior Flash Developer"})
#training_data.append({"class":"work", "sentence":"Serving as Senior Data Analyst at Baidu,CA"})
#training_data.append({"class":"work", "sentence":"Beyond Education, London, UK. Backend Developer"})
#training_data.append({"class":"work", "sentence":"National Institute of Technology Raipur, Raipur, Chhattisgarh, India Developer – Student Marksheet Generator"})
#training_data.append({"class":"work", "sentence":"Asahi India Glass Limited (AIS) & Accenture, India Developer – AIS InfoBoard"})
#training_data.append({"class":"work", "sentence":"Front end Web Developer Google, London "})
training_data.append({"class":"work", "sentence":"Front End Developer at Google, London"})
"""training_data.append({"class":"work", "sentence":"Senior Web Coder / Designer Shelter, London"})
training_data.append({"class":"work", "sentence":"Faculty of Applied Sciences Web Developer Lancaster University v"})
training_data.append({"class":"work", "sentence":"Freelance Web development Pixel UK Ltd; E-scape Media Ltd."})
training_data.append({"class":"work", "sentence":"Web Developer Eunite Ltd (Zendor Group), Manchester; "})
training_data.append({"class":"work", "sentence":"Programmer/Research Assistant KINDS Project, Salford University"})
training_data.append({"class":"work", "sentence":"Founder, Portland Data Ltd "})
training_data.append({"class":"work", "sentence":"Senior Technology Transfer Manager, King's College London "})
training_data.append({"class":"work", "sentence":"PHP Developer (Contract), Adaptive Lab "})
training_data.append({"class":"work", "sentence":"Senior PHP Developer (Contract), Havas Worldwide"})
training_data.append({"class":"work", "sentence":"Technical Lead (Contract), MBA & Company "})
training_data.append({"class":"work", "sentence":"Senior PHP Developer (Contract), Amaze "})
training_data.append({"class":"work", "sentence":"Senior PHP Developer (Contract), MBA & Company"})
training_data.append({"class":"work", "sentence":"Back End Developer, SHOWstudio "})
training_data.append({"class":"work", "sentence":"CakePHP Developer, Moonrocket Interactive "})
training_data.append({"class":"work", "sentence":"PHP Developer, Abraxor "})
training_data.append({"class":"work", "sentence":"Developer Operations engineer W3C/MIT"})
training_data.append({"class":"work", "sentence":"JavaScript developer TEKsystems"})
training_data.append({"class":"work", "sentence":"Web developer at Ericsson"})
training_data.append({"class":"work", "sentence":"Web developer, co-founder Evocatio Solutions technologiques Inc"})
training_data.append({"class":"work", "sentence":"Web integrator Groupe Informatique TechSolCom Inc"})
training_data.append({"class":"work", "sentence":"Web integrator / PHP Developer Câble Axion Digitel Inc"})
training_data.append({"class":"work", "sentence":"Web integrator / PHP Developer Inexis solution web Inc"})
training_data.append({"class":"work", "sentence":"Internet Marketing Manager Graybar Electric Company, Inc"})
training_data.append({"class":"work", "sentence":"Web Developer Tacony Developer "})
training_data.append({"class":"work", "sentence":"Web Developer DeniServ"})
training_data.append({"class":"work", "sentence":"Web Developer Monsanto/Net Effects"})
training_data.append({"class":"work", "sentence":"Web Developer Brighton/Net Effects "})
training_data.append({"class":"work", "sentence":"Web Developer NextStart.com "})
training_data.append({"class":"work", "sentence":"Webmaster Skywalker Communications "})
training_data.append({"class":"work", "sentence":"FLASH ACCESSIBILITY CONSULTANT Freelance "})
training_data.append({"class":"work", "sentence":"INTERACTIVE TECHNOLOGY LEAD Modernista"})
training_data.append({"class":"work", "sentence":"SENIOR WEB DEVELOPER Houghton Mifflin Company"})
training_data.append({"class":"work", "sentence":"DEVELOPER/PROGRAMMER Red98 LLC"})
training_data.append({"class":"work", "sentence":"Freelance web developer, database programmer, application architect"})
training_data.append({"class":"work", "sentence":"WEBSTIK ltd Owner / Web developer "})
training_data.append({"class":"work", "sentence":"OSI Front End developer"})
training_data.append({"class":"work", "sentence":"Mansion Productions Web Developer"})
training_data.append({"class":"work", "sentence":"REXINTEGRA UI/UX Developer "})
training_data.append({"class":"work", "sentence":"Promega Corporation, Indianapolis, IN Web DeveloperSGate Entertainment, Indianapolis, IN Web Developer"})
training_data.append({"class":"work", "sentence":"SapientNitro Senior interactive develope"})
training_data.append({"class":"work", "sentence":"Endice Software  Senior web developer"})
training_data.append({"class":"work", "sentence":"U&CO Founder & developer "})
training_data.append({"class":"work", "sentence":"Mountainview Technical lead"})
training_data.append({"class":"work", "sentence":"I have worked regularly as a remote Drupal Developer for Vancouver-based Drupal shop, ImageX Media "})
training_data.append({"class":"work", "sentence":"Web Design Company - Birmingham WEB DEVELOPER "})
training_data.append({"class":"work", "sentence":"SEO Company - Coventry   TRAINEE WEB DEVELOPER "})
training_data.append({"class":"work", "sentence":"Office Assistant - Caplan Industries"})
training_data.append({"class":"work", "sentence":"Web Developer Business Alternatives, Eugene, OR"})
training_data.append({"class":"work", "sentence":"Web instructor Mania Marketing, Eugene, OR"})
training_data.append({"class":"work", "sentence":"Salesforce – Atlanta, GA UX Engineer"})
training_data.append({"class":"work", "sentence":"POP – Seattle, WA Senior Interactive Developer"})
training_data.append({"class":"work", "sentence":"Amazon – Seattle, WA Software Development Engineer"})
training_data.append({"class":"work", "sentence":"CareerBuilder – Norcross, GA Senior Software Engineer"})
training_data.append({"class":"work", "sentence":"Turner Broadcasting – Atlanta, GA Advanced Software Developer"})
training_data.append({"class":"work", "sentence":"CareerBuilder – Norcross, GA Senior Software Engineer"})
training_data.append({"class":"work", "sentence":"Objectware – Norcross, GA Web Developer "})



training_data.append({"class":"skills", "sentence":"Agile Methodology, Responsive Web Design, Browser Performance, Mobile Web, Accessibility, Ajax, Unit Testing, MV*, Android App Development, Preprocessors "})
training_data.append({"class":"skills", "sentence":"JavaScript (native, Ember, Backbone, Node, jQuery), HTML, CSS, SVG, Sass, Less, Grunt, Gulp, ASP.NET (Web Forms, MVC), C#, Visual Basic, Java, PHP, SQL, Regex  "})
training_data.append({"class":"skills", "sentence":"Source Control (Git, TFS, SVN), Photoshop, Illustrator, Visual Studio, Eclipse, Heroku, WordPress, Google Analytics "})
training_data.append({"class":"skills", "sentence":"Planned, developed and published multi-page web sites "})
training_data.append({"class":"skills", "sentence":"Planned, developed and published multi-page web sites "})

#New Ended"""


training_data.append({"class":"trivial", "sentence":"Was part of college drama team"})
training_data.append({"class":"trivial", "sentence":"Projects Seminars Internships"})
training_data.append({"class":"trivial", "sentence":"Address email github linkedin"})
training_data.append({"class":"trivial", "sentence":"Was part of cricket team football team"})



print ("%s sentences in training data" % len(training_data))


words = []
classes = []
documents = []
ignore_words = ['?']
# loop through each sentence in our training data
for pattern in training_data:
    # tokenize each word in the sentence
    w = nltk.word_tokenize(pattern['sentence'])
    # add to our words list
    words.extend(w)
    # add to documents in our corpus
    documents.append((w, pattern['class']))
    # add to our classes list
    if pattern['class'] not in classes:
        classes.append(pattern['class'])

# stem and lower each word and remove duplicates
#words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
#words = list(set(words))

# remove duplicates
classes = list(set(classes))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)


# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    training.append(bag)
    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    output.append(output_row)

print ("# words", len(words))
print ("# classes", len(classes))

# sample training/output
i = 0
w = documents[i][0]
print (w)
print (training[i])
print (output[i])

import numpy as np
import time

# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)
 
def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    #sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

def think(sentence, show_details=False):
    x = bow(sentence.lower(), words, show_details)
    if show_details:
        print ("sentence:", sentence, "\n bow:", x)
    # input layer is our bag of words
    l0 = x
    # matrix multiplication of input and hidden layer
    l1 = sigmoid(np.dot(l0, synapse_0))
    # output layer
    l2 = sigmoid(np.dot(l1, synapse_1))
    return l2


    # ANN and Gradient Descent code from https://iamtrask.github.io//2015/07/27/python-network-part2/
def train(X, y, hidden_neurons=10, alpha=1, epochs=50000, dropout=False, dropout_percent=0.5):

    print ("Training with %s neurons, alpha:%s, dropout:%s %s" % (hidden_neurons, str(alpha), dropout, dropout_percent if dropout else '') )
    print ("Input matrix: %sx%s    Output matrix: %sx%s" % (len(X),len(X[0]),1, len(classes)) )
    np.random.seed(1)

    last_mean_error = 1
    # randomly initialize our weights with mean 0
    synapse_0 = 2*np.random.random((len(X[0]), hidden_neurons)) - 1
    synapse_1 = 2*np.random.random((hidden_neurons, len(classes))) - 1

    prev_synapse_0_weight_update = np.zeros_like(synapse_0)
    prev_synapse_1_weight_update = np.zeros_like(synapse_1)

    synapse_0_direction_count = np.zeros_like(synapse_0)
    synapse_1_direction_count = np.zeros_like(synapse_1)
        
    for j in iter(range(epochs+1)):

        # Feed forward through layers 0, 1, and 2
        layer_0 = X
        layer_1 = sigmoid(np.dot(layer_0, synapse_0))
                
        if(dropout):
            layer_1 *= np.random.binomial([np.ones((len(X),hidden_neurons))],1-dropout_percent)[0] * (1.0/(1-dropout_percent))

        layer_2 = sigmoid(np.dot(layer_1, synapse_1))

        # how much did we miss the target value?
        layer_2_error = y - layer_2

        if (j% 10000) == 0 and j > 5000:
            # if this 10k iteration's error is greater than the last iteration, break out
            if np.mean(np.abs(layer_2_error)) < last_mean_error:
                print ("delta after "+str(j)+" iterations:" + str(np.mean(np.abs(layer_2_error))) )
                last_mean_error = np.mean(np.abs(layer_2_error))
            else:
                print ("break:", np.mean(np.abs(layer_2_error)), ">", last_mean_error )
                break
                
        # in what direction is the target value?
        # were we really sure? if so, don't change too much.
        layer_2_delta = layer_2_error * sigmoid_output_to_derivative(layer_2)

        # how much did each l1 value contribute to the l2 error (according to the weights)?
        layer_1_error = layer_2_delta.dot(synapse_1.T)

        # in what direction is the target l1?
        # were we really sure? if so, don't change too much.
        layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)
        
        synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
        synapse_0_weight_update = (layer_0.T.dot(layer_1_delta))
        
        if(j > 0):
            synapse_0_direction_count += np.abs(((synapse_0_weight_update > 0)+0) - ((prev_synapse_0_weight_update > 0) + 0))
            synapse_1_direction_count += np.abs(((synapse_1_weight_update > 0)+0) - ((prev_synapse_1_weight_update > 0) + 0))        
        
        synapse_1 += alpha * synapse_1_weight_update
        synapse_0 += alpha * synapse_0_weight_update
        
        prev_synapse_0_weight_update = synapse_0_weight_update
        prev_synapse_1_weight_update = synapse_1_weight_update

    now = datetime.datetime.now()

    # persist synapses
    synapse = {'synapse0': synapse_0.tolist(), 'synapse1': synapse_1.tolist(),
               'datetime': now.strftime("%Y-%m-%d %H:%M"),
               'words': words,
               'classes': classes
              }
    synapse_file = "synapses.json"

    with open(synapse_file, 'w') as outfile:
        json.dump(synapse, outfile, indent=4, sort_keys=True)
    print ("saved synapses to:", synapse_file)

X = np.array(training)
y = np.array(output)

start_time = time.time()

train(X, y, hidden_neurons=20, alpha=0.1, epochs=100000, dropout=True, dropout_percent=0.3)

elapsed_time = time.time() - start_time
print ("processing time:", elapsed_time, "seconds")


# probability threshold
ERROR_THRESHOLD = 0.7
# load our calculated synapse values
synapse_file = 'synapses.json' 
with open(synapse_file) as data_file: 
    synapse = json.load(data_file) 
    synapse_0 = np.asarray(synapse['synapse0']) 
    synapse_1 = np.asarray(synapse['synapse1'])

def classify(text, show_details=False):
    work=[]
    edu=[]
    trivial=[]
    zero=[]
    for sentence in text:
        
        results = think(sentence, show_details)

        results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD ] 
        results.sort(key=lambda x: x[1], reverse=True) 
        return_results =[[classes[r[0]],r[1]] for r in results]
        print ("%s \n classification: %s" % (sentence, return_results))
        if not return_results:
            trivial.append(sentence)
        for x,y in return_results:
            if x=='work':
                work.append(sentence)
            elif x=='edu':
                edu.append(sentence)
            elif x=='trivial':
                trivial.append(sentence)
           
        
    return work,edu,trivial

#classify("sudo make me a sandwich")

#c=classify("I have experience with python")
#classify("I have experience with html")
#classify("who are you?")
#classify("make me some lunch")
#print (c)

#classify("how was your lunch?", show_details=True)

