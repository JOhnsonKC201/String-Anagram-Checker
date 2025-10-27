
# Implement _ecking off Method
def anagram_solution_1(s1, s2):
    # implement the function

    for _ in [" ", "$", "'", ",", ".", "!", "?"]:
        s1 = s1.replace(_, "")
        s2 = s2.replace(_, "")

    # _anged those string to list
    list1 = list(s1)
    list2 = list(s2)

    #_ecking the length of s1 = s2
    if len(list1)!= len(list2):
        return False

    cntr1 = 0
    still_OK = True
    while cntr1 < len(list1) and still_OK:
        cntr2 = 0
        found = False
        while cntr2 < len(list2) and not found:
            if list1[cntr1] == list2[cntr2]:
                found = True
            else:
                cntr2 = cntr2 +1
        if found:
            list2[cntr2]= None
        else:
            still_OK = False
        cntr1= cntr1 +1
    return still_OK



#Implement Sorting and Compare Method
def anagram_solution_2(s1, s2):
    # implement the function by sort and compile

    for _ in [" ", "$", "'", ",", ".", "!", "?"]:
        s1 = s1.replace(_, "")
        s2 = s2.replace(_, "")

    # _anged those string to list
    list1 = list(s1)
    list2 = list(s2)

    #SORT 
    list1.sort()
    list2.sort()

    # if length is not equal false
    if len(list1) != len(list2):
        return False
    
    cntr1 = 0
    same =  True

    while cntr1 < len(list1) and same:
        if list1[cntr1] == list2[cntr1]:
            cntr1 = cntr1 +1 
        else:
            same = False
    return same



#Implement Counting _aracter Frequencies
def anagram_solution_4(s1, s2):
    # implement the function
    for _ in [" ", "$", "'", ",", ".", "!", "?"]:
        s1 = s1.replace(_, "")
        s2 = s2.replace(_, "")

    # if length is not equal false
    if len(s1) != len(s2):
        return False

    cntr1 = [0] * 26
    cntr2 = [0] * 26

    # counting hte frequencies in s1
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a") 
        cntr1[pos] = cntr1[pos] + 1

    # counting the frequencies in s2
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        cntr2[pos] =cntr2[pos]+ 1

    # then  compareing  counters
    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if cntr1[j] == cntr2[j]:
            j += 1
        else:
            still_ok = False
    return still_ok

# Test cases
string_pairs = [
    ("listen", "silent"),
    ("dormitory", "dirtyroom"),
    ("a gentleman", "elegant man"),
    ("s_ool master", "the classroom"),
    ("conversation", "voices rant on"),
    ("the eyes", "they see"),
    ("debit card", "bad credit"),
    ("a decimal point", "I'm a dot in place"),
    ("eleven plus two", "twelve plus one"),
    ("slot ma_ines", "cash lost in me"),
    ("the earthquakes", "that queer shake"),
    ("william shakespeare", "I am a weakish speller"),
    ("triangle", "integral"),
    ("computer science", "scene computer"),
    ("evil", "vile")
]

# Test the algorithms and print results
for s1, s2 in string_pairs:
    print(f'Testing "{s1}" and "{s2}":')
    print(f'Solution 1: {anagram_solution_1(s1.lower(), s2.lower())}')
    print(f'Solution 2: {anagram_solution_2(s1.lower(), s2.lower())}')
    print(f'Solution 4: {anagram_solution_4(s1.lower(), s2.lower())}')
    print()  # Print a blank line between results
# print the three Big O notations for the three methods
print("Big-O of Solution 1 is  O(n^2)")       
print("Big-O of Solution 2 is   O(n log n)")      
print("Big-O of Solution 4 is   O(n)")        
