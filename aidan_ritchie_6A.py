#Create functions to validate phone numbers, social security numbers and zip codes
# using regular expressions. Create a main function to get input from a user and
# then displaying if the phone number, social security number and zip code they entered is valid.

#import re to be able to use regular expressions in code
import re

#create function, passing in "phone" that creates regular expression so that
#user's input can be validated or invalidated, using re.match
def validate_phone_number(phone):
    #create pattern to have a specific format that is required from user
    pattern = r'^\(\d{3}\)-\d{3}-\d{4}$'  # Format: (123) 456-7890
    return re.match(pattern, phone) is not None

#create another function with same goal, but for a user's SSN
def validate_ssn(ssn):
    #create pattern for specific format
    pattern = r'^\d{3}-\d{2}-\d{4}$'  # Format: 123-45-6789
    return re.match(pattern, ssn) is not None

#create another function with same goal, but for user's zip code.
def validate_zip_code(zip_code):
    #create pattern for specific format
    pattern = r'^\d{5}(-\d{4})?$'  # Format: 12345 or 12345-6789
    return re.match(pattern, zip_code) is not None

#create main function that will ask for user input and print validity
def main():

    #assign variables, ask for input
    phone = input("Enter your phone number (ex: (123)-345-7890): ")
    ssn = input("Enter your social security number (ex: 123-45-6789): ")
    zip_code = input("Enter your zip code (ex: 12345 or 12345-6789): ")

    #validate inputs
    phone_valid = validate_phone_number(phone)
    ssn_valid = validate_ssn(ssn)
    zip_code_valid = validate_zip_code(zip_code)

    #print results using if-else statements
    print("\nValidation Results:")
    print(f"Phone Number Valid: {'Valid' if phone_valid else 'Invalid'}")
    print(f"Social Security Number Valid: {'Valid' if ssn_valid else 'Invalid'}")
    print(f"Zip Code Valid: {'Valid' if zip_code_valid else 'Invalid'}")

#call function
main()
