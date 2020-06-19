import sys
from subprocess import run # runs bash commands
sys.stdout = open('output.tex', 'w') # redirect output to file

def read_header():
    with open("header.tex") as g:
        for line in g:
            print(line, end='')

def parse_tex():
    is_enclosed=False # flag to ensure we only print relevant tex
    with open("example.tex") as f:
        for line in f:
            if any("begin"+str(el) in line for el in sys.argv): # we are at the beginning of relevant tex
                is_enclosed=True
            elif any("end"+str(el) in line for el in sys.argv): # we are at the end of relevant tex
                print(line)
                is_enclosed=False
            if is_enclosed: # we are within the relevant tex
                print(line,end='')

def write_tex():
    read_header() # gets any necessary packages, environments etc.
    print("\\begin{document}") # start of .tex file
    parse_tex() # prints the tex code we're interested in
    print("\\end{document}") # end of .tex file
    sys.stdout.close()

write_tex()

run(["pdflatex", "output.tex"]) # converts new .tex file to pdf
