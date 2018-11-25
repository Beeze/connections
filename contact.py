import class_utils


class ContactUtils:
    # EXCLUDED_MERGE_ATTRIBUTES: All Contact attribute we don't want to use when merging two or more Contact objects.
    EXCLUDED_MERGE_ATTRIBUTES = ['prefix', 'name', 'first_name', 'last_name', 'suffix', 'nickname', 'company', 'job_title',
                                 'birthday', 'gender', 'relationship', 'notes']
    LIST_ATTRIBUTES = ['company', 'job_title']

    def __init__(self):
        pass


class Contact:

    def __init(self):
        self.contact_id = -1
        self.prefix = ""
        self.name = ""
        self.first_name = ""
        self.last_name = ""
        self.suffix = ""
        self.nickname = ""
        self.birthday = ""
        self.gender = ""
        self.relationship = ""
        self.company = []
        self.job_title = []
        self.email = []
        self.phone = []
        self.addresses = []
        self.notes = []
        self.website = []
        self.twitter = []
        self.linkedin = []
        self.facebook = []
        self.instagram = []

    def __hash__(self):
        hash_code = 0
        if self.company and len(self.company) > 0:
            for company in self.company:
                hash_code += hash(company)

        if self.job_title and len(self.job_title) > 0:
            for job_title in self.job_title:
                hash_code += hash(job_title)

        if self.email and len(self.email) > 0:
            for email in self.email:
                hash_code += hash(email)

        if self.phone and len(self.phone) > 0:
            for phone in self.phone:
                hash_code += hash(phone)

        if self.addresses and len(self.addresses) > 0:
            for address in self.addresses:
                hash_code += hash(address)

        if self.notes and len(self.notes) > 0:
            for note in self.notes:
                hash_code += hash(note)

        if self.website and len(self.website) > 0:
            for website in self.website:
                hash_code += hash(website)

        if self.twitter and len(self.twitter) > 0:
            for twitter in self.twitter:
                hash_code += hash(twitter)

        if self.linkedin and len(self.linkedin) > 0:
            for linkedin in self.linkedin:
                hash_code += hash(linkedin)

        if self.facebook and len(self.facebook) > 0:
            for facebook in self.facebook:
                hash_code += hash(facebook)

        if self.instagram and len(self.instagram) > 0:
            for instagram in self.instagram:
                hash_code += hash(instagram)

        hash_code += hash(self.contact_id)
        hash_code += hash(self.prefix)
        hash_code += hash(self.name)
        hash_code += hash(self.first_name)
        hash_code += hash(self.last_name)
        hash_code += hash(self.suffix)
        hash_code += hash(self.nickname)
        hash_code += hash(self.birthday)
        hash_code += hash(self.gender)

        return hash_code

    @classmethod
    def init_from_icloud_csv_row(cls, row):
        cls.prefix = row.get('Name Prefix', '')
        cls.name = row.get('Name', '')
        cls.first_name = row.get('Given Name', '')
        cls.last_name = row.get('Family Name', '')
        cls.suffix = row.get('Name Suffix', '')
        cls.nickname = row.get('Nickname', '')
        cls.birthday = row.get('Birthday', '')
        cls.gender = row.get('Gender', '')

        cls.company = []

        if row.get(row.get('Organization Name', '')):
            cls.company.append(row.get('Organization Name', ''))

        cls.website = []

        if row.get('Website 1 - Value', ''):
            cls.website.append(row.get('Website 1 - Value', ''))

        cls.email = []

        if row.get('Email 1 - Value', ''):
            cls.email.append(row['Email 1 - Value'])

        if row.get('Email 2 - Value', ''):
            cls.email.append(row['Email 2 - Value'])

        if row.get('Email 3 - Value', ''):
            cls.email.append(row['Email 3 - Value'])

        cls.phone = []

        if row.get('Phone 1 - Value', ''):
            cls.phone.append(row['Phone 1 - Value'])

        if row.get('Phone 2 - Value', ''):
            cls.phone.append(row['Phone 2 - Value'])

        if row.get('Phone 3 - Value', ''):
            cls.phone.append(row['Phone 3 - Value'])

        cls.addresses = []

        if row.get('Address 1 - Value', ''):
            cls.addresses.append(row['Phone 3 - Value'])

        return cls

    @classmethod
    def init_from_apple_vcard(cls, vcard):
        cls.name = vcard.get('fn', '')
        cls.birthday = vcard.get('bday', '')

        cls.phone = []

        if vcard.get('tel'):
            cls.phone.append(vcard.get('tel'))

        cls.email = []

        if vcard.get('email'):
            cls.email.append(vcard.get('email'))

        cls.notes = []

        if vcard.get('note'):
            cls.notes.append(vcard.get('note'))

        cls.job_title = []

        if vcard.get('title'):
            cls.job_title.append(vcard.get('title'))

        cls.website = []

        if vcard.get('url'):
            cls.website.append(vcard.get('url'))

        return cls

    @classmethod
    def init_from_merging_two_contacts(cls, c1, c2):
        # TODO: How do we handle two contacts having different values for the same param?
        # TODO: Create method to handle choosing an attribute value from one of the Contact objects.
        attributes = class_utils.get_class_attributes(Contact())
        new_c = Contact()

        # Go through each attribute for Contact, and set with a value.
        for attribute in attributes:
            # Neither Contact() objects have this attribute, skip it
            if not class_utils.is_one_class_with_attribute(c1, c2, attribute):
                continue

            # Both Contact() objects have this attribute,
            # we'll append unique values from lists, and compare strings for likeness.
            # Each attribute type should have it's own validator, but for now, we'll just choose whichever string has
            # multiple strings.
            # TODO: give each attribute it's own validator/selector method
            if class_utils.both_classes_have_none_null_attributes(c1, c2, attribute):
                # TODO: figure out how to handle this case
                # String vs List
                continue
                pass

            # Only one of Contact() objects have this attribute, so we'll figure out which one and use it's value.
            setattr(new_c, attribute, class_utils.get_attribute_from_class(c1, c2, attribute))

        return new_c
