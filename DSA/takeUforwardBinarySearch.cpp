#include <bits/stdc++.h>
using namespace std;

int main(){
	int a[] = {3,1,6,7,3,9,2};
	
	sort(a,a+7);
	for(auto it: a){
		cout<<it<<" ";
	}
	cout<<"\n";
	
	bool binSea = binary_search(a,a+7,9);
	cout<<binSea;
	
	return 0;
}