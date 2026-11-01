import pandas as pd
import matplotlib.pyplot as plt
import os


if not os.path.exists("charts"):
    os.mkdir("charts")


players = pd.read_csv("data/players.csv")
matches = pd.read_csv("data/matches.csv")

print("Players ka data:")
print(players.head())
print()
print("Matches ka data:")
print(matches.head())
print()


print("Total players:", len(players))
print("Total matches:", len(matches))
print("Teams:", players["team"].nunique())
print("Missing values:", players.isnull().sum().sum())
print()


players["strike_rate"] = (players["runs"] / players["balls_faced"]) * 100
players["strike_rate"] = players["strike_rate"].round(2)


top_runs = players.sort_values("runs", ascending=False).head(5)
print("Top 5 Run Scorers:")
print(top_runs[["player", "team", "runs"]])
print()

plt.figure(figsize=(8, 5))
plt.bar(top_runs["player"], top_runs["runs"], color="green")
plt.title("Top 5 Run Scorers")
plt.xlabel("Player")
plt.ylabel("Runs")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("charts/top_run_scorers.png")
plt.show()


top_wickets = players.sort_values("wickets", ascending=False).head(5)
print("Top 5 Wicket Takers:")
print(top_wickets[["player", "team", "wickets"]])
print()

plt.figure(figsize=(8, 5))
plt.bar(top_wickets["player"], top_wickets["wickets"], color="orange")
plt.title("Top 5 Wicket Takers")
plt.xlabel("Player")
plt.ylabel("Wickets")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("charts/top_wicket_takers.png")
plt.show()


good = players[players["runs"] >= 500]
best_sr = good.sort_values("strike_rate", ascending=False).head(5)
print("Best Strike Rate (min 500 runs):")
print(best_sr[["player", "team", "strike_rate"]])
print()

team_runs = players.groupby("team")["runs"].sum().sort_values(ascending=False)
print("Team wise total runs:")
print(team_runs)
print()

plt.figure(figsize=(9, 5))
plt.bar(team_runs.index, team_runs.values, color="blue")
plt.title("Team Wise Total Runs")
plt.ylabel("Runs")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("charts/team_runs.png")
plt.show()

wins = matches["winner"].value_counts()
print("Team wise wins:")
print(wins)
print()

plt.figure(figsize=(9, 5))
plt.barh(wins.index, wins.values, color="purple")
plt.title("Team Wise Total Wins")
plt.xlabel("Wins")
plt.tight_layout()
plt.savefig("charts/team_wins.png")
plt.show()

roles = players["role"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(roles.values, labels=roles.index, autopct="%1.1f%%")
plt.title("Players by Role")
plt.savefig("charts/roles.png")
plt.show()

print("Season-wise Champion (Most Wins):")
for season in sorted(matches["season"].unique()):
    season_data = matches[matches["season"] == season]
    champ = season_data["winner"].value_counts().idxmax()
    print(season, "->", champ)

print()
print("Analysis complete! Charts 'charts' save in the folder .")
