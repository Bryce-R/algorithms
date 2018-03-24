    int lastRemaining(int n) {
        if(n==1) return 1;
        int begin = 1, end = n, diff = 1, temp = 0;
        while( end != begin ){
           if( n&1 ) { temp = begin; begin = end- diff; end = temp+diff; }
           else { temp = begin; begin = end; end = temp +diff; }
           diff*=-2;
           n>>=1;
        }
        return begin;
    }
