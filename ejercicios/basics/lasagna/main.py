import lasagna

print("Expected time bake is: "+ str(lasagna.EXPECTED_BAKE_TIME))

print("\n")
input_data = [1, 2, 5, 7, 10, 15, 17, 23, 25, 30, 33, 35, 39]

for time in input_data:
    print("Minutes "+str(time)+", backe time remaining is: "+ str(lasagna.bake_time_remaining(time)))

print("\n")
print("Preparation peer number of layers: "+ str(lasagna.preparation_time_in_minutes(2)))

print("\n")
print("Calculate total elapsed cooking time: "+ str(lasagna.elapsed_time_in_minutes(1,3)))
