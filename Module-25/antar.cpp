#include<bits/stdc++.h>
using namespace std;
typedef long long ll;


ll gcd(ll a, ll b){
    if(a==0) return b;
    gcd(b%a, a);
}

ll lcd(ll a, ll b){
    return ((a * b) / gcd(a, b));
}
int main()
{
    ll n;
    cin>>n;
    ll ans = 1;
    for(ll i=2;i<=n;i++){
        ans = lcd(i, ans);
    }
    cout<<ans;
    

}