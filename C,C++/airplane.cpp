#include <iostream>
#include <string.h>
#include <vector>

using namespace std;

class airline
{
    char model_number[21];
    int airline_code;
    int fine_code;
    float fine_amt;

public:
    airline()
    {
        strcpy(model_number, "AIRBUS");
        airline_code = 0;
        fine_code = 0;
        fine_amt = 0.0;
    }
    void assign_amt(int f)
    {
        if (f == 1)
            fine_amt = 100.0;
        if (f == 2)
            fine_amt = 500.0;
        if (f == 3)
            fine_amt = 1000.0;
        if (f == 4)
            fine_amt = 5000.0;
        if (f == 5)
            fine_amt = 2500.0;
        // cout<<"Assigned\n";
    }
    void get_data(char m[21],int a, int f)
    {
        strcpy(model_number,m);
        airline_code = a;
        fine_code = f;
        assign_amt(f);
    }
    void put_data()
    {
        cout << model_number << " ";
        cout << airline_code << " ";
        cout << fine_code << " ";
        cout << fine_amt;
    }
};

int main()
{
    int i = 0;
    airline A[5];

    char m[21];
    int a;
    int f;


    for (i; i < 2; i++)
    {
        cin>>m;
        cin>>f;
        cin>>a;
        A[i].get_data(m,a,f);
    }

    for (i=0; i < 1; i++)
    {
        A[i].put_data();
        cout << "\n";
    }
    A[i].put_data();

    return 0;
}