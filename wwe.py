blanks=['___0___', '___1___','___2___', '___3___','___4___', '___5___'] 

prompt1 = '''World Wrestling Entertainment is the longets running tv show ran by Vince ___0___. In the year 1997 till the year 2002 WWE was known also by the name ___1___.The most popular era in the wwe was the ___2___ era. Wwe bigest competition in the 90's was ___3___.\n'''
key1 = ['McMahon', 'WWF', 'Attitude', 'WCW']

prompt2 = '''WCW was owned by Ted ___0___. The most popular wrestler to come out of WCW was ___1___. The most popular group to come out of WCW was ___2___ also known as the wolf pack.The most popular wrestler to go form wwe to wcw was Hulk ___3___.\n'''
key2 = ['Turner', 'Goldberg', 'NWO', 'Hogan']

prompt3 = '''WWE has two major championships. One is called the wwe ___0___ championship. And the second one is called the ___1___ championship. The champions are Kevin ___2___. And AJ ___3___.\n'''
key3 = ['Universal', 'WWE', 'Owens', 'Styles']

def difficultySelector():
    """Returns chosen difficulty"""
    difficulty=''
    while difficulty!='hard' and difficulty!='medium' and difficulty!='easy':
          difficulty=raw_input("Easy, Medium, or Hard? ").lower()
    return difficulty

def failState(strikes):
    """checks if player has used allotted strikes"""
    Max_allowed_tries=0
    if strikes>=Max_allowed_tries:
        return True
    return False

def checkAnswer(answer, blank, key):
    """returns True if given answer matches blank"""
    if answer.lower()==key[blank].lower():
        return True
    else:
        return False

def blankTranslator(blank):
    """accepts int, outputs formatted str"""
    stringBlank='___%d___'%blank
    return stringBlank

def playAgain():
    yn=''
    while yn!='y' and yn!='n':
        yn=raw_input("Play Again? y/n").lower()
    if yn=='n':
        return False
    return True

def quizzer(prompt, key):
    """presents prompt and accepts answers, returns True if player is successful, otherwise False"""
    strike, blank=0, 0
    for i in key:
        print prompt
        answer=raw_input("Your answer: ").lower()
        while checkAnswer(answer, blankTranslator(blank), key)==False:
            strike+=1
            print "strike %d!" %strike
            if failState(strike)==True:
                return False
            print prompt
            answer=raw_input("Your answer: ").lower()
        prompt=prompt.replace(blankTranslator(blank), answer)
        blank+=1
        strike=0
    print prompt.replace(blankTranslator(blank), answer)
    return True

tryAgain=True
while tryAgain==True:
    print "you have three chances per answer."
    difficulty=difficultySelector()
    if difficulty=='easy':
        success=quizzer(prompt1, key1)
    if difficulty=='medium':
        success=quizzer(prompt2, key2)
    if difficulty=='hard':
        success=quizzer(prompt3, key3)
    if success==True:
        print 'Congratulations!'
        tryAgain=playAgain()
    if success==False:
        print 'Game Over!'
        tryAgain=playAgain()
