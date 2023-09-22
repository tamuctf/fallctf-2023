#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

void win() {
    char flag[64];
    FILE* f = fopen("flag.txt", "r");
    if (!f) {
        perror("couldn't read the flag");
        return;
    }
    fgets(flag, sizeof(flag), f);
    puts(flag);
}

int main() {
    init();

    int magic = 0;
    char name[16];

    fgets(name, 36, stdin);

    if (magic == 0x69696969) {
        win();
    } else {
        printf("magic was 0x%08x :(\n", magic);
    }
}
