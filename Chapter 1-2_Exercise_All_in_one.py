#1.How many seconds in an hour? Use python interpreter as calculator -
#multiply number of minutes in minute by the number of minutes in an hour:

second = 1
sec_per_minute = second * 60
print(f"""\tNumber of seconds in one minute is {sec_per_minute},
        Number of minutes in an hour is {sec_per_minute * 60}""")



#2.Assign last result to the new variable named "seconds_per_hour"

sec_per_hour = sec_per_minute * 60
print(sec_per_hour)



#3.How many seconds in day? Use last variable "seconds_per_hour"

print(f"There are {sec_per_hour * 24} seconds in a day")



#4.Calculate sec_per_day again. This time save the result in a variable

sec_per_day = sec_per_hour * 24
print(sec_per_day)



#5.Divide variable sec_per_day by variable sec_per_hour.
    #Use floating point division

print(sec_per_day / sec_per_hour)



#6.Divide them again using integer division.
    #Does the result match to the last one?

print(sec_per_day // sec_per_hour)
if (sec_per_day / sec_per_hour) == (sec_per_day // sec_per_hour):
    print("Looks the same to the last one")
else:
    print("Looks different to the last one")





