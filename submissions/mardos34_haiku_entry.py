from random import randint

wordList1 = ["Much", "Be", "Yes", "Wow", "Delicate"]
wordList2 = ["cheapEth", "distance", "conscience", "process", "normie"]
wordList3 = ["superstitious", "contrasting", "graceful", "inviting", "contradicting", "overwhelming"]
wordList4 = ["true", "dark", "cold", "warm", "great"]
wordList5 = ["butt","meme", "reee","earth","no moon","Winter","cum","9000"]
wordList6 = ["undeniable", "beautiful", "irreplaceable", "unbelievable", "irrevocable"]
wordList7 = ["inspiration", "imagination", "wisdom", "cheapEth"]
        
wordIndex1=randint(0, len(wordList1)-1)
wordIndex2=randint(0, len(wordList2)-1)
wordIndex3=randint(0, len(wordList3)-1)
wordIndex4=randint(0, len(wordList4)-1)
wordIndex5=randint(0, len(wordList5)-1)
wordIndex6=randint(0, len(wordList6)-1)
wordIndex7=randint(0, len(wordList7)-1)

haiku = wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",\n" 
haiku = haiku + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList5[wordIndex5]  + ",\n"
haiku = haiku + wordList6[wordIndex6] + " " + wordList7[wordIndex7] + "."

print(haiku)