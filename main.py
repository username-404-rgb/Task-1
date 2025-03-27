import requests
from spellbook import * 



def main():
    print ('Welcome to the spell helper')
    print ('1 - Search for a spell')
    print ('2 - Add spell to spellbook')
    print ('3 - View Spellbook')
    print ('4 - Remove spell from Spellbook')
    print ('5 - Quit Program')
    print ('')
    choice = input('What Do You Choose?')
    if choice == '1':
        use_search()
        print('Back to main') #TODO
    elif choice == '2':
        use_add
    elif choice == '3':
        print ('Spellbook') #TODO
    elif choice == '4':
        print ('remove form book') #TODO
    elif choice == '5':
        print ('QUIT') #TODO
    else:
        print ('Err')
# Example usage
main()

