# Ophishal Mail

Find the malicious sender in the email logs.

Flag format - gigem{id}

## Solution

I was able to find the user that stood out using vim to search for the domain `taharkabrothers.com`. Only one address was not highlighted on this search meaning that UID `3508` is the suspicious user.

flag:
`gigem{3508}`
