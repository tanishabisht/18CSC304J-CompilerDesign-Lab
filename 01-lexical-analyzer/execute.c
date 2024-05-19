# include < stdio.h >

void main ( ) {
    int n , i , sum = 0 ;
    scanf ( "%d" , & n ) ;
    for ( i = 1 , i <= n , ++ i ) {
        sum += 1 ;
    }
    printf ( "%d" , sum ) ;
    return 0 ;
}
