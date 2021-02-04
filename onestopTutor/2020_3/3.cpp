// 15회 E-pper
// 3. 재고없는 날

////////////// error 한글 타이핑 깨짐 현상 발생

// 문제 생략
// https://level.goorm.io/exam/100817/15%ED%9A%8C-e-pper-3%EB%B2%88/quiz/1

# include <stdio.h>

int solution(int n, int m){
    // 변수의 n 은 노트북의 개수
    // m일에 도매점으로부터 노트북이 입고
    // 재고가 0이 될 때 까지 며칠이 걸리는 지 리턴
    int answer = 0; // 함수의 리턴값으로 사용할 변수 지정 -> 기본 포멧임
    int p=0;
    
    while(n){
        n--; // 하루에 한개씩 팔리기 때문에 n-1 연산 취해줌
        p++; // 노트북이 입고된 후 며칠이 지났는지
        answer++;
        /////////////////////////////error 중괄호 후 엔터 빠르게 처리하면 tab 간격 유지 되지 않음
        if(m==p){
            n++;
            p=0;
        }
    }
    return answer;
}

int main() {
    int n, m, answer;
    scanf("%d %d", &n,&m);
	answer = solution(n, m);
	printf("%d\n", answer);

	return 0;
}

















