import dns
import dns.resolver
import dns.reversename
import argparse
import requests

bucket = False
parser = argparse.ArgumentParser()

# Adding our Domain argument
parser.add_argument("-d", "--Domain", help="Domain to search for")
args = parser.parse_args()
matches = ["aws", "s3", "amazonaws"]


if args.Domain:
    result = dns.resolver.resolve(args.Domain, "A")

    for ipval in result:
        #        print('IP', ipval.to_text())
        rev_query = dns.reversename.from_address(ipval.to_text())
        try:
            rev = dns.resolver.resolve(rev_query, "PTR")
        except:
            print("Not an S3 bucket!")
            exit()
        for rr in rev:
            if all([x in str(rr) for x in matches]):
                bucket = True

    if bucket:
        print("The specified domain is hosted via Amazon S3!")
        url = "http://" + args.Domain
        response = requests.get(url)
        takeover_text = ["specified bucket does not exist", "NoSuchBucket"]
        for bucketxt in takeover_text:
            if bucketxt in response.text:
                print("Domain may be vulnerable to Subdomain Takeover")
                break
    else:
        print("Not an S3 Bucket!")
else:
    parser.print_help()
