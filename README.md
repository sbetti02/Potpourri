# Potpourri
A collection of random files and programs I've written

# Trees/trie.py
This program takes a prefix and returns the most common words that start with the given prefix.
I create a trie that represents English words learned from the first 50,000 sentences of the Brown corpus.
Each node is a letter, and its children are all letters that link to a real word seen in the corpus.  
A counter keeps track of the number of times each node has been traversed
and whether or not the sequence of letters in the trie up to that point represent a real word.

# fib.py
A few explorations into different ways to generate a Fibonacci sequence and how
different methods impact performance.

# Trees/treeFuncs.py
A binary tree structure that may be expanded to include different methods of balancing a binary tree
