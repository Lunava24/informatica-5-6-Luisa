import requests
import csv

def main():
    dictionary = {
        "Eastern Arizona College": {
            "Number of Majors": 140,
            "Average semester cost": 0,
            "Closest campus location": "Thatcher",
            "Distance_km": 451,
        },
        "URN": {
            "Number of Majors": 29,
            "Average semester cost": 10000,
            "Closest campus location": "Cuidad Juarez",
            "Distance_km": 275,
        },
        "tec_Casas_Grandes": {
            "Number of Majors": 8,
            "Average semester cost": 3000,
            "Closest campus location": "Casas Grandes",
            "Distance_km": 12,
        },
        "BYU_Pathway": {
            "Number of Majors": 30,
            "Average semester cost": 30000,
            "Closest campus location": "Online",
            "Distance_km": 0,
        },
        "UACJ": {
            "Number of Majors": 37,
            "Average semester cost": 5000,
            "Closest campus location": "Cuidad Juarez",
            "Distance_km": 265,
        }
    }

    name_university = input("Select a university: ")
    while name_university not in dictionary:
        name_university = input("Not a valid university, select a university: ")
    
    print(dictionary[name_university])

    data_link = "https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json"
    uni = requests.get(data_link).json()
    
    website = ""
    for i in uni: 
        if name_university in i["name"]:
            website = i["web_pages"]
            print("Website(s):", website)  # Show the website(s)
            break

    with open("Universities.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(['University Name', 'Number of Majors', 'Average Semester Cost', 'Closest Campus Location', 'Distance (km)', 'Website(s)'])

        uni_data = dictionary[name_university]
        writer.writerow([
            name_university,
            uni_data['Number of Majors'],
            uni_data['Average semester cost'],
            uni_data['Closest campus location'],
            uni_data['Distance_km'],
            website if website else "No website found"
        ])

    print(f"Data for {name_university} written to 'Universities.csv'.")

main()
