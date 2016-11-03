----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    13:00:59 10/18/2016 
-- Design Name: 
-- Module Name:    ps1 - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
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

entity ps1 is
port (
	a : in std_logic_vector (9 downto 0);
	b : in std_logic_vector (9 downto 0);
	reset : in std_logic; -- active low
	flip : in std_logic;
	cs : in std_logic; -- active low
	--clk : in std_logic;
	led : out std_logic_vector (3 downto 0) -- eq, lt, gt, flip
		); 
end ps1;

architecture Behavioral of ps1 is

begin
	process(a,b,reset,flip,cs)
	begin
	if (reset = '0') and (flip = '0') and (cs = '0') then -- all are active low.
		if (a=b) then led(0) <= '1'; else led(0) <= '0'; end if;
      if (a<b) then led(1) <= '1'; else led(1) <='0'; end if;
		if (a>b) then led(2) <= '1'; else led(2) <= '0'; end if; 
		led(3) <= '0';
	elsif (reset = '0') and (flip = '1') and (cs = '0')then -- greater than, less than flipped.
		if (a=b) then led(0) <= '1'; else led(0) <= '0'; end if;
		if (a>b) then led(1) <= '1'; else led(1) <='0'; end if;
		if (a<b) then led(2) <= '1'; else led(2) <= '0'; end if; 
		led(3) <= '1';
	else
		led <= "0000";
	end if;
	end process;

end Behavioral;