class Contact:
    # EXCLUDED_MERGE_ATTRIBUTES: All Contact attribute we don't want to use when merging two or more Contact objects.
    EXCLUDED_MERGE_ATTRIBUTES = ['prefix', 'first_name', 'last_name', 'suffix', 'nickname', 'company', 'job_title',
                                 'birthday', 'gender', 'relationship', 'notes']
    LIST_ATTRIBUTES = ['company', 'job_title']

    def __init(self):
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

    @classmethod
    def init_from_icloud_csv_row(self, row):
        self.prefix = row.get('Name Prefix', '')
        self.name = row.get('Name', '')
        self.first_name = row.get('Given Name', '')
        self.last_name = row.get('Family Name', '')
        self.suffix = row.get('Name Suffix', '')
        self.nickname = row.get('Nickname', '')
        self.birthday = row.get('Birthday', '')
        self.gender = row.get('Gender', '')

        self.company = []

        if row.get(row.get('Organization Name', '')):
            self.company.append(row.get('Organization Name', ''))

        self.website = []

        if row.get('Website 1 - Value', ''):
            self.website.append(row.get('Website 1 - Value', ''))

        self.email = []

        if row.get('Email 1 - Value', ''):
            self.email.append(row['Email 1 - Value'])

        if row.get('Email 2 - Value', ''):
            self.email.append(row['Email 2 - Value'])

        if row.get('Email 3 - Value', ''):
            self.email.append(row['Email 3 - Value'])

        self.phone = []

        if row.get('Phone 1 - Value', ''):
            self.phone.append(row['Phone 1 - Value'])

        if row.get('Phone 2 - Value', ''):
            self.phone.append(row['Phone 2 - Value'])

        if row.get('Phone 3 - Value', ''):
            self.phone.append(row['Phone 3 - Value'])

        self.addresses = []

        if row.get('Address 1 - Value', ''):
            self.addresses.append(row['Phone 3 - Value'])

        return self

    @classmethod
    def init_from_apple_vcard(self, vcard):
        self.name = vcard.get('fn', '')
        self.birthday = vcard.get('bday', '')

        self.phone = []

        if vcard.get('tel'):
            self.phone.append(vcard.get('tel'))

        self.email = []

        if vcard.get('email'):
            self.email.append(vcard.get('email'))

        self.notes = []

        if vcard.get('note'):
            self.notes.append(vcard.get('note'))

        self.job_title = []

        if vcard.get('title'):
            self.job_title.append(vcard.get('title'))

        self.website = []

        if vcard.get('url'):
            self.website.append(vcard.get('url'))

        return self
