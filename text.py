main_menu = ['MAin menue',
             'Open file',
             'Save file',
             'Show phonebook',
             'Create contact',
             'Find contact',
             'Change contact',
             'Remove contact',
             'Exit']

main_menu_choice = 'Choose punct in menue: '

load_successful = 'Phonebook successfully uploaded'
save_successful = 'Phonebook successfully saved'

empty_phone_book = 'Phonebook empty or closed'

new_contact = ['Enter name: ',
               'Enter phone number: ',
               'Enter comment: ']


def new_contact_added_successful(name: str) -> str:
    return f'Contact {name} successfully uploaded'


input_search_word = 'Enter word to start searching: '


def contacts_not_found(word: str) -> str:
    return f'Contacts including {word} were not found'


input_id_change_contact = 'Enter contact ID, you want to change: '

change_contact = ['Enter new name or Enter to skip changes: ',
                  'Enter new number or Enter to skip changes: ',
                  'Enter new  comment or Enter to skip changes: ']


def contact_change_successful(name: str) -> str:
    return f'Contact {name} successfully changed'


input_id_deleted_contact = 'Enter contact ID you want to remove: '


def contact_delete_successful(name: str) -> str:
    return f'Contact {name} successfully removed'

good_bye = 'See you'