#include <stdio.h>
#include <stdlib.h>

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

void arbitrary_write(unsigned long a, unsigned long v) {
    *(unsigned long*)a = v;
    asm(
        "xor %rax, %rax\n"
        "xor %rbx, %rbx\n"
        "xor %rcx, %rcx\n"
        "xor %rdx, %rdx\n"
        "xor %rdi, %rsi\n"
        "xor %r8, %r8\n"
        "xor %r9, %r9\n"
        "xor %r10, %r10\n"
        "xor %r11, %r11\n"
        "xor %r12, %r12\n"
        "xor %r13, %r13\n"
        "xor %r14, %r14\n"
        "xor %r15, %r15\n"
    );
}

int main() {
    init();

    unsigned long address;
    unsigned long value;

    puts("hello!");
    printf("puts = 0x%016lx\n", (unsigned long)puts);

    puts("enter target address in base 10:");
    scanf("%ld", &address);
    puts("enter target value in base 10:");
    scanf("%ld", &value);

    arbitrary_write(address, value);
    puts("bye!");
}

