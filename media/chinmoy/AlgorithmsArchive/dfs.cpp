#include <iostream>
#include <fstream>
#include <cmath>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int **adjacencyMatrix;
int numberOfVertex;

void makeAdjacencyMatrix()
{
	adjacencyMatrix = new int *[numberOfVertex];
	for(int i=0; i<numberOfVertex; i++)
	{
		adjacencyMatrix[i] = new int [numberOfVertex];
	}
}

void destroyAdjacencyMatrix()
{
	for(int i=0; i<numberOfVertex; i++)
	{
		delete [] adjacencyMatrix[i];
	}
	delete [] adjacencyMatrix;

}

bool openFile(char *fileName)
{
	ifstream iFile;
	iFile.open(fileName);
	if(iFile.is_open())
	{
		iFile >> numberOfVertex;
		
		makeAdjacencyMatrix();
		
		for(int i=0; i<numberOfVertex; i++)
		{
			for(int j=0; j<numberOfVertex; j++)
			{
				iFile >> adjacencyMatrix[i][j];
			}
		}
		
		iFile.close();
		
		return true;
	}
	else
	{
		cout << "coud not open input file" << endl;
		return false;
	}
	
}

void dfsVisit(int *color, int &time, int *prev, int *d, int *f, int u)
{
	color[u]=1;
	time++;
	d[u]=time;
	for(int v=0; v<numberOfVertex; v++)
	{
		if(adjacencyMatrix[u][v]==1)
		{
			if(color[v]==0)
			{
				prev[v]=u;
				dfsVisit(color, time, prev, d, f, v);
			}
		}
	}
	color[u]=2;
	time++;
	f[u]= time;
}

void dfs(int *color, int &time, int *prev, int *d, int *f)
{
	for(int u=0; u<numberOfVertex; u++)
	{
		color[u]=0;
		prev[u]=-1;//-1 for NULL
		f[u] = (int) pow(2,31)-10;
		d[u] = (int) pow(2,31)-10;
	}
	
	for(int u=0; u<numberOfVertex; u++)
	{
		if(color[u]==0) dfsVisit(color, time, prev, d, f, u);
	}
}


void printResult(int *color, int *prev, int *d, int*f)
{
	string arr = "SABCDEFG";
	string col = "WGB";
	for(int i=0; i<numberOfVertex; i++)
	{
		cout 	<< arr[i] << "\t"
				<< col[color[i]] << "\t" 
				<< d[i] << "\t"
				<< f[i] << "\t"
				<< arr[prev[i]] << endl;
	}
}

struct Pair
{
	int f;
	string item;
};

bool sortingRule (Pair i, Pair j)
{
	return i.f > j.f;
}

void printResultForTopological(int *color, int *prev, int *d, int*f)
{
	string arr[9] = {"Shirt", "Tie", "Jacket", "ug", "pant", "belt", "socks", "shoe", "watch"};
	
	vector <Pair> pairVec;
	
	for(int i=0; i<numberOfVertex; i++)
	{
		Pair temp;
		temp.f = f[i];
		temp.item = arr[i];
		pairVec.push_back(temp);
	}
	
	sort(pairVec.begin(), pairVec.end(), sortingRule);
	
	for(int i=0; i<numberOfVertex; i++)
	{
		cout << pairVec[i].item << "\t";
	}
	cout << endl;
}

int main (int argc, char *argv[])
{
	if(!openFile(argv[1])) return -1;
	
	int *color, *prev, *d, *f, time =0;
	//color =0-white, =1-grey, =2-black
	
	color = new int [numberOfVertex];
	prev = new int [numberOfVertex];
	d = new int [numberOfVertex];
	f = new int [numberOfVertex];
	
	dfs(color, time, prev, d, f);
	
	//printResult(color, prev, d, f);
	printResultForTopological(color, prev, d, f);
	
	delete [] f;
	delete [] d;
	delete [] prev;
	delete [] color;
	destroyAdjacencyMatrix();
	return 0;
}

