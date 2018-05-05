#include<bits/stdc++.h>

using namespace std;

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
int maxw=0;
/*struct Trie{
	struct Trie *children[4];
	int occur;
	//int level;
	//bool isLeaf;
};
struct Trie *getNode(void){
	struct Trie *root = new Trie;
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
	for(int i=0;i<4;i++){
		Node->children[i]=NULL;
	}
	temp=(Node->occur)*(level1+1);

	if(temp>maxw){
		maxw=temp;
	}
	return Node;

}*/

void run(int number){
	maxw=0;

	int n;
	string falseLine;
	scanf("%d",&n);
	getline(cin,falseLine);
	//struct Trie *root=getNode();
	//struct Trie *yolo=root;
	int temp1=0;
	string s[n];
	
	int occur[50][4];
	for(int i=0;i<50;i++){
		memset(occur[i],0,sizeof(occur[i]));
	}




	for(int y=0;y<n;y++){
		getline(cin,s[y]);
	}
	for(int y=0;y<n;y++){
		//yolo=root;
		for(int i=0;i<s[y].length();i++){

			if(s[y][i]=='A'){
				occur[i][0]++;
				temp1=occur[i][0]*(i+1);
				cout << "A"<<temp1<<"  ";
				if(temp1>maxw){
					maxw=temp1;
				}
				//yolo=insert(yolo,0,i);
			}
			else if(s[y][i]=='C'){
				occur[i][1]++;
				temp1=occur[i][1]*(i+1);
				cout << "C"<<temp1<<"  ";
				if(temp1>maxw){
					maxw=temp1;
				}
				//yolo=insert(yolo,1,i);
			}
			else if(s[y][i]=='G'){
				occur[i][2]++;
				temp1=occur[i][2]*(i+1);
				cout <<"G" <<temp1<<"  ";
				if(temp1>maxw){
					maxw=temp1;
				}
				//yolo=insert(yolo,2,i);
			}
			else if(s[y][i]=='T'){
				occur[i][3]++;
				temp1=occur[i][3]*(i+1);
				cout <<"T"<< temp1<<"  ";
				if(temp1>maxw){
					maxw=temp1;
				}
				//yolo=insert(yolo,3,i);
			}

			
		}
	cout <<"\n\n\n";
	}
	//delete root;
	//delete yolo;
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