from AppleVcardImporter import AppleVcardImporter
from GoogleCSVImporter import GoogleCSVImporter
from contact import Contact, ContactUtils
import class_utils

class ContactImporter:
    def __init__(self):
        self.user = self.fetch_user_from_db(123)
        self.blacklisted_contact_ids = self.get_blacklisted_contacts_from_user()
        self.saved_contacts = self.get_saved_contacts_for_user()
        self.contacts_queued_for_blacklist = {}
        self.contacts_queued_to_save = {}
        self.contacts_queued_to_update = {}
        self.new_contacts = self.import_new_contacts()

    def fetch_user_from_db(self, user_id):
        return {'123': {'contacts': {'blacklist': {}, 'saved': {}}}}

    def get_blacklisted_contacts_from_user(self):
        return self.user.get('contacts', {}).get('blacklist', {})

    def get_saved_contacts_for_user(self):
        return self.user.get('contacts', {}).get('saved', {})

    def import_new_contacts(self):
        apple_contacts = AppleVcardImporter().get_contacts_from_vcard_file()
        google_contacts = GoogleCSVImporter().get_contacts_from_google_csv_file()
        all_contacts = apple_contacts + google_contacts
        self.get_new_contacts(all_contacts)
        len(self.contacts_queued_to_save)
        return self.contacts_queued_to_save

    def get_new_contacts(self, contacts):
        # Merge and remove duplicate contacts (by attribute)

        # Add contact as unique value to all relevant attribute dictionaries.
        attribute_dicts = self.create_attribute_dicts(contacts)
        # create list of unique contact entries from attribute dict entries.
        # 'unique' is defined as a contact id that we haven't already saved or blacklisted.
        unique_contacts = self.get_unique_contacts_from_attribute_dicts(attribute_dicts)
        # Let the user select which contacts they'd like to save and blacklist.
        self.select_contacts(unique_contacts)
        # Persist contacts to save and contacts to blacklist
        self.persist_contacts_to_db()

    # Creates n <Attribute, Contact> attributes_dictionaries, where 'n' is the number of attributes on Contact.
    def create_attribute_dicts(self, contacts):
        attribute_dicts = {}

        # create n <Attribute, Contact> attribute_dictionaries, where 'n' is the number of Contact attributes
        contact_class_attributes = class_utils.get_class_attributes(Contact())

        for attribute in contact_class_attributes:
            if attribute not in ContactUtils().EXCLUDED_MERGE_ATTRIBUTES:
                attribute_dicts[attribute] = {}

        # Add each contact to each attribute_dictionary, using it's unique Contact.attribute as key.
        for contact in contacts:
            # Used to keep track of the keys we've used for this Contact across dictionary entries
            attribute_keys_for_contact = []

            # Keeps track of which attributes were present for this Contact instance.
            attributes_stored = []

            for attribute in attribute_dicts.keys():
                if not hasattr(contact, attribute):
                    continue

                value = getattr(contact, attribute)

                # Validate value isn't default
                if len(value) <= 0:
                    continue

                if type(value) is list:
                    key = value[0]
                    attribute_keys_for_contact.append(value[0])

                elif type(value) is str:
                    key = value
                    attribute_keys_for_contact.append(value)

                else:
                    raise ValueError("Class attribute is not of type list or str. "
                                     "attribute: {} Contact.attribute type: {}".format(attribute, type(value)))

                if key in attribute_dicts[attribute]:
                    # if an entry in the attribute_dict matches contact.Attribute,
                    # merge the Contacts as new_c, and store new_c in attribute_dict.
                    stored_contact = attribute_dicts[attribute]
                    merged_contact = self.merge_two_contacts(stored_contact, contact)
                    attribute_dicts[attribute][value] = merged_contact

                    # also, propagate new_c to all other matching attribute dicts.
                    attribute_dicts = self.update_contact_metadata_in_attribute_dicts(attribute_dicts,
                                                                                      attributes_stored,
                                                                                      attribute_keys_for_contact,
                                                                                      merged_contact)

                else:
                    attribute_dicts[attribute][value] = contact

                attributes_stored.append(value)
                attribute_keys_for_contact.append(value)

        # Now that we're out of for loop, we'll want to take these attribute dicts and create the final contact object.
        # Keys should be some sort of hash using all of a contacts metadata,
        # that way we can match dict entries across class attribute_dictionaries.
        return attribute_dicts

    def merge_two_contacts(self, c1, c2):
        return Contact().init_from_merging_two_contacts(c1, c2)

    def update_contact_metadata_in_attribute_dicts(self, attribute_dicts, attributes_stored, attribute_keys, updated_metadata):
        for i, attribute in enumerate(attributes_stored):
            attribute_dicts[attribute][attribute_keys[i]] = updated_metadata
        return attribute_dicts

    def get_unique_contacts_from_attribute_dicts(self, attribute_dicts):
        unique_contacts = {}

        for attribute_dict in attribute_dicts.items():
            contact_ids = attribute_dict.keys()

            for contact_id in contact_ids:
                # Only keep contacts who aren't already saved, blacklisted, or already cached
                if self.contact_is_blacklisted(contact_id) or self.contact_is_saved(contact_id):
                    continue

                if self.saved_contact_should_be_updated(contact_id):
                    self.contacts_queued_to_update[contact_id] = attribute_dict[contact_id]
                    continue

                unique_contacts[contact_id] = attribute_dict[contact_id]

        return unique_contacts

    def contact_is_blacklisted(self, contact_id):
        return contact_id in self.blacklisted_contact_ids or contact_id in self.contacts_queued_for_blacklist

    def contact_is_saved(self, contact_id):
        return contact_id in self.saved_contacts or contact_id in self.contacts_queued_to_save

    def saved_contact_should_be_updated(self, contact_id):
        return False

    def select_contacts(self, contacts):
        contacts_to_save = []
        contacts_to_blacklist = []

        contact_ids = contacts.keys()
        index_of_contact_under_review = 0

        while index_of_contact_under_review is not len(contacts):
            contact_id = contact_ids[index_of_contact_under_review]
            current_contact = contacts[contact_id]
            # Present contact
            # Save or blacklist contact based on user input
            # Process next contact
            index_of_contact_under_review += 1

        return contacts_to_save, contacts_to_blacklist

    def save_contact(self, contact_id, contact):
        self.contacts_queued_to_save[contact_id] = contact

    def blacklist_contact(self, contact_id):
        self.contacts_queued_for_blacklist[contact_id] = True

    def persist_contacts_to_db(self):
        if len(self.contacts_queued_to_save.keys()):
            # add to push
            pass

        if len(self.contacts_queued_for_blacklist.keys()):
            # add to push
            pass

        # persist self.contacts_queued_to_save and self.contact_ids_queued_for_blacklist in one call
        return True

    def view_saved_contacts(self):
        pass


if __name__ == '__main__':
    contactImporter = ContactImporter()

