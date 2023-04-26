#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    int i=1;
    while(n--){
        double a;
        cin>>a;
        double ans = (4*a*a)-(2*acos(0.0)*a*a);
        cout<<"Case "<<i<<": ";
        printf("%0.2lf\n", ans);
        i++;
    }
}