#include <iostream>

using namespace std;

/* class publication
{
    char title[20];
    float price;
    public:
    void getdata()
    {
        // cout<<"Title: ";
        cin >> title;
        // cout<<"Price: ";
        cin>>price;
    }
    void putdata()
    {
        cout<<"Title: ";
        cout<<title<<"\n";
        cout<<"Price: ";
        cout<<price;
    }
};

class book : private publication
{
    int page_count;
    public:
    void getdata()
    {
        publication::getdata();
        cin >> page_count;
    }
    void putdata()
    {
        publication::putdata();
        cout<<"\nPages: : ";
        cout<<page_count<<"\n";
    }
};

class pamplet : private publication
{
    int page_count;
    public:
    void getdata()
    {
        publication::getdata();
        cin >> page_count;
    }
    void putdata()
    {
        publication::putdata();
        cout<<"\nPages: ";
        cout<<page_count<<"\n";
    }
};


class tape : private publication
{
    float minutes;
    public:
    void getdata()
    {
        publication::getdata();
        cin >> minutes;
    }
    void putdata()
    {
        publication::putdata();
        cout<<"\nPlaying amount: ";
        cout<<minutes<<"\n";
    }
}; */

/* class dashboard
{
    char name[10];
    int id;

public:
    void getdata()
    {
        cin>>name>>id;
    }
    void display()
    {
        cout<<"Name: "<<name<<"\nID: "<<id<<"\n";
    }
};

class Engineering : private dashboard
{
    char sub_courses[10];
    public:
    void getdata()
    {
        dashboard::getdata();
        cin>>sub_courses;
    }
    void display()
    {
        dashboard::display();
        cout<<sub_courses;
    }
};

class Management : private dashboard
{
    char sub_courses[10];
    public:
    void getdata()
    {
        dashboard::getdata();
        cin>>sub_courses;
    }
    void display()
    {
        dashboard::display();
        cout<<sub_courses;
    }
};

class Medicine : private dashboard
{
    char sub_courses[10];
    public:
    void getdata()
    {
        dashboard::getdata();
        cin>>sub_courses;
    }
    void display()
    {
        dashboard::display();
        cout<<sub_courses;
    }
};

int main()
{
    Engineering E;
    E.getdata();
    E.display();

    printf("\n");
    Management M;
    M.getdata();
    M.display();

    printf("\n");
    Engineering S;
    S.getdata();
    S.display();

    
    return 0;
} */

class GST
{
    public:
    double total;
    void get_data()
    {
        total = 0;
    }
    virtual void display(int C)
    {
        cout << total;
    }
};

class Solar_heater : public GST
{
    public:
    void display(int C)
    {
        total = C + 0.05*C;
        cout<<total;
    }
};

class Electric_vehicle : public GST
{
    public:
    void display(int C)
    {
        total = C + 0.12*C;
        cout<<total;
    }
};

int main()
{
    Solar_heater S;
    Electric_vehicle V;

    int C;
    cin>>C;
    S.display(C);

    cin>>C;
    V.display(C);



    return 0;
}
