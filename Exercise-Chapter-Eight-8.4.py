#file_name = input ("Enter file:\n")
#file_hand = open(file_name , 'r')
file_hand = open( 'romeo.txt', 'r')
count = 0

words = []
smart_words = []
for line in file_hand :
    words = line.split()
x = len(words)
while count < x :
    if words[count] in smart_words :
        count = count + 1
        continue
    smart_words.append(words[count])
    count = count + 1
smart_words.sort()
print (smart_words)
