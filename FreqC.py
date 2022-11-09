def freq(str):
  
    # break the string into list of words 
    str = str.split()         
    str2 = []
    
  
    # loop till string values present in list str
    for i in str:             
  
        # checking for the duplicacy
        if i not in str2:
  
            # insert value in str2
            str2.append(i) 
              
    for i in range(0, len(str2)):
  
        # count the frequency of each word(present 
        # in str2) in str and print
        k=str2[i], str.count(str2[i])    
    maxlen = 0
    longest_word = ''
    for word in str2:
        if len(word) > maxlen:
            maxlen = len(word)
            longest_word = word
    print(longest_word, maxlen)    

  
def main():
    str ='apple mango guava'
    freq(str)                    
  
if __name__=="__main__":
    main()             # call main function
