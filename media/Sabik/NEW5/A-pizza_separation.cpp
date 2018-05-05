#include<bits/stdc++.h>

using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

void run(){
	int slices;
	cin >> slices;
	int part[slices];
	for(int x=0;x<slices;x++){
		cin >> part[x];
	}
	//sort(part,part+slices);
	/*for(int x=0;x<slices;x++){
		cout << part[x]<< " ";
	}*/
	int i=0,j=0,sum=part[0];
	int min,ll;
	if(180-sum>0){
		min=180-sum;
	}
	else{
		min=10000;
	}
	while(true){
		if(sum==180){
			printf("0\n");
			break;
		}
		else if(sum<180 && i!=slices-1){
			i++;
			sum+=part[i];
			ll=180-sum;
			if(ll<min && ll>0){
				min=ll;
			}
		}
		else if(sum>180 && j!=slices){
			ll=sum-180;
			if(ll<min && ll>0){
				min=ll;
			}
			sum-=part[j];
			j++;
			ll=180-sum;
			if(ll<min && ll>0){
				min=ll;
			}
		}
		else{
			printf("%d\n",min*2);
			break;
		}
		if(i==slices-1 && j==slices){
			printf("%d\n",min*2);
			break;
		}

	}

}

int main(){
	//file();
	run();
	return 0;
}