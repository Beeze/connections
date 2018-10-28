class Contact:
    prefix = ""
    name = ""
    first_name = ""
    last_name = ""
    suffix = ""
    nickname = ""
    company = ""
    job_title = ""
    email = []
    phone = []
    addresses = []
    birthday = ""
    gender = ""
    website = ""
    relationship = ""
    twitter = ""
    linkedin = ""
    facebook = ""
    instagram = ""
    notes = ""

    def init_from_icloud_csv_row(self, row):
        self.prefix = row.get('Name Prefix', '')
        self.name = row.get('Name', '')
        self.first_name = row.get('Given Name', '')
        self.last_name = row.get('Family Name', '')
        self.suffix = row.get('Name Suffix', '')
        self.nickname = row.get('Nickname', '')
        self.company = row.get('Organization Name', '')
        self.birthday = row.get('Birthday', '')
        self.gender = row.get('Gender', '')
        self.website = row.get('Website 1 - Value', '')

        if row.get('Email 1 - Value', ''):
            self.email.append(row['Email 1 - Value'])

        if row.get('Email 2 - Value', ''):
            self.email.append(row['Email 2 - Value'])

        if row.get('Email 3 - Value', ''):
            self.email.append(row['Email 3 - Value'])

        if row.get('Phone 1 - Value', ''):
            self.phone.append(row['Phone 1 - Value'])

        if row.get('Phone 2 - Value', ''):
            self.phone.append(row['Phone 2 - Value'])

        if row.get('Phone 3 - Value', ''):
            self.phone.append(row['Phone 3 - Value'])

        if row.get('Address 1 - Value', ''):
            self.addresses.append(row['Phone 3 - Value'])

        return self

    def init_from_apple_vcard(self, vcard):
        self.name = vcard.get('fn', '')
        self.phone = vcard.get('tel', '')
        self.notes = vcard.get('note', '')
        self.email = vcard.get('email', '')
        self.birthday = vcard.get('bday', '')
        self.website = vcard.get('url', '')
        self.job_title = vcard.get('title', '')

        return self
