#include <stdio.h>

int main() {
  int n = 0;
  int a = 1;
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) { // for문은 조건을 만족하지 않을 때까지 실행되기
                                 // 때문에 n+1만큼 실행됨
    printf("%d", i); // for문 내부는 만족할 때까지 실행되기 때문에 n만큼 실행됨
  }

  return 0;
}
//이 코드의 수행 시간을 빅오표기법으로 나타내면 O(n)이다.