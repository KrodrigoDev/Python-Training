import re

regex_ip = re.compile(r'^(2[0-4][0-9])')
for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, regex_ip.findall(ip))
