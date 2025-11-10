import requests
import json
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

    name_university = input("Select a  university: ")
    while name_university not in dictionary:
        name_university = input("Not a valid university select a university: ")
    print(dictionary[name_university])

    data_link = "https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json"
    uni = (requests.get(data_link)).json()
    for i in uni: 
        if name_university in i["name"]:
            print (i["web_pages"])
            website = i["web_pages"]
        
            with open("Universities.csv", "w") as file:
                writer = csv.writer(file)
            for i2 in dictionary[name_university]:
                writer.writerow(['i2'])
                writer.writerow([website])
            break
    
    with open("Universities.csv", "w") as file:
        writer = csv.writer(file)
        for i2 in dictionary[name_university]:
            writer.writerow(['i2'])
        writer.writerow([website])


main()