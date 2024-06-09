
num_elements = int(input("Enter the number of elements: "))

total_sum = 0.0
count = 0

while count < num_elements:
  

    number = float(input("Enter a number: "))

  
    total_sum = number + total_sum
    count = count+1




mean = total_sum / count
print("The mean of the", count, "numbers is:", mean)
