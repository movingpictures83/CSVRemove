import sys
import numpy
import random
import PyPluMA

class CSVRemovePlugin:
   def input(self, filename):
      self.txtfile = open(filename, 'r')
      self.parameters = dict()
      for line in self.txtfile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()
      if len(PyPluMA.prefix()) != 0:
         self.parameters['csvfile'] = PyPluMA.prefix() + "/" + self.parameters['csvfile']
   def run(self):
      self.newlines = []
      column = int(self.parameters['column'])
      csvfile = open(self.parameters['csvfile'], 'r')
      for line in csvfile:
         line = line.strip()
         contents = line.split(',')
         contents = contents[0:column] + contents[column+1:]
         newline = ""
         for j in range(len(contents)):
            newline += contents[j]
            if (j != len(contents)-1):
               newline += ','
         self.newlines.append(newline)


   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      for i in range(len(self.newlines)):
         filestuff2.write(self.newlines[i])
         if (i != len(self.newlines)-1):
            filestuff2.write('\n')



