#!/usr/bin/env python3
'''Test a human's ability to do mental squaring.'''

# python
import sys
from time import sleep
from random import random
# pyttsx
import pyttsx3

def main(nQuestions, nDigits, delay):
  '''Entrypoint to the program.'''

  # PARAMETERS =====================================================================================
  
  rate = 120
  
  # INITIALIZATION =================================================================================
  
  # RUN TEST =======================================================================================
  
  for question in range(nQuestions):
    
    x = 0
    while x <= 1: # prevent trivial questions
      x = int(10**nDigits*random())
      y = x * x
    
    speechEng = pyttsx3.init()
    speechEng.setProperty("rate", rate)
    speechEng.say(str(x) + " squared")
    speechEng.runAndWait()
    del speechEng
    sleep(delay)

    print("Question: {}. {}^2 = {}".format(question+1,x,y))    
    speechEng = pyttsx3.init()
    speechEng.setProperty("rate", rate)
    speechEng.say(str(y))
    speechEng.runAndWait()
    del speechEng
    input("Press [Enter] to continue...")
  
if __name__ == "__main__":
  '''Call main with the appropriate command line arguments.'''
  
  try:
    nQuestions = int(sys.argv[1])
    nDigits = int(sys.argv[2])
    delay = int(sys.argv[3])
  except:
    print("Usage: TestSquares.py nQuestions nDigits delay")
    exit()
  
  main(nQuestions, nDigits, delay)
  exit()