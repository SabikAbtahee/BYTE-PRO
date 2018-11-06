#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <set>

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


	CHANGED HERE

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

void initializeSingleSource(int *distance, int *previous)
{
	for(int i=0; i<numberOfVertex; i++)
	{
		distance[i] = (int) pow(2,31)-10;
		previous[i] = -1; //-1 for NIL
	}
	distance[startVertex]=0;
}

int extractMinFromQ(int *distance, set <int> &q)
{
	int vertex;
	if(q.size()==1)
	{
		vertex = *(q.begin());
		q.clear();
		return vertex;
	}
	
	set<int>::iterator itToBeDeleted=q.begin();
	int minDistance;
	
	set<int>::iterator it=q.begin();
	vertex = *it;
	minDistance= distance[*it];
	
	it++;	
	for( ; it != q.end(); ++it)
	{
		if(distance[*it] < minDistance)
		{
			minDistance= distance[*it];
			vertex = *it;
			itToBeDeleted = it;
		}
	}
	q.erase(itToBeDeleted);
	return vertex;
}

void relax(int u, int v, int *distance, int *previous)
{
	if(distance[v] > distance[u]+adjacencyMatrix[u][v])
	{
		distance[v] = distance[u]+adjacencyMatrix[u][v];
		previous[v] = u;
	}
}

void dijkstraAlg(int *distance, int *previous)
{
	initializeSingleSource(distance, previous);
	set <int> q;
	for(int i=0; i<numberOfVertex; i++)
	{
		q.insert(i);
	}
	
	while(!q.empty())
	{
		int u = extractMinFromQ(distance, q);
		
		for(int v=0; v<numberOfVertex; v++)
		{
			if(adjacencyMatrix[u][v]!=0)
			{
				relax(u,v, distance, previous);
			}
		}
	}
}

void printResult(int *distance, int *previous)
{
	string arr = "stxyz";
	for(int i=0; i<numberOfVertex; i++)
	{
		cout 	<< arr[i] << "\t"
				<< distance[i] << "\t"
				<< arr[previous[i]] << endl;
	}
}

int main (int argc, char *argv[])
{
	if(!openFile(argv[1])) return -1;
	
	int *distance, *previous;
	distance = new int[numberOfVertex];
	previous = new int[numberOfVertex];
	
	dijkstraAlg(distance, previous);
	
	printResult(distance, previous);
	
	delete [] previous;
	delete [] distance;	
	destroyAdjacencyMatrix();
	return 0;
}
