# TexScrape
CLI tool written for Linux, though if you're a Windows user you can compile it using 'Ubuntu on Windows'.
TexScrape parses a given .tex file for specific keywords that are placed between \begin{} or \end{} (e.g. Theorem in \begin{theorem}...\end{theorem}) and outputs a pdf of the paragraphs in between these keywords. E.g. if you have a set of Mathematics lecture notes written in LaTeX but you only want to see a list of the theorems, proofs, definitions, etc. then this will produce a pdf of such a list.

Usage
=====

python3 texscrape.py {k1} {k2} ... {kn}

This produces two files, "output.tex" and "output.pdf". The .tex file is the relevant LaTeX that has been produced by the tool.

Dependencies
============
pdflatex

File named "header.tex" that includes any packages, environments, etc. that you have used in your .tex file. 
