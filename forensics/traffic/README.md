# Traffic

Some ports just aren't secure.

## Solution

Opening the pcap with wireshark and string searching for `gigem` reveals the flag as an url encoded http parameter.

flag:
`gigem{4ttp1sN0tS3cur3}`
