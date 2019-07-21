#!/usr/bin/python
# 
# CIS 472/572 -- Programming Homework #1
#
# Starter code provided by Daniel Lowd, 1/20/2017
#
# Author: Yueqi Zhu, Haomin He



import sys
import re
import math
# Node class for the decision tree
import node


# SUGGESTED HELPER FUNCTIONS:
# - compute entropy of a 2-valued (Bernoulli) probability distribution 
# - compute information gain for a particular attribute
# - collect counts for each variable value with each class label
# - find the best variable to split on, according to mutual information
# - partition data based on a given variable 


# Load data from a file
def read_data(filename):
  f = open(filename, 'r')
  p = re.compile(',')
  data = []
  header = f.readline().strip()
  varnames = p.split(header)
  namehash = {}
  for l in f:
    data.append([int(x) for x in p.split(l.strip())])
  return (data, varnames)

# Saves the model to a file.  Most of the work here is done in the 
# node class.  This should work as-is with no changes needed.
def print_model(root, modelfile):
  f = open(modelfile, 'w+')
  root.write(f, 0)

def get_entropy(data):
  num_0=0.0
  num_1=0.0
  for example in data:
    if example[-1]==0:
      num_0=num_0+1
    else:
      num_1=num_1+1
  num_exp=num_0+num_1
 
  if num_0==0 or num_1==0:    
    return 0.0
  return 0-num_0/num_exp*math.log(num_0/num_exp,2)-num_1/num_exp*math.log(num_1/num_exp,2)
  
# Build tree in a top-down manner, selecting splits until we hit a
# pure leaf or all splits look bad.
def build_tree(data, varnames):
    # >>>> OUR CODE GOES HERE <<<<
    entropy=get_entropy(data)
    if entropy==0:
      return node.Leaf(varnames,data[0][-1])
    allsame=True
    for i in range(0,len(varnames)):
      t=0
      for j in data:
        t=t+j[i]
      if t==0 or t==len(data):
        same=True
      else:
        same=False
      allsame=allsame and same
    if allsame:
      num_0=0
      num_1=1
      for j in data:
        if j[-1]==0:
          num_0=num_0+1
        else:
          num_1=num_1+1
      if num_1>num_0:
        return node.Leaf(varnames,1)
      else:
        return node.Leaf(varnames,0)  
    
    maxig=-1
    for i in range(0,len(varnames)):
      list_0=[]
      list_1=[]
      for example in data:
        if example[i]==0:
          list_0.append(example)
        else:
          list_1.append(example)
      entropy_0=get_entropy(list_0)
      entropy_1=get_entropy(list_1)
      ig=entropy-float(len(list_0))/float(len(data))*entropy_0-float(len(list_1))/float(len(data))*entropy_1
      
      if ig>maxig or i==0:
        maxig=ig
        rootvar=i
        left=list_0
        right=list_1
     
    return node.Split(varnames, rootvar, build_tree(left,varnames), build_tree(right,varnames))

    # For now, always return a leaf predicting "1":
    # return node.Leaf(varnames, 1)

# Load train and test data.  Learn model.  Report accuracy.
def main(argv):
  if (len(argv) != 3):
    print 'Usage: id3.py <train> <test> <model>'
    sys.exit(2)
  # "varnames" is a list of names, one for each variable
  # "train" and "test" are lists of examples.  
  # Each example is a list of attribute values, where the last element in
  # the list is the class value.
  (train, varnames) = read_data(argv[0])
  (test, testvarnames) = read_data(argv[1])
  modelfile = argv[2]
  varnames.pop()
  # build_tree is the main function you'll have to implement, along with
  # any helper functions needed.  It should return the root node of the
  # decision tree.
  root = build_tree(train, varnames)
  root.write(sys.stdout, 0)
  

  print_model(root, modelfile)
  correct = 0
  # The position of the class label is the last element in the list.
  yi = len(test[0]) - 1
  for x in test:
    # Classification is done recursively by the node class.
    # This should work as-is.
    pred = root.classify(x)
    if pred == x[yi]:
      correct += 1
  acc = float(correct)/len(test)
  print "Accuracy: ",acc

if __name__ == "__main__":
  main(sys.argv[1:])
