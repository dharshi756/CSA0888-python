inputstring = "My name is Eve,I come from chennai,India,Iam here for research work."
sentences = inputstring.split(',')
longestsentence = max(sentences, key=lambda sentence: len(sentence))
print(longestsentence)
