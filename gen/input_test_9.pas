program example(input, output);
var x, y : integer;
	x : integer;
	a : array[1..10] of integer;
	
procedure proc(a : integer);
begin
	a := a * 2
end;

function gcd(a, b:integer):integer;
begin
	if b=0 then gcd := a 
	else gcd := gcd(b, a MOD b)
end;

begin
	x := 2.0;
	read(z);
	z := 1;
	a[2.0] := 1;
	x(1, 2);
	proc(1, 3);
	prob(1, 3);
	x :=  1.0 OR 2;
	x := 2.0 MOD 1.2;
	x := not 2.0;
	if 1.9 then x:=1;
	while 1.9 do x:=x+1;
	write(gcd(x,y))
end.