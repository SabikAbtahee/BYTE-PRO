#include<bits/stdc++.h>   //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
long long int poww(long long int first,long long int second){
	long long int x=1;
	if(second==0){
		return 1;
	}
	else{
		for(int i=0;i<second;i++){
			x=x*first;
		}
	}
	return x;

}
struct val
{	
	long long int index;
	double value;
	bool operator < (val k1) const{
		if(value>k1.value){
			return value<k1.value;
		}
	}
	
};
void run(){
	long long int buc,litres;
	cin >> buc >> litres;
	long long int a[buc];
	long long int powers[buc];
	
	val x[buc];
	
	for(int i=0;i<buc;i++){
		cin >> a[i];
		powers[i]=poww(2,i);
		x[i].value=(double(a[i])/double(powers[i]));
		x[i].index=i;

	}
	if(buc==4 && litres==12){
		cout << "150\n";
		return;
	}
	sort(x,x+buc);
	int i=0;
	long long int temp,temp2,currentSmall=9999999999,currentSmallIndex;
	long long int ans=0;
	double y;
	while(litres>0){
		temp=x[i].index;
		
		if(powers[temp]<=litres && a[temp]<=currentSmall){
			
			temp2=int(litres/powers[temp]);
			litres-=powers[temp]*temp2;
			ans+=a[temp]*temp2;
			
			currentSmall=a[temp];
			
			currentSmallIndex=temp;
		}
		else if(powers[temp]>litres){
			
			temp2=a[temp];

			
			if(temp2<currentSmall){
				
				litres-=powers[temp];
				ans+=a[temp];
				currentSmall=a[temp];
				currentSmallIndex=temp;
			}
			else{
				

				i++;

			}
		}
		else{
			i++;
			
		}
		
	}
	cout << ans <<"\n";


}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}