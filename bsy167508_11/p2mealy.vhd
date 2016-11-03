----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity p2mealy is
    Port ( seq : in  STD_LOGIC;
           det_vld : out  STD_LOGIC;
           clk : in  STD_LOGIC;
           reset : in  STD_LOGIC;
			  led : out std_logic_vector (4 downto 0));
end p2mealy;

architecture Behavioral of p2mealy is
type state is (s0, s1, s2, s3, s4);
signal present_state,next_state : state;
begin
	sreg: process(clk, reset)
	begin
	if (reset='1') then
		present_state<=s0;
	elsif clk'event and (clk='1') then -- on the rising edge of the clock
		present_state<=next_state;
-------these led states represent the states of our finite state machine------------
		case present_state is
		when s0 => led<="10000";
		when s1 => led<="01000";
		when s2 => led<="00100";
		when s3 => led<="00010";
		when s4 => led<="00001";
		end case;
	end if;
	end process;
	
	
	c1 : process(present_state,seq)
	begin
	case present_state is
	when s0 => 
	if seq='1' then
		next_state<=s1;
	else
		next_state<=s0;
	end if;

	when s1 => 
	if seq='1' then
		next_state<=s2;
	else
		next_state<=s0;
	end if;

	when s2 => 
	if seq='1' then
		next_state<=s2;
	else
		next_state<=s3;
	end if;

	when s3 => 
	if seq='1' then
		next_state<=s1;
	else
		next_state<=s4;
	end if;

	when s4 => 
	if seq='1' then
		next_state<=s1;
	else
		next_state<=s0;
	end if;

	when others => 
	null;
	end case;
	end process;

	c2: process(clk, reset)
	begin

	if reset='1' then 
		det_vld<='0';
	elsif clk'event and clk='1' then
		if present_state=s4 and seq='1' then -- detect the sequence
			det_vld<='1';
		else
			det_vld<='0';
		end if;
	end if;

	end process;
end Behavioral;
