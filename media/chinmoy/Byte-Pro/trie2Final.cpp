#include<bits/stdc++.h>
using namespace std;

struct Node{
    char ch;
    struct Node *child[26];
    bool isLeaf;
};
Node *root;

struct Node *initNode(Node *newNode, char ch){
    newNode->ch = ch;
    for(int i =0;i<26;i++){
        newNode->child[i] = NULL;
    }
    newNode->isLeaf = false;
    return newNode;
}

int main(){
    root =  initNode(root,'a');
}

