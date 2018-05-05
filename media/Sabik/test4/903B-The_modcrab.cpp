#include<bits/stdc++.h>

using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

void run(){
	int health,attack,regen,enemy,enemyAtt,count=0,ans,temp;
	cin >> health >> attack >> regen >> enemy >> enemyAtt;
	int strike;
	strike=enemy/attack;
	if(enemy%attack>0){
		strike++;
	}
	int x=health;
	for(int j=0;j<strike;j++){
		x-=enemyAtt;
	}
	if(x+health>0){
		
	}
	temp=strike*enemyAtt;

	while(true){
		if(temp>health){
			health+=regen;
			count++;
		}
		else{
			break;
		}
	}
	ans=count+strike;
	cout << ans << "\n";
	for(int i=0;i<count;i++){
		cout << "HEAL\n";
	}
	for(int i=0;i<strike;i++){
		cout << "STRIKE\n";
	}


}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}
