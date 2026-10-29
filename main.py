import pandas as pd
import json
import glob
import time
import os
import zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
URL = "https://cricsheet.org/downloads/?utm_source=chatgpt.com"
driver.get(URL)
time.sleep(5)
mi_json = driver.find_element(By.XPATH, '//*[@id="main"]/div/table[3]/tbody/tr[13]/td[2]/ul/li[1]/a')
mi_json.click()
with zipfile.ZipFile(r"C:\Users\NEEL\Downloads\mumbai_indians_json.zip") as zip_file:
    zip_file.extractall("bronze")
total = 0
silayer = []
batter_runs = {}
all_files = glob.glob("bronze/*.json")

for file in all_files:
    df = json.load(open(file))
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None) # none means all coluns will be shown
    squad = df["info"]["players"]["Mumbai Indians"]
    #print(squad)

    neon = next(
        (innings for innings in df["innings"]
         if innings["team"] == "Mumbai Indians"),
        None)

    if neon is None:
        continue

    for x in range(len(neon["overs"])):
        neon1 = (neon["overs"][x])
        #print(neon1)
        neon2 = neon1["deliveries"]
        for y in range(0, len(neon2)):
            neon3 = neon2[y]
            #print(f"{neon3}")
            list1 = []
            if neon3["batter"] in squad:
                neon4 = neon3["runs"]["batter"]
                total = total + neon4

                batter = neon3["batter"]

                if batter not in batter_runs:
                    batter_runs[batter] = 0

                batter_runs[batter] += neon4
                silayer.append({
                    "over": neon1["over"],
                    "batter": neon3["batter"],
                    "bowler": neon3["bowler"],
                    "runs": neon3["runs"]["batter"],
                    "is_wide":
                        "wides" in neon3.get("extras", {}),
                    "legal_ball":
                        "wides" not in neon3.get("extras", {})

                })

#print(total)
#print(batter_runs)
maxi = max(batter_runs.values())
#for key, value in batter_runs.items():
#if value == maxi:
#print(f"The highest run scorer is {key} with {value} runs.")

print(silayer)
print("------------------------------------------------------------------------------")
silverdata = pd.DataFrame(silayer)
silverdata.index = silverdata.index + 1
silverdata["over"] = silverdata["over"] + 1
#print(silverdata)
silverdata.to_csv("silver/silverdata.csv", index=False)

runs = silverdata.groupby("batter")["runs"].sum()
balls_faced = silverdata[silverdata["legal_ball"]].groupby("batter").size()
sr = runs / balls_faced * 100
maximum_sr = max(sr)
maximum_runs = max(runs)
print(f"{runs}{balls_faced}{sr}")
helo = {"orange_cap": f"{runs.idxmax()}-{maximum_runs}",
        "best_sr": f"{sr.idxmax()}-{maximum_sr}"
        }# idmax() returns the name of batter with highest runs and sr
stats = pd.DataFrame([helo])
print(stats)
stats.to_csv("gold/stats.csv", index=False)
run_table = pd.DataFrame({
    "runs": runs,
    "balls_faced": balls_faced,
    "strike_rate": sr
})
run_table = run_table.reset_index()  # for making batter  as columns

run_table.columns = [
    "batter",
    "runs",
    "balls_faced",
    "strike_rate"
]
run_table.sort_values("runs", ascending=False, inplace=True)

print(run_table)

run_table.to_csv("gold/run_table.csv", index=False)
sr_table = pd.DataFrame({
    "runs": runs,
    "balls_faced": balls_faced,
    "strike_rate": sr
})
sr_table = sr_table.reset_index()
sr_table.columns = [
    "batter",
    "runs",
    "balls_faced",
    "strike_rate"

]
sr_table.sort_values("strike_rate", ascending=False, inplace=True)
print("\n")
print(sr_table)
sr_table.to_csv("gold/sr_table.csv", index=False)
