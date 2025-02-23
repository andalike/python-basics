# Get the Oldest/Youngest person, and Average Age, Sum of all the age
import requests
from typing import Dict
import json
from datetime import datetime

class UserAgeAnalyzer:
    def __init__(self):
        self.api_url = "https://randomuser.me/api/"
        self.users_data =[]

    def fetch_users(self, count : int = 10) -> None:
        try:
            response = requests.get(f"{self.api_url}?results={count}")
            if response.status_code == 200:
                self.users_data = response.json()['results']
                self.save_to_file()
            else:
                print(f"API Returned error : {response.status_code}")
        except Exception as e:
            print("Error in fetching data from API: {e}")

    def save_to_file(self) -> None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"user_data_{timestamp}.json"
        with open(filename,'w') as f:
            json.dump(self.users_data,f,indent=2)
        print(f"Data is saved to {filename}")

    def analyze_ages(self) -> Dict:
        if not self.users_data:
            return {"error":"No User Data is Foind"}
        
        age_data = []
        for user in self.users_data:
            name = f"{user['name']['first']}{user['name']['last']}"
            age = user['dob']['age']
            age_data.append((name,age))

        min_age_user = min(age_data, key=lambda x: x[1])
        max_age_user = max(age_data, key=lambda x: x[1])
        
        ages = [age for _, age in age_data]
        avg_age = sum(ages) / len(ages)

        analysis = {
            "total_users" : len(age_data),
            "youngest_person" :{
               "name": min_age_user[0],
               "age":min_age_user[1]
            },
            "oldest_person":{
                "name": max_age_user[0],
               "age":max_age_user[1]
            },
            "average_age" : round(avg_age,1),
            "sum_of_age" :sum(ages),
            "all_users":[{"name":name, "age":age} for name,age in age_data]  
        }
        return(analysis)
    

def main():
    analyzer = UserAgeAnalyzer()

    print("Callig API to fetch the users")
    analyzer.fetch_users(20)
    # Analyse all the ages of the people and operation
    analysis = analyzer.analyze_ages()

    print("Analysis")
    print(f"Total Users: {analysis['total_users']}")
    print(f"\n Yongest Person : {analysis['youngest_person']['name']} ({analysis['youngest_person']['age']})")
    print(f"\n Oldest Person : {analysis['oldest_person']['name']} ({analysis['oldest_person']['age']})")
    print(f"Average Age:{analysis['average_age']} years")
    print(f"sum of all the ages:{analysis['sum_of_age']} years")
    print("\n All User List")
    for user in analysis['all_users']:
        print(f"{user['name']} : { user['age'] } years")

if __name__ == "__main__":
    main()










