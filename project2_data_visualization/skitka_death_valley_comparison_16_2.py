# This solution has a bug, cannot display the data correctly.
# It looks like the get_weather_data calling doesn't changed
# the three lists.

import csv
from matplotlib import pyplot as plt
from datetime import datetime

def get_weather_data(filename, dates, highs, lows):
    """Get dates, high, and low temperatures from file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
    
        # Delete the following line, otherwise it will hide the parameters!!
        # Causing the result cannot be passed out!!!!!
        # dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:    
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)


# Get weather data for Sitka.

dates, highs, lows = [], [], []
get_weather_data('sitka_weather_2014.csv', dates, highs, lows)
print(highs)
print(lows)
# Plot Sitka weather data.
# The follwing alpha value controls a color's transparency.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.6)
plt.plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# Get weather data for death valley.

dates, highs, lows = [], [], []
get_weather_data('death_valley_2014.csv', dates, highs, lows)

print(highs)
print(lows)
# Plot Death Valley weather data.
# The follwing alpha value controls a color's transparency.
plt.plot(dates, highs, c='red', alpha=0.3)
plt.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

# Format plot.
title = "Daily high and low temperatures - 2014"
title += "\nSitka, AK and Death Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
# draws the date labels diagonally to prevent them from overlapping
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
# Most important part, set y value range.
plt.ylim(10, 120)

plt.show()
