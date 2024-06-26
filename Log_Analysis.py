import os
import re

# Add this file in the Log file location
path = "D:\Logs"
file_size = 0

# Change the directory
os.chdir(path)


with open('result1.log', 'w') as d:
    d.write("")


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        aadhar = r"[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}"
        pancard = r"[A-Z]{5}[0-9]{4}[A-Z]{1}"
        Account_number = r"[0-9]{2}[33|11|43]{2}[0-9]{11}[01]{1}"
        Credit_card = "^(?:4[0-9]{12}(?:[0-9]{3})?|[25][1-7][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$"
        passport = r"[A-Z]{1}[1-9]{1}[0-9]{6}$"
        cvv = r"\b(?:CVV|cvv)\b"
        dob = r"\b(?:DOB|D.O.B|dob)\b"
        text = f.read()
        aadhar_result = re.findall(aadhar, text, re.MULTILINE)
        pancard_result = re.findall(pancard, text, re.MULTILINE)
        account_result = re.findall(Account_number, text, re.MULTILINE)
        credit_result = re.findall(Credit_card, text, re.MULTILINE)
        cvv_result = re.findall(cvv, text, re.MULTILINE)
        passport_result = re.findall(passport, text, re.MULTILINE)
        dob_result = re.findall(dob, text, re.MULTILINE)
        print(f.read())
        file_size = os.path.getsize("result1.log")
        if file_size == 0:
            with open("result1.log", 'w') as d:
                d.write(str(file_path))
                d.write('\n')
                d.write('\nAadhar Result: \n')
                for x in aadhar_result:
                    d.write(str(x))
                    d.write('\n')

                d.write('\nPanCard Result: \n')
                for x in pancard_result:
                    d.write(str(x))
                    d.write('\n')

                d.write('\nAccount Result: \n')
                for x in account_result:
                    d.write(str(x))
                    d.write('\n')

                d.write('\nCredit Card Result: \n')
                for x in credit_result:
                    d.write(str(x))
                    d.write('\n')
                d.write('\n')

                d.write('\nCvv Result: \n')
                for x in cvv_result:
                    d.write(str(x))
                    d.write('\n')
                d.write('\n')

                d.write('\nPassport Result: \n')
                for x in passport_result:
                    d.write(str(x))
                    d.write('\n')
                d.write('\n')

                d.write('\nDOB Result: \n')
                for x in dob_result:
                    d.write(str(x))
                    d.write('\n')
                d.write('\n')

        else:
            with open("result1.log", 'a') as d:
                d.write(str(file_path))
                d.write('\n')
                d.write('\nAadhar Result: \n')
                for x in aadhar_result:
                    d.write(str(x))
                    d.write('\n')

                d.write('\nPanCard Result: \n')
                for x in pancard_result:
                    d.write(str(x))
                    d.write('\n')

                d.write('\nAccount Result: \n')
                for x in account_result:
                    d.write(str(x))
                    d.write('\n')

                d.write('\nCredit Card Result: \n')
                for x in credit_result:
                    d.write(str(x))
                    d.write('\n')
                d.write('\n')

                d.write('\nCvv Result: \n')
                for x in cvv_result:
                    d.write(str(x))
                    d.write('\n')
                d.write('\n')

                d.write('\nPassport Result: \n')
                for x in passport_result:
                    d.write(str(x))
                    d.write('\n')
                d.write('\n')

                d.write('\nDOB Result: \n')
                for x in dob_result:
                    d.write(str(x))
                    d.write('\n')
                d.write('\n')


for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
        # call read text file function
        read_text_file(file_path)
