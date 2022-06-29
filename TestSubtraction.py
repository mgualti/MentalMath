#!/usr/bin/env python3
'''Test a human's ability to do mental subtraction.'''

# python
import sys
import time
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
    
    a = int(10**nDigits*random())
    b = int(10**nDigits*random())
    
    # no negatives for this test
    if b > a:
      tmp = a; a = b; b = tmp
      
    c = a - b
    
    speechEng = pyttsx3.init()
    speechEng.setProperty("rate", rate)
    speechEng.say(str(a) + " minus " + str(b))
    speechEng.runAndWait()
    del speechEng
    time.sleep(delay)

    print("Question: {}. {} - {} = {}".format(question+1,a,b,c))    
    speechEng = pyttsx3.init()
    speechEng.setProperty("rate", rate)
    speechEng.say(str(c))
    speechEng.runAndWait()
    del speechEng
    #time.sleep(delay)
    input("Press [Enter] to continue...")
  
if __name__ == "__main__":
  '''Call main with the appropriate command line arguments.'''
  
  try:
    nQuestions = int(sys.argv[1])
    nDigits = int(sys.argv[2])
    delay = int(sys.argv[3])
  except:
    print("Usage: TestSubtraction.py nQuestions nDigits delay ")
    exit()
  
  main(nQuestions, nDigits, delay)
  exit()