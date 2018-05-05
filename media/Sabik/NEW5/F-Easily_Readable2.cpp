#include<bits/stdc++.h>

using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

void separateSentence(string x){
	istringstream iss(x);
	string word;
	while(iss >> word){
		cout << word <<"\n";
	}
	
}
struct TrieNode{
	struct TrieNode *children[58];
	vector<char> alphabets;
	char firstWord;
	char lastWord;
	int length;
	int value;
};

struct TrieNode *getNode(void){
	struct TrieNode *root=new TrieNode;
	for(int i=0;i<58;i++){
		root->children[i]=NULL;
	}
	root->value=0;
	return root;
}

struct TrieNode *insert(struct TrieNode *root,string word){
	char first,last;
	int length=word.size();
	first=word[0];
	last=word[length-1];
	int index = first-65;
	vector<char> tempVec;
	tempVec.clear();
	if(root->children[index]==NULL){
		root->children[index]=getNode();
		root=root->children[index];
		root->firstWord=first;
		root->lastWord=last;
		root->length=length;
		for(int i=1;i<length-1;i++){
			root->alphabets.push_back(word[i]);
		}
		sort(root->alphabets.begin(),root->alphabets.begin()+(length-2));
		root->value++;
	}
	else {
		root=root->children[index];
		if(root->lastWord==lastWord && root->length==length){
			for(int i=1;i<length-1;i++){
				tempVec.push_back(word[i]);
			}
			sort(tempVec.begin(),tempVec.begin()+(length-2));
			if(root->alphabets==tempVec){
				root->value++;
			}
		}
		
	}

}

void run2(int testCase){
	int wordNumber;
	string falseLine;
	scanf("%d",&wordNumber);
	getline(cin,falseLine);
	string allWords[wordNumber];
	for(int i=0;i<wordNumber;i++){
		getline(cin,allWords[i]);
	}
	sort(allWords,allWords+wordNumber);
	struct TrieNode *root=getNode();
	for(int j=0;j<wordNumber;j++){
		insert(root,allWords[j]);
	}
	scanf("%d",&sentenceNumber);
	getline(cin,falseLine);
	string sentence[sentenceNumber];
	for(int i=0;i<sentenceNumber;i++){
		getline(cin,sentence[i]);
	}


}

void run(){
	int testCase;
	scanf("%d",&testCase);
	for(int i=1;i<=testCase;i++){
		run2(i);
	}
}

int main(){
	file();
	run();
	return 0;
}


