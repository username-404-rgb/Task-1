import requests
from spellbook import * 



def main():
    print ('Welcome to the spell helper')
    print ('1 - Search for a spell')
    print ('2 - View Spellbook')
    print ('3 - Remove spell from Spellbook')
    print ('4 - Quit Program')
    print ('')
    choice = input('What Do You Choose?')
    if choice == '1':
        use_search()
    elif choice == '2':
        print ('Spellbook') #TODO
    elif choice == '3':
        print ('3 done') #TODO
    elif choice == '4':
        print ('QUIT') #TODO
    else:
        print ('Err')
# Example usage
main()

