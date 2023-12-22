import json
import csv
from datetime import datetime

# Read the JSON data from a file or API endpoint
with open('data.json') as json_file:
    data = json.load(json_file)

# Extract the fields you want to include in the CSV file
fields = ['username', 'address', 'formattedDate AM', 'formattedDate PM', 'image', 'imageUrl']

# Open a new CSV file and write the header row
with open('data1.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(fields)

    # Write each data row to the CSV file
    for entry_key, entry_value in data.items():
        if isinstance(entry_value, dict):
            # Check if all values in the dictionary are empty strings
            if all(value == '' for value in entry_value.values()):
                print(f"Skipping entry with key {entry_key} as it is empty.")
            else:
                # Extract AM/PM from the formattedDate
                date_str = entry_value.get('formattedDate', '')
                am_pm = ''
                formatted_date_am = ''
                formatted_date_pm = ''
                if date_str:
                    # Try parsing with the initial format
                    try:
                        date_obj = datetime.strptime(date_str, '%B %d, %Y, %I:%M %p')
                        am_pm = date_obj.strftime('%p')
                        if am_pm == 'AM':
                            formatted_date_am = date_obj.strftime('%B %d, %Y at %I:%M %p')
                        else:
                            formatted_date_pm = date_obj.strftime('%B %d, %Y at %I:%M %p')
                    except ValueError:
                        # If initial format fails, try parsing with the new format
                        try:
                            date_obj = datetime.strptime(date_str, '%B %d, %Y at %I:%M %p')
                            am_pm = date_obj.strftime('%p')
                            if am_pm == 'AM':
                                formatted_date_am = date_obj.strftime('%B %d, %Y at %I:%M %p')
                            else:
                                formatted_date_pm = date_obj.strftime('%B %d, %Y at %I:%M %p')
                        except ValueError:
                            print(f"Error parsing date for entry with key {entry_key}: {date_str}")

                # Write to the CSV file
                writer.writerow([
                    entry_value.get('username', ''),
                    entry_value.get('address', ''),
                    formatted_date_am,
                    formatted_date_pm,
                    entry_value.get('image', ''),
                    entry_value.get('imageUrl', '')
                ])
        else:
            # Handle the case where the entry_value is not a dictionary
            print(f"Processing non-dictionary entry with key {entry_key}. Content: {entry_value}")
            # Directly write the entry_value as a single cell in the CSV file
            writer.writerow([entry_value])



# import json
# import csv
# from datetime import datetime

# # Read the JSON data from a file or API endpoint
# with open('data.json') as json_file:
#     data = json.load(json_file)

# # Extract the fields you want to include in the CSV file
# fields = ['username', 'address', 'formattedDate AM', 'formattedDate PM', 'image', 'imageUrl']

# # Open a new CSV file and write the header row
# with open('data1.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(fields)

#     # Write each data row to the CSV file
#     for entry_key, entry_value in data.items():
#         if isinstance(entry_value, dict):
#             # Check if all values in the dictionary are empty strings
#             if all(value == '' for value in entry_value.values()):
#                 print(f"Skipping entry with key {entry_key} as it is empty.")
#             else:
#                 # Extract AM/PM from the formattedDate
#                 date_str = entry_value.get('formattedDate', '')
#                 am_pm = ''
#                 formatted_date_am = ''
#                 formatted_date_pm = ''
#                 if date_str:
#                     try:
#                         date_obj = datetime.strptime(date_str, '%B %d, %Y at %I:%M %p')
#                         am_pm = date_obj.strftime('%p')
#                         if am_pm == 'AM':
#                             formatted_date_am = date_obj.strftime('%B %d, %Y at %I:%M %p')
#                         else:
#                             formatted_date_pm = date_obj.strftime('%B %d, %Y at %I:%M %p')
#                     except ValueError:
#                         print(f"Error parsing date for entry with key {entry_key}: {date_str}")

#                 # Write to the CSV file
#                 writer.writerow([
#                     entry_value.get('username', ''),
#                     entry_value.get('address', ''),
#                     formatted_date_am,
#                     formatted_date_pm,
#                     entry_value.get('image', ''),
#                     entry_value.get('imageUrl', '')
#                 ])
#         else:
#             # Handle the case where the entry_value is not a dictionary
#             print(f"Processing non-dictionary entry with key {entry_key}. Content: {entry_value}")
#             # Directly write the entry_value as a single cell in the CSV file
#             writer.writerow([entry_value])





# import json
# import csv

# # Read the JSON data from a file or API endpoint
# with open('data.json') as json_file:
#     data = json.load(json_file)

# # Extract the fields you want to include in the CSV file
# fields = ['username', 'address', 'formattedDate', 'image', 'imageUrl']
# # fields = ['address', 'formattedDate', 'image', 'imageUrl', 'username']

# # Open a new CSV file and write the header row
# with open('data1.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(fields)

#     # Write each data row to the CSV file
#     for entry_key, entry_value in data.items():
#         if isinstance(entry_value, dict):
#             # Check if all values in the dictionary are empty strings
#             if all(value == '' for value in entry_value.values()):
#                 print(f"Skipping entry with key {entry_key} as it is empty.")
#             else:
#                 writer.writerow([entry_value.get(field, '') for field in fields])
#         else:
#             # Handle the case where the entry_value is not a dictionary
#             print(f"Processing non-dictionary entry with key {entry_key}. Content: {entry_value}")
#             # Directly write the entry_value as a single cell in the CSV file
#             writer.writerow([entry_value])
