#include<bits/stdc++.h>                      //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

int query(int *input,int *tree,int node,int start,int end,int l,int r){
	
	if(l<start || r>end){
		return 0;
	}
	if(l==start && r==end){
			return tree[node-1];
	}
		
	int mid =(start+end)/2;
	if(l==start){
		int p1 = query(input,tree,2*node,start,mid,l,r);
		//int p2 = query(input,tree,2*node+1,mid+1,end,l,r);
		return p1;
		}
	if(r==end){
	 	//int p1 = query(input,tree,2*node,start,mid,l,r);
		int p2 = query(input,tree,2*node+1,mid+1,end,l,r);
		return(p2);
	}

	
}
void updateRange(int *input,int *tree, int node, int start, int end, int l, int r, int val){
    // out of range
    if (start > end or start > r or end < l)
        return;

    // Current node is a leaf node
    if (start == end)
    {
        // Add the difference to current node
        tree[node-1] += val;
        return;
    }

    // If not a leaf node, recur for children.
    int mid = (start + end) / 2;
    updateRange(input,tree,node*2, start, mid, l, r, val);
    updateRange(input,tree,node*2+1, mid + 1, end, l, r, val);

    // Use the result of children calls to update this node
    tree[node-1] = tree[node*2-1] + tree[node*2];
}

void update(int *input,int *tree,int node,int start,int end,int index,int value){

	if(start==end){
		input[index]+=value;
		tree[node-1]+=value;
	}
	else{
		int mid=(start+end)/2;
		if(index>=start && index<=mid){
			update(input,tree,2*node,start,mid,index,value);
		}
		else{
			update(input,tree,2*node+1,start,mid,index,value);
		}
		tree[node-1]=tree[2*node-1]+tree[2*node];
	}


}

void Build(int *input,int *tree,int node,int start,int end){
	
	if(start==end){
		tree[node-1]=input[start];
	}
	else{
		int mid=int((start+end)/2);

		Build(input,tree,2*node,start,mid);
		Build(input,tree,2*node+1,mid+1,end);
		tree[node-1]=tree[2*node-1]+tree[2*node];
	}
}


void run(){
	int x;
	cin >> x;
	int a[x];
	int tree[4*x-1];
	memset(tree,0,sizeof(tree));
	for(int i=0;i<x;i++){
		cin >> a[i];
	}

	Build(a,tree,1,0,x-1);
	//update(a,tree,1,0,x-1,0,5);
	int w=query(a,tree,1,0,x-1,0,4);
	cout << w <<"\n";
	for(int i=0;i<(3*x-1);i++){
		cout << i<<" - "<<tree[i] <<"\n";
	}
	
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}