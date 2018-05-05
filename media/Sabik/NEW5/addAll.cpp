#include<bits/stdc++.h>
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}


int mai(){
    long long int N = -1;
    while(N!=0){
    cin>>N;
    if(N==0)
        break;
    else{
        long long int cost=0,totalcost=0;

        long long int *numbers = new long long int [N];
        for(int i=0;i<N;i++)
            cin>>numbers[i];
        sort(numbers,numbers+N);
        cost=numbers[0];
        for(int i=1;i<N;i++){
            cost=cost+numbers[i];
            totalcost=totalcost+cost;
            //cout<<"iteration"<<i<<"cost"<<cost<<" totalcost"<<totalcost<<endl;
        }
        cout<<totalcost<<endl;
        delete numbers;
    }

    }


    return 0;
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	//run();
	mai();
	return 0;
}