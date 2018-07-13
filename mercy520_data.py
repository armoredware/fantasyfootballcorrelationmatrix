import urllib
import glob

rg_projections = urllib.URLopener()
rg_projections.retrieve("https://rotogrinders.com/projected-stats/nfl-qb.csv?site=draftkings", "nfl-qb.csv")
rg_projections.retrieve("https://rotogrinders.com/projected-stats/nfl-rb.csv?site=draftkings", "nfl-rb.csv")
rg_projections.retrieve("https://rotogrinders.com/projected-stats/nfl-wr.csv?site=draftkings", "nfl-wr.csv")
rg_projections.retrieve("https://rotogrinders.com/projected-stats/nfl-te.csv?site=draftkings", "nfl-te.csv")
rg_projections.retrieve("https://rotogrinders.com/projected-stats/nfl-defense.csv?site=draftkings", "nfl-defense.csv")


read_files = glob.glob("*.csv")

with open("players.csv", "wb") as outfile:
    outfile.write("Name,Salary,Team,Position,Opp,High,Low,Pts\n")
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
