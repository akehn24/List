#pragma once
#include <iostream>
#include <typeinfo>

using namespace std;

template<class T>
class List
{
public:
	List();
	~List();

	string addItem(T item);
	void removeItem(T item);
	void removeTopItem();
	string deleteList();
	void moveItemUp(T item);
	void moveItemDown(T item);

private:
	T* listArray[20]{};
	T item;

	bool resizeList();

};

