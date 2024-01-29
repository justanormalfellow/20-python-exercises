def introduction():
    print("\t\t\tYou've Been Arrested!\t\n\n\tSelect the weekday you've been jailed (from 0 to 6) and the number\n\tof days you'll stay.")
    arrest = int(input("\n\nDay of arrest (from 0 to 6): ")) 
    jailtime = int(input("Jailtime: "))

    return arrest, jailtime


def determine_day(stay, first_day):
    days = (stay + first_day) % 7
    return days

def week_day(result):
    dct = {"sunday": 0, "monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6 }
    for day, value in dct.items():
        if value == result:
            return day



# Main program
if __name__ == "__main__":
    arrest_p, jailtime_p = introduction()
    release_day = determine_day(jailtime_p, arrest_p)
    print(f"\n\nYou'll be released on a {week_day(release_day)}")
