#include<bits/stdc++.h>

using namespace std;

string separateSentence(string x);
string IntToStr(int x);
int strToInt(string x);
int charToInt(char x);

void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

void run(){
	
}

int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}
//////////////////////////////////////////////////**********************/////////////////////

int strToInt(string x){             //Converts a string to integer
	int number;
	istringstream(x) >> number;
	return number;
}


string IntToStr(int x){                 ///Converts a integer to string
	string str;
	//str=to_string(x);
	ostringstream ss;
	ss << x;
	return ss.str();
}


string separateSentence(string x){      // Separates individual words in a sentence
	istringstream iss(x);
	string word;
	while(iss >> word){
		cout << word <<"\n";
	}
	return x;
}
int charToInt(char x){              //Takes input a character and converts to int
	int p=int(x)-48;
	return p;
}


///////////////////***********************/////////////////////////////
long long decimalToBinary(long long n){         // DECimal number to binary conversion
	long long binaryNumber = 0;
    int R, i = 1, step = 1;

    while (n!=0)
    {
        R = n%2;
        n /= 2;
        binaryNumber += R*i;
        i *= 10;
    }
    return binaryNumber;
}
int convertBinaryToDecimal(long long n)             //Binary to decimal
{
    int decimalNumber = 0, i = 0, remainder;
    while (n!=0)
    {
        remainder = n%10;
        n /= 10;
        decimalNumber += remainder*pow(2,i);
        ++i;
    }
    return decimalNumber;
}
///////////////////************************///////////////////
int *a=new int[n];              // dynamic array initializing

int poww(int first,int second){         //power function
	int x=1;
	if(second==0){
		return 1;
	}
	else{
		for(int i=0;i<second;i++){
			x=x*first;
		}
	}
	return x;

}



/////////////////////********************////////////////////////


#include<bits/stdc++.h>                      //START OF EVERY FORMAT
using namespace std;
void file(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}
void run(){
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	file();
	run();
	return 0;
}





//////////////*****************************///////////////////////////


memset(arr,0,sizeof(arr));          //INITIALIZING AN ARRAY ALL TO ZERO

//////////*************//////////////////////

double intlog(double base, double x) {
    return (double)(log(x) / log(base));
}




/////////////////////////////DAY1 not very important
#include <bits/stdc++.h>
using namespace std;


struct c{
    int x, y;
    string s;
    bool operator < (c k1) const{
        if(y == k1.y){
            if(x == k1.x){
                return s < k1.s;
            }
            return x < k1.x;
        }
        return y < k1.y;
    }

    bool operator == (c k1) const{
        if(y == k1.y and x == k1.x and s == k1.s)
            return true;
        return false;
    }

    c operator + (c k1) const{
        c temp;
        temp.x = x + k1.x;
        temp.y = y - k1.y;
        temp.s = s + k1.s;
        return temp;
    }

    void print(){
        cout << "x: " << x << " y: " << y << " s: " << s << endl;
    }
};

void usingMap(){
    map <string, double> mp;
    mp["Sabik"] = 829.0;
    mp["Jamil"] = 802.5;
    mp["Khalil"] = 804.2;


    cout << mp["Sabik"] << endl;
    //cout << "Before Khayrul size " << mp.size() << endl;
    /*if(mp.find("Khayrul") == mp.end()){
        cout << "nai\n";
    }*/
    mp.erase("Sabik");
    cout << mp.size() << endl;

    for(auto it = mp.begin(); it != mp.end(); it++){
        //pair <string, double> p = *it;
        //cout << p.first << " " << p.second << endl;
        cout << it -> first << " " << it -> second << endl;
    }

    cout << "After Khayrul size " << mp.size() << endl;
}

bool f(c k1, c k2){
    if(k1.y == k2.y){
       if(k1.x == k2.x){
            return k1.s < k2.s;
       }
       return k1.x < k2.x;
    }
    return k1.y < k2.y;
}

void usingSet(){
    set <c> s;
    c k1, k2;
    k1.x = 10;
    k1.y = 21;
    k1.s = "a";
    s.insert(k1);


    k1.x = 9;
    k1.y = 210;
    k1.s = "A";
    s.insert(k1);

    k1.x = 9;
    k1.y = 210;
    k1.s = "A";
    s.insert(k1);


    cout << s.size() << endl;

}

void usingPriorityQueue(){

    priority_queue <c> pq;
    c k1, k2;
    k1.x = 10;
    k1.y = 21;
    k1.s = "a";
    pq.push(k1);


    k1.x = 9;
    k1.y = 210;
    k1.s = "A";
    pq.push(k1);

    k1.x = 9;
    k1.y = 210;
    k1.s = "A";
    pq.push(k1);

    cout << pq.size() << endl;
    while(!pq.empty()){
       // pq.top().print();
        c temp = pq.top();
        temp.print();
        pq.pop();
    }


}

void usingVector(){
    vector <c> v;
    c k1, k2;
    k1.x = 10;
    k1.y = 21;
    k1.s = "a";
    v.push_back(k1);
    k2.x = 10;
    k2.y = 21;
    k2.s = "a";
    v.push_back(k2);

    c temp = k1 + k2;
    temp.print();
    /*k1.x = 9;
    k1.y = 210;
    k1.s = "b";
    v.push_back(k1);

    k1.x = 9;
    k1.y = 210;
    k1.s = "A";
    v.push_back(k1);

    sort(v.begin(), v.end(), f);

    for(int i = 0; i < v.size(); i++){
        cout << v[i].x << " " << v[i].y << " " << v[i].s << endl;
    }*/
}
int main(){
    //usingSet();
    //usingPriorityQueue();
    usingMap();
}

///////////*****************///////////////////////

//passing an array as a parameter 
void pass(int *array,int length){
    for(int i=0;i<length;i++){
        array[i]+=1;
    }
}

void first(){
    int a[5]={1,2,3,4,5};
    int length=sizeof(a)/sizeof(a[0]);

    pass(a,length);
    for(int i=0;i<length;i++){
        cout << a[i];
    }   //   values of a will be changed here because of pointer concept;
}





