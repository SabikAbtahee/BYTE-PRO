#include <iostream>
#include <fstream>


using namespace std;

int **adjacencyMatrix;
int **pathLengths;
int numberOfVertex;

int findMin(int old, int updated)
{
	if(old == 0) return updated;
	else if (old > updated) return updated;
	else return old;
}

void runWarshall(int k)
{
	for(int i=0; i<numberOfVertex; i++)
	{
		for(int j=0; j<numberOfVertex; j++)
		{
			
				pathLengths[i][j] = findMin(pathLengths[i][j], pathLengths[i][k]+pathLengths[k][j]);
			
		}
	}
}

void warshallAlgorithm(void)
{
//	for(int iteration = 0; iteration<numberOfVertex ; iteration++)
//	{
		for(int k =0; k<numberOfVertex; k++)
		{
			runWarshall(k);
		}

//	}
}

void printPathLengths(void)
{
	for(int i=0; i<numberOfVertex; i++)
	{
		for(int j=0; j<numberOfVertex; j++)
		{
			 cout << pathLengths[i][j] << " ";
		}
		cout << endl;
	}
}

void copyMatrices(void)
{
	for(int i=0; i<numberOfVertex; i++)
	{
		for(int j=0; j<numberOfVertex; j++)
		{
			 pathLengths[i][j] = adjacencyMatrix[i][j];
		}
	}
}

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

void makePathLengths()
{
	pathLengths = new int *[numberOfVertex];
	for(int i=0; i<numberOfVertex; i++)
	{
		pathLengths[i] = new int [numberOfVertex];
	}
}

void destroyPathLengths()
{
	for(int i=0; i<numberOfVertex; i++)
	{
		delete [] pathLengths[i];
	}
	delete [] pathLengths;

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

int main (int argc, char *argv[])
{
	if(!openFile(argv[1])) return -1;
	
	makePathLengths();
	copyMatrices();

	warshallAlgorithm();
	
	printPathLengths();
	
	destroyPathLengths();
	destroyAdjacencyMatrix();
	return 0;
}

