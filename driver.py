#!/usr/bin/env python3

# cli option(s) [1] csv location
import sys
import urllib.request
import urllib.parse
import base64


# https://stackoverflow.com/questions/13261802/converting-a-string-to-and-from-base-64/13267801
def string_to_base64_string(s):
    s2 = base64.b64encode(s.encode('UTF-8')).decode('UTF-8')
    return s2


# https://username:password@domains.google.com/nic/update?hostname=subdomain.yourdomain.com&myip=1.2.3.4

def make_request(username, password, fully_qualified_domain_name, ip):
    url = f"https://domains.google.com/nic/update?hostname={fully_qualified_domain_name}&myip={ip}"
    my_request = urllib.request.Request(url)
    auth = '%s:%s' % (username, password)
    auth_string = "Basic %s" % string_to_base64_string(auth)
    my_request.add_header("Authorization", auth_string)
    result = urllib.request.urlopen(my_request).read().decode('UTF-8')
    return result


def get_ip():
    return urllib.request.urlopen("https://api.ipify.org").read().decode('UTF-8')


# [0] username [1] password [2] fullyQualifiedName
def read_and_make_requests(file, ip):
    with open(file, 'r') as file:
        # trash first line because that's a header
        file.readline()
        for line in file:
            use_this = line.split(',')
            print(make_request(use_this[0].strip(), use_this[1].strip(), use_this[2].strip(), ip))


def main():
    # currently assuming there is a header and I'm ignoring it.
    if len(sys.argv) != 2:
        sys.exit('Either to few arguments or too many arguments. I need a csv file location')
    read_and_make_requests(sys.argv[1], get_ip())


main()
