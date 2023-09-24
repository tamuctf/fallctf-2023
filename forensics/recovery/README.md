# Recovery

Empty?

Download the file here:
https://drive.google.com/file/d/1Mu4JaTLDJNnZmD_5etS2LJ1pBBUaYL8V/view?usp=sharing

Author: Noam

## Solution

The file type vhd is a virtual hard disk, which a forensic capture of a disk.

Opening the virtual hard disk in the digital forensics application autopsy reveals several deleted files named `secret0` through `secret4` all of which have different sections of the flag encoded in different ways.

- `secret0` - rot13
- `secret1` - base32
- `secret2` - hex
- `secret3` - decimal
- `secret4` - base64

When all of the flag segments are combined it reveals the flag.

flag:
`gigem{4u70p5y_15_4_v3ry_u53ful_700l}`
