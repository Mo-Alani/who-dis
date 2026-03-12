'''
who-dis.py
Created by: Mohammed M. Alani
https://github.com/Mo-Alani

This is a script designed to gather small pieces of information about a domain or an IP address using open-source intelligence (OSINT).
The script can be used to obtain additional info from ipinfo.io. To use that feature, you'll need to signup for free at the website, and obtain and access code.

Packages needed:
* python-whois
* cymruwhois
* ipinfo
'''
import argparse
import sys
import socket
import whois
from cymruwhois import Client
import ipinfo

# Setting up the colors to change how the text looks (results are printed in green)
class tcolors:
    GREEN = '\033[92m'
    ENDC = '\033[0m'

# A function to resolve the IP address of a given domain
def get_ip(domain_name):
    ip_address = socket.gethostbyname(domain_name)
    return str(ip_address)

# A function to extract the domain name from a URL. 
# The user can type a domain like mohammedalani.com, 
# or a full URL like https://www.mohammedalani.com, 
# and this function would extract the domain name alone
def domain_from_url(url):
    url = str(url).lower()
    domain = ''
    p1 = url.find('//')+2
    if p1 == 1:
        p1 = 0
    p2 = url.find('/',p1)+1
    if p2 == 0:
        domain = url[p1:]
    else:
        domain = url[p1:p2-1]
    ds = domain.count(".")
    if ds == 2:
        domain = domain[domain.find('.')+1:]
    return domain

# Parsing the input arguments
parser = argparse.ArgumentParser(description="who-dis is tool used to find and display small pieces of information about a domain or an IP address through OSINT.")
parser.add_argument("-d", "--domain", metavar="DOMAIN-NAME",type=str, help="The domain that you're looking to inspect.")
parser.add_argument("-i","--ip", metavar="IP-ADDRESS",type=str,help="The IP address that you want to inspect.")
parser.add_argument("-a","--access-token", metavar="IPINFO-ACCESS-TOKEN", type=str, help="You can get additional information by using an access token from ipinfo.io")
args = parser.parse_args()

# If there is no input IP or domain name, the script will print its help page and exit
if (not args.domain) and (not args.ip):
        parser.print_help()
        sys.exit()

# If the user includes a domain name AND an IP address, an error message will be shown
if (args.domain) and (args.ip):
    parser.print_help()
    print("You can choose either a domain name or an IP. NOT BOTH!!!")
    sys.exit()

# Printing the preamble
print("who-dis is tool used to find and display small pieces of information about a domain or an IP address through OSINT.\n")
print("Retrieving information..")

# Print this information is the input is a domain name
if (args.domain):
    domain = domain_from_url(args.domain)
    ip_address = get_ip(domain)
    try:
        w = whois.whois(domain) # This information is obtained using python-whois
    except:
        print("The service is timing out for some reason. Try again later.")
        sys.exit()
    print(f"Domain Name:{tcolors.GREEN} {domain}{tcolors.ENDC}")
    print(f"Domain Creation Date:{tcolors.GREEN} {w.creation_date}{tcolors.ENDC}")
    print(f"Domain Expiry Date:{tcolors.GREEN} {w.expiration_date}{tcolors.ENDC}")
    if w.registrar != None:
        print(f"Registrar:{tcolors.GREEN} {w.registrar}{tcolors.ENDC}")
    else:
        print("Registrar information could not be obtained")
    try:
        print("Name Servers:",f"{tcolors.GREEN}",' '.join(sn.lower() for sn in w.name_servers),f"{tcolors.ENDC}")
    except:
        print("Name servers information could not be obtained")
    if w.name != None:
        print(f"Registered under the name:{tcolors.GREEN} {w.name}{tcolors.ENDC}")
    else:
        print("Registrant name information could not be obtained")
    try:
        print("Emails:",f"{tcolors.GREEN}", ' '.join(em.lower() for em in w.emails),f"{tcolors.ENDC}")
    except:
        print("Emails information could not be obtained")
else:
    # If there is no domain in the input, fetch the IP address from the arguments
    ip_address = args.ip

# Print this information based on the IP address
c = Client()
r = c.lookup(ip_address) # This information is obtained using cymruwhois
print(f"IP address:{tcolors.GREEN} {ip_address}{tcolors.ENDC}")
print(f"ASN:{tcolors.GREEN} {r.asn}{tcolors.ENDC}")
print(f"Country Code:{tcolors.GREEN} {r.cc}{tcolors.ENDC}")
print(f"IP Block Owner:{tcolors.GREEN} {r.owner}{tcolors.ENDC}")

# If an access token for ipinfo.io is provided, the following information will be extracted and displayed.
if (args.access_token):
    print("\nRetrieving more information from ipinfo.io ..")
    access_token = args.access_token
    handler = ipinfo.getHandler(access_token)
    try:
        details = handler.getDetails(ip_address)
    except:
        print("Could not retrieve the information from ipinfo.io")
        sys.exit()
    print(f"Country:{tcolors.GREEN} {details.country_name}{tcolors.ENDC}")
    print(f"City:{tcolors.GREEN} {details.city}{tcolors.ENDC}")
    print(f"Location:{tcolors.GREEN} {details.loc}{tcolors.ENDC}")
    try:
        print(f"Hostname:{tcolors.GREEN} {details.hostname}{tcolors.ENDC}")
    except:
        print("Hostname information is not available")

print("\n That's all for now.")

