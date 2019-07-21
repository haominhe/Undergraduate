#!/usr/bin/python
#
# CIS 472/572 - Perceptron Template Code
#
# Author: Daniel Lowd <lowd@cs.uoregon.edu>
# Date:   2/10/2017
#
# (You are free to use this code in your solution if you wish.)
# Authors: Yueqi Zhu, Haomim He
#
import sys
import re
from math import log
from math import exp

MAX_ITERS = 100

# Load data from a file
def read_data(filename):
  f = open(filename, 'r')
  p = re.compile(',')
  data = []
  header = f.readline().strip()
  varnames = p.split(header)
  namehash = {}
  for l in f:
    example = [int(x) for x in p.split(l.strip())]
    x = example[0:-1]
    y = example[-1]
    # Each example is a tuple containing both x (vector) and y (int)
    data.append( (x,y) )
  return (data, varnames)


# Learn weights using the perceptron algorithm
def train_perceptron(data):
    # Initialize weight vector and bias
    numvars = len(data[0][0])
    
    w = [0.0] * numvars
    b = 0.0

    #
    # OUR CODE HERE!
    #

    # Max iteration
    for i in range(MAX_ITERS):
      for (x,y) in data:
        a=0
        for j in range(numvars):
          a=a+w[j]*x[j]
        a=a+b
        if y*a<=0:
          for j in range(numvars):
            w[j]=w[j]+y*x[j]
          b=b+y

    return (w,b)


# Load train and test data.  Learn model.  Report accuracy.
def main(argv):
  # Process command line arguments.
  # (You shouldn't need to change this.)
  if (len(argv) != 3):
    print 'Usage: perceptron.py <train> <test> <model>'
    sys.exit(2)
  (train, varnames) = read_data(argv[0])
  (test, testvarnames) = read_data(argv[1])
  modelfile = argv[2]

  # Train model
  (w,b) = train_perceptron(train)

  # Write model file
  # (You shouldn't need to change this.)
  f = open(modelfile, "w+")
  f.write('%f\n' % b)
  for i in xrange(len(w)):
    f.write('%s %f\n' % (varnames[i], w[i]))

  # Make predictions, compute accuracy
  correct = 0
  numvars = len(test[0][0])
  for (x,y) in test:
    a=0
    for j in range(numvars):
      a=a+w[j]*x[j]
    a=a+b
    activation = a # <-- OUR CODE HERE
    print activation
    if activation * y > 0:
      correct += 1
  acc = float(correct)/len(test)
  print "Accuracy: ",acc

if __name__ == "__main__":
  main(sys.argv[1:])
