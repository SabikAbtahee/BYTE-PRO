#include<bits/stdc++.h>                      //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

struct Trie{					//Example with 3 children you can customize as needed
	struct Trie *children[3];
	int value;
	bool isLeaf;
};

struct Trie *getNode(void){				//This makes a node and returns the node
										// as a structure
	struct Trie *root = new Trie;
	root->isLeaf=false;
	for(int i=0;i<3;i++){	//Customize as needed
		root->children[i]=NULL;
	}
}

struct Trie *insert(struct Trie *root,int value,bool isLeaf){	//This needs full customization
	
	if(root->children[value]==NULL){
		root->children[value]=getNode();
		root=root->children[value];
		root->isLeaf=isLeaf;
		root->value=value;
		return root;	
	}
	else{
		root=root->children[value];
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
		for(int i=0;i<3;i++){	//small customization
			deleteAll(root->children[i]);
			delete root->children[i];
		}
	}
}


void run(){
	int a[3]={1,2,3};
	struct Trie *root=getNode();	//First root node banailam
	for(int i=0;i<3;i++){
		root=insert(root,a[i],true);	//First root e 1 insert korlam
	}

}



int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}