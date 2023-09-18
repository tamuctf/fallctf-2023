#include <stdio.h>
void g() {
    FILE* f = fopen("real_flag.txt", "r");
    char flag[30];
    fgets(flag, 30, f);
    int something = 5/0;
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