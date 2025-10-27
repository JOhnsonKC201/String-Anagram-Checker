# String-Anagram-Checker
# Anagram Checker — Three Algorithms, Three Complexities

This project explores three different ways to check if two strings are anagrams, and it compares their performance. It's part of a lab assignment for learning about strings, lists, and Big-O runtime.

An anagram means:  
two phrases use the exact same letters with the same counts (ignoring spaces/punctuation and case).  
Example:  
"Listen" ⇔ "Silent"  
"A decimal point" ⇔ "I'm a dot in place"

---

## Core Features

### 1. Checking-Off Method (`anagram_solution_1`)
- For each letter in the first string, we try to “cross off” a matching letter in the second string.
- If we can match every letter, it's an anagram.
- This is kind of like doing it by hand on paper.
- **Time Complexity:** O(n²) (slowest)

### 2. Sort and Compare (`anagram_solution_2`)
- We clean both strings, sort the letters, and compare the sorted results.
- If the sorted strings are identical, it's an anagram.
- **Time Complexity:** O(n log n)

### 3. Frequency Count / Hash Map (`anagram_solution_4`)
- We count how many times each character appears in each string.
- Then we compare the two frequency maps.
- This handles multi-word phrases like `"william shakespeare"` vs `"I am a weakish speller"`.
- We also normalize by:
  - making everything lowercase
  - ignoring spaces and punctuation
- **Time Complexity:** O(n) (fastest)

---

## Why this matters

Same task. Three different solutions. Three different runtimes.

This is a simple example of algorithm design:
- A “works but slow” solution (O(n²))
- A “better in practice” solution (O(n log n))
- An “optimal” solution (O(n))

This is exactly what we talk about in data structures and algorithms:  
how the choice of approach directly impacts performance.

---

## Example Input Pairs We Test

We test classic anagram pairs like:
- `"listen"` vs `"silent"`
- `"dormitory"` vs `"dirty room"`
- `"debit card"` vs `"bad credit"`
- `"william shakespeare"` vs `"I am a weakish speller"`

The code runs all 15 sample pairs and prints `True` or `False` for each method.

---

## Tech details

- Language: Python 3
- Data structure used:
  - Custom Stack (for other labs)
  - Lists
  - Dictionaries / hash maps
- We normalize strings by:
  - converting to lowercase
  - removing spaces and punctuation
  - keeping only alphanumeric characters

This means:
`"A decimal point"` and `"I'm a dot in place"` are treated as the same multiset of letters.

---

## How to run

Clone the repo and run:

String Anagram Checker.py
