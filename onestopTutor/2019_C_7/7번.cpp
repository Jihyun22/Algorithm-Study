/*
2020-09-14
[����žƩ��] 2020 EPEER ��� ���⹮�� Ǯ�� (��� 17������)
2019�⵵ 13ȸ c�ι� 7�� - ȸ��(���)
*/

#include <stdio.h>

//���� ����
int arr[10];
int answer = 0;

//�Լ� ����
void cal(int a, int b);

int main(void){
    int a, b, n;
    
    scanf("%d", &n);
    for(int i=0; i<n; i++)
        scanf("%d", &arr[i]);
    
    a=0;
    b=n-1;
    cal(a, b);
    
    printf("%d\n", answer);
    
    return 0;
}

void cal(int a, int b){
    if(a>=b)
        return;
    if(arr[a] == arr[b])
        cal(a+1, b-1);
    else{
        if(arr[a] > arr[b]){
        	arr[b-1] += arr[b];
            answer++;
            cal(a, b-1);
        }
        else{
            arr[a+1] += arr[a];
            answer++;
            cal(a+1, b);
        }
    }
}



















