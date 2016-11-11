library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity p2moore is
    Port ( seq : in  STD_LOGIC;
           clk : in  STD_LOGIC;
           reset : in  STD_LOGIC;
           det_vld : out  STD_LOGIC;
			  led : out std_logic_vector (5 downto 0));
end p2moore;

architecture Behavioral of p2moore is
	type state is (s0, s1, s2, s3, s4, s5);
	signal present_state,next_state : state;
	begin
	sreg: process(clk, reset)
		begin
		if (reset='1') then
			present_state<=s0;
		elsif clk'event and (clk='1') then
			present_state<=next_state;
-------these led states represent the states of our finite state machine------------
			case present_state is
			when s0 => led<="100000";
			when s1 => led<="010000";
			when s2 => led<="001000";
			when s3 => led<="000100";
			when s4 => led<="000010";
			when s5 => led<="000001";
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
			next_state<=s0;
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

	c2: process(present_state)
	begin
	if present_state=s4 then
		det_vld<='1';
	else
		det_vld<='0';
	end if;
	end process;
end Behavioral;

