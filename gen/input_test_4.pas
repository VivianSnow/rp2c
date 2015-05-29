program test(input, output);
var a : integer;
    b, c : real;
	x, y : integer;
procedure swap(var x, y : integer);
var temp : integer;
begin
	temp := x;
	x := y;
	y := temp
end;

procedure test(a : integer);
var k : integer;
begin
	k := 1
end;

begin
	x := 1;
	y := 3;
	swap(x, y);
	test(1)
end.