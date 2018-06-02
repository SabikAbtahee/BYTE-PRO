#include<bits/stdc++.h>
using namespace std;
void file(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
}
void run(){
    string s;
    int ans=0,len;
    bool flag=false;
    while(getline(cin,s)){
        ans=1;
        len=s.length();
        for(int i=0;i<len;i++){
            if(s[i]==32 && flag==true){
                ans++;
            }
        }
        cout << ans <<"\n";

    }

}
//HELLOW
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    file();
    run();
    return 0;
}