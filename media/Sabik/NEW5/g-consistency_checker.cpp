#include<bits/stdc++.h>

using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
bool found=false;
struct Trie{
	struct Trie *children[10];
	int value;
	bool isLeaf;
};

int strToInt(string x){
	int number;
	istringstream(x) >> number;
	return number;
}
string IntToStr(int x){
	string str;
	//str=to_string(x);
	ostringstream ss;
	ss << x;
	return ss.str();
}

struct Trie *getNode(void){
	struct Trie *root = new Trie;
	root->isLeaf=false;
	for(int i=0;i<10;i++){
		root->children[i]=NULL;
	}
}

struct Trie *insert(struct Trie *root,char c,bool sad){
	int index=c-48;
	if(root->children[index]==NULL){
		root->children[index]=getNode();
		root=root->children[index];
		root->isLeaf=sad;
		root->value=index;
		return root;	
	}
	else{
		root=root->children[index];
		if(root->isLeaf==true){
			found=true;
		}
		return root;
	}
	
}

void deleteAll(struct Trie *root){
	if(root==NULL){
		return;
	}
	else{
		for(int i=0;i<10;i++){
			deleteAll(root->children[i]);
			delete root->children[i];
		}
	}
}

void operation(struct Trie *root,string yolo){
	string s = yolo;
	int length=s.size();
	
	for(int i=0;i<length;i++){
		if(i==length-1){
			root=insert(root,s[i],true);
		}
		else{
			root=insert(root,s[i],false);	
		}
	}
	//cout << found<<"asd" <<"\n\n";
}

void run2(int testCase){
	int lineNumber;
	string falseLine;
	scanf("%d",&lineNumber);
	getline(cin,falseLine);
	string lines[lineNumber];
	struct Trie *root=getNode();
	bool answer=false;
	for(int j=0;j<lineNumber;j++){
		getline(cin,lines[j]);


	}
	sort(lines,lines+lineNumber);

	for(int i=0;i<lineNumber;i++){
		//scanf("%d",&lines[i]);
		found=false;
		if(answer==false){
			operation(root,lines[i]);
		}
		if(found==true){
			answer=true;
		}
		
	}

	
	if(answer){
		printf("Case %d: NO\n",testCase);
	}
	else{
		printf("Case %d: YES\n",testCase);	
	}
	deleteAll(root);
}

void run(){
	int testCase;
	scanf("%d",&testCase);
	for(int j=1;j<=testCase;j++){
		run2(j);
	}
}

int main(){
	file();
	run();
	return 0;
}