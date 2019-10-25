# TexScrape
Written for Linux.
Simple tool that parses some .tex file for specific keywords that are placed in \begin{} or \end{} (e.g. Theorem, Proof) and outputs a pdf of the paragraphs in between these keywords
E.g. if you have a set of Mathematics lecture notes written in LaTeX but you only want to see a list of the theorems, proofs, definitions, etc. then this will produce a pdf of such a list.

Usage
=====

python3 tex_scraper.py {k1} {k2} ... {kn}

Would produce a .pdf with all text that is included with \begin{ki} and \end{ki} for each i. 

Dependencies
===========
pdflatex,

File named "header.tex" that includes any packages, environments, etc. that you bave used in your .tex file. 
