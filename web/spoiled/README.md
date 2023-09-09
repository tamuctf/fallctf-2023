# Spoiled

I think my website might be past its expiration date. Maybe its time to get a new one.

## Solution

We can see that the website is running using PHP. When sending a web request to a page, we can see one of the response headers states:
X-Powered-By: PHP/8.1.0-dev

Using this header, we know exactly what version of PHP is being run. We can look up 'php 8.1.0 dev exploit' in google and find that this version of PHP has a backdoor allowing for remote code execution. In order to exploit this vulnerability, all we need to do is add the header 'User-Agentt', which then with function 'zerodiumsystem()', allows for any command we want to be run remotely on the system. 
Below is an example header which lists files in the current directory. 

User-Agentt: zerodiumsystem('ls');

We see that there is no flag files in that directory, so we can check a lower directory with ls .., and then ls ../..
We see that command 'ls ../../..' displays a file 'flag.txt', so all we need to do is to read the file. The below header obtains the flag, thus solving the challenge. 

User-Agentt: zerodiumsystem('cat ../../../flag.txt');

flag:
`gigem{sp0il3d_php_v3rsi0n}`
