#include<bits/stdc++.h>   //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

void operate(int testCase){

	string binNum;
	getline(cin,binNum);


	int query;
	scanf("%d",&query);

	int a[query],b[query],answer[query];
	int j=0,swap=0,index;
	int u=0;
	char c;
	printf("Case %d:\n",testCase);
	for(int i=0;i<query;i++){
		
		cin >> c;
		
		if(c=='I'){
			scanf("%d",&a[j]);
			scanf("%d",&b[j]);
			j++;
		}
		else if(c=='Q'){
			scanf("%d",&index);
			
			swap=0;

			for(int k=j-1;k>=0;k--){
				if(index>=a[k] && index<=b[k]){
					swap++;
				}
			}
			
			if((swap%2)==1){
				
				if(binNum[index-1]=='1'){
					answer[u]=0;
				}
				else{
					answer[u]=1;
				}
			}
			else{
				
				if(binNum[index-1]=='1'){
					answer[u]=1;
				}
				else{
					answer[u]=0;
				}
			}
			
			printf("%d\n",answer[u]);
			u++;
		}

	}
	
	

}
void run(){
	int testCase;
	string falseLine;
	scanf("%d",&testCase);
	//cout <<testCase;
	
	
	for(int i=1;i<=testCase;i++){	
		getline(cin,falseLine);
		operate(i);
	}
}
int main(){
	//ios_base::sync_with_stdio(false);
    //cin.tie(NULL);
	file();
	run();
	return 0;
}