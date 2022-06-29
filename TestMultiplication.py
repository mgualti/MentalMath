#!/usr/bin/env python3
'''Test a human's ability to do mental multiplication.'''

# python
import sys
from time import sleep
from random import random
# pyttsx
import pyttsx3

def main(nQuestions, nDigitsTop, nDigitsBottom, delay):
  '''Entrypoint to the program.'''

  # PARAMETERS =====================================================================================
  
  rate = 120
  
  # INITIALIZATION =================================================================================
  
  # RUN TEST =======================================================================================
  
  for question in range(nQuestions):
    
    a = 0; b = 0
    while a <= 1 or b <= 1: # prevent trivial questions
      a = int(10**nDigitsTop*random())
      b = int(10**nDigitsBottom*random())
      c = a * b
    
    speechEng = pyttsx3.init()
    speechEng.setProperty("rate", rate)
    speechEng.say(str(a) + " times " + str(b))
    speechEng.runAndWait()
    del speechEng
    sleep(delay)

    print("Question: {}. {} * {} = {}".format(question+1,a,b,c))    
    speechEng = pyttsx3.init()
    speechEng.setProperty("rate", rate)
    speechEng.say(str(c))
    speechEng.runAndWait()
    del speechEng
    input("Press [Enter] to continue...")
  
if __name__ == "__main__":
  '''Call main with the appropriate command line arguments.'''
  
  try:
    nQuestions = int(sys.argv[1])
    nDigitsTop = int(sys.argv[2])
    nDigitsBottom = int(sys.argv[3])
    delay = int(sys.argv[4])
  except:
    print("Usage: TestMultiplication.py nQuestions nDigitsTop nDigitsBottom delay")
    exit()
  
  main(nQuestions, nDigitsTop, nDigitsBottom, delay)
  exit()