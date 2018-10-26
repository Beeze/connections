import vobject
from contact import Contact

filename = "vcard.vcf"

excludes = {'version', 'prodid', 'org', 'rev', 'x-ablabel', 'x-abshowas', 'x-abadr', 'x-abrelatednames', 'x-apple-sublocality', 'x-apple-subadministrativearea', 'x-activity-alert'}

fields = {}

with open(filename, "r", encoding="utf-8") as vcard_file:
    # Grab all the vcards in the file and turn into iterable
    vcards = vobject.readComponents(vcard_file.read())

    # Select first vcard in stack
    vcard = next(vcards, None)

    # While we still have a vcard object
    while vcard is not None:

        # Go through each contentLine of the vcard
        for content in vcard.contents:
            # Skip contentLine's we don't care about
            # TODO: key each entry in fields with unique identifier.
            # Also, handle collisions in keys - should go through unique fields (email, phone etc.) and find a match.
            # if match found, go through every field of each object, append any differences in value.
            # If no match found, either ask user if both entries are the same (which would result in merge), or,
            # Created another entry for this user.
            # Maybe we can avoid all of this by just keying with a random UUID? or changing them to Contact objects?
            if content not in excludes:
                content_line = vcard.contents[content]
                # content_line can have one or more items.
                if len(content_line) is 1:
                    fields[content] = content_line[0].value
                else:
                    fields[content] = []
                    # Go through each content line item, parse, and add to list.
                    for item in content_line:
                        fields[content].append(item.value)

        # Increment vcard we have selected
        vcard = next(vcards, None)

    print(fields)


def parse_contentLine(contentLine):
    pass
    # if typ

    # Check if name already exists in database.
        # if name exists, ask if can merge.
            # if can merge, merge.
            # If no merge, fall through.

    # Check if we should save this contact
        # if no
            # continue
        # if yes:
            # convert vcard into contact domain object.
            # save contact in our db, and update our local cache (saved_contacts lists [name, number, etc.])
            # with new value.