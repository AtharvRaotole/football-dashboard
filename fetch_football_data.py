import requests  # type: ignore
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

# API Details
api_key = "YOUR API KEY"  # Replace with your actual API key
base_url = "https://api.football-data.org/v4"
headers = {"X-Auth-Token": api_key}
competition_id = 2001  # UEFA Champions League example


# Step 2: Fetch Competition Details
def fetch_competition_details():
    response = requests.get(f"{base_url}/competitions/{competition_id}", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"Competition Name: {data['name']}")
        print(f"Area: {data['area']['name']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")


# Step 3: Fetch Competition Standings
def fetch_competition_standings():
    response = requests.get(f"{base_url}/competitions/{competition_id}/standings", headers=headers)
    if response.status_code == 200:
        standings_data = response.json()
        standings = standings_data['standings'][0]['table']
        standings_df = pd.DataFrame([
            {
                'Position': team['position'],
                'Team': team['team']['name'],
                'Played Games': team['playedGames'],
                'Won': team['won'],
                'Draw': team['draw'],
                'Lost': team['lost'],
                'Points': team['points'],
                'Goals For': team['goalsFor'],
                'Goals Against': team['goalsAgainst'],
                'Goal Difference': team['goalDifference']
            }
            for team in standings
        ])
        return standings_df  # Explicitly return DataFrame
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


# Step 4: Fetch Top Scorers
def fetch_top_scorers():
    response = requests.get(f"{base_url}/competitions/{competition_id}/scorers", headers=headers)
    if response.status_code == 200:
        scorers_data = response.json()
        top_scorers = scorers_data['scorers']
        scorers_df = pd.DataFrame([
            {
                'Player': player['player']['name'],
                'Team': player['team']['name'],
                'Goals': player['goals'],
                'Assists': player.get('assists', 0),
                'Matches Played': player['playedMatches']
            }
            for player in top_scorers
        ])
        return scorers_df  # Explicitly return DataFrame
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


# Step 5: Visualization

# Top 10 Teams by Points
def plot_top_10_teams(standings_df):
    top_10 = standings_df.sort_values(by='Points', ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    plt.bar(top_10['Team'], top_10['Points'])
    plt.title('Top 10 Teams by Points')
    plt.xlabel('Teams')
    plt.ylabel('Points')
    plt.xticks(rotation=45)
    plt.show()


# Goals For vs Goals Against
def plot_goals_for_vs_against(standings_df):
    plt.figure(figsize=(12, 6))
    plt.scatter(standings_df['Goals For'], standings_df['Goals Against'], c='b', marker='o')
    plt.title('Goals For vs Goals Against')
    plt.xlabel('Goals For')
    plt.ylabel('Goals Against')
    plt.show()


# Top 5 Scorers by Goals
def plot_top_5_scorers(scorers_df):
    top_5 = scorers_df.sort_values(by='Goals', ascending=False).head(5)
    plt.figure(figsize=(12, 6))
    plt.bar(top_5['Player'], top_5['Goals'])
    plt.title('Top 5 Scorers by Goals')
    plt.xlabel('Players')
    plt.ylabel('Goals')
    plt.xticks(rotation=45)
    plt.show()


# Goals vs Matches Played
def plot_goals_vs_matches(scorers_df):
    plt.figure(figsize=(12, 6))
    plt.scatter(scorers_df['Matches Played'], scorers_df['Goals'], c='r', marker='o')
    plt.title('Goals vs Matches Played')
    plt.xlabel('Matches Played')
    plt.ylabel('Goals')
    plt.show()

# Top Defensive Teams
def plot_top_defensive_teams(standings_df):
    top_defensive = standings_df.sort_values(by='Goals Against').head(5)
    plt.figure(figsize=(12, 6))
    plt.bar(top_defensive['Team'], top_defensive['Goals Against'])
    plt.title('Top 5 Defensive Teams (Fewest Goals Conceded)')
    plt.xlabel('Teams')
    plt.ylabel('Goals Conceded')
    plt.xticks(rotation=45)
    plt.show()


# Top Attacking Teams
def plot_top_attacking_teams(standings_df):
    top_attacking = standings_df.sort_values(by='Goals For', ascending=False).head(5)
    plt.figure(figsize=(12, 6))
    plt.bar(top_attacking['Team'], top_attacking['Goals For'])
    plt.title('Top 5 Attacking Teams (Most Goals Scored)')
    plt.xlabel('Teams')
    plt.ylabel('Goals Scored')
    plt.xticks(rotation=45)
    plt.show()


# Efficiency Analysis: Points per Game
def plot_team_efficiency(standings_df):
    standings_df['Points per Game'] = standings_df['Points'] / standings_df['Played Games']
    top_efficiency = standings_df.sort_values(by='Points per Game', ascending=False).head(5)
    plt.figure(figsize=(12, 6))
    plt.bar(top_efficiency['Team'], top_efficiency['Points per Game'])
    plt.title('Top 5 Teams by Points per Game')
    plt.xlabel('Teams')
    plt.ylabel('Points per Game')
    plt.xticks(rotation=45)
    plt.show()


# Top Assisters
def plot_top_assisters(scorers_df):
    top_assisters = scorers_df.sort_values(by='Assists', ascending=False).head(5)
    plt.figure(figsize=(12, 6))
    plt.bar(top_assisters['Player'], top_assisters['Assists'])
    plt.title('Top 5 Assisters')
    plt.xlabel('Players')
    plt.ylabel('Assists')
    plt.xticks(rotation=45)
    plt.show()


# Goals per Match
def plot_goals_per_match(scorers_df):
    scorers_df['Goals per Match'] = scorers_df['Goals'] / scorers_df['Matches Played']
    top_efficiency = scorers_df.sort_values(by='Goals per Match', ascending=False).head(5)
    plt.figure(figsize=(12, 6))
    plt.bar(top_efficiency['Player'], top_efficiency['Goals per Match'])
    plt.title('Top 5 Players by Goals per Match')
    plt.xlabel('Players')
    plt.ylabel('Goals per Match')
    plt.xticks(rotation=45)
    plt.show()


# Main Execution
if __name__ == "__main__":
    # Fetch Competition Details
    fetch_competition_details()
    
    # Fetch and Visualize Standings
    standings_df = fetch_competition_standings()
    if standings_df is not None:
        plot_top_10_teams(standings_df)
        plot_goals_for_vs_against(standings_df)
    else:
        print("Failed to fetch standings data. Please check the API response.")
    
    # Fetch and Visualize Top Scorers
    scorers_df = fetch_top_scorers()
    if scorers_df is not None:
        plot_top_5_scorers(scorers_df)
        plot_goals_vs_matches(scorers_df)
    else:
        print("Failed to fetch scorers data. Please check the API response.")

    # Advanced Standings Analysis
    if standings_df is not None:
        plot_top_defensive_teams(standings_df)
        plot_top_attacking_teams(standings_df)
        plot_team_efficiency(standings_df)

        # Advanced Scorers Analysis
    if scorers_df is not None:
        plot_top_assisters(scorers_df)
        plot_goals_per_match(scorers_df)

    
    # Save DataFrames to CSV
    if standings_df is not None:
        standings_df.to_csv('standings_data.csv', index=False)
        print("Standings data saved as 'standings_data.csv'")

    if scorers_df is not None:
        scorers_df.to_csv('scorers_data.csv', index=False)
        print("Scorers data saved as 'scorers_data.csv'")

    
