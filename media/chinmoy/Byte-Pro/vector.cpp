


#include<bits/stdc++.h>
using namespace std;
void file(){
    freopen("input.txt","r",stdin);
}

int main(){
    //file();

    vector< int > vect;
    vect.assign(1000000000,0);
    for(long long int i=0;i<1000000000;i++){
        vect[i]++;
    }for (long long int i=0;i<1000000000;i++) cout<<vect[i]<<endl;
    //cout<<vect.max_size();
    return 0;
        //one comment added
            //ratul comment
}

