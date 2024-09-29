# Tak3


Tool to check whether a given domain is hosted via an Amazon S3 bucket. 
If the domain is hosted via S3, the script also checks whether there's a possibility of subdomain takeover.

Requirements:

    Python 3

Installation:

```
git clone https://github.com/AMetz-InfosecGuy/s3-takeover-checker.git
cd s3-takeover-checker/
pip install -r requirements.txt
```
Usage:

```
python s3-takeover-checker.py -d example.com
```
