library IEEE;
use IEEE.STD_LOGIC_1164.ALL;


--this is how entity for test bench code has to be declared.
entity testbench is
end testbench;

architecture behavior of testbench is
--signal declarations.
signal a : std_logic_vector(9 downto 0) :="0010000000";  
signal b : std_logic_vector(9 downto 0) :="1001000000";  
signal reset,flip,cs :  std_logic:='0';
signal led : std_logic_vector(3 downto 0):="0000"; -- others => "0"

begin
--entity instantiation
UUT : entity work.ps1 port map(a,b,reset,flip,cs,led);


--definition of simulation process
tb1 : process
begin
wait for 100 ns;
reset <= not reset;
end process tb1;

tb2 : process
begin
wait for 50 ns;
flip <= not flip;
end process tb2;

tb3 : process
begin
wait for 25 ns;
cs <= not cs;
end process tb3;

end;
