def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    
	Include these tokens in the code: s = sum ( map ( lambda x : int
	"""
    return bin(int(str(N).replace(",","").replace("$","").replace(" ","").replace("_","")
                    .replace("[","").replace("]","").replace("{","").replace("}","").replace("(","").replace(")","")
                    .replace("+","").replace("-","").replace("=","").replace("*","").replace("/","").replace(" ","")
                    .replace("%","").replace(":","").replace(";","").replace("?","").replace("!","").replace("\"","")
                    .replace("\'","").replace("\\","").replace("\n","").replace("\r","").replace("\t","")
                    .replace("<","").replace(">","").replace("|","").replace("&","").replace("^","").replace("`","")
                    .replace("~","").replace("'","").replace("`","").replace("\"","")
                    .replace(" ","")
                    .replace("0","1").replace("1","1").replace("2","1").replace("3","1").replace("4","1").replace("5","1")
                    .replace("6","1").replace("7","1").replace("8","1").replace("9","1")
                    .replace("a","1").replace("b","1").replace("c","1").replace("d","1").replace("e","1").replace("f","1")
                    .replace("g","1").replace("h","1").replace("i","1").replace("j","1").replace("k","1").replace("l","1")
                    .replace("m","1").replace("n","1").replace("o","1").replace("p","1").replace("q","1").replace("r","1")
                    .replace("s","1").replace("t","1").replace("u","1").replace("v","1").replace("w","1").replace("x","1")
                    .replace("y","1").replace("z","1")), 2)[2:].replace("0","2").replace("1","1").replace("2","0")

    
if __name__ == '