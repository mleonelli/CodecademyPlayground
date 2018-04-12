def censor(text, word):
  l = len(word)
  i = 0
  censored = ""
  while i < len(text):

    if(i > len(text) - len(word)):
      censored += text[i]
      i += 1
    else:  
    
      found_at_i = True
      for j in range(0, l):
        if(text[i + j] != word[j]):
          found_at_i = False
      if(found_at_i == True):
        censored += '*' * l 
        i += l  
      else:
        censored += text[i]
        i += 1
  
  return censored 
