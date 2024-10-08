# various imports
#from IPython.display import display, Markdown, Latex
#from random import *
import numpy as np
import sigfig as sf
#from numpy.random import random

# generates exam as a markdown file
#! LaTeX version
# randomizes answer order
# WIP randomizes answer values
# TODO randomizes question order

# Any markdown code may be written to the output file, e.g. to insert LaTeX code or images, etc.

# The random seed goes here.  Change this value to generate new exam versions.

# prefix for output filenames
outputfolder = "output/"
fileprefix = outputfolder+"exam_"

# Seeds for this exam
examlist = [
['A', 1],
['B', 2],
['C', 3],
['D', 4]
]

#! You must manually set the exam version indication:
# TODO make this a loop
thisversionnumber=0
thisexam=examlist[thisversionnumber]
exam_version=thisexam[0]
rng=np.random.default_rng(seed=thisexam[1])

# Do you want to print the key at the end of the output file?
#printkey = True
qshuffle=True
#! Check that the list below contains the correct number of questions
# Reminder: counting starts from zero
question_groups=[[0,1]]#[[0,1,[2,3],4,5],[6,7,8,9,10],[11,12,13,14,15]]

def print_answers(alist):
    '''
    Returns the answer block as a string and the index of the correct answer.
    alist = list of answers, with the correct answer first
    '''
    alphabet = "ABCDE"
    order = rng.permutation(len(alist))
    correct = np.argmin(order)
    output = r"\begin{choices}"+"\n"
    for i in range(len(alist)):
        if i == correct:
            output=output+(r"\CorrectChoice "+alist[order[i]]+"\n")
        else:
            output=output+(r"\choice "+alist[order[i]]+"\n")
    output = output+r"\end{choices}"+"\n"
    return output, correct

alphabet = "ABCDE"

# Showing how to print significant figures
#thisval = np.power(10,6.0*(rng.random(7)-0.5))
#
#print("Random number rounding test")
#print(thisval)
#print([sf.round(i,sigfigs=2,output_type=str) for i in thisval])

# Each question is stored as a string consisting of the question text and the answer block.
# each question is then appended to the list `qlist`
# At the end these strings are shuffled and written to the output file

qlist = [] # empty list to store the question strings
keylist = [] # empty list to store the answer key strings
qcount = 0 # count questions

def addquestion(q,al,pretext=""):
    global qcount
    qcount=qcount+1
    atext, key = print_answers(al)
    qlist.append(pretext+r"% Q"+f"{qcount}\n"+r"\question "+q+"\n"+atext)
    keylist.append(alphabet[key])

# helpers for rounding, including explicit sign in string reps.

def round2(x,plus=False):
    if x>=0. and plus:
        s = "+"+sf.round(x,2,output_type=str)
    else:
        s = sf.round(x,2,output_type=str)
    return s

def round3(x,plus=False):
    if x>=0. and plus:
        s = "+"+sf.round(x,3,output_type=str)
    else:
        s = sf.round(x,3,output_type=str)
    return s

def dec1(x,plus=False):
    if x>=0. and plus:
        s = "+"+sf.round(x,decimals=1,output_type=str)
    else:
        s = sf.round(x,decimals=1,output_type=str)
    return s

def dec2(x,plus=False):
    if x>=0. and plus:
        s = "+"+sf.round(x,decimals=2,output_type=str)
    else:
        s = sf.round(x,decimals=2,output_type=str)
    return s

def dec3(x,plus=False):
    if x>=0. and plus:
        s = "+"+sf.round(x,decimals=3,output_type=str)
    else:
        s = sf.round(x,decimals=3,output_type=str)
    return s
def sci2(x,plus=False):
    if x>=0. and plus:
        s = "+"+sf.round(x,2,notation='sci')
    else:
        s = sf.round(x,2,notation='sci')
    return s

def sci3(x,plus=False):
    if x>=0. and plus:
        s = "+"+sf.round(x,3,notation='sci')
    else:
        s = sf.round(x,3,notation='sci')
    return s


headertext = r'''
\include{header1.tex}
% Define the following to propagate the title, author, etc. through the titlepage and headers
\newcommand{\mytitle}{Exam XXX - '''+\
f'Form {exam_version}'+\
r'''} % exam name
\newcommand{\myauthor}{XXX} % course name
\newcommand{\mydate}{XXX} % exam date

\include{header2.tex}
'''

# insert footer sheets
footertext = r'''
\include{footer.tex}
\end{document}
'''

######################
# The questions
# Specify where to break section blocks above in question_groups

# Question 1
qtext='''\
This is a basic question text block.  What is the first letter of the English alphabet?
'''

thisalist=[
    "a",
    "x",
    "d",
    "z",
    "j"]

addquestion(qtext,thisalist)

# Question 1

# Some constants for the following question.
# Note that these can be randomized, but it is up to the user to check that
# the values are feasible.

a = 3.0 + rng.uniform(-1,1)
b = 4.0 + rng.uniform(-2,2)

# below is an example showing some raw LaTeX and formatted strings.
# Be careful if you need to escape characters, e.g. \ and { in LaTeX code.
# using sections of r'' strings + f'' strings might be helpful.

# some rounding functions are defined above for convenience.

qtext=r'The perpendicular legs of a right triangle have lengths $a='+f'{round2(a)}'+r'\,\mathrm{m}$ and $b='+f'{round2(b)}'+r'\,\mathrm{m}$.  What is the length of the hypotenuse?'

# here are some calculated answer choices.  The first entry is the correct answer
thisalist=[
    f"${round2(np.sqrt(a**2+b**2))}"+r"\,\mathrm{m}$",
    f"${round2(a+b)}"+r"\,\mathrm{m}$",
    f"${round2(np.sqrt(np.abs(b**2-a**2)))}"+r"\,\mathrm{m}$",
    f"${round2(0.5*a*b)}"+r"\,\mathrm{m^2}$",
    f"${round2(np.arctan(b/a)*180./np.pi)}"+r"^\circ$"]

addquestion(qtext,thisalist)

# Done with the data

def flatten(lis):
    flatList = []
    # Iterate with outer list
    for element in lis:
        if type(element) is list:
            # Check if type is list than iterate through the sublist
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList

#for thisexam in examlist:
if True:
    #rng=np.random.default_rng(seed=thisexam[1])
    fileout = fileprefix+thisexam[0]+".tex"
    keyout = fileprefix+thisexam[0]+"_key.txt"

    # question order
    if qshuffle:
        for i, batch in enumerate(question_groups):
            #print(batch)
            if len(batch)==1:
                continue # do nothing if the group has only one question
            rng.shuffle(batch)
        qorder=(flatten(flatten(question_groups)))
    else:
        qorder = list(range(len(qlist)))
    
    # begin output
    with open(fileout, "w") as f:
        # TODO check breaks between writes
        # Write the header
        f.write(headertext)
    
        f.write(r'\begin{questions}'+"\n")
        # Write the questions
        
        for q in range(len(qlist)):
            #f.write(f"{q+1}.  ")
            f.write(qlist[qorder[q]])
            f.write("\n"+r"\vspace*{\stretch{1}}"+"\n") # space between questions
            if q % 2 == 1: # newpage after even questions (counting starts at 0)
                f.write(r"\newpage{}"+"\n")
    
        # Write the key
        # TODO format this better
        f.write(r'''
\end{questions}
''')
        if True:
            f.write(r'''
\ifprintanswers
\newpage{} 

\section*{Answer Key for Form '''
+f'{exam_version}'+r'''}

\begin{enumerate}
''')
            for k in range(len(keylist)):
                f.write(r"\item "+f"{keylist[qorder[k]]} \n")
            f.write(r'\end{enumerate}'+"\n"+r'\fi'+"\n")
            print("Answers: ",[keylist[i] for i in qorder])
        # Write the footer
        f.write(footertext)
    
    with open(keyout, "w") as f:
        f.write(f"Key for Form {thisexam[0]}\n")
        f.write( "--------------\n")
        for n, i in enumerate(qorder):
            f.write(f"{n+1}:\t{keylist[i]}\n")

# debug
#print(keylist)
