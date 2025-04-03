import requests
from spellbook import * 



def main():
    print ('')                                              #Fancy UI for user
    print ('     Welcome to the Spell Helper')
    print ('     ► 1 - Search for a spell ◄')
    print ('   ► 2 - Add spell to spellbook ◄')
    print ('       ► 3 - View Spellbook ◄')
    print (' ► 4 - Remove spell from Spellbook ◄')
    print ('       ► 5 - Quit Program ◄')
    print ('')
    choice = input('What Do You Choose? ◄')
    if choice == '1':                                       #Search for spell
        use_search()
        main()
    elif choice == '2':                                     #Add a spell to spellbook
        user_spell = input('Enter Spell Name: ')
        add_spell_to_spellbook(user_spell)
        main()
    elif choice == '3':                                     #View spellbook
        view_spellbook()
        main()
    elif choice == '4':                                     #Remove a spell from spellbook
        remove_spell()
        main()
    elif choice == '5':                                     #End program
        print ('QUIT') #TODO
    else:                                                   #Displays if invalid input
        print ('Err')
        main()
# Example usage
main()

