#include <iostream>

using namespace std;

template <class ABCtype>
void display(ABCtype val)
{
    cout << val << "\n";
}

template <class ABCtype>
void display(ABCtype val, int n) // overloading template functions
{
    cout << val << " " << n << "\n";
}

template <class X1>
X1 func(X1 x, X1 y)
{
    return x > y ? x : y;
}

int main()
{
    int a = 9;
    char c = 'g';
    char s[4] = "afw";
    float f = 6.83;

    display(a);
    display(c);
    display(s);
    display(f);

    display(a, 1);
    display(c, 2);
    display(s, 3);
    display(f, 4);

    cout << func(45, 54) << "\n";
    cout << func('w', 'z') << "\n";
    cout << func("qew", "rqe") << "\n";

    return 0;
}