#include<bits/stdc++.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

int block=0;


struct Q{
	int L;
	int R;
	int index;
	bool operator < (Q k) const{
		if(k.L/block==L/block){
			return R<k.R;
		}
		return L/block<k.L/block;
	}
};

void run(){

	int prevL=0,prevR=0;
	int count[100003];
	int count2[100003];
	int answer=0;
	
	memset(count,0,sizeof(count));
	memset(count2,0,sizeof(count2));

	int n,q;
	scanf("%d%d",&n,&q);
	int newAnswer[q+2];
	int arr[100000];
	Q query[q];
	arr[0]=-100;
	for(int i=1;i<=n;i++){
		scanf("%d",&arr[i]);
		/*if(arr[i]<=10000){
			count[arr[i]]+=1;
		}*/
	}
	for(int j=0;j<q;j++){
		scanf("%d%d",&query[j].L,&query[j].R);
		query[j].index=j+1;

	}

	block=sqrt(n);
	sort(query,query+q);

	/*for(int i=0;i<q;i++){
		cout << query[i].L/block<<" "<< query[i].L << " "<<query[i].R <<"   "<<query[i].index << endl;
	}
*/
	
	prevL=query[0].L;
	prevR=query[0].L;
	//bool flag1=true;
	//bool flag4=true;
	//bool flag2=true;
	//bool flag3=true;

	//cout << prevL << prevR;
	
	for(int i=0;i<q;i++){
		//flag1=true;
		while(query[i].L<prevL){
			//cout << "First\n\n";
			if(arr[prevL-1]<=100000){
				count[arr[prevL-1]]+=1;
				if(count[arr[prevL-1]]==arr[prevL-1]  && count2[arr[prevL-1]]==0){
					answer+=1;
					count2[arr[prevL-1]]=1;
					//flag1=false;
				}
				else if(count[arr[prevL-1]]!=arr[prevL-1] && count2[arr[prevL-1]]==1){
					answer-=1;
					count2[arr[prevL-1]]=0;
					//flag1=false;
				}
			}
			prevL--;
		}
		


		while(query[i].L>prevL){
			//cout << "Second\n\n";
			if(arr[prevL]<=100000){
				count[arr[prevL]]-=1;
				if(count[arr[prevL]]==arr[prevL]  && count2[arr[prevL]]==0){
					answer+=1;
					count2[arr[prevL]]=1;
					//flag2=false;
				}
				else if(count[arr[prevL]]!=arr[prevL] && count2[arr[prevL]]==1){
					answer-=1;
					count2[arr[prevL]]=0;
					//flag2=true;
				}
			}
			//cout << answer <<"\n\n";
			prevL++;
		}





		while(query[i].R<prevR-1){
			//cout << "Third\n\n";
			if(arr[prevR-1]<=100000){
				count[arr[prevR-1]]-=1;
				if(count[arr[prevR-1]]==arr[prevR-1]  && count2[arr[prevR-1]]==0){
					answer+=1;
					count2[arr[prevR-1]]=1;
					//flag3=false;
				}
				else if(count[arr[prevR-1]]!=arr[prevR-1] && count2[arr[prevR-1]]==1){
					answer-=1;
					count2[arr[prevR-1]]=0;
					//flag3=true;
				}
			}
			//cout << answer <<"\n\n";
			prevR--;
		}

		while(query[i].R>=prevR){
			//cout << "Fourth\n\n";
			if(arr[prevR]<=100000){
				count[arr[prevR]]+=1;
				if(count[arr[prevR]]==arr[prevR]  && count2[arr[prevR]]==0){
					answer+=1;
					count2[arr[prevR]]=1;
				}
				else if(count[arr[prevR]]!=arr[prevR] && count2[arr[prevR]]==1){
					answer-=1;
					count2[arr[prevR]]=0;
				}
			}
			//cout << answer <<"\n\n";
			prevR++;
		}
		
		newAnswer[query[i].index-1]=answer;
		
	}
	for(int i=0;i<q;i++){
		printf("%d\n",newAnswer[i]);
	}
	//cout << block;

	//cout << answer << "\n";



	
}

int main(){
	//file();
	run();
	return 0;
}