#!/usr/bin/python
#
# CIS 472/572 - Logistic Regression Template Code
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
from math import sqrt

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
    data.append( (x,y) )
  return (data, varnames)


# Train a logistic regression model using batch gradient descent
def train_lr(data, eta, l2_reg_weight):
  numvars = len(data[0][0])
  w = [0.0] * numvars
  b = 0.0

  #
  # OUR CODE HERE
  #

  for i in range(MAX_ITERS):
    g=[0.0]*numvars
    gb=0.0
    for (x,y) in data:
      pred=0
      for j in range(numvars):
        pred=pred+w[j]*x[j]
      pred=pred+b
      for j in range(numvars):
        g[j]=g[j]-1.0/(1+exp(0-y*pred))*y*x[j]
      gb=gb-1.0/(1+exp(0-y*pred))*y
    #print sum(g)
    for j in range(numvars):
      g[j]=g[j]-l2_reg_weight*w[j]
      w[j]=w[j]+eta*g[j]
    b=b+eta*gb

  b=-b
  for j in range(numvars):
    w[j]=-w[j]
  return (w,b)


# Load train and test data.  Learn model.  Report accuracy.
def main(argv):
  if (len(argv) != 5):
    print 'Usage: lr.py <train> <test> <eta> <lambda> <model>'
    sys.exit(2)
  (train, varnames) = read_data(argv[0])
  (test, testvarnames) = read_data(argv[1])
  eta = float(argv[2])
  lam = float(argv[3])
  modelfile = argv[4]

  # Train model
  (w,b) = train_lr(train, eta, lam)

  # Write model file
  f = open(modelfile, "w+")
  f.write('%f\n' % b)
  for i in xrange(len(w)):
    f.write('%s %f\n' % (varnames[i], w[i]))

  # Make predictions, compute accuracy
  correct = 0
  for (x,y) in test:
    s=0
    for i in range(len(x)):
      s=s+x[i]*w[i]
    s=s+b
    prob = 1.0/(1+exp(0-s)) # <-- OUR CODE HERE
    print prob 
    if (prob - 0.5) * y > 0:
      correct += 1
  acc = float(correct)/len(test)
  print "Accuracy: ",acc

if __name__ == "__main__":
  main(sys.argv[1:])
