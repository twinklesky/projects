#include "StdAfx.h"
#include "testVector.h"

TestVector::TestVector(void)
{
}

TestVector::~TestVector(void)
{
}

void TestVector::execute(){
		
	cout<<m_vec.size()<<"\t"<<m_vec.capacity()<<endl;
	
	for (int index=0;index<10;index++)
	{
		m_vec.push_back(index);
	}

	cout<<m_vec.size()<<"\t"<<m_vec.capacity()<<endl;

	cout<<"the address of the front element "<<&m_vec.at(0)<<endl;
	m_vec.reserve(20);
	cout<<"the address of the front element "<<&m_vec.at(0)<<endl;
	m_vec.resize(15);
	cout<<"the address of the front element "<<&m_vec.at(0)<<endl;

	vector<int>(m_vec).swap(m_vec);
	cout<<m_vec.size()<<"\t"<<m_vec.capacity()<<endl;

	m_vec.clear();
	cout<<m_vec.size()<<"\t"<<m_vec.capacity()<<endl;

	m_vec.swap(vector<int>());
	cout<<m_vec.size()<<"\t"<<m_vec.capacity()<<endl;

	//m_vec.shrink_to_fit();

}
