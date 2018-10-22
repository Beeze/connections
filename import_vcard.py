import vobject
from contact import Contact

filename = "vcard.vcf"
file = open(filename, "r", encoding="utf-8")

# TODO: make this a method
for vcard in vobject.readComponents(file):
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

    print(vcard.fn.value)