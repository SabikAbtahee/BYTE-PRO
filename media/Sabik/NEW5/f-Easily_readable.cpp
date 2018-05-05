#include<bits/stdc++.h>

using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

string IntToStr(int x){
	string str;
	//str=to_string(x);
	ostringstream ss;
	ss << x;
	return ss.str();
}
int strToInt(string x){
	int number;
	istringstream(x) >> number;
	return number;
}
void run2(int testCase){
	int wordCount,sentenceCount;
	string falseLine;
	scanf("%d",&wordCount);
	//cout << wordCount;
	string words[wordCount];
	int counting[wordCount];
	map<string,int> all;
	memset(counting,0,sizeof(counting));
	getline(cin,falseLine);
	string temp,a,b;
	int s;
	for(int i=0;i<wordCount;i++){
		getline(cin,words[i]);
		//cout << words[i];
		s=words[i].length();
		temp=IntToStr(s);
		a=toupper(words[i][0]);
		b=toupper(words[i][words[i].length()-1]);
		temp=temp+a+b;
		//cout << temp <<"\n";
		all[temp]+=1;
		//cout << all[temp]<<"  ";

	}

	scanf("%d",&sentenceCount);
	
	getline(cin,falseLine);
	
	//cout << sentenceCount;
	string sentence[sentenceCount],temp2;
	int sum=1;
	printf("Case %d:\n",testCase);
	for(int j=0;j<sentenceCount;j++){
		sum=1;
		getline(cin,sentence[j]);
		//cout << sentence[j];
		istringstream iss(sentence[j]);
    	string word2,a,b;
    	while(iss >> word2) {
    		temp2=IntToStr(word2.length());
    		a=toupper(word2[0]);
    		b=toupper(word2[word2.length()-1]);
        	temp2=temp2+a+b;
        	/*if(all[temp2]==0){
        		sum=0;
        		break;
        	}*/
        	//cout << sum <<" ";
        	//cout << all[temp2];
        	sum*=all[temp2];
    	}
		printf("%d\n",sum);
	}
	




}

void run(){
	int testCase;
	scanf("%d",&testCase);
	//cout << testCase;
	for(int i=1;i<=testCase;i++){
		run2(i);
	}
}

int main(){
	file();
	run();
	return 0;
}