#include <stdio.h>

int main()
{
    int A[1001],n;
    scanf("%d",&n);
    
    for(int i=0; i<n; i++){
        int k;
        scanf("%d",&k);
        
        for(int i=0; i<k; i++){
            scanf("%d",&A[i]);
        }
        
        float S=0;
        for(int i=0; i<k; i++){
            S+=A[i];
        }
        float aver=S/k;
        
        int m=0;
        for(int i=0; i<k; i++){
            if(aver<A[i])m++;
        }
        
        float X=((float)m/(float)k)*100;
        
        printf("%.3f%%\n",X);
       
    }
}