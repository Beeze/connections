import csv
# https://docs.google.com/spreadsheets/d/1Vb5xJNHkj3Dqx6gvFdmpgpve9rHfdrIq0VW5iS4IjME/edit#gid=824790542
filename = "csv.csv"

# TODO: make this a method
with open(filename, 'rt', encoding='utf-8') as csv_file:
    has_header = csv.Sniffer().has_header(csv_file.readline())

    if not has_header:
        # we can't use this file
        print("csv file must have a header.")
        exit()

    csv_file.seek(0)
    contact_reader = csv.reader(csv_file, delimiter=' ', quotechar = "|")

    header = next(contact_reader)

    for row in contact_reader:
        print(row)
        # Check if name already exists in database.
        # if name exists, ask if can merge.
        # if can merge, merge.
        # If no merge, fall through.

        # Check if we should save this contact
        # if no, continue
        # if yes:
        # convert row into contact domain object.
        # save contact in our db, and update our local cache (saved_contacts lists [name, number, etc.])
        # with new value.
