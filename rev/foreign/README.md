# Foreign

Run the binary. That's it.

## Hints

<details>
<summary>
Hint 1
</summary>

Are there any tools on linux that allow us to run userspace applications from foreign architectures?

</details>

## Solution

The provided binary is compiled with `s390x` which is an old IBM mainframe architecture. Running this binary on a different architecture requires some type of emulation. Luckily, QEMU is capable of emulating `s390x`. The simplest way to do this is to use a multiarch docker container.

Using the google search `s390x docker container`, I came across [this blog post](https://docs.gitlab.com/omnibus/development/s390x.html). Using the commands listed I was able to execute the binary inside docker.

```
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
docker run --rm -it s390x/ubuntu bash
docker cp ./foreign <name>:/
```

flag:
`gigem{y0u_4r3_cl34reD_t0_3n7er}`
