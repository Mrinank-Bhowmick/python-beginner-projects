# Historical Data Breach Search

The historical data breach python program, uses the HaveIBeenPwned (HIBP) API to act as a search engine for organisations/domains that have had known data breaches. If the organisation has had a known data breach, insights into the breach will be displayed including:
* Organisation
* The date of the data breach
* The number of accounts that had had data breached
* A description of the breach
* The datatypes that were contained in the breach

The program is valuable, as users can search for the services and domains that they have accounts for, in order to get an understanding of if their own personal data may have been breached. This will help users to remain informed, proactive in their personal cybersecurity, and aware of the data that may be circulating about them.

## Usage

From within the Historical Data Breaches directory, launch the program using the command:

> python main.py

The interactive program will then request input from the user for an organisation name or domain that they would like to check. The input is not caps sensitive, allowing the search to be more versatile.

If a single organisation has had multiple data breaches, they will all be displayed.

## Examples

### Example 1: Organisation name
```
Enter organisation name or domain: adobe

Name: Adobe
Date of breach: 2013-10-04
Number of accounts breached: 152,445,165
Description: In October 2013, 153 million Adobe accounts were breached with each containing an internal ID, username, email, <em>encrypted</em> password and a password hint in plain text. The password cryptography was poorly done and many were quickly resolved back to plain text. The unencrypted hints also disclosed much about the passwords adding further to the risk that hundreds of millions of Adobe customers already faced.
Data contained in breach:
 * Email addresses
 * Password hints
 * Passwords
 * Usernames
```

### Example 2: Domain
```
Enter organisation name or domain: twitter.com

Name: Twitter
Date of breach: 2022-01-01
Number of accounts breached: 6,682,453
Description: In January 2022, a vulnerability in Twitter's platform allowed an attacker to build a database of the email addresses and phone numbers of millions of users of the social platform. In a disclosure notice later shared in August 2022, Twitter advised that the vulnerability was related to a bug introduced in June 2021 and that they are directly notifying impacted customers. The impacted data included either email address or phone number alongside other public information including the username, display name, bio, location and profile photo. The data included 6.7M unique email addresses across both active and suspended accounts, the latter appearing in a separate list of 1.4M addresses.
Data contained in breach:
 * Bios
 * Email addresses
 * Geographic locations
 * Names
 * Phone numbers
 * Profile photos
 * Usernames

Name: Twitter200M
Date of breach: 2021-01-01
Number of accounts breached: 211,524,284
Description: In early 2023, over 200M records scraped from Twitter appeared on a popular hacking forum. The data was obtained sometime in 2021 by abusing an API that enabled email addresses to be resolved to Twitter profiles. The subsequent results were then composed into a corpus of data containing email addresses alongside public Twitter profile information including names, usernames and follower counts.
Data contained in breach:
 * Email addresses
 * Names
 * Social media profiles
 * Usernames
```