# Ask the user for their name
username = input("Whats is your name?")

# Ask the user for their favorite integer
fav_num = int(input("Favorite Number?"))

# Double, halve and sqaure the number
double = fav_num * 2
half = fav_num / 2
sqaured = fav_num * fav_num

print()
# Greet the user
print("Hi {}, your favorite number is {}".format(username, fav_num))
print()
# Output the results of doudling,halving
#and sqauring their favorite number
print("double {} is {}".format(fav_num, double))
print("half {} is {}".format(fav_num, half))
print("{} sqaured is {}".format(fav_num, sqaured))
print()