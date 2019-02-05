#!/usr/bin/env python3

# cli option(s) [1] csv location
import sys
import requests
import json

email = ''
api_key = ''
ip = ''
dns_entries = []
zone_id = ''


# This script will receive the names of the entries from the file , and replace them with the Cloud Flare ID's


# make a new cloudflare request
def get_headers():
    return {"X-Auth-Email": email, "X-Auth-Key": api_key}


# get zone id
def get_zone():
    url = "https://api.cloudflare.com/client/v4/zones/"
    response = requests.get(url, headers=get_headers())
    data = json.loads(response.text)
    global zone_id
    for elem in data["result"]:
        if elem['name'] == zone_id:
            zone_id = elem['id']


def get_record_ids():
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    response = requests.get(url, headers=get_headers())
    data = json.loads(response.text)
    data = data["result"]
    new_entries = []
    global dns_entries
    for curr in data:
        if curr['name'] in dns_entries:
            new_entries.append(curr["id"])
    dns_entries = new_entries


def get_ip():
    global ip
    ip = requests.get("https://api.ipify.org").text


# json tutorial https://realpython.com/python-json/#python-supports-json-natively
def read_config(file_loc):
    with open(file_loc, 'r') as file:
        data = json.loads(file.read())
        global email
        email = data["email"]
        global api_key
        api_key = data["api_key"]
        global zone_id
        zone_id = data["zone"]["name"]
        global dns_entries
        dns_entries = data["zone"]["A"]


def main():
    # currently assuming there is a header and I'm ignoring it.
    if len(sys.argv) != 2:
        sys.exit('Either to few arguments or too many arguments. I need the json config file location')
    get_ip()
    read_config(sys.argv[1])
    get_zone()
    get_record_ids()


main()
