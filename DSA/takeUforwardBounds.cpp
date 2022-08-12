#include <bits/stdc++.h>
using namespace std;

int main(){
	int a[] = {7,4,2,5,6,9,3};
	
	sort(a,a+7);
	for(auto it: a){
		cout<<it<<" ";
	}
	cout<<"\n";
	
	auto lb = lower_bound(a,a+7,1)-a;
	cout<<lb<<"\n";
	auto ub = upper_bound(a,a+7,1)-a;
	cout<<ub;
	
	return 0;
}