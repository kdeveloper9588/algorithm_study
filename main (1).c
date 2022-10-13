#include <stdio.h>
int main() {
	int a[100],size=0,i;
	for(i=0;i<100;i++){
		scanf("%d",&a[i]);
		if(a[i]==0)
			break;
		size++;
	}
	size--;
	for(i=size;i>=0;i--){
		printf("%d ",a[i]);
	}
	
	return 0;
}