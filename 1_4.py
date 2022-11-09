test_string = "GfG is lemma for CS and also best for Learning"
  
# initializing target word 
tar_word = "emma"
  
# printing original string 
print("The original string : " + str(test_string))
  
# using rfind()
# Find last occurrence of substring
res = test_string.rfind(tar_word)
  
# print result
print("Index of last occurrence of substring is : " + str(res))