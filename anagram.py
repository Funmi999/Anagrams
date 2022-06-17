# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(a, b):
      # [assignment] Add your code here
  return sorted(a.lower()) == sorted(b.lower())
  
print(find_anagrams('west', 'stews'))
print(find_anagrams('crepe', 'creep'))
       
