// test.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "testVector.h"


int _tmain(int argc, _TCHAR* argv[])
{
	TestVector *tv = new TestVector();
	tv->execute();
	system("pause");
	return 0;
}

