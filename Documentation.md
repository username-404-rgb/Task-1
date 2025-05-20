# 2025 Software Engineering Preliminary

#

## By Alexander Adams

## Requirements definition

### Functional requirements

* User must be able to view any spell

* User must be able to store spells

* Program must be able to display error messages

* User inputs through text

### Non-functional requirements

* Program should be able to run on low end devices

* Program should be consistent in its output

* Program should be understandable to user

## Determining Specifications
### Functional Specifications

* **User Requirements:**
    * User should be able to search for spells, save spells and cast spells

* **Inputs & Outputs:** 
    * Input: Program should read shorthand commands from user [1, 2, 3], allocated to showing spell list, searching for spells and saving spell to spellbook
    * Output: Program should show spell list, searched spell, spells in spell book based on which of the inputs was provided by the user

* **Core Features:** Summary of whole program 
    * Program should allow user to view and store spells from DnD

* **User Interaction:**
    * Program should display spells in a readable format, a help command should display list of shorthand commands for users

* **Error Handling**:
    * In event of error should display "something went wrong" message

### Non-Functional Specifications

* **Performance**:
    * Program should take less than 10 seconds per command

* **Useability**:
    * More can be done for ease of navigation, program could have a good use of menus, clear structure for the user

* **Reliability**:
    * Potential errors include duplicate data, inaccurate data, data retrieval crashes, and can be fixed through repeated testing

## Use Case

* **Actor -** User

* **Preconditions -** Internet connection; API for DnD 5e available

* **Main Flow -**
    * ***Search for spell***: User enters a spell name and system retrieves and displays details for spell
    * ***Store Spell***: Current spell is saved to list of stored spells
    * ***View Spellbook***: Displays list of stored spells
    * ***Use Spell***: Spell is removed from spellbook
    * ***Exit***: Program is closed

* **Postconditions -** Spell is displayed, stored, viewed, removed or program close

## Design

![Structure Chart](/images/structue_chart.png "Structure Chart")
![Algorithm 1](/images/algorithm_1.png "Algorithm 1")
![Algorithm 2](/images/algorithm_2.png "Algorithm 2")
![Data Dictionary](/images/data_dictionary.png "Data Dictionary")

## Maintenance

* Limited need for maintenance, potential for errors with updates to the DnD API



