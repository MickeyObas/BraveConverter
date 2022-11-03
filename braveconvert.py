"""
- Take CSV as input
- Generate a CHIP-007 compatible JSON file for each CSV input row
- Generate the sha256 encryption of each file
- Append the sha256 hash to each line in the original csv (filename.output.csv)
"""

import csv 
import json
import hashlib
import pandas as pd

import os
import argparse

# Error messages 
INVALID_FILETYPE_MSG = "Error: Whoops. Invalid file format. %s must be a .csv file."
INVALID_PATH_MSG = "Error: Whoops. Invalid file/path name. Path %s does not exist."

def validate_file(file_name):
    '''
    Validate file name and path.
    '''
    if not valid_filetype(file_name):
        print(INVALID_PATH_MSG%(file_name))
        print("If it does, it sure doesn't look like a CSV file. Please try again")
        quit()
    return

def valid_filetype(file_name):
    # Validate file type
    return file_name.endswith('.csv')

def valid_path(path):
    # Validate file type
    return os.path.exists(path)

def list_to_dict(lst):
    it = iter(lst)
    dict_to_return = dict(zip(it, it))
    return dict_to_return


def main():
    # Create parser object
    parser = argparse.ArgumentParser(description='Process your CSV file here and get the required output')
    # Defining argument(s)
    parser.add_argument("file", type=str, nargs=1, help="Reads your NFT csv file, generates the json files for each NFT, hashes them, then returns an updated CSV.",
    metavar="file_name", default=None)

    args = parser.parse_args()

    if args.file != None:
        validate_file(args.file[0])
        file_name = args.file[0]

    # I initiate an empty list which i'll temporarily use to hold hash values
    hash_list = []
    

    with open(file_name, 'r') as f:
        reader = csv.reader(f)

        for row in reader:
            attribute_list = []
            team_name = row[0]
            series_number = row[1]
            filename = row[2]
            name= row[3]
            description= row[4]
            gender = row[5]
            attributes = row[6]
           
            for attribute in attributes.split("; "):
                attribute_new = attribute.split(":")
                result = list_to_dict(attribute_new)
                attribute_list.append(result)

            uuid = row[7]

            # I create a response model using the format given by the HNG9 mentors, then named it 'nft'
            nft = {
                "format": "CHIP-0007",
                "name": name,
                "description": description,
                "minting_tool": "Team {}".format(team_name),
                "sensitive_content": False,
                "series_number": series_number,
                "series_total": 420,
                "attributes": attribute_list
                ,
                "collection": {
                    "name": "Zuri NFT tickets for free lunch",
                    "id": uuid,
                    "attributes": [
                        {
                            "type": "description",
                            "value": "Rewards for accomplishments during HNGi9"
                        }
                    ]
                },
            }

            # Each nft entry is dumped on its own '.json' file
            with open("{}.json".format(filename), 'w') as outfile:
                json.dump(nft, outfile, indent=4, separators=(", ", ": "))
                outfile.close()

            # This line of code prevents the script from hashing what it's not supposed to hash
            if filename == "Filename":
                pass

            else:
                with open("{}.json".format(filename), "rb") as f:
                    bytes = f.read()
                    readable_hash = hashlib.sha256(bytes).hexdigest()
                    hash_list.append(readable_hash)
                    f.close()
        
        # The newly generated sha256 hash values for each nft file is appended their respective rows in the original csv file, then exported to a new one
        csv_input = pd.read_csv(file_name)
        csv_input['Hash'] = hash_list
    
        csv_input.to_csv('filename.output.csv', index=False)


if __name__ == "__main__":
    # Calling the main function
    main()


        