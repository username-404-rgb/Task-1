import requests
from spellbook import * 



def main():
    print ('')
    print ('Welcome to the Spell Helper')
    print ('1 - Search for a spell')
    print ('2 - Add spell to spellbook')
    print ('3 - View Spellbook')
    print ('4 - Remove spell from Spellbook')
    print ('5 - Quit Program')
    print ('')
    choice = input('What Do You Choose? ')
    if choice == '1':
        use_search()
        main()
    elif choice == '2':
        user_spell = input('Enter Spell Name: ')
        add_spell_to_spellbook(user_spell)
        main()
    elif choice == '3':
        view_spellbook()
        main()
    elif choice == '4':
        remove_spell()
        main()
    elif choice == '5':
        print ('QUIT') #TODO
    else:
        print ('Err')
        main()
# Example usage
main()

