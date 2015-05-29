program test(input, output);
var a : integer;
    b, c : real;
	x, y : integer;

procedure print(a : integer);
begin
	write(a)
end;

function power(a, b : integer) : integer;
begin
	power := 1;
	while b > 0 do
	begin
		power := power * a;
		b := b - 1
	end
end;

begin
	read(x, y);
	write(power(x, y));
	read(a);
	print(a);
	read(b, c);
	write(b, c)
end.