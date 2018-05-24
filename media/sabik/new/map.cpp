#include<bits/stdc++.h>
using namespace std;
int main(){

    long long int size;
    cin>>size;
    string arr[size];
    map<string,int> mymap;
    map<string,int>::iterator it;
    string s;

    int temp;


    for (int i=0; i<size; i++){

         cin>>s;
         if(i==0){
            mymap.insert(pair<string,int>(s,i));
         }
         else{
            it = mymap.find(s);
            if (it != mymap.end()){ // found it
                temp = mymap.find(s)->second;
                mymap.erase (it);
                mymap.insert(pair<string,int>(s,i));
                arr[temp] = "0";
            }else{
                mymap.insert(pair<string,int>(s,i));
            }
         } arr[i] = s;


    }
    cout<<"---"<<endl;
    for (int z=size-1;z>=0;z--){
        if(arr[z]!="0") cout<<arr[z]<<endl;

    }

   return 0;

}
