import csv
from contact import Contact
# https://docs.google.com/spreadsheets/d/1Vb5xJNHkj3Dqx6gvFdmpgpve9rHfdrIq0VW5iS4IjME/edit#gid=824790542


class ICloudCSVImporter:

    filename = "csv.csv"
    desired_headers = {
        'Name': True,  # Full Name
        'Given Name': True,  # First Name
        'Family Name': True,  # Last Name
        'Name Prefix': True,
        'Name Suffix': True,
        'Nickname': True,
        'Organization 1 - Type': True,  # Company
        'Organization 1 - Name': True,  # Company
        'E-mail 1 - Type': True,
        'E-mail 1 - Value': True,
        'E-mail 2 - Type': True,
        'E-mail 2 - Value': True,
        'E-mail 3 - Type': True,
        'E-mail 3 - Value': True,
        'Phone 1 - Type': True,
        'Phone 1 - Value': True,
        'Phone 2 - Type': True,
        'Phone 2 - Value': True,
        'Phone 3 - Type': True,
        'Phone 3 - Value': True,
        'Address 1 - Type': True,
        'Address 1 - Formatted': True,
        'Website 1 - Type': True,
        'Website 1 - Value': True,
        'Birthday': True,
        'Gender': True,
        'Notes': True,
    }
    header_key_map = {}

    def parse_csv(self):
        with open(self.filename, 'rt', encoding='utf-8') as csv_file:
            has_header = csv.Sniffer().has_header(csv_file.readline())

            if not has_header:
                # we can't use this file
                print("csv file must have a header.")
                exit()

            csv_file.seek(0)
            contact_reader = csv.reader(csv_file)

            header = next(contact_reader)
            self.header_key_map = {}

            # Create a map of key => index, for easy parsing of each row.
            for i, key in enumerate(header):
                if key in self.desired_headers:
                    self.header_key_map[key] = i

            # Ensure we got an index for every desired header.
            assert len(self.header_key_map.keys()) is len(self.desired_headers.keys())

            for row in contact_reader:
                contact = self.convert_row_into_contact_domain_object(row)

                # Check if name already exists in database.
                # if name exists, ask if can merge.
                should_merge = self.check_for_merge(contact)
                # if can merge, merge.
                if should_merge:
                    pass
                # Check if we should save this contact
                # if no, continue
                # if yes:
                # convert row into contact domain object.
                # save contact in our db, and update our local cache (saved_contacts lists [name, number, etc.])
                # with new value.

    def convert_row_into_contact_domain_object(self, row):
        raw_row_object = {}

        print(len(row))
        # Create an object using header fields as keys.
        for key, index in self.header_key_map.items():
            raw_row_object[key] = row[index]
        # Now that row is an object, we'll init a Contact domain object.
        return Contact().init_from_icloud_csv_row(raw_row_object)

    def check_for_merge(self, contact):
        return False
