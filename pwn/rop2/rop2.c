#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

int good = 0;

void useful_gadgets() {
    asm(
        "pop %rdi\n"
        "ret\n"
        "pop %rsi\n"
        "ret\n"
        "pop %rdx\n"
        "ret\n"
    );
}

void win() {
    char flag[64];
    FILE* f = fopen("flag.txt", "r");
    if (!f) {
        perror("couldn't read the flag");
        return;
    }
    fgets(flag, sizeof(flag), f);
    if (good) {
        puts(flag);
    }
}

void check(int a, int b, int c) {
    if (a == 1 && b == 2 && c == 3) {
        good = 1;
        puts("check passed!");
    } else {
        printf("whoops, a = %d, b = %d, c = %d\n", a, b, c);
    }
}

void vuln() {
    char buf[8];
    gets(buf);
}

int main() {
    init();
    puts("hello!");
    vuln();
}

