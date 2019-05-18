import csv
data = list(csv.reader(open("file.csv")))
scores=[]
def getMaxFormatLength(arr):
  m=0
  for i in arr:
    if len(i[0])>m:
      m=len(i[0])
  return m
def getMaxB(arr):
  m=0
  for i in arr:
    if int(i[2])>m:
      m=int(i[2])
  return m
def printArr(arr):
  for i in arr:
    print(*i)
def convertNuma(a): #makes ranks more understandable (into percentage)
  return int(a)/64*100
def convertNumb(b):
  maxB=getMaxB(data)
  b=abs(int(b))
  b=maxB-b
  return b/maxB*100
def calcAvg(a,b): #gets score of media
  s=convertNuma(a) + convertNumb(b)
  return str(round(s/2,1))

def printScores(d):
  maxFormatLength=getMaxFormatLength(scores)
  print("Rankings:".center(10, " "))
  for i in range(len(d)):
    l=len(d[i][0])
    spaces=" "*(maxFormatLength-l+1)
    print(str(i+1)+"\t"+d[i][0]+":"+spaces+d[i][1]+"%")
# print(data[1:])

data=data[1:] # remove headers

for i in range(len(data)):
  scores.append([data[i][0],calcAvg(data[i][1],data[i][2])])
# print(scores)
scores.sort(key=lambda x: float(x[1]), reverse=True)
printScores(scores)


# printArr(data)



