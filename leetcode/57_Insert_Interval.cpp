    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        if(intervals.empty()) return {newInterval};
        vector<Interval> ans = intervals;
        if(newInterval.end < intervals[0].start ) { ans.insert( ans.begin(), newInterval); return ans; }
        if(newInterval.start > intervals.back().end ) { ans.push_back(newInterval); return ans; }
        int b = 0, e = intervals.size()-1;
        for(int i =0; i<intervals.size();i++){
            if(  intervals[i].end < newInterval.start ) {
                b = i+1;  }
            if( intervals[i].start > newInterval.end ) {
                e = i-1;  break; }
        }
        Interval toInsert( min(intervals[b].start, newInterval.start), max(intervals[e].end, newInterval.end) );
        ans.erase( ans.begin()+b, ans.begin()+e+1 );
        ans.insert(ans.begin()+b, toInsert);
        
        return ans;
    }
