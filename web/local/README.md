# Local

My parents wanted me to make them a web server where they can upload all of the pictures on their phones. Let me know what you think of my first draft.

Note: The flag is located at `/tmp/flag.txt`

## Solution

The vulnerability shown is local file inclusion. In index.php you can clearly see that it's reading in a file and it's using php's `preg_replace` with a regex to avoid allowing people to traverse up the directory. However, the regex can be avoided with a slightly more obfuscated payload.  
this is the payload, replace in the get request to the server: `/index.php?file=....//....//....//....//....//....//....//....//....//tmp/flag.txt`

flag:
`gigem{organic_and_locally_sourced}`
