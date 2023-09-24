# Zen

Sometimes, the best thing to do is sit back and listen within.

Author: Addison

## Hints

<details>
<summary>
Hint 1
</summary>

I've heard that `strace` is a great way to achieve inner peace, though you may have to wait to find it.

</details>

<details>
<summary>
Hint 2
</summary>

There's more than one way to _listen_ to yourself.

</details>

## Solution

The challenge description implies that I should just listen. My first thought was GDB but to no avail. When my 313 professor started talking about `strace` in class, I was enlightened.

When I ran the binary with `strace`, it seemed to hang for several minutes before doing anything. This aligned pretty well with the challenge description, and after some time, interesting things happened.

```
getpeername(10, {sa_family=AF_INET, sin_port=htons(443), sin_addr=inet_addr("162.159.134.233")}, [128 => 16]) = 0
getsockname(10, {sa_family=AF_INET, sin_port=htons(34620), sin_addr=inet_addr("10.231.131.39")}, [128 => 16]) = 0
```

These lines from the `strace` output showed that the program was making network connections. To listen to these requests, all I had to do was use Wireshark to capture the traffic. When the binary made its connections, Wireshark showed an HTTP connection to Discord's CDN

The request was for: `https://cdn.discordapp.com/attachments/1145319627933626503/1151947823659622541/b90adf9d8c9679f87d175ec470aad360cbd7d06cc9fa8efb8de11f1868f7e3889ebfccdb1b9e821ac8b93aba27695044b6cf879b9bc655ee40d38bf22ef71fc6`

Downloading this attachment provides the flag as shown below.

flag:
`gigem{z3nfu1_4nd_in7r0sp3ct1v3}`

