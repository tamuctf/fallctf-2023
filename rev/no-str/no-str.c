#include <stdio.h>
#include <string.h>

int main() {
  char password[24] = {'g', 'i', 'g', 'e', 'm', '{', 's', 't', '4', 't', 'i', 'c', 'a', 'l', 'l', 'y', '_', 'r', '3', 'v', 'e', 'd', '}', '\0'};
  char input[32];

  puts("Enter your password: ");
  fgets(input, 32, stdin);

  if(strncmp(password, input, 23) == 0) {
    printf("Correct!\n");
  }
}
