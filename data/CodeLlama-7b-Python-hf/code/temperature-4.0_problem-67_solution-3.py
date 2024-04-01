def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    print("s: {} type: {} len: {} n {}".format(s,type(s),len(s),n) )
    splitted = s.split(' ')
    
    #get only the integers
    # splited = ['5','apples','6','orange',',']  #list of string 6 strings in this example
    count_apples = [i for i in splitted if i.isnumeric()[0]]
    count_apples = ''.join(count_apples)
    count_apples_int = (10**len(count_apples))-1 #get the largest number possible like if 3333 return int(3) for example 233 will be int(233)
    # 12300364100591749844519147897369452445423794589114444190351902910312312210223231284734876348973498688473498349586486343674687867586463446757896786674678354735436784736473645436757364579878676476847764767867584636475764573685847846763674856784763678476785476573677647765786798897979876467867769987647996784764664789756789646786746998646567486776484674686846768486746864699866785664699864669998689985867686996769979999676565985646559554564654659674685695646465686664698564685648648569864564546464564664566453676896467999995656468564568956456859565685696484685649856468956985869859669595869669859665665966556556466646466486485866458566569645696956469656966464856658566569564684648956658689564695665696566564645665998665664856655659569566958665699856695664664595666465699986566955966966966856656566656456564664656656665686956568