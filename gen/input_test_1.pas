program test(input, output);
var a : integer;
    b : real;
	rec : record
        ra : integer;
        rb : real;
		aa : record
			t:integer;
			cd : array[1..100] of real
		end;
		arr : array[1..100] of real
    end;
	arra : array[1..100] of Boolean;
	arrb : array[1..50] of integer;
	boo : Boolean;

begin
	a := 2;
	b := 2.0;
	arra[1] := false;
	arrb[1] := 1;
	a := arra[1];
	arra[1] := a;
	boo := true
end.