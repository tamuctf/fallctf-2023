#include <stdio.h>

int main(){
    char input[64];
    printf("Tell me the flag and I will verify it for you :)\n");
    scanf("%s", input);
    unsigned int correct = 1;
    char key[] = "h0wdy";
    char string[] = {15, 89, 16, 1, 20, 19, 84, 14, 10, 24, 5, 89, 20, 59, 11, 13, 70, 40, 12, 28, 0, 85, 10};
    for(int x=0; x < 23; x++)  {
        string[x] = string[x] ^ key[x % 5];
        if (string[x] != input[x])
            correct = 0;
    }

    if (correct)
        printf("yay that is the flag\n");
    else
        printf("sorry that is not the flag :(\n");

    return 0;
};