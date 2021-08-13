#include <iostream>
#include <math.h>

using namespace std;

class Vec3
{
    int x, y, z;

public:
    int returnx() {return x;}
    int returny() {return y;}
    int returnz() {return z;}

    void getdata()
    {
        cout << "x: ";
        cin >> x;
        cout << "y: ";
        cin >> y;
        cout << "z: ";
        cin >> z;
    }
    double magnitude()
    {
        double x1 = pow(x, 2);
        double y1 = pow(y, 2);
        double z1 = pow(z, 2);
        double w = sqrt(x1 + y1 + z1);
        return w;
    }
    double dot_prod(Vec3 V)
    {
        double dprod = x * V.returnx() + y * V.returny() + z*V.returnz();
        return dprod;
    }
    double cross_prod(Vec3 V)
    {
        double m1 = magnitude();
        double m2 = V.magnitude();
        double mxm = m1*m2;
        double cos_angle = dot_prod(V)/mxm;
        double angle = (acos(cos_angle))*180/3.1415;
        double cprod = magnitude()*V.magnitude()*sin(angle);
        return cprod;
    }
};

int main()
{
    Vec3 v1;
    Vec3 v2;
    v1.getdata();
    v2.getdata();

    cout<<v1.magnitude()<<"\n"<<v2.magnitude()<<"\n";
    cout<<v1.dot_prod(v2)<<"\n";
    cout<<v1.cross_prod(v2)<<"\n";

    return 0;
}