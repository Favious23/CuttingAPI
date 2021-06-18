set O := {0,1};
set JJ := {1..2};
set J:= {0..28};
set Q{J,O};
param a{o in O, k in J, Q[k,o], J diff {0}} default 0;
param Dem{ JJ };
var X{ o in O, j in J, Q[j,o] } >= 0 integer;
var Y{ JJ } >= 0 integer;
minimize z : sum{ o in O, j in J, q in Q[j,o] }X[o, j, q];
s.t.
r1{ j in JJ }:sum{ o in O, k in J, q in Q[k,o] }a[o, k, q, j] * X[o, k, q] =
	sum{ o in O, q in Q[j,o] }X[o, j, q] + Y[j];
r2{ j in J diff JJ diff {0} }:sum{ o in O, k in J, q in Q[k,o] }a[o, k, q, j] * X[o, k, q] =
	sum{ o in O, q in Q[j,o] }X[o, j, q];
r3{ j in JJ }:Y[j] >= Dem[j]; 
