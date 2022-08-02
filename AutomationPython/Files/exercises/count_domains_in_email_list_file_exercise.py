"""
Read the list of email addresses from the input file and create a dictionary
with keys being domain name and value being the number of occurrences for the domain.
In other words count how many times each domain exists and create a report of the count as a dictionary.
Save the output into a .json file.

- input file: count_domains_in_email_list_file_exercise_input.csv
- output file: count_domains_in_email_list_file_exercise_output.json

Example output:
{'yahoo.com': 19, 'gmail.com': 20, 'msn.com': 16, 'supersqa.com': 20, 'outlook.com': 25}

"""
import json

input_file = "count_domains_in_email_list_file_exercise_input.csv"
output_file = "count_domains_in_email_list_file_exercise_output.json"


def get_emails_from_file(file_path):
    with open(file_path, 'r') as f:
        emails_raw = f.readlines()
    emails_clean = [i.strip(',\n') for i in emails_raw]

    return emails_clean


def count_domains(list_of_emails):
    domains_list = []
    for email in list_of_emails:
        domain = email.split('@')[-1]
        domains_list.append(domain)

    unique_domains = set(domains_list)

    email_count = dict()
    for domain in unique_domains:
        email_count[domain] = domains_list.count(domain)
    return email_count

def save_output_in_json_file(counts_dict, json_file_path):
    print(f"Saving file: {json_file_path}")
    with open(json_file_path, 'w') as f:
        json_obj = json.dumps(counts_dict)
        f.write(json_obj)

emails_list = get_emails_from_file(input_file)

counts = count_domains(emails_list)
print(counts)
save_output_in_json_file(counts, output_file)