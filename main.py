TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

registered_users = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
    }
separator = "-" * 40

# login
print("Welcome to the Text Analyzer!")
username = input("username: ")
password = input("password: ")

if username not in registered_users or registered_users[username] != password:
    print("unregistered user, terminating the program..")
else:
    print(separator)
    print(f"Welcome to the app, {username}")
    
    # text selection
    print(separator)
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print(separator)
    
    valid_choice = False
    while not valid_choice:
        choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
        
        if not choice.isnumeric():
            print("Invalid input. Please enter a number.")
        else:
            choice_num = int(choice)
            if 1 <= choice_num <= len(TEXTS):
                valid_choice = True
                text_index = choice_num - 1
            else:
                print(f"Please enter a number between 1 and {len(TEXTS)}.")
    
    # TEXT ANALYSIS
    selected_text = TEXTS[text_index]
    words = selected_text.split()
    
    word_count = len(words)
    titlecase_count = 0
    uppercase_count = 0
    lowercase_count = 0
    numeric_count = 0
    numeric_sum = 0
    word_lengths = {}
    
    for word in words:
        clean_word = word.strip('.,!?;:')
        
        if clean_word.istitle():
            titlecase_count += 1
        
        if clean_word.isupper() and clean_word.isalpha():
            uppercase_count += 1
        
        if clean_word.islower():
            lowercase_count += 1
        
        if clean_word.isnumeric():
            numeric_count += 1
            numeric_sum += int(clean_word)
        
        word_len = len(clean_word)
        if word_len > 0:
            if word_len in word_lengths:
                word_lengths[word_len] += 1
            else:
                word_lengths[word_len] = 1
    
    # OUTPUT RESULTS
    print(separator)
    print(f"There are {word_count} words in the selected text.")
    print(f"There are {titlecase_count} titlecase words.")
    print(f"There are {uppercase_count} uppercase words.")
    print(f"There are {lowercase_count} lowercase words.")
    print(f"There are {numeric_count} numeric strings.")
    print(f"The sum of all the numbers {numeric_sum}")
    print(separator)
    print("LEN|  OCCURRENCES  |NR.")
    print(separator)
    
    sorted_lengths = sorted(word_lengths.keys())
    for length in sorted_lengths:
        count = word_lengths[length]
        bar = '*' * count
        print(f"{length:>3}|{bar:<15}|{count}")
