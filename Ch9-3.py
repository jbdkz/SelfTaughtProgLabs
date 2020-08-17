import csv

with open("st.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    list = [["Top Gun", "Risky Business", "Minority Report"],["Titanic", "The Revenant", "Inception"],["Training Day", "Man on Fire", "Flight"]] 
  
    write.writerow(list[0])
    write.writerow(list[1])

