import re

sentanceList = []
reverse_sentance =[]
sentance = input("Enter a sentance: ")
sentanceList = sentance.split()
print("this is the original sentence", sentanceList)
#reverse_sentance = sentance.reverse()
print(sentanceList.reverse())
sentance_final = " ".join(sentanceList)
print(sentance_final)
    
