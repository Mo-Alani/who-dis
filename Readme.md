# who-dis
Doesn't it bother you when emails from random domain names appear in your inbox? You got a hunch that this is not a good domain, but you're not 100% sure. What do you do? you look it up.

**who-dis** is a simple python script designed to get you some information about an IP address or a domain name using open-source intelligence (OSINT).

This tool can help security specialists, and regular users get some background information about a certain domain or IP address quickly, and without a hassle.

**Disclaimer**: The information provided by this tool relies on publicly available information through WHOIS databases, and public registry information. Therefore, we provide no guarantee nor we hold the responsibility of the accuracy and availability of the information obtained using the tool.

* Current version is 0.1.1.

## Installation
Download the repository using:

        git clone https://github.com/Mo-Alani/who-dis.git

The required packages are:

* python-whois
* cymruwhois
* ipinfo

You can install them using ``pip install -r requirements.txt`` in the folder of the project.

## Usage
Inside the folder of the project, run the project using:

        python who-dis.py -d domain-name
Where you replace the ``domain-name`` with the domain of your choice.

The script can be used to obtain information about domains using the ``-d domain-name`` argument to obtain information such as registration date, expiration date, registrar name, registrant name (if available), and name servers.

If you're inspecting an IP address, you can use ``-i ip-address`` argument to obtain IP information such as autonomous system number (ASN), country code (based on IP), and IP block owner. Using the ``-d`` argument will get you the domain and IP address information.

If you're looking for IP geolocation data, you can signup to [ipinfo.io](https://ipinfo.io) for free to obtain an API access key. Once you have that key, you can add ``-a access-token`` to the script, and it would fetch additional information for you from ipinfo.io, such as hostname, country and city, and location coordinates. This is by no means and endorsement for ipinfo.io. There are many other similar services who provide this information for free, with certain limitations.

## Contributors:
[Mohammed M. Alani](https://www.mohammedalani.com) ([Mo-Alani](https://github.com/Mo-Alani/))