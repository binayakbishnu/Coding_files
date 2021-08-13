#include <iostream>

using namespace std;

void inc(int *p1,int *p2)
{
	*p1=*p1+2;
	//cout<<*p1<<endl;
	*p2=*p2+2;
	//cout<<*p2<<endl;	
}
void abc(int a[10])
{
	a[0]=a[0]+2;
}

int main()
{
	int a = 10;
	
    int *p = &a;
    
    cout<<a<<endl;  //returns value of a
    cout<<&a<<endl; //returns memory location of a
    cout<<p<<endl;  //returns value of p == memory location of a
    cout<<&p<<endl; //returns memory location of p
    cout<<*p<<endl; //returns value of a pointed by p
    *p = 42; //changes value of a as well
    cout<<*p<<" "<<a<<endl;
    cout<<"a="<<a<<endl;
    
    
    
    int c=10;
    int b=20;
    inc(&c,&b);
    cout<<"c= "<<c<<endl;
    cout<<"b= "<<b<<endl;
    int x=c; //new value of
    cout<<x<<endl;
    
    int arr[10]={1,2,3,4};
    abc(arr);
    cout<<arr[0]<<endl;
	
	return 0;
}
