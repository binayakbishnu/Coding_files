#include <bits/stdc++.h>
using namespace std;

int main(){
	set<int> st;
	
	st.insert(9); st.insert(4); st.insert(14); st.insert(6); st.insert(5);
	for(auto it: st){
		cout<<it<<" ";
	}
	cout<<"\n";
	
	auto it = st.find(9);
	cout<<*it;
	it++;
	cout<<*it;
	
	return 0;
}