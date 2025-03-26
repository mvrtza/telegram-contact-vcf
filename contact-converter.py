import sys
import json

input_file = sys.argv[1]
output_file = sys.argv[2]

output_file = open(output_file, 'wb')

def to_vcf_string(first_name, last_name, phone):
    vcf_lines = [
    'BEGIN:VCARD',
    'VERSION:4.0',
    f'N:{last_name};{first_name}',
    f'FN:{first_name}{" " if last_name else ""}{last_name}',
    f'TEL:{phone}',
    'END:VCARD'
    ]
    vcf_string = '\n'.join(vcf_lines) + '\n'
    return vcf_string

with open(input_file, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    contacts_list = data['contacts']['list']
    for contact in contacts_list:
        first_name = contact['first_name']
        last_name = contact['last_name']
        if len(first_name) == 0 and len(last_name) == 0:
                continue
            
        phone = contact['phone_number']

        output_file.write(to_vcf_string(first_name, last_name, phone).encode('utf-8'))
    output_file.close()