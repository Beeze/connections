import vobject
from contact import Contact


class AppleVcardImporter:
    filename = "vcard.vcf"
    excludes = {
        'n',
        'version',
        'prodid',
        'org',
        'rev',
        'x-ablabel',
        'x-abshowas',
        'x-abadr',
        'x-abrelatednames',
        'x-apple-sublocality',
        'x-apple-subadministrativearea',
        'x-activity-alert'
    }
    fields = {}
    contacts = []

    def get_contacts_from_vcard_file(self):
        with open(self.filename, "r", encoding="utf-8") as vcard_file:
            # Grab all the vcards in the file and turn into iterable
            vcards = vobject.readComponents(vcard_file.read())

            # Select first vcard in stack
            vcard = next(vcards, None)

            # While we still have a vcard object
            while vcard is not None:
                self.fields = {}

                # Go through each contentLine of the vcard
                for content in vcard.contents:

                    # Skip contentLine's we don't care about
                    if content not in self.excludes:
                        content_line = vcard.contents[content]

                        # content_line can have one or more items.
                        if len(content_line) is 1:
                            self.fields[content] = content_line[0].value

                        else:
                            self.fields[content] = []

                            # Go through each content line item, parse, and add to list.
                            for item in content_line:
                                self.fields[content].append(item.value)

                # Only save named contacts.
                if 'fn' in self.fields:
                    contact = Contact().init_from_apple_vcard(self.fields)
                    self.contacts.append(contact)

                # Increment vcard we have selected
                vcard = next(vcards, None)

        return self.contacts
