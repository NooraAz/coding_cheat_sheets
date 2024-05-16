//// vectors

//initiating a vector
std::vector <int> my_vector(size);

//appending:
my_vector.push_back(13);
    
//iterating:
my_vector[0];
for(vector<int>::iterator i = my_vector.begin(); i!= my_vector.end(); i++)
    cout << *i;

//size of vector:
my_vector.size();
    
//zeros vector:
fill(my_vector.begin(),my_vector.end(),0) 
    
// Pi 
#include <math.h>
pi = M_PI

// creating a namaspace
namespace namespace1{
    // whatever
};

// using a member of another name space
// 1. including the whole namespace in the beginning (not a good practice for std)
using namespace std;
// 2. including the specific member in the beginning
using std::cout;
using std::endl;
// 3. adressing the namespace in each instance of using member
std::cout << 300 << std::endl;

// if not defined
#ifndef _ENGINE_H
// define it
#define _ENGINE_H