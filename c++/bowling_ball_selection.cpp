#include <vector>
#include <iostream>
#include <math.h>
using namespace std;


int factorial(int n){
    int ret=1;
    for(int i=n;i>1;i--)
        ret*=i;
    return ret;
}

int comb(int n,int r){
    return factorial(n)/(factorial(n-r)*factorial(r));
}

void solve(){
    int n,m;
    cin >> n >> m;
    vector<int>weights(n);
    vector<int>weights_num(m+1,0);
    for(int i=0;i<n;i++){
        cin >> weights[i];
    }
    int total_select = comb(n,2);
    for(int i=0;i<weights.size();i++){
        weights_num[weights[i]]++;
    }
    for(int i=1;i<=m;i++){
        if(weights_num[i]>1){
            total_select -= comb(weights_num[i],2);
        }
    }
    cout << total_select << "\n";
}

int main(){
    solve();
}