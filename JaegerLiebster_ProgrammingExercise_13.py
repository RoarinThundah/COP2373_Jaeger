import sqlite3
import random
import matplotlib.pyplot as plt
import sys

# Config
DB_NAME = "population_AI.db"
INITIAL_YEAR = 2023
SIMULATION_YEARS = 20
SIMULATION_END_YEAR = INITIAL_YEAR + SIMULATION_YEARS

# Initial data for 10 Florida cities for 2023
FLORIDA_CITIES_2023 = [
    ("Miami", 440000),
    ("Orlando", 316000),
    ("Tampa", 390000),
    ("Jacksonville", 971000),
    ("St. Petersburg", 260000),
    ("Hialeah", 238000),
    ("Tallahassee", 201000),
    ("Fort Lauderdale", 188000),
    ("Port St. Lucie", 240000),
    ("Cape Coral", 220000),
]


def create_and_initialize_db(db_name, initial_data):

    # Creates the SQLite database, the population table, and inserts the initial data for 2023.

    print(f"1. Creating database and table: {db_name}")
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Create table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS population (
                city TEXT NOT NULL,
                year INTEGER NOT NULL,
                population INTEGER NOT NULL,
                PRIMARY KEY (city, year)
            )
        ''')
        conn.commit()

        # Insert initial 2023 data
        insert_query = "INSERT OR IGNORE INTO population (city, year, population) VALUES (?, ?, ?)"

        data_to_insert = [(city, INITIAL_YEAR, pop) for city, pop in initial_data]
        cursor.executemany(insert_query, data_to_insert)

        conn.commit()
        print(f"   Successfully inserted initial data for {len(initial_data)} cities for the year {INITIAL_YEAR}.")

    except sqlite3.Error as e:
        print(f"Database error during initialization: {e}")
    finally:
        if conn:
            conn.close()


def simulate_population_changes(db_name, start_year, end_year):

    print(f"2. Simulating population for the next {end_year - start_year} years (2024 - {end_year}).")
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Retrieve initial population for starting year
        cursor.execute("SELECT city, population FROM population WHERE year = ?", (start_year,))
        city_populations = {city: pop for city, pop in cursor.fetchall()}

        total_records_inserted = 0

        # Loop through years after initial year
        for current_year in range(start_year + 1, end_year + 1):
            new_populations = []

            for city, current_pop in city_populations.items():
                # Randomly determine an annual rate of change between -2.0% and +3.5%
                # This simulates varying growth and decline
                rate = random.uniform(-0.02, 0.035)

                # Calculate new population (ensuring it's an integer and never drops below zero)
                new_pop = int(current_pop * (1 + rate))
                new_pop = max(0, new_pop)  # Ensure population is non-negative

                new_populations.append((city, current_year, new_pop))

                # Update the population for the next year's calculation
                city_populations[city] = new_pop

            # Insert the newly calculated population data into the database
            insert_query = "INSERT OR IGNORE INTO population (city, year, population) VALUES (?, ?, ?)"
            cursor.executemany(insert_query, new_populations)
            total_records_inserted += len(new_populations)

        conn.commit()
        print(f"   Simulation complete. Inserted {total_records_inserted} new population records.")

    except sqlite3.Error as e:
        print(f"Database error during simulation: {e}")
    finally:
        if conn:
            conn.close()


def plot_population_growth(db_name):

    #Prompts the user to select a city and displays its population growth over time using Matplotlib.

    print("\n3. Population Growth Visualizer")
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Get the list of available cities
        cursor.execute("SELECT DISTINCT city FROM population ORDER BY city")
        cities = [row[0] for row in cursor.fetchall()]

        if not cities:
            print("No city data found in the database to plot.")
            return

        print("\nAvailable Cities:")
        for i, city in enumerate(cities):
            print(f"  {i + 1}. {city}")

        # Get user input
        while True:
            try:
                choice = input(f"\nEnter the number of the city you want to plot (1-{len(cities)}): ")
                city_index = int(choice) - 1
                if 0 <= city_index < len(cities):
                    selected_city = cities[city_index]
                    break
                else:
                    print("Invalid selection. Please choose a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Retrieve data for the selected city
        print(f"Fetching data for {selected_city}...")
        cursor.execute(
            "SELECT year, population FROM population WHERE city = ? ORDER BY year",
            (selected_city,)
        )
        data = cursor.fetchall()

        if not data:
            print(f"No population data found for {selected_city}.")
            return

        years = [row[0] for row in data]
        populations = [row[1] for row in data]

        # Matplotlib Plotting
        plt.style.use('seaborn-v0_8-darkgrid')
        plt.figure(figsize=(10, 6))

        plt.plot(years, populations,
                 marker='o',  # Add circular markers
                 linestyle='-',  # Solid line
                 color='#1f77b4',  # Standard blue color
                 linewidth=2,
                 markersize=6,
                 label=f'{selected_city} Population')

        # Add titles and labels
        plt.title(f'Simulated Population Growth/Decline for {selected_city} ({INITIAL_YEAR} - {SIMULATION_END_YEAR})',
                  fontsize=14, fontweight='bold')
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Population', fontsize=12)

        # Customize ticks and grid
        plt.xticks(years, rotation=45, ha='right')
        plt.yticks(fontsize=10)
        plt.ticklabel_format(style='plain', axis='y')  # Prevent scientific notation on y-axis

        # Add annotations for start and end points
        plt.annotate(f'Start: {populations[0]:,}', (years[0], populations[0]),
                     textcoords="offset points", xytext=(-15, 15), ha='center',
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2", color='green'))

        plt.annotate(f'End: {populations[-1]:,}', (years[-1], populations[-1]),
                     textcoords="offset points", xytext=(15, 15), ha='center',
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2", color='red'))

        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()  # Adjust layout to prevent labels from overlapping

        # Display the plot
        plt.show()

    except sqlite3.Error as e:
        print(f"Database error during plotting: {e}")
    except Exception as e:
        print(f"An error occurred during plotting: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    # 1. Create and Initialize Database
    create_and_initialize_db(DB_NAME, FLORIDA_CITIES_2023)

    # 2. Simulate Population Changes
    simulate_population_changes(DB_NAME, INITIAL_YEAR, SIMULATION_END_YEAR)

    # 3. Visualize the Results
    plot_population_growth(DB_NAME)

    print("\nProgram finished. Check the generated chart for the selected city.")