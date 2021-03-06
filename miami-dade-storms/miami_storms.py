import matplotlib.pyplot as plt
import pandas as pd
import statistics as st

from rich_dataframe import prettify


# Import csv into DataFrame
miami = pd.read_csv(
    "../datasets/miami-dade-storm-data.csv",
    header=0,
    sep=",",
    low_memory=False,
    parse_dates=["BEGIN_DATE"],
)
# Show the DataFrame
print(miami)
# Make it pretty - just for fun!
prettify(miami)
# Display the shape of the dataset
print(f"The shape of the Miami-Dade County storm wind events dataset is {miami.shape}.")
# Display descriptive statistics for numerical values in the dataset
miami.describe()
# Count totals of each wind event type in the dataset
events = miami["EVENT_TYPE"]
events.value_counts()
# For this EDA, I am only interested in the dates and event types
miami_storms = miami[["BEGIN_DATE", "EVENT_TYPE"]]
print(miami_storms)
# Plot the dates and events
y = miami_storms["EVENT_TYPE"]
x = miami_storms["BEGIN_DATE"]
plt.plot_date(x, y)
# Create sample sizes
sample_twenty = miami_storms.sample(20)
sample_thirty = miami_storms.sample(30)
# Repeat the samples to make different samples and display in bar graphs
(sample_twenty.groupby(["BEGIN_DATE", "EVENT_TYPE"]).size().unstack().plot.bar())
(sample_thirty.groupby(["BEGIN_DATE", "EVENT_TYPE"]).size().unstack().plot.bar())
# Count annual occurrences of storm wind events in Miami-Dade County
events_annual = miami_storms.groupby(pd.Grouper(key="BEGIN_DATE", axis=0, freq="1Y")).count()
print(events_annual)
events_annual.describe()
# Plot the annual frequencies for storm wind events
ev_plot = events_annual.plot()
ev_plot.set_xlabel("Year")
ev_plot.set_ylabel = "Wind Events Frequency"
# Now analyze the magnitude of Thunderstorm Winds over the time period
thunderstorm_winds = miami[miami["EVENT_TYPE"]=="Thunderstorm Wind"]
thunderstorm_winds = thunderstorm_winds[["BEGIN_DATE", "EVENT_TYPE", "MAGNITUDE"]]
print(thunderstorm_winds)
# Make it pretty - just for fun!
prettify(thunderstorm_winds)
# Check value types
thunderstorm_winds.info()
# Magnitude is an "Object" but needs to be numerical
thunderstorm_winds["MAGNITUDE"] = thunderstorm_winds["MAGNITUDE"].astype(float)
# Now get a few descriptive statistics
thunderstorm_winds.describe()
# Create a plot of the magnitudes.
y = thunderstorm_winds["MAGNITUDE"]
x = thunderstorm_winds["BEGIN_DATE"]
plt.plot_date(x, y)
# Return the population variance of Thunderstorm Wind magnitudes
print(st.pvariance(thunderstorm_winds["MAGNITUDE"]))
# Return the mode of wind magnitudes
print(st.mode(thunderstorm_winds["MAGNITUDE"]))
