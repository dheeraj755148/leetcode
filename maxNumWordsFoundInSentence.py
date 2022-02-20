sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

maxSum = len(sentences[0].split(" "))
for i in range(1,len(sentences)-1):
    tempSum = max(len(sentences[i].split(" ")),len(sentences[i+1].split(" ")))
    maxSum = max(tempSum,maxSum)

print(maxSum)