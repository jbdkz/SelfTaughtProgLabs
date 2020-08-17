color = input("What is your favorite color?")

with open ("st.txt","w") as f:
    f.write("John's favorite color is " + color)

with open ("st.txt","r") as f:
    print(f.read()) 




