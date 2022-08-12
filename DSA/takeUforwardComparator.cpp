#include <bits/stdc++.h>
using namespace std;

bool comp(pair<int, int> p1, pair<int, int> p2){
	if(p1.second<p2.second) return true;
	if(p1.second>p2.second) return false;
	// now if equal
	if(p1.first<p2.first) return false;
	return true;
}

int main(){
	vector<pair<int, int>> pv;
	pv.push_back({1,2});
	pv.push_back({2,1});
	pv.push_back({5,6});
	pv.push_back({8,9});
	pv.push_back({3,9});
	pv.push_back({4,1});
	
	// sort(pv.begin(), pv.end());
	// sort by: asc by second element, desc by first element if second equal
	sort(pv.begin(), pv.end(), comp);
	
	for(auto it : pv){
		cout<<it.first<<" "<<it.second<<"\n";
	}
	
	return 0;
}