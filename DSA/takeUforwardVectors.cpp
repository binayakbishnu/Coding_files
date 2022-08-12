#include <bits/stdc++.h>
using namespace std;

int main(){
	vector<int> v;
	v.push_back(1);
	v.emplace_back(2);	//faster
	cout<<v[0]<<v[1];
	
	cout<<"\n";
	vector<pair<int, int>> v2;
	v2.push_back({1,2});
	v2.emplace_back(1,2);	//assumes as pair
	
	vector<int> v3(5,100);	//prefilled vector with 5 100's
	
	cout<<"\n";
	vector<int> v4;
	v4.emplace_back(1);
	v4.emplace_back(21);
	v4.emplace_back(13);
	v4.emplace_back(49);
	vector<int>::iterator it = v4.begin();
	cout<<*it;
	it+=2;	cout<<" ";
	cout<<*it;
	
	return 0;
}