# user interface here
import requests


# API Base URL
API_URL = "https://www.dnd5eapi.co/api/spells/"

# Dictionary to store spells
spellbook = {}

def search_spell(spell_name):
    """Search for a spell in the D&D API and return its details."""
    response = requests.get(API_URL + spell_name.lower().replace(" ", "-"))
    if response.status_code == 200:
        spell_data = response.json()
        return {
            "name": spell_data["name"],
            "level": spell_data["level"],
            "description": spell_data["desc"][0]  # First part of the description
        }
    else:
        print("Spell not found.")
        return None

def add_spell_to_spellbook(spell_name):
    """Add a spell to the spellbook if found.""" 
    spell = search_spell(spell_name)
    if spell:
        spellbook[spell_name] = spell
        print(f"Added {spell_name} to your spellbook!")

def view_spellbook():
    """Display all stored spells."""
    if not spellbook:                           #If spellbook empty, print 'your spellbook is empty'
        print("Your spellbook is empty.")
    else:
        for spell in spellbook.values():
            print(f"{spell['name']} (Level {spell['level']}): {spell['description']}")     #Displays the spell name, level, and description

def use_search():
    user_spell = input('Enter Spell Name: ')
    spell_found = search_spell(user_spell)
    print(spell_found)

def remove_spell():
    """Remove a spell from the spellbook"""
    if not spellbook:                           #If the spell searched for isn't in book, just prints spellbook, otherwise removes it then prints
        print("Your spellbook is empty.")
    else: 
        remove = input("Remove which spell? ")
        if remove in spellbook:
            spellbook.pop(remove)
            view_spellbook()
        else:
            print('Spell not in spellbook')
            view_spellbook()