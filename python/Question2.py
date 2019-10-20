# modify this function, and create other functions below as you wish
def question02(trader,risk,bonus):
    for val1 in range(len(trader)):
        for val in range(len(risk)):
            d=0
            total1=0
            if (trader[val1] > risk[val] or trader[val1] == risk[val]):
                pos.append(val)
            for item2 in pos:
               total.append(bonus[item2])

        d=max(total,key=int)
        max_val.append(d)
    for sum_tot in max_val:
     total1 = total1 + int(sum_tot)


    return pos,max_val,total1


def trader_input(trader,num_of_traders):
    if num_of_traders >1 and num_of_traders < 10000:
      for item1 in range(num_of_traders):
        x = input("Enter the values of trader{}:".format(item1))
        trader.append(x)



def risk_input(risk,num_of_risk):
    if num_of_risk > 1 and num_of_risk < 10000:
        for item2 in range(num_of_risk):
            x = input("Enter the values of risk{}:".format(item2))
            risk.append(x)


def bonus_input(bonus,num_of_bonus):

    if num_of_bonus > 1 and num_of_bonus < 10000:
     for item3 in range(num_of_bonus):
        x = input("Enter the values of bonus{}:".format(item3))
        bonus.append(x)



def input1():
 l=int(input("Enter the number of values you want to give for risk:"))
 m=int(input("Enter the number of values you want to give for trader:"))
 n=int(input("Enter the number of values you want to give for bonus:"))
 return l,m,n

num_of_risk,num_of_trader,num_of_bonus = input1()


risk=[]
trader=[]
bonus=[]
pos=[]
total=[]

max_val=[]
c=0
trader_input(trader,num_of_trader)
print("The values of trader are:{}".format(trader))
risk_input(risk,num_of_risk)
print("The values of risk are:{}".format(risk))
bonus_input(bonus,num_of_bonus)
print("The values of bonus are:{}".format(bonus))
pos1,pos2,pos3=question02(trader,risk,bonus)
print("The positions where the trader value is greater than the risk is:{}".format(pos1))
print("The maximum bonus are:{}".format(pos2))

print("The total bonus is: {}".format(pos3))
