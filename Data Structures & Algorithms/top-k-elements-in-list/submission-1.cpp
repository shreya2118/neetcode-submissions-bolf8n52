class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        for(int n:nums){
            mp[n]++;
        }
        vector<int> res;
        vector<pair<int,int>> temp;
        for(auto it:mp){
            temp.push_back(make_pair(it.second,it.first));
        }
        sort(temp.rbegin(),temp.rend());
        for(int i=0;i<temp.size() && k!=0;i++){
            res.push_back(temp[i].second);
            k--;
        }
        return res;
    }
};
