from rich.console import Console
import subprocess as sp
import pymysql
import pymysql.cursors
from colorama import Fore, Style, init
init(autoreset=True)  # Automatically reset styles after each print

from banner import print_banner
from divine_weapons import get_divine_weapons
from warriors import get_warriors_by_kingdom
from battle_formations import get_battle_formations
from kingdoms import get_kingdoms_by_alliance
from anga import get_total_strength_by_anga
from warrior_name import search_warriors_by_name
from div_weapon_kingdom import list_divine_weapons_by_kingdom
from add_warrior import Add_warrior
from delete_event import delete_event_and_related_data
from formation_warrior import get_formation_and_warrior_names
from add_formation import add_new_formation
from modify_battle_form import modify_battle_formation
from print_menu import print_menu   

console = Console()

def Delete_warrior():
    print("delete warrior")

def dispatch(ch):
    if ch == 1:
        get_warriors_by_kingdom(cur)
    elif ch == 2:
        get_divine_weapons(cur)
    elif ch == 3:
        get_battle_formations(cur)
    elif ch == 4:
        get_kingdoms_by_alliance(cur)
    elif ch == 5:
        get_total_strength_by_anga(cur)
    elif ch == 6:
        search_warriors_by_name(cur)
    elif ch == 7:
        list_divine_weapons_by_kingdom(cur)
    elif ch == 8:
        get_formation_and_warrior_names(cur)
    elif ch == 9:
        Add_warrior(cur,con)
    elif ch == 10:
        modify_battle_formation(cur, con)
    elif ch == 11:
        delete_event_and_related_data(cur, con)
    elif ch == 12:
        add_new_formation(cur, con)
        
    else:
        print(Fore.LIGHTRED_EX+ Style.BRIGHT + "Error: Invalid Option" + Style.RESET_ALL)


# Get database connection details from the user
# user = input("Enter the database username (default 'root'): ") or "root"
# password = input("Enter the database password: ")
# db = input("Enter the database name (default 'ldb'): ") or "ldb"
user = "root"
password = "pass@dna123A"
db = "pp4"

# Global
try:
    # Establish the database connection once
    con = pymysql.connect(
        host='localhost',
        port=3306,
        user=user,
        password=password,
        db=db,
        cursorclass=pymysql.cursors.DictCursor
    )
    
    sp.call('clear', shell=True)
    print_banner()

    if con.open:
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Connected to database!" + Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Failed to connect to database." + Style.RESET_ALL)
        exit()

    input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Press ENTER to continue..." + Style.RESET_ALL)

    with con.cursor() as cur:
        # Loop for user interaction
        while True:
            sp.call('clear', shell=True)
            print_banner()
            print_menu()
            ch = int(input(Fore.LIGHTCYAN_EX+ Style.BRIGHT + "Enter your choice: " + Style.RESET_ALL))
            sp.call('clear', shell=True)

            if ch == 14:
                print(Fore.LIGHTRED_EX+ Style.BRIGHT + "Goodbye!" + Style.RESET_ALL)
                break  # Exit the loop
            else:
                try:
                    dispatch(ch)
                except Exception as e:
                    print(Fore.LIGHTRED_EX+ Style.BRIGHT + "Error during operation: " + Style.RESET_ALL + str(e))
                input(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "Press ENTER to continue..." + Style.RESET_ALL)

except Exception as e:
    sp.call('clear', shell=True)
    print(Fore.LIGHTRED_EX+ Style.BRIGHT + "Failed to connect to the database: " + Style.RESET_ALL + str(e))

finally:
    if 'con' in locals() and con.open:
        con.close()
        print(Fore.LIGHTCYAN_EX+ Style.BRIGHT + "Database connection closed." + Style.RESET_ALL)
