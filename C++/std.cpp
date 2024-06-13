using namespace std;

#include <utility>
std::pair<int,std::string> stundent(26,'Noora');
std::cout << student.first  << std::endl; // prints 26
std::cout << student.second << std::endl; // print Noora


// changing data type
std::static_cast<int>(9.23) // converts the data type of value in () to the type in <>
std::stoi("9")   // string to int
std::stol("0")   // string to long
std::stoul("8")  // string to unsigned long
std::stof("7.0") // string to float
std::stod("6.0") // string to double

// vector 
std::vector<int> myVector;
int a = myVector[1];

// vector of tuples
std::vector<std::tuple<int, int, int>> vec;
vec.emplace_back(0, 1, 2);