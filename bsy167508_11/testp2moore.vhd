LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY testp2moore IS
END testp2moore;

ARCHITECTURE behavior OF testp2moore IS 

   signal clk,reset,seq,det_vld : std_logic := '0';
	---declare sequence to be detected
   signal sequence : std_logic_vector (17 downto 0):= "110011001001100110";
	---initialise the system
   signal led : std_logic_vector(5 downto 0) := "000000";
   constant clk_period : time := 10 ns;

BEGIN

    -- Instantiate the Unit Under Test (UUT)
   uut: entity work.p2moore PORT MAP (
          clk => clk,
          reset => reset,
          seq => seq,
          det_vld => det_vld,
			 led => led
        );

   -- Clock process definitions
   clk_process :process
   begin
        clk <= '0';
        wait for clk_period/2;
        clk <= '1';
        wait for clk_period/2;
   end process;

   -- Stimulus process : Apply the bits in the sequence one by one.
   stim_proc: process
   begin        
   for i in 0 to 17 loop
	seq <= sequence(i);
	wait for clk_period;
	end loop;
   end process;

END;
