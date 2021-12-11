import re

s_all = 'user password database -v -A scanme.nmap.org -oX fileisfileyes'
# print(s_all)

database_info, scan_options = s_all.split('-', 1)

print(database_info)

print(scan_options)