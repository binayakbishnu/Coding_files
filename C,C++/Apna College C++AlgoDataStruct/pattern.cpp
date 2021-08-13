#include <iostream>

using namespace std;
/*
int main()
{
    for(int i =0;i<5;i++)
    {
        for(int j=5;j>i;j--)
        {
            cout<<"*";
        }
    cout<<"\n";}
}
*/
/*
int main()
{
    for(int i =0;i<5;i++)
    {
        for(int j=4;j>i;j--)
        {
            cout<<" ";
        }
        for(int k=0;k<i+1;k++)
        {
            cout<<"*";
        }
        cout<<"\n";
    }
}
*/
/*
int main()
{
    for (int i=0; i<5;i++)
    {
        for(int j =0;j<i+1;j++)
            cout<<i+1;
        cout<<"\n";
    }
}
*/
/*
int main()
{
    int x=1;
    for (int i =0;i<5;i++)
    {
        for (int j=0;j<=i;j++)
        {
            cout<<x++<<" ";
        }
    cout<<"\n";
    }
}
*/
/*
int main()
{   int n=4; int i=0;
    for(i=0;i<n;i++)
    {
        for(int j=0;j<=i;j++)
        {
            cout<<"* ";
        }
        for(int k=2*(n-i-1);k>0;k--)
        {
            cout<<"  ";
        } 
        for(int j=0;j<=i;j++)
        {
            cout<<"* ";
        }
    cout<<"\n";
    }
}
*/
/*
int main()
{
    for (int i =5;i>0;i--)
    {
        for (int j=0;j<i;j++)
        {
            cout<<j+1<<" ";
        }
        cout<<"\n";
    }
}
*/
/*
//1 01 101 0101 10101
int main()
{   int x=1;
    int s=x;
    for (int i=0;i<5;i++)
    {   
        for (int j=0;j<=i;j++)
        {
            cout<<x;
            if (x==0){x=1;}
            else if (x==1){x=0;}
            //cout<<"\nx="<<x<<"\n";
        }
    cout<<"\n";
    if (s==0){s=1;}
    else if (s==1){s=0;}

    x=s;
    //cout<<"\nx="<<x<<"\n";
    }
}
*/
/*
int main()
{
    for (int i=0;i<5;i++)
    {
        for (int k=0;k<5-i-1;k++)
        {
            cout<<" ";
        }
        for (int j=0;j<5;j++)
        {
            cout<<"*";
        }
    cout<<"\n";
    }
}
*/
/*
int main()
{
    int n=5;

    for (int i =0 ;i<n;i++)
    {   
        int x = 1;
        for (int j=n-1;j>i;j--)
        {
            cout<<" ";
        }
        for (int k=0;k<i+1;k++)
        {
            cout<<x++<<" ";
        }
        cout<<"\n";
    }

    return 0;
}
*/
/*
int main()
{
    int n=5;
    int i,j,k;

    for (i=0;i<n;i++)
    {
        for (j=n-1;j>i;j--)
        cout<<" ";

        for (k=i+1;k>0;k--)
        cout<<k;

        for (j=2;j<i+2;j++)
        cout<<j;

        cout<<"\n";
    }

    return 0;
}
*/
int main()
{
    cout<<"Hi";
    return 0;
}