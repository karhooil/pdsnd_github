# <Project: Explore US Bikeshare Data>
# In this project, you will write Python code to import US bike share data and answer interesting questions about it by computing descriptive statistics. 
# You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.
# You can submit your files as a .zip archive or you can link to a GitHub repository containing your project files. There is no need for you to include any data files with your submission.

import time
import datetime
import pandas as pd

CITY_DATA = {'Chicago':'10_2-chicago.csv', 'New York City':'10_2-new_york_city.csv', 'Washington':'10_2-washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) input_city - name of the city to analyze
        (int if filtering; otherwise str) input_month - name of the month to filter by, or "all" to apply no month filter
        (int if filtering; otherwise str) input_dow - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city
    while True:
        input_city = input("\nPlease select city ('Chicago', 'New York City' or 'Washington') to be analyzed: ").strip().title()
        if input_city == 'Chicago':
            break
        elif input_city == 'New York City':
            break
        elif input_city == 'Washington':
            break
        else:
            print('Invalid city or please check spelling.')
            continue

    # get user input for month
    while True:
        input_month = input("\nPlease select month ('Jan', 'Feb', ... , 'Dec') to be filtered by, or you may enter 'all' to view all months: ").strip().title()
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        if input_month in months:
            input_month = months.index(input_month) + 1
            break
        elif input_month == 'All':
            input_month = 'All'
            break
        else:
            print('Invalid month or please check spelling. Please ensure you\'ve entered the abbreviated 3-letter month if you\'re filtering by month.')
            continue

    # get user input for day of week 
    while True:
        input_dow = input("\nPlease select day of week ('Mon', 'Tue', ... , 'Sun') to be filtered by, or you may enter 'all' to view all days: ").strip().title()
        dows = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        if input_dow in dows:
            input_dow = dows.index(input_dow)
            break
        elif input_dow == 'All':
            input_dow = 'All'
            break
        else:
            print("Invalid day of week (dow) or please check spelling. Please ensure you\'ve entered the abbreviated 3-letter dow if you\'re filtering by dow.")
            continue

    print('-'*40)
    return input_city, input_month, input_dow

# city, month, dow = get_filters() # testing

def load_data(city, month, dow):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (int if filtering; otherwise str) month - name of the month to filter by, or "all" to apply no month filter
        (int if filtering; otherwise str) dow - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city]) 

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['starting_month'] = df['Start Time'].dt.month
    df['starting_month_name'] = df['Start Time'].dt.month_name()
    df['starting_day_of_week'] = df['Start Time'].dt.dayofweek
    df['starting_day_name'] = df['Start Time'].dt.day_name()
    df['starting_hour'] = df['Start Time'].dt.hour

    if month != 'All':
        df = df[df['starting_month'] == month]

    if dow != 'All':
        df = df[df['starting_day_of_week'] == dow]
        
    if df.empty:
        print('No data is available for the selected filter(s).')
        return df
    else:
        return df

# city, month, dow = get_filters() # testing
# df = load_data(city, month, dow) # testing

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    if df.empty:
        print('No data is available for the selected filter(s).')
    else:
        print('\nCalculating: The Most Frequent Times of Travel...\n')

        start_time = time.time()

        # display the most common starting month
        mode_month = df['starting_month_name'].mode()[0]
        print('\nMost Common Starting Month:', mode_month)

        # display the most common starting day of week
        mode_dow = df['starting_day_name'].mode()[0]
        print('\nMost Common Starting Day of Week:', mode_dow)

        # display the most common starting hour
        mode_hour = df['starting_hour'].mode()[0]
        print('\nMost Common Starting Hour:', mode_hour)

        print("\nThis calculation took {} seconds.".format(time.time() - start_time))
        print('-'*40)

# city, month, dow = get_filters() # testing
# df = load_data(city, month, dow) # testing
# time_stats(df) # testing

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    if df.empty:
        print('No data is available for the selected filter(s).')
    else:
        print('\nCalculating: The Most Popular Stations and Trip...\n')

        start_time = time.time()

        # display most commonly used start station
        mode_start_station = df['Start Station'].mode()[0]
        print('\nMost Common Starting Station:', mode_start_station)

        # display most commonly used end station
        mode_end_station = df['End Station'].mode()[0]
        print('\nMost Common Ending Station:', mode_end_station)

        # display most frequent combination of start station and end station trip
        df['trip'] = "from '" + df['Start Station'] + "' to '" + df['End Station'] + "'"
        mode_trip = df['trip'].mode()[0]
        print('\nMost Common Trip:', mode_trip)

        print("\nThis calculation took {} seconds.".format(time.time() - start_time))
        print('-'*40)

# city, month, dow = get_filters() # testing
# df = load_data(city, month, dow) # testing
# time_stats(df) # testing
# station_stats(df) # testing

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    if df.empty:
        print('No data is available for the selected filter(s).')
    else:
        print('\nCalculating: Trip Duration...\n')

        start_time = time.time()

        # display total travel time
        total_dur = df['Trip Duration'].sum()
        print('\nTotal Travel Time:', total_dur, 'seconds')

        # display mean travel time
        mean_dur = df['Trip Duration'].mean()
        print('\nAverage Travel Time:', mean_dur, 'seconds')

        print("\nThis calculation took {} seconds.".format(time.time() - start_time))
        print('-'*40)

# city, month, dow = get_filters() # testing
# df = load_data(city, month, dow) # testing
# time_stats(df) # testing
# station_stats(df) # testing
# trip_duration_stats(df) # testing

def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    if df.empty:
        print('No data is available for the selected filter(s).')
    else:
        print('\nCalculating: User Stats...\n')

        start_time = time.time()

        # Display counts of user types
        user_dist = df['User Type'].value_counts().sort_values(ascending=False)
        print('\nThe following shows the distribution of user type: ')
        print(user_dist)

        if city == 'Chicago' or city == 'New York City':
            # Display counts of gender
            gender_dist = df['Gender'].value_counts().sort_values(ascending=False)
            print('\nThe following shows the distribution of gender type: ')
            print(gender_dist)
            # Display earliest, most recent, and most common year of birth
            earliest_yr = df['Birth Year'].min()
            print('\nThe Earliest Year of Birth:', int(earliest_yr))
            latest_yr = df['Birth Year'].max()
            print('The Latest Year of Birth:', int(latest_yr))
            mode_year = df['Birth Year'].mode()[0]
            print('Most Common Year of Birth:', int(mode_year))

        print("\nThis calculation took {} seconds.".format(time.time() - start_time))
        print('-'*40)

# city, month, dow = get_filters() # testing
# df = load_data(city, month, dow) # testing
# time_stats(df) # testing
# station_stats(df) # testing
# trip_duration_stats(df) # testing
# user_stats(df, city) # testing

def dis_raw(df):
    """Displays up to 5 rows of raw data each time when prompted."""
    if df.empty:
        print('No data is available for the selected filter(s).')
    else:
        start_count = 0
        df = df.reset_index()
        for index, row in df.iterrows():
            input_raw = input("Would you like to view the raw data in the multiples of 5 ('yes' or 'no')?\n").strip().lower()
            if input_raw == 'yes':
                print(df.loc[start_count : start_count + 4])
                start_count = start_count + 5
                if start_count > len(df.index):
                    print('No more data to be displayed.')
                    break
            elif input_raw == 'no':
                break
            else:
                print("Invalid input. Please enter 'yer' or 'no'.")

            print('-'*40)   

# city, month, dow = get_filters() # testing
# df = load_data(city, month, dow) # testing
# time_stats(df) # testing
# station_stats(df) # testing
# trip_duration_stats(df) # testing
# user_stats(df, city) # testing
# dis_raw(df) # testing

def main():
    while True:
        city, month, dow = get_filters()
        df = load_data(city, month, dow)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        dis_raw(df)

        input_restart = input("\nWould you like to restart? Please enter 'yes' or 'no': ").strip().lower()
        if input_restart != 'yes':
            break

if __name__ == "__main__":
	main()