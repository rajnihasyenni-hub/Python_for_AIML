distance = float(input("Enter distance travelled (km): "))

fare = 0

if distance <= 12:
    fare = 100
elif distance <= 16:
    fare = 100 + (distance - 12) * 8
elif distance <= 20:
    fare = 100 + (4 * 8) + (distance - 16) * 6
else:
    fare = 100 + (4 * 8) + (4 * 6) + (distance - 20) * 5

print("Total fare: Rs.", fare)
