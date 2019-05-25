import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Get dates, high, and low temperatures from file.
# filename = 'death_valley_2014.csv'
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
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
    
    print(highs)

    # Plot data.
    # The follwing alpha value controls a color's transparency.
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    title = "Daily high and low temperatures - 2014\nSitka, AK"
    # title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    # draws the date labels diagonally to prevent them from overlapping
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    # Most important part, set y value range.
    plt.ylim(10, 120)

    plt.show()
