#include<bits/stdc++.h>

using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
int maxw=0;
struct Trie{
	struct Trie *children[4];
	int occur;
};
struct Trie *getNode(void){
	struct Trie *root = new Trie;
	//struct Trie *root;
	root->occur=0;
	//root->level=0;
	for(int i=0;i<4;i++){
		root->children[i]=NULL;
	}
	//root->isLeaf=false;
	return root;
}

struct Trie *insert(struct Trie *Node,int x,int level1){
	
	int temp;
	if(Node->children[x]==NULL){
		Node->children[x]=getNode();
	}
	
	Node=Node->children[x];
	//Node->occur=(Node->occur)+1;
	Node->occur++;
	//Node->level=level1;
	/*for(int i=0;i<4;i++){
		Node->children[i]=NULL;
	}*/
	temp=(Node->occur)*(level1+1);

	if(temp>maxw){
		maxw=temp;
	}
	return Node;

}
void deleteAll(struct Trie *root){
	if(root==NULL){
		//printf("S\n");
		return;
	}
	else{
		for(int i=0;i<4;i++){
			deleteAll(root->children[i]);
			delete root->children[i];
		}
	}
}
void run(int number){
	maxw=0;
	int n;
	string falseLine;
	scanf("%d",&n);
	getline(cin,falseLine);
	struct Trie *root=getNode();
	struct Trie *yolo=root;
	/*for(int u=0;u<50;u++){
		root=createNodes(root);
	}
	*/

	string s[n];
	for(int y=0;y<n;y++){
		getline(cin,s[y]);
	}
	for(int y=0;y<n;y++){
		yolo=root;
		for(int i=0;i<s[y].length();i++){

			if(s[y][i]=='A'){
				yolo=insert(yolo,0,i);
			}
			else if(s[y][i]=='C'){
				yolo=insert(yolo,1,i);
			}
			else if(s[y][i]=='G'){
				yolo=insert(yolo,2,i);
			}
			else if(s[y][i]=='T'){
				yolo=insert(yolo,3,i);
			}
			
		}
	}
	deleteAll(root);
	printf("Case %d: %d\n",number,maxw);
	return;


}

int main(){
	file();
	int testCase;
	scanf("%d",&testCase);
	for(int l=1;l<=testCase;l++){
		
		run(l);
	}
	return 0;
}