#include<iostream>
#include<string>
#include<unordered_map>
#include<vector>
using namespace std;
int main(){
    vector<int> arr;
    int n;
    cout<<"Enter the size of the array: ";
    cin>>n;
    for(int i=0; i<n;i++){
        int x;
        cout<<"Enter the element: ";
        cin>>x;
        arr.push_back(x);
    }

    vector<int> ans;
    unordered_map<int, bool> mp;
    for(int i=0;i<n;i++){
        if(mp.count(arr[i])>0){
            continue;

        }
        mp[arr[i]]=true;
        ans.push_back(arr[i]);
    }
    
    cout<<"The unique elements are: ";
    for (int i=0; i<ans.size();i++){
        cout<<ans[i]<<" ";
    }
}