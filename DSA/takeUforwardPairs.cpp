#include <bits/stdc++.h>
using namespace std;

int main(){
	pair<int, int> p = {1,3};
	cout<<p.first<<" "<<p.second;
	
	cout<<"\n";
	pair<int, pair<int, int>> q = {1, {2, 3}};
	cout<<q.first<<q.second.first<<q.second.second;
	
	cout<<"\n";
	pair<int, int> arr[] = {
		{1,2},
		{3,4},
	};
	
	cout<<arr[0].first;

	return 0;
}