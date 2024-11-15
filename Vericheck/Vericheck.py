import re
import argparse
import requests
import sys
from colorama import Fore, Style

def display_menu(page=1):
    print(Fore.CYAN + f"\nWelcome to VeriCheck - Your Advanced CLI Validator (Page {page})" + Style.RESET_ALL)
    print(Fore.YELLOW + "===============================================" + Style.RESET_ALL)
    if page == 1:
        print("Select the type of data to check (General):")
        print("1. Email Address")
        print("2. IP Address")
        print("3. URL")
        print("4. Domain")
        print("5. Phone Number")
        print("6. MAC Address")
        print("7. ZIP Code")
        print(">. Next Page")
        print("0. Exit")
    elif page == 2:
        print("Select the type of data to check (Vehicles):")
        print("8. VIN (Vehicle Identification Number)")
        print("9. License Plate Number")
        print("10. Vehicle Registration Certificate Number")
        print("11. IMEI (International Mobile Equipment Identity)")
        print(">. Next Page")
        print("<. Previous Page")
        print("0. Exit")
    elif page == 3:
        print("Select the type of data to check (Finance & Identity):")
        print("12. Credit Card Number")
        print("13. SSN")
        print("14. IBAN (International Bank Account Number)")
        print("15. Bitcoin Address")
        print("16. CPF (Brazilian Individual Taxpayer Identifier)")
        print("17. CNPJ (Brazilian Company Identifier)")
        print(">. Next Page")
        print("<. Previous Page")
        print("0. Exit")
    elif page == 4:
        print("Select the type of data to check (Social Media and Online Accounts):")
        print("18. Discord Token")
        print("19. Instagram Handle")
        print("20. Twitter Handle")
        print("21. Facebook Profile ID")
        print("22. LinkedIn Profile URL")
        print("23. Telegram Username")
        print(">. Next Page")
        print("<. Previous Page")
        print("0. Exit")
    elif page == 5:
        print("Select the type of data to check (Location-based and Geographical):")
        print("24. Latitude and Longitude Coordinates")
        print("25. Geohash Code")
        print("26. Postal Address Validator")
        print("27. Country Code")
        print("28. Airport IATA Code")
        print(">. Next Page")
        print("<. Previous Page")
        print("0. Exit")
    elif page == 6:
        print("Select the type of data to check (Technology Identifiers):")
        print("29. UUID (Universally Unique Identifier)")
        print("30. IP Range (CIDR)")
        print("31. GitHub Repository URL")
        print("32. SSH Key Validator")
        print("33. Slack Workspace URL")
        print(">. Next Page")
        print("<. Previous Page")
        print("0. Exit")
    elif page == 7:
        print("Select the type of data to check (Medical and Health Identifiers):")
        print("34. NPI (National Provider Identifier, US)")
        print("35. NHS Number (UK Healthcare Number)")
        print("36. Medical Insurance Policy Number")
        print("37. Prescription Code Validator")
        print(">. Next Page")
        print("<. Previous Page")
        print("0. Exit")
    elif page == 8:
        print("Select the type of data to check (Document Identifiers):")
        print("38. ISBN (Books and Publications)")
        print("39. ISSN (International Standard Serial Number)")
        print("40. DOI (Digital Object Identifier for Research Papers)")
        print("<. Previous Page")
        print("0. Exit")
    print(Fore.YELLOW + "===============================================" + Style.RESET_ALL)

def get_user_input():
    return input(Fore.GREEN + "\nEnter your choice: " + Style.RESET_ALL)

def get_data_input(data_type):
    return input(Fore.BLUE + f"Enter the {data_type}: " + Style.RESET_ALL)

# Validators for different data types
validators = {
    'email': r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
    'ip': r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
    'url': r'^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$',
    'domain': r'^([a-zA-Z0-9-]{2,63})\.([a-zA-Z\.]{2,5})$',
    'phone_number': r'^\+?[1-9]\d{1,14}$',
    'mac_address': r'^[0-9A-Fa-f]{2}([-:])[0-9A-Fa-f]{2}(\1[0-9A-Fa-f]{2}){4}$',
    'zip_code': r'^[0-9]{5}(?:-[0-9]{4})?$',
    'vin': r'^[A-HJ-NPR-Z0-9]{17}$',
    'license_plate': r'^[A-Z0-9- ]{1,10}$',
    'vehicle_registration': r'^[A-Z0-9]{1,15}$',
    'imei': r'^\d{15}$',
    'credit_card': r'^[0-9]{16}$',
    'ssn': r'^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$',
    'iban': r'^[A-Z]{2}\d{2}[A-Z0-9]{1,30}$',
    'bitcoin_address': r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$',
    'cpf': r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
    'cnpj': r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$',
    'discord_token': r'[A-Za-z\d]{24}\.[A-Za-z\d]{6}\.[A-Za-z\d-_]{27}',
    'instagram_handle': r'^@[A-Za-z0-9_]{1,15}$',
    'twitter_handle': r'^@[A-Za-z0-9_]{1,15}$',
    'facebook_profile_id': r'^[0-9]{1,20}$',
    'linkedin_profile_url': r'^https:\/\/([a-z]{2,3}\.)?linkedin\.com\/.*$',
    'telegram_username': r'^@[A-Za-z0-9_]{5,32}$',
    'latitude_longitude': r'^-?\d{1,3}\.\d+,\s?-?\d{1,3}\.\d+$',
    'geohash': r'^[a-z0-9]{1,12}$',
    'postal_address': r'^[a-zA-Z0-9 \n,.-]+$',
    'country_code': r'^[A-Z]{2}$',
    'airport_iata_code': r'^[A-Z]{3}$',
    'uuid': r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$',
    'ip_range': r'^([0-9]{1,3}\.){3}[0-9]{1,3}\/\d{1,2}$',
    'github_repo_url': r'^https:\/\/github\.com\/[^\s/$.?#].[^\s]*$',
    'ssh_key': r'^ssh-(rsa|dss|ed25519) [A-Za-z0-9+/=]+ [^\n]*$',
    'slack_workspace_url': r'^https:\/\/([a-z0-9]+)\.slack\.com$',
    'npi': r'^\d{10}$',
    'nhs_number': r'^[0-9]{10}$',
    'medical_insurance': r'^[A-Za-z0-9]{8,15}$',
    'prescription_code': r'^[A-Z0-9]{5,10}$',
    'isbn': r'^(97(8|9))?\d{9}(\d|X)$',
    'issn': r'^\d{4}-\d{3}[\dxX]$',
    'doi': r'^10\.\d{4,9}/[-._;()/:A-Z0-9]+$',
}

# Function to validate input
def validate_input(data_type, data):
    pattern = validators.get(data_type)
    if not pattern:
        return False
    return re.match(pattern, data)

def main():
    page = 1
    while True:
        display_menu(page)
        choice = get_user_input()

        if choice == '0':
            print(Fore.RED + "\nThank you for using VeriCheck. Goodbye!" + Style.RESET_ALL)
            sys.exit()
        elif choice == '<' and page > 1:
            page -= 1
        elif choice == '>' and page < 8:
            page += 1
        else:
            data_types = {
                '1': 'email',
                '2': 'ip',
                '3': 'url',
                '4': 'domain',
                '5': 'phone_number',
                '6': 'mac_address',
                '7': 'zip_code',
                '8': 'vin',
                '9': 'license_plate',
                '10': 'vehicle_registration',
                '11': 'imei',
                '12': 'credit_card',
                '13': 'ssn',
                '14': 'iban',
                '15': 'bitcoin_address',
                '16': 'cpf',
                '17': 'cnpj',
                '18': 'discord_token',
                '19': 'instagram_handle',
                '20': 'twitter_handle',
                '21': 'facebook_profile_id',
                '22': 'linkedin_profile_url',
                '23': 'telegram_username',
                '24': 'latitude_longitude',
                '25': 'geohash',
                '26': 'postal_address',
                '27': 'country_code',
                '28': 'airport_iata_code',
                '29': 'uuid',
                '30': 'ip_range',
                '31': 'github_repo_url',
                '32': 'ssh_key',
                '33': 'slack_workspace_url',
                '34': 'npi',
                '35': 'nhs_number',
                '36': 'medical_insurance',
                '37': 'prescription_code',
                '38': 'isbn',
                '39': 'issn',
                '40': 'doi'
            }

            if choice in data_types:
                data_type = data_types[choice]
                data = get_data_input(data_type)
                is_valid = validate_input(data_type, data)

                if is_valid:
                    print(Fore.GREEN + f"\nValid {data_type.replace('_', ' ').title()}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"\nInvalid {data_type.replace('_', ' ').title()}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "\nInvalid choice. Please try again." + Style.RESET_ALL)

if __name__ == '__main__':
    main()
