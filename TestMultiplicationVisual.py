#!/usr/bin/env python
'''Test a human's ability to do mental multiplication when the question is visible.'''

# python
import sys
from time import sleep
from random import random
# pyttsx
import pyttsx

def main(nQuestions, nDigitsTop, nDigitsBottom, delay):
  '''Entrypoint to the program.'''

  # PARAMETERS =====================================================================================
  
  rate = 120
  
  # INITIALIZATION =================================================================================
  
  # RUN TEST =======================================================================================
  
  for question in xrange(nQuestions):
    
    a = 0; b = 0
    while a <= 1 or b <= 1: # prevent trivial questions
      a = int(10**nDigitsTop*random())
      b = int(10**nDigitsBottom*random())
      c = a * b
    
    sys.stdout.write("Question: {}. {} * {} = ".format(question+1,a,b))
    sys.stdout.flush()
    speechEng = pyttsx.init()
    speechEng.setProperty("rate", rate)
    speechEng.say(str(a) + " times " + str(b))
    speechEng.runAndWait()
    del speechEng
    sleep(delay)
    
    sys.stdout.write("{}\n".format(c))
    sys.stdout.flush()
    speechEng = pyttsx.init()
    speechEng.setProperty("rate", rate)
    speechEng.say(str(c))
    speechEng.runAndWait()
    del speechEng
    raw_input("Press [Enter] to continue...")
  
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