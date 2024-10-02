#include <stdio.h>

int main(){
    int i;
    
    // 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    for(i = 1 ; i <= 10; i++){
		printf("%d ", i);
    }
    printf("\n\n");
    
    // 1, 3, 5, 7, 9
    for(i=1;i<=10;i+=2){
		printf("%d ", i);
	}
	printf("\n\n");
	
	// 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
	for(i=10;i>=1;i--){
    printf("%d ", i);
	}
	printf("\n\n");
	
	// 1, 2, 3, 4, 5
	for(i=1;i<=5;i++){
		if(i<=4){
    printf("%d, ", i);	
		} else{
			printf("%d", i);
		}
	}
	printf("\n\n");
    return 0;
}
