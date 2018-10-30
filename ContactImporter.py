from AppleVcardImporter import AppleVcardImporter
from GoogleCSVImporter import GoogleCSVImporter
from contact import Contact
import class_utils

def perform_contact_import():
    apple_contacts = AppleVcardImporter().get_contacts_from_vcard_file()
    google_contacts = GoogleCSVImporter().get_contacts_from_google_csv_file()
    contacts = apple_contacts + google_contacts

    print(merge_contacts(contacts))

def merge_contacts(contacts):
    # create n <Attribute, Contact> attribute_dictionaries, where 'n' is the number of Contact attributes
    contact_class_attributes = class_utils.get_class_attributes(Contact())
    attribute_dicts = {}

    for attribute in contact_class_attributes:
        if attribute not in Contact().EXCLUDED_MERGE_ATTRIBUTES:
            attribute_dicts[attribute] = {}

    # Add contact as unique value to all relevant attribute dictionaries.
    for contact in contacts:
        for attribute in attribute_dicts.keys():
            if not hasattr(contact, attribute):
                continue

            value = getattr(contact, attribute)

            if value in attribute_dicts[attribute]:
                # if an entry in the attribute_dicts matches contact.Attribute,
                # merge the Contacts as new_c, and store new_c in attribute_dict.
                stored_contact = attribute_dicts[attribute]
                merged_contact = merge_two_contacts(stored_contact, contact)
                # also, propogate new_c to all other matching attribute dicts.
                pass


def merge_two_contacts(c1, c2):
    return Contact()

if __name__ == '__main__':
    perform_contact_import()

