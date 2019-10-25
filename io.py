#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:42:07 2019

@author: brett
"""
# user input
num = input ("Enter number :") 
print(num) 

x=input('enter the term of interest.')
x=x.lower()

 # file input output
 
 # open a file
f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode
f.close()

# read file line by line

import glob
files = glob.glob("test.txt")
for fname in files:
  with open(fname) as f: #file
     for line in f:
         print(line)
         
# read multiple files
def load_stops(stopwords,path):
 spath = path + "/*.txt"
 files = glob.glob(spath)
 for fname in files:
     with open(fname) as f: #file
         for line in f:
             load_line(line.strip().split(' '), stopwords)
             

def load_line(l_line, stopwords):
   for word in l_line:
       stopwords.insert(0,word.lower())


# makes all word in line lowercase
# implements stemming
# Updates word count in fname for every word
#
def line_proc(line, dict_terms,dict_docs,fname,stopwords):
   for word in line:
       w=word.lower()
       w=ps.stem(w)
       if w not in stopwords:
           dict_docs[fname] += 1
           if w in dict_terms:
               curterm= dict_terms[w]
               if curterm.existposting(fname):
                   curterm.incrdocfreq(fname)
               else:
                   curterm.insertposting(fname)
           else:
               postings={}
               postings[fname]=1
               t =term(1,postings)
               dict_terms[w] = t
