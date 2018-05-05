#include<bits/stdc++.h>   //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
string IntToStr(long long int x){
	string str;
	//str=to_string(x);
	ostringstream ss;
	ss << x;
	return ss.str();
}
long long int strToInt(string x){
	long long int number;
	istringstream(x) >> number;
	return number;
}
long long int change(long long int woah){
	/*long long int x;
	string s,ans;
	s=IntToStr(woah);
	ans="90";
	for(int i=1;i<s.length()-1;i++){
		ans+="0";
	}
	ans+="02";
	x=strToInt(ans);
	return x;
	*/

}
void run(){
	long long int a ,mod;
	cin >> a >> mod;
	long long int p[a];
	p[0]=0;
	long long int i=1,x=10,yeah=11,woah=902,sum=0,brah=89100,a1,count=0;
	while(true){
		if(i>a){
			break;
		}
		if(i>10 && i%10==0){
			a1=i;
			while(true){
				count++;
				a1=a1/10;
				yeah=(yeah/10);
				if(a1%10!=0){
					break;
				}
				
			}
			p[i]=p[i-1]+yeah;
			for(int l=0;l<count;l++){
				yeah=yeah*10;
			}
			count=0;
			//cout << p[i] << endl;
			sum+=p[i];
			i++;
		}
		else{

			p[i]=p[i-1]+yeah;
			//cout << p[i] << endl;
			sum+=p[i];
			i++;
		}
		if(i==x){
			x=x*10;
			p[i]=p[i-1]+woah;
			//cout << p[i] << endl;
			sum+=p[i];
			i++;
			woah=woah+brah;
			brah=brah*100;
			//woah=change(woah);
			//cout << woah << endl;
			yeah=yeah*10;
		}
		
	} 
	cout << sum%mod  << endl;
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//file();
	run();
	return 0;
}