# Modified

What's different?

## Solution

Since the challenge description states "What's different", the challenge likely requires us to find which file is different from the rest. In the given .zip file, we have over 1000 .jpeg files, as well as a file titled 'hashes.txt', which has the result of the command 'md5sum' ran on all of the files. As such, the challenge seems to imply that one of the 1000+ images has an incorrect md5sum listed in 'hashes.txt', and the challenge will be solved by identifying this file.

To solve this challenge, I wrote a bash script, which parses through all files with extension '.jpeg' in their filename, and sorts them numerically, just like they are in the given 'hashes.txt' file. The script then runs 'md5sum' on the filenames, and then outputs that result into a file 'newhashes.txt'. The script then runs the command 'diff hashes.txt newhashes.txt', which compares the two files and finds the different line in both of them. The resulting output shows us that the different md5sum result was for file 'img_465.jpeg'. 

We then run 'exiftool' on file 'img_465.jpeg' to examine the file's metadata, and find that the description in the file metadata contains the flag.

flag:
`gigem{4a54s_4r3_co0l}`
