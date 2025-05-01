# Program to count leap years in a given range

def count_leap_years(start_year, end_year):
    leap_years = 0
    for year in range(start_year, end_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1
    return leap_years

# Input range
start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))

# Count and display leap years
leap_year_count = count_leap_years(start_year, end_year)
print(f"Number of leap years between {start_year} and {end_year}: {leap_year_count}")