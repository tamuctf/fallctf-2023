#include <stdio.h>
#include <string.h>

void vault() {
  char account[10];
  char password[256];
  
  printf("Welcome to your personal vault\nAccount Number: ");
  fgets(account, 0x10, stdin);

  printf("Password: ");
  fgets(password, 256, stdin);

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
