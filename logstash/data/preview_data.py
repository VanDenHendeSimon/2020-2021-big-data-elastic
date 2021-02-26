import os
import pandas as pd

path = "/home/student/2020-2021-big-data-elastic/logstash/data"

movies_data = pd.read_csv(os.path.join(path, "movies.csv"))
links_data = pd.read_csv(os.path.join(path, "links.csv"))

print("Movies:")
print(movies_data.head())
print("")

print("Links:")
print(links_data.head())


