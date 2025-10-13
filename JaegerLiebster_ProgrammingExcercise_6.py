import re

def validate_phone(phone_number):
    #Validates phone numbers based on a U.S. format
    pattern = re.compile(r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
    if pattern.match(phone_number):
        return True
    return False

def validate_ssn(ssn):
    #Validates SSN
    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    if pattern.match(ssn):
        return True
    return False

def validate_zip_code(zip_code):
    #Validates ZIP code
    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    if pattern.match(zip_code):
        return True
    return False

def run_tests():
    #Tests validity of phone number, ssn, and zip code against common formats
    print("Testing validity")

    # Test cases
    phone_tests = {
        "123-456-7890": True, "(123) 456-7890": True, "123.456.7890": True,
        "123 456 7890": True, "1234567890": True, "123-456-789": False,
        "123-456-78900": False, "abc-def-ghij": False
    }
    ssn_tests = {
        "123-45-6789": True, "123-456-789": False, "123456789": False,
        "12-34-5678": False, "123-45-67890": False
    }
    zip_tests = {
        "12345": True, "12345-6789": True, "1234": False,
        "123456": False, "12345-678": False, "12345-67890": False
    }

    # Execute tests
    for number, expected in phone_tests.items():
        assert validate_phone(number) == expected
    print("Phone number valid.")

    for ssn, expected in ssn_tests.items():
        assert validate_ssn(ssn) == expected
    print("SSN valid.")

    for zc, expected in zip_tests.items():
        assert validate_zip_code(zc) == expected
    print("ZIP code valid.")

def main():
    # Gets and validates user input

    phone = input("Enter a phone number: ")
    ssn = input("Enter a Social Security Number (XXX-XX-XXXX): ")
    zip_code = input("Enter a ZIP code (XXXXX or XXXXX-XXXX): ")

    # Display validation results
    print("\n--- Validation Results ---")
    if validate_phone(phone):
        print(f"Phone Number '{phone}' is valid.")
    else:
        print(f"Phone Number '{phone}' is invalid.")

    if validate_ssn(ssn):
        print(f"Social Security Number '{ssn}' is valid.")
    else:
        print(f"Social Security Number '{ssn}' is invalid.")

    if validate_zip_code(zip_code):
        print(f"ZIP Code '{zip_code}' is valid.")
    else:
        print(f"ZIP Code '{zip_code}' is invalid.")


if __name__ == "__main__":
    run_tests()
    print("\n--- User Input Validation ---\n")
    main()