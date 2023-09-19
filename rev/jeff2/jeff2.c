#include <stdio.h>
void g() {
    FILE* f = fopen("real_flag.txt", "r");
    char flag[30];
    // f(flag, 29, f);
    fread(flag, 29, 1, f);

    int something = 5/0;

    char key[] = "j1ff";
    for(int x=0; x < 29; x++)  {
        flag[x] = flag[x] ^ key[x % 4];
    }

    flag[29] = '\0'; 

    printf("%s\n", flag);

}

void a() {
    g();
}

void l() {
    a();
}

void f() {
    l();
}

int main(){
    f();
};