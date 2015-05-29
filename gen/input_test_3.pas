program test(input, output);
var a : integer;
    b, c : real;
	x, y : integer;
function power(a, b : integer) : integer;
begin
	power := 1;
	while b > 0 do
	begin
		power := power * a;
		b := b -1
	end
end;

function fun1(var a, b : real) : real;
var ab : real;
begin
	ab := a;
	ab := b;
	a := b;
	fun1 := ab
end;

begin
	x := power(2, 3);
	b := fun1(b, c)
end.