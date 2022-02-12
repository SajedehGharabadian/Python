# OS11-homework
echo "Enter Operator:" --> for print

read O --> this command takes some value from the user's keyboard

if [ $O == "Minus" ] then  res= echo $a - $b | bc --> if the if statement is true, it calculates the subtraction a, b (int,float)

elif [ $O == "Add" ] then   res= echo $a + $b | bc --> if the if statement is true, it calculates the addition a, b (int,float)

elif [ $O == "Mul" ] then   res= echo $a \* $b | bc --> if the if statement is true, it calculates the multiply a, b
(int,float)

elif [ $O == "Div" ] then  res= echo "scale=2; $a / $b" | bc --> if the if statement is true, it calculates the division a, b (int,float)

else echo Error   --> if the user enters a command other than these, the Error command will be printed
