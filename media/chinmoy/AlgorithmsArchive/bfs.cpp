#include <iostream>
#include <fstream>
#include <cmath>
#include <queue>
#include <string>

using namespace std;

int **adjacencyMatrix;
int numberOfVertex;
int startVertex;

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
		
		iFile >> startVertex;
		
		iFile.close();
		
		return true;
	}
	else
	{
		cout << "coud not open input file" << endl;
		return false;
	}
	
}

void bfsInitialize(int *distance, int *color, int *prev, queue <int> &bfsQueue)
{
	//color: 0=white, 1=grey, 2=black
	//prev: -1 for NULL
	
	for(int i=0; i<numberOfVertex; i++)
	{
		color[i] = 0;
		prev[i] = -1;
		distance[i] = (int) pow(2,31)-10;
	}
	
	color[startVertex] = 1;
	//prev[startVertex] = NULL;
	distance[startVertex] = 0;
	
	bfsQueue.push(startVertex);
}

void bfs(int *distance, int *color, int *prev)
{
	queue <int> bfsQueue;
	
	bfsInitialize(distance, color, prev, bfsQueue);

	while(!bfsQueue.empty())
	{
		int u = bfsQueue.front();
		bfsQueue.pop();
		
		for(int v=0; v<numberOfVertex; v++)
		{
			if(adjacencyMatrix[u][v]==1)
			{
				if(color[v]==0)
				{
					color[v]=1;
					distance[v] = distance[u]+1;
					prev[v] = u;
					bfsQueue.push(v);
				}
			}
		}
		color[u] = 2;
	}
}

void printResult(int *distances, int *color, int *prev)
{
	string arr = "rstuvwxy";
	string col = "WGB";
	for(int i=0; i<numberOfVertex; i++)
	{
		cout 	<< arr[i] << "\t"
				<< col[color[i]] << "\t" 
				<< distances[i] << "\t"
				<< arr[prev[i]] << endl;
	}
}

int main (int argc, char *argv[])
{
	if(!openFile(argv[1])) return -1;
	
	int * distances, *color, *prev;
	
	distances= new int [numberOfVertex];
	color = new int [numberOfVertex];
	prev = new int [numberOfVertex];
	
	bfs(distances, color, prev);
	
	printResult(distances, color, prev);
	
	delete [] color;
	delete [] prev;
	delete [] distances;
	
	destroyAdjacencyMatrix();
	
	return 0;
}
