/*
2020-09-14
[원스탑튜터] 2020 EPEER 대비 기출문제 풀이 (담당 17권지현)
2019년도 13회 c부문 8번 - 후위표기법
*/

#include <stdio.h>

//변수선언
int top = -1;
int stack[12] = {0};
char input[12];

//함수선언
int cal(int n);
int pop(void);
void push(int a);

int main(void){
    int n, answer;
    
    scanf(" %d", &n);
    for(int i=0; i<n; i++)
        scanf(" %c", &input[i]);
    
    answer = cal(n);
    printf("%d\n", answer);
    return 0;
}

int cal(int n){
    int i;
    for(i=0; i<n; i++){
        if(input[i] >= '0' && input[i]<= '9')
            push(i);
        else{
            switch(input[i]){
                case '+':
                    stack[top] += pop();
                    break;
                case '-':
                    stack[top] -= pop();
                    break;
                case '*':
                    stack[top] *= pop();
                    break;
                case '/':
                    stack[top] /= pop();
                    break;
            }
        }
    }
    return stack[0];
}

int pop(void){
    return stack[top--];
}

void push(int a){
    top++;
    stack[top] = input[a] - '0'; //char -> int
}









