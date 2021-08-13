#include <iostream>

using namespace std;

template <class ABC>
class trial
{
    vector<ABC> x;

public:
    void push(ABC);
    void pop();
    ABC top() const;
    int isEmpty() { return x.empty(); }
};

template <class ABC>
void trial<ABC>::push(ABC element)
{
    x.push_back(element);
}

template <class ABC>
void trial<ABC>::pop()
{
    if (isEmpty() == 1)
    {
        cout << "Empty\n";
        return;
    }
    x.pop_back();
}

template <class ABC>
ABC trial<ABC>::top() const
{
    if (isEmpty() == 1)
    {
        cout << "Empty\n";
        return;
    }
    return x.back();
}

int main()
{
    trial<int> intStack;
    trial<string> stringStack;

    // manipulate int stack
    intStack.push(7);
    cout << intStack.top() << endl;

    // manipulate string stack
    stringStack.push("hello");
    // cout << stringStack.top();
    stringStack.pop();
    stringStack.pop();

    return 0;
}