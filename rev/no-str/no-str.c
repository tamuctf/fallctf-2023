#include <stdio.h>
#include <string.h>

int main() {
  char password[22] = {'g', 'i', 'g', 'e', 'm', '{', 's', 't', '4', 't', 'i', 'c', 'a', 'l', 'l', 'y', '_', 'r', '3', 'v', 'e', 'd'};
  char input[22];

  puts("Enter your password: ");
  fgets(input, 22, stdin);

  if(strncmp(password, input, 22) == 0) {
    printf("Correct!");
  }
}
