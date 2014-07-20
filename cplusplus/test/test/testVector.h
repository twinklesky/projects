#pragma once
#include <vector>
#include <iostream>
using namespace std;

class TestVector
{
public:
	TestVector(void);
	~TestVector(void);
	void execute();
private:
	vector<int> m_vec;
	
};
