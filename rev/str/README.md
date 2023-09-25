# str

We have a binary that has a flag in it! How do we tell what strings exist in it?

## Solution

I first ran this command "strings str | grep gigeme" and it only gave the first part of the flag. I then looked at some of the lines under with this command "strings str | grep -A 3 gig" and got the whole flag.

```
gigem{li
terally_
just_str
ings}
```

Which I inferred the flag to be gigem{literally_just_strings}.

flag:
`gigem{literally_just_strings}`
