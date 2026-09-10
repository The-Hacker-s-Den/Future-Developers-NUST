import numpy
import math

#The Pendulum Experiment:

print("\n\nPendulum Experiment:\n")

#Calculated Raw Data

lengths_of_string = [36.4,36.6,35.5,36.4,36.4]
Diameters_of_bob = [1.105,1.105,1.105,1.0475,1.105]
radii_of_bob = [d/2 for d in Diameters_of_bob]
total_time_10_cycles = [12.78,13.34,12.93,12.12,11.19,11.97]
time_periods = [t/10 for t in total_time_10_cycles]



#Working On Radius
mean_radius_of_bob = numpy.mean(radii_of_bob)
print("\n\nThe mean Radius of the bob is: " + str(round(mean_radius_of_bob, 4)))

standard_deviation_radius_of_bob = numpy.std(radii_of_bob, ddof = 4)
print("The Standard Deviation in the radius of the bob is: " + str(round(standard_deviation_radius_of_bob, 4)))

standard_error_radius_of_bob = standard_deviation_radius_of_bob/numpy.sqrt(len(radii_of_bob))
print("The Standard Error in the radius of the bob is: " + str(round(standard_error_radius_of_bob, 4)))



#Working On String
mean_length_of_string = numpy.mean(lengths_of_string)

standard_deviation_length_of_string = numpy.std(lengths_of_string, ddof = 2)
print("Standard Deviation is: " + str(round(standard_deviation_length_of_string, 4)))

standard_error_length_of_string = standard_deviation_length_of_string/numpy.sqrt(len(lengths_of_string))
print("Standard Error in Length: " + str(round(standard_error_length_of_string, 4)))



#Working On Total Length of the String
total_length = mean_length_of_string + mean_radius_of_bob
standard_error_total_length = numpy.sqrt((pow(standard_error_radius_of_bob, 2) + pow(standard_error_length_of_string, 2)))
print("\nThe mean Total Length of the string is: " + str(round(total_length, 4)))

standard_deviation_total_length_of_string = numpy.std(lengths_of_string, ddof = 2)
print("The Standard Deviation in the Total length of the string is: " + str(round(standard_deviation_length_of_string, 4)))

standard_error_length_of_string = standard_deviation_length_of_string/numpy.sqrt(len(lengths_of_string))
print("The Standard Error in the length of the string is: " + str(round(standard_error_length_of_string, 4)))



#Working On Time Periods
mean_time_period = numpy.mean(time_periods)
print("\nThe mean Time Period is: " + str(round(mean_time_period, 4)))

standard_deviation_time_period = numpy.std(time_periods, ddof = 2)
print("The Standard Deviation in Time Period is: " + str(round(standard_deviation_time_period, 4)))

standard_error_time_period = standard_deviation_time_period/numpy.sqrt(len(time_periods))
print("The Standard Error in Time Period is: " + str(round(standard_error_time_period, 4)))

#Working with Mean Squared Time Period
Mean_Squared_Time_Period = pow(mean_time_period, 2)
standard_error_squared_time_period = numpy.sqrt(((pow(mean_time_period, 2) + pow(standard_error_time_period, 2)))*2)
print("The Standard Error in the square of the Time Period is: " + str(round(standard_error_squared_time_period, 4)))

ratio_length_to_time_period_squared = total_length/Mean_Squared_Time_Period

mean_value_gravitational_acceleration = 4*math.pi*math.pi*ratio_length_to_time_period_squared

print("\nThe mean value of Gravitational Acceleration is: " + str(round(mean_value_gravitational_acceleration, 4)))


#Plz calculate the standard error in the mean value of Gravitational Acceleration

standard_error_gravitational_acceleration = numpy.sqrt(((pow((1/Mean_Squared_Time_Period), 2)*pow(standard_error_total_length, 2))+(pow((total_length/Mean_Squared_Time_Period), 2)*pow(standard_error_squared_time_period, 2))))
print("\nThe Standard Error in the mean value of Gravitational Acceleration is: " + str(round(standard_error_gravitational_acceleration, 4)))