# Written by Trevor Decker
# Copyright Trevor Decker 2017

import csv

#TODO add cash option
#TODO add ability to downolad and read a bunch of diffrent stocks 
#TODO add ability to plot
#TODO add ability to sell stock
#TOOD add ability to buy stock
#TODO add ability to have stock mixtures

#TODO develop train/test structure
#TODO add suddon sector loss preventions, will force the system to diversify by showing a bunch of examples of single stocks failing
#TOOD add TF for RL based learned approach

#policy 1. all cash
#policy 2. all stock
#policy 3. buy when 2% lower then set point, sell after 2% gain

#for monday I want a device which given my current portflio will tell me what to sell and what to buy 

#TOOD crate a class for policy
#TODO crate a class for actions

#TODO build list of historic data
with open('data/aapl.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     i = 0
     opens = []
     for row in spamreader:
          if i > 0:
               line = row[0]
               sections = line.split(",")
               #0 is date
               #1 is open
               #2 is low
               #3 is close
               #4 is Volume
               opens.append(float(sections[1]))
          i = i+1

     opens = opens[::-1]

     row_count = len(opens)

     stockAmount = 0.0
     cashAmount = 1.0
     buyValue = opens[0]
     sellValue = opens[0]

     for rowNum in xrange(0,row_count):
          currentStock = opens[rowNum]
          print currentStock, cashAmount, stockAmount
          if(stockAmount > 0.0):
               #see if we should sell
               if(currentStock - buyValue > 2.0):
                    #sell
                    print "Sell"
                    sellValue = currentStock
                    cashAmount = stockAmount*currentStock
                    stockAmount = 0.0;
          else:
               #see if we should buy 
               if(currentStock - sellValue < -2.0):
                    #buy
                    print "Buy"
                    buyValue = currentStock
                    stockAmount = cashAmount/buyValue
                    cashAmount = 0.0

     print cashAmount + stockAmount*opens[row_count-1]
     print opens[row_count-1]/opens[0]
