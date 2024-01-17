# import subprocess
# subprocess.run(["pip", "install", "selenium"])
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClinicalTrialsInfo:
    def __init__(self, NCTid):
        self.url = "https://clinicaltrials.gov/study/" + str(NCTid) + "?aggFilters=results:with&rank=1&tab=results"
        self.adverse_events = None
        self.collaborators = None

    def get_adverse_events(self):
        driver = webdriver.Chrome()  # You can change this according to your WebDriver

        try:
            driver.get(self.url)
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "adverse-events"))
            )

            element_list = element.text.split("\n")
            element_list = element_list[element_list.index('Serious Adverse Events'):]
            totals = []
            totals_indices = []
            for index, item in enumerate(element_list):
                if "Total" in item.split(" "):
                    totals.append(item)
                    totals_indices.append(index)
            for index, item in enumerate(element_list):
                if index > max(totals_indices) and "%" in list(item):
                    totals.append(item)

            self.adverse_events = totals

        finally:
            driver.quit()

    def get_collaborators(self):
        driver = webdriver.Chrome()  # You can change this according to your WebDriver

        try:
            driver.get(self.url)
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "collaborators-and-investigators"))
            )
            element_list = element.text.split("\n")
            colab_indices = [element_list.index("Sponsor"), element_list.index("Collaborators"),
                             element_list.index("Investigators")]
            colabs = []
            for item in colab_indices:
                colabs.append(element_list[item + 1])

            self.collaborators = colabs

        finally:
            driver.quit()


# Usage:
# NCTid = "NCT02199574"
# trial_info = ClinicalTrialsInfo(NCTid)
# trial_info.get_adverse_events()
# trial_info.get_collaborators()

# print("Adverse Events:", trial_info.adverse_events)
# print("Collaborators:", trial_info.collaborators)

def get_adverse_events(nct_list):
    adverse_events = []

    for nct in nct_list:
        try:
            trial_info = ClinicalTrialsInfo(nct)
            
            trial_info.get_adverse_events()

            adverse_events.append(trial_info.adverse_events)
        except Exception as e:
            
            print(f"Error processing NCT ID {nct}: {str(e)}")
            adverse_events.append(None)  

    return adverse_events


def get_collabs(nct_list):
    collabs = []

    for nct in nct_list:
        try:
            trial_info = ClinicalTrialsInfo(nct)
            
            trial_info.get_collaborators()

            collabs.append(trial_info.collaborators)
        except Exception as e:
            
            print(f"Error processing NCT ID {nct}: {str(e)}")
            collabs.append(None)  

    return collabs

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py NCTid1 NCTid2 NCTid3 ...")
        sys.exit(1)

    nct_list = sys.argv[1:]

    adverse_events = get_adverse_events(nct_list)
    collabs = get_collabs(nct_list)

    for nct, events, collaborators in zip(nct_list, adverse_events, collabs):
        print(f"NCT ID: {nct}")
        print("Adverse Events:", events)
        print("Collaborators:", collaborators)
        print("\n")
        with open("temp_results.txt","w") as file:
            file.write(f"NCT ID: {nct}, Adverse Events: {events}, Collaborators: {collaborators}")


if __name__ == "__main__":
    main()
#call using python3 /Users/manas/Documents/GitHub/trading/virtenv/GetResults.py NCT02199574
    
sys.exit()