#include <stdio.h>
#include <string.h>

void vault() {
  char password[0x100];
  
  printf("Welcome to the vault of 0x%lx\nPassword: ", &password);
  fgets(password, 0x110, stdin);

  if(strncmp(password, "f8e74ee96c21b2aab1e6ef81bb548764", 32) == 0) {
    printf("Welcome:\nBalance: $14.36\nAccount Summary: You're poor\n");
  }
}

int main() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
  vault();
}
