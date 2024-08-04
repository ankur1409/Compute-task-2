import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('data.csv')

# Checking  for duplicates
duplicate_count = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_count}")

# Drop/remove duplicates
df.drop_duplicates(inplace=True)

# Print data types
print(df.dtypes)






# Checking  for missing values
for col in df.columns:
    if df[col].isnull().any():
        print(f"Column '{col}' has {df[col].isnull().sum()} missing values")
num_columns = df.shape[1]
print(f"Number of columns: {num_columns}")
#inputting values for body type using work rate column
conditions = [
    (df['work_rate'] == 'High/High'),
    (df['work_rate'] == 'High/Medium'),
    (df['work_rate'] == 'Medium/Medium'),
    (df['work_rate'] == 'Medium/Low'),
    (df['work_rate'] == 'Low/Low'),
]
values = ['Muscular','Lean','Fit','Slim','Normal']
df['body_type'] = np.select(conditions, values, default=df['body_type'])

#  a pie chart of the top 100 players based on overall value, separated by nationality
top_players = df.nlargest(100, 'overall')
nationality_counts = top_players['nationality'].value_counts()
others_count = nationality_counts[nationality_counts < 2].sum()
nationality_counts = nationality_counts[nationality_counts >= 2]
nationality_counts['Others'] = others_count

plt.figure(figsize=(18,15))
plt.pie(nationality_counts, labels=nationality_counts.index, autopct=lambda p : '{:.0f}'.format(p * sum(nationality_counts)/100))
plt.title('Top 100 Players by Nationality')
plt.show()

#  a histogram of the distribution of player ages
plt.figure(figsize=(10,6))
sns.histplot(df['age'], bins=10)
plt.title('Distribution of Player Ages')
plt.show()

# Calculating the average of overall, potential, and value_eur
df['avg_rating'] = (df['overall'] + df['potential'] + df['value_eur']) / 3

# Getting the top 100 players based on the average rating
top_players = df.nlargest(100, 'avg_rating')

# Getting the distribution of player positions for the top 100 players
position_counts = top_players['player_positions'].value_counts()
other_count = position_counts[position_counts < 2].sum()
position_counts = position_counts[position_counts >= 2]
position_counts['Others'] = other_count

# a pie chart of the distribution of player positions
plt.figure(figsize=(10,6))
plt.pie(position_counts, labels=position_counts.index, autopct=lambda p : '{:.0f}'.format(p * sum(position_counts)/100))
plt.title('Distribution of Player Positions (Top 100 by Average Rating)')
plt.show()
#  a scatter plot of the relationship between player overall value and age
plt.figure(figsize=(10,6))
sns.scatterplot(x='age', y='overall', data=df)
plt.title('Relationship between Player Overall Value and Age')
plt.show()



# a scatter plot of the relationship between player potential and age
plt.figure(figsize=(10,6))
sns.scatterplot(x='age', y='potential', data=df)
plt.title('Relationship between Player Potential and Age')
plt.show()

# a scatter plot of the relationship between player overall value and potential
plt.figure(figsize=(10,6))
sns.scatterplot(x='potential', y='overall', data=df)
plt.title('Relationship between Player Overall Value and Potential')
plt.show()

# a 3D scatter plot of the relationship between player overall value, potential, and age
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['age'], df['potential'], df['overall'])
ax.set_xlabel('Age')
ax.set_ylabel('Potential')
ax.set_zlabel('Overall Value')
plt.title('Relationship between Player Overall Value, Potential, and Age')
plt.show()

# calculate the average rating for each player
df['average_rating'] = (df['overall'] + df['potential'] + df['value_eur']) / 3

# get the top 20 players based on average rating
top_20_players = df.nlargest(20, 'average_rating')

# calculate the probability of winning the Ballon d'Or for each player
top_20_players['probability'] = top_20_players['average_rating'] / top_20_players['average_rating'].sum()

# plot a bar graph showing the probability of the top 20 players winning the Ballon d'Or
plt.figure(figsize=(12,8))
sns.barplot(x='short_name', y='probability', data=top_20_players)
plt.title('Probability of Top 20 Players Winning the Ballon d\'Or')
plt.xlabel('Player Name')
plt.ylabel('Probability')
plt.xticks(rotation=90)
plt.show()


# Get the top 100 players based on overall
top_players = df.nlargest(100, 'overall')

# Group the top players by team and count the number of players in each team
team_counts = top_players['team'].value_counts()

# Get the top 25 teams with the highest number of top players
top_teams = team_counts.nlargest(25)

# Plot a bar graph of the top 25 teams
plt.figure(figsize=(12,8))
sns.barplot(x=top_teams.index, y=top_teams.values)
plt.title('Top 25 Teams with the Highest Number of Top 100 Players')
plt.xlabel('Team Name')
plt.ylabel('Number of Top 100 Players')
plt.xticks(rotation=90)
plt.show()
