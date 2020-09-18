/*
2020-09-14
[����žƩ��] 2020 EPEER ��� ���⹮�� Ǯ�� (��� 17������)
2019�⵵ 13ȸ c�ι� 9�� - ������ȹ��
*/

#include <stdio.h>

//��������
int money[30000] = {0};
int dp[30000] = {0};

//�Լ�����
int max(int a, int b);
int cal(int n);

int main(void){
    int n, answer;
    
    scanf("%d", &n);
    for(int i=0; i<n; i++)
        scanf("%d", &money[i]);
    
    answer = cal(n);
    printf("%d\n", answer);
    
    return 0;
}

int max(int a, int b){
    if(a>b)
        return a;
    return b;
}

int cal(int n){
    dp[0] = money[0];
    dp[1] = money[0] + money[1];
    dp[2] = max(dp[1], max(money[1]+money[2], dp[0]+money[2]));
                    
    for(int i = 3; i<n; i++){
        dp[i] = max(dp[i-1],
                    max(dp[i-3]+money[i-1]+money[i], dp[i-2]+money[i]));
    }
    return dp[n-1];
}
