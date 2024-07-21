noOfWords=0
dictionary=[]
with open("Dictionary.txt","r") as file:
    for word in file:
        word=word[0:-1]
        dictionary.append(word)
        
class TrieNode:
    def __init__(self, word=''):
        self.word=word
        self.child=dict()
        self.isTerminal=False
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):  
        ## Space Complexity --> O(n*m)  Time Complexity --> O(m*n) where m -> No. of words and n is average length of each word
        current = self.root
        for i,character in enumerate(word):
            # If character not exist (prefix of given word is not there in trie)
            if character not in current.child:
                prefix=word[0:i+1]
                # Making a new node for the character
                current.child[character] = TrieNode(prefix)
            # Moving to next node in trie
            current = current.child[character]
        # After iterating through the entire word, mark the last character node as Terminal node
        current.isTerminal=True
        
    def find(self,word):  # Time Complexity -> O(n) where n is the length of the word
        # Check if the input word is lowercase word
        if self.isLower(word)==True:
            current=self.root
            for character in word:
                if character not in current.child:
  # If a given character of the word is not found, then suggest some words having the given valid prefix as there may be a spell error
                    suggested_words=self.suggestions(word)
                    # If suggestions exist
                    if suggested_words:
                        print("Looks like there is a spell error in the input. Here are some suggested words from the dictionary given below")
                        return suggested_words
                    # The given word is not a valid English word and is not in dictionary
                    return False
                current = current.child[character]
            # If Terminal Node is there then word exist in dictionary else not
            return current.isTerminal
        
        # If input word is not lowercase word
        return False
    
    def isLower(self,word):
        # If word is an empty string
        if word=='':
            print('Not a valid Word')
            return False
        
        for character in word:
            # If word consists of Uppercase letter, special symbols or numbers
            if not (character >= 'a' and character <= 'z'):
                print('Not a valid word')
                return False
        return True
    
    def suggestions(self, word):
        suggested_words = []
        current = self.root

        # Loop through the characters of the word
        for i, character in enumerate(word):
            
            # If there is a mismatch found
            if character not in current.child:
                # Find suggestions
                suggested_words.extend(self.find_suggestions(current))
                return suggested_words 
            current = current.child[character]
            
        # If entire word traversed and no mismatch found, no suggestions
        return []

    def find_suggestions(self, current_node):
        # Explore child nodes for the current node
        suggestions = []
        for child in current_node.child.values():
            # If child node represents a complete word, add it as a suggestion
            if child.isTerminal:
                suggestions.append(child.word)
            # Continue exploring child nodes
            suggestions.extend(self.find_suggestions(child))
        return suggestions

# Making an object of Trie class
trie=Trie()
for word in dictionary:
    trie.insert(word)  # Inserting all the words in a list

print('How many words you want to search ?',end=' ')
noOfWords=int(input())    
count=0
      
while True:
    count+=1
    if count>noOfWords:
         break
    print('Enter word: ',end=' ')
    word=input()
    result=trie.find(word)
    if result== True:
        print('Word exist in Dictionary')
    elif result==False:
        print('Word does not exist in the dictionary')
    else:
        print(result)