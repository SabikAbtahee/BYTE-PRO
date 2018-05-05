#include<bits/stdc++.h>   //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
	int n,pos,l,r;
	cin >> n>> pos >> l >>r;
	int ans=0,temp1,temp2;
	if(l==1 && r==n){
		ans=0;
	}
	else if(l>1 && r==n){
		if(pos==l){
			ans=1;
		}
		else if(pos<l){
			ans=l-pos+1;//
		}
		else if(pos>l){
			ans=(pos-l)+1;
		}
	}
	else if(l==1 && r<n){
		if(pos==r){
			ans=1;
		}
		else if(pos<r){
			ans=(r-pos)+1;
		}
		else if(pos>r){
			ans=pos-r+1;//
		}
	}
	else if(l>1 && r<n){
		if(pos>l && pos<r){
			temp1=pos-l;
			temp2=r-pos;
			if(temp1>=temp2){
				ans=temp2+temp2+temp1+2;
			}
			else if(temp1<temp2){
				ans=temp1+temp1+temp2+2;
			}
		}
		else if(pos==l){
			ans=(r-pos)+2;
		}
		else if(pos==r){
			ans=(pos-l)+2;
		}
		else if(pos<l){
			ans=r-pos+1;
			if(pos==1){
				ans++;
			}
			else{
				ans++;
			}

		}
		else if(pos>r){
			ans=pos-l+1;
			if(pos==n){
				ans++;
			}
			else{
				ans++;
			}

		}
	}

	cout << ans <<"\n";
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}