import time
import pandas as pd
import numpy as np

CITY_DATA_files = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington).
    print('Please, Enter the name of the city you want to explore')
    print('The data available is for the cities of Chicago, New York city and Washington \nSo choose one of them, please:')

    while True:
        city = input().lower()
        if city in ['chicago', 'new york city', 'washington']
            print('Please, enter the month you wish to see data for, between january to june')
            print('If you want to check the data for all months available, please ente all')

                # Get user input for month (all, january, february, ... , june)
            while True:
                month = input().lower()
                if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                    print('Please, enter the day you wish to see data for from monday to sunday \nor all if you want to see data for the whole week')

                    # get user input for day of week (all, monday, tuesday, ... sunday)
                    while True:
                        day=input().lower()
                        if day in ['monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'all']:
                            print('Great, let\'s see the data you want')
                            break
                        else:
                            print('Maybe there is a mistake in the name of the day, please entter the day again')
                    break
                else:
                    print('the month you entered is wrong or not available, please enter another month or all again')
            break
        else:
            print('the name of city you entered may have a mistake, or you entered a non-available city')
            print('please enter the name of the city again from the list mentioned above')


    print('-'*40)
    return city, month, day



def load_data(city, month, day):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_com_month = df['month'].mode()[0]
    print('the most common month is: ', most_com_month)

    # TO DO: display the most common day of week
    most_com_day = df['day_of_week'].mode()[0]
    print('the most common day of week is: ', most_com_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_com_hour = df['hour'].mode()[0]
    print('the most common hour is: ', most_com_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


dimport time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington).
    print('Please, Enter the name of the city you want to explore')
    print('The data available is for the cities of Chicago, New York city and Washington \nSo choose one of them, please:')

    while True:
        city = input().lower()
        if city in ['chicago', 'new york city', 'washington']:
            print('Please, enter the month you wish to see data for, between january to june')
            print('If you want to check the data for all months available, please ente all')

                # Get user input for month (all, january, february, ... , june)
            while True:
                month = input().lower()
                if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                    print('Please, enter the day you wish to see data for from monday to sunday \nor all if you want to see data for the whole week')

                    # get user input for day of week (all, monday, tuesday, ... sunday)
                    while True:
                        day=input().lower()
                        if day in ['monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'all']:
                            print('Great, let\'s see the data you want')
                            break
                        else:
                            print('Maybe there is a mistake in the name of the day, please entter the day again')
                    break
                else:
                    print('the month you entered is wrong or not available, please enter another month or all again')
            break
        else:
            print('the name of city you entered may have a mistake, or you entered a non-available city')
            print('please enter the name of the city again from the list mentioned above')


    print('-'*40)
    return city, month, day



def load_data(city, month, day):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_com_month = df['month'].mode()[0]
    print('the most common month is: ', most_com_month)

    # TO DO: display the most common day of week
    most_com_day = df['day_of_week'].mode()[0]
    print('the most common day of week is: ', most_com_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_com_hour = df['hour'].mode()[0]
    print('the most common hour is: ', most_com_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_com_st_station = df['Start Station'].mode()[0]
    print('The most common Start Station is: ',most_com_st_station)

    # TO DO: display most commonly used end station
    most_com_end_station = df['End Station'].mode()[0]
    print('The most common End Station is: ',most_com_end_station)

    # Display most common trip
    df['Trips']=df['Start Station']+' -- To -- '+df['End Station']
    most_com_trip = df['Trips'].value_counts()
    print('The most trip is between:\t\t',most_com_trip.index[0],'\n','Count:\t\t',most_com_trip.values[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('the total travel time across all trips in this period is (minute): ', total_travel_time/60)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('the mean travel time across all trips in this period is (minute): ', mean_travel_time/60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('the count of all users is: \n',user_type_count)

    # TO DO: Display counts of gender
    gender_count = df['Gender'].value_counts()
    print('the count of gender available is: \n',gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    early_yob = df['Birth Year'].min()
    recent_yob = df['Birth Year'].max()
    com_yob = df['Birth Year'].mode()[0]
    print('The earliest year of birth is: ',early_yob)
    print('The most recent year of birth is: ',recent_yob)
    print('The most common year of birth is: ',com_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print('Displaying the statistics on the most frequent times of travel...')
        time_stats(df)
        print('Displaying the statistics on the most popular stations and trip...')
        station_stats(df)
        print('Displaying the statistics on the total and average trip duration ...')
        trip_duration_stats(df)
        print('Displaying the statistics on the bikeshare users...')
        user_stats(df)
        print('Do you want to see sample of the individual trip data during this period? please type yes or no')
        # Check if the user want to see the individual trip data
        while True:
            reply = input().lower()
            if reply == 'yes':
                n=5
                print('Okay, here is the sample of the trip data during this period')
                while n>=5:
                    print(df[['Start Station','End Station','Start Time','End Time','Trip Duration','Gender','User Type','Birth Year']].head(n))
                    print('Do you want longer samples? please type yes or no:')
                    reply2 = input().lower()
                    if reply2 == 'yes':
                        print('Okay, here is the longer sample of the trip data during this period')
                        n+=5
                    else:
                        break
                break
            else:
                print('please type yes or no only')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

        df = load_data(city, month, day)
        print('Displaying the statistics on the most frequent times of travel...')
        time_stats(df)
        print('Displaying the statistics on the most popular stations and trip...')
        station_stats(df)
        print('Displaying the statistics on the total and average trip duration ...')
        trip_duration_stats(df)
        print('Displaying the statistics on the bikeshare users...')
        user_stats(df)
        print('Do you want to see sample of the individual trip data during this period? please type yes or no')
        # Check if the user want to see the individual trip data
        while True:
            reply = input().lower()
            if reply == 'yes':
                n=5
                print('Okay, here is the sample of the trip data during this period')
                while n>=5:
                    print(df.head(n))
                    print('Do you want longer samples? please type yes or no:')
                    reply2 = input().lower()
                    if reply2 == 'yes':
                        print('Okay, here is the longer sample of the trip data during this period')
                        n+=5
                    else:
                        break
                break
            else:
                print('please type yes or no only')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
