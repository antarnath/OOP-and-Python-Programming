#include<stdio.h>

#include<string.h>


int main(){
    
    
    int n;
    // scanf("%d",&n);
    scanf("%*[^\n]%*d",&n);
    // scanf("%*d",&n);
    for(int i=0;i<n;i++){
        char s[100];
        fgets(s,100,stdin);
        int d = strlen(s) - 1;
        printf("%d\n",d);
        if (d>10){
            printf("%c%d%c\n",s[0],d-2,s[d-1]);
        }
        else{
            printf(s);
        }
    }
    

}