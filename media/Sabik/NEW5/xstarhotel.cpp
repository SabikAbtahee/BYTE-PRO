#include<bits/stdc++.h>   //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run2(){
	int row,col;
	cin >> row >> col;
	char box[row][col],hotelName[row*col];
	int rating[row*col],x=0;
	memset(rating,0,sizeof(rating));
	memset(hotelName,'[',sizeof(hotelName));
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			cin >> box[i][j];
		}
	}
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){

			if(box[i][j]!='*'){
				if(j+1!=col){
					if(box[i][j+1]=='*'){
						rating[x]++;
						hotelName[x]=box[i][j];						
					}
				}
				if(j-1!=-1){
					if(box[i][j-1]=='*'){
						rating[x]++;
						hotelName[x]=box[i][j];
					}
				}
				if(i+1!=row){
					if(box[i+1][j]=='*'){
						rating[x]++;
						hotelName[x]=box[i][j];
					}
				}
				if(i-1!=-1){
					if(box[i-1][j]=='*'){
						rating[x]++;
						hotelName[x]=box[i][j];
					}
				}

				if((i-1!=-1) && (j-1!=-1)){
					if(box[i-1][j-1]=='*'){
						rating[x]++;
						hotelName[x]=box[i][j];
					}
				}
				if((i-1!=-1)&& (j+1!=col)){
					if(box[i-1][j+1]=='*'){
						rating[x]++;
						hotelName[x]=box[i][j];
					}
				}
				if((i+1!=row)&& (j-1!=-1)){
					if(box[i+1][j-1]=='*'){
						rating[x]++;
						hotelName[x]=box[i][j];
					}
				}
				if((i+1!=row)&& (j+1!=col)){
					if(box[i+1][j+1]=='*'){
						rating[x]++;
						hotelName[x]=box[i][j];
					}
				}

			}	

			x++;
		}
		//cout << "\n";
	}
	int highestV=0;
	char highestC='[';
	int index;
	//memset(index,-1,sizeof(index));
	for(int i=0;i<x;i++){
		if(rating[i]>=highestV ){		//&& hotelName[i]<=highestC
			index=i;
			highestV=rating[i];
			highestC=hotelName[i];
		}
	}
	for(int i=0;i<x;i++){
		if(rating[i]==highestV && hotelName[i]<=highestC ){		//&& hotelName[i]<=highestC
			index=i;
			//highestV=rating[i];
			highestC=hotelName[i];
		}
	}
	/*for(int i=0;i<x;i++){
		cout << index <<"\n";
	}*/
	if(hotelName[index]!='['){
		cout << hotelName[index]<<"\n";
	}
	else{
		cout << "Ajob na?\n";
	}
}
void run(){
	int testCase;
	cin >> testCase;
	for(int i=0;i<testCase;i++){
		run2();
	}

}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}