#include "List.h"

/**
* List Constructor
* 
* Initalizes listArray as an empty List
* for the user to manipulate. 
**/
template<class T>
List<T>::List() {

}

/**
* List Destructor
*
* Deletes all list items and deletes the list array.
**/
template<class T>
List<T>::~List();

/**
* Adds given item to the end of the list array.
*
* Return: string denoting success.
**/
template<class T>
string List<T>::addItem(T item) {

}

/**
* Deletes the given item from the list array.
*
**/
template<class T>
void List<T>::removeItem(T item) {
	// find item and delete
}

/**
* Deletes the given item at the front of the list arry.
*
**/
template<class T>
void List<T>::removeTopItem() {
	// delete 0
}

/**
* Deletes all items from the list array.
*
* Return: string denoting success.
**/
template<class T>
string List<T>::deleteList() {

}

/**
* Moves given item to the front of the List.
*
* Parameter:
*	item - specified item to be moved
**/
template<class T>
void List<T>::moveItemUp(T item) {

}

/**
* Moves given item to the end of the List.
*
* Parameter:
*	item - specified item to be moved
**/
template<class T>
void List<T>::moveItemDown(T item) {

}

/**
* Resizes the list array if it becomes full.
*
* Return: boolean value on success of resize.
**/
template<class T>
bool List<T>::resizeList() {

}