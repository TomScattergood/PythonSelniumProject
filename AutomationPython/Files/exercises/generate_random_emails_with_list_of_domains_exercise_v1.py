"""
Exercises:
Create a file with list of randomly generated email addresses.
The email addresses must have domain name from the
given list of domains.
* Domain list is provided as variable 'list_of_domains'
"""

import random
import string

list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

length_of_email = 10
number_of_emails_per_domain = 20
letters = string.ascii_lowercase
output_path = 'out_generate_random_email_with_list_of_domains_v1.csv'


all_emails = []
for domain in list_of_domains:
    for i in range(number_of_emails_per_domain):
        random_string = ''.join(random.choice(letters) for i in range(length_of_email))
        email = f"{random_string}@{domain}"
        all_emails.append(email)

with open (output_path, 'w') as f:
    f.write(',\n'.join(all_emails))