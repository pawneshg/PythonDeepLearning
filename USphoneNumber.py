import re

def findPhoneNumber(string):
    r = re.compile(r"(\d{3}[-]??\d{3}[-]??\d{4}|\(\d{3}\)\s*\d{3}[-]??\d{4})")
    results = r.findall(string)
    return results

findPhoneNumber('124-1234-435789')
findPhoneNumber('(988) 678-9876')
