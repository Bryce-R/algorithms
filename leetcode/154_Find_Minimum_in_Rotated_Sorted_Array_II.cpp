    int findMin(vector<int>& nums) {
        
        return findMin(nums, 0, nums.size()-1);
    }
    int findMin(vector<int>& nums, int l, int r) {
        
        while(l<r){
            int m = l + (r-l)/2;
            if(nums[m]<nums[r]){
                r = m;
            }else{
                int k = findMin(nums, l, m-1);
                k = min(k, findMin(nums, m+1, r) );
                return k;
            }
        }
        return nums[l];
    }
