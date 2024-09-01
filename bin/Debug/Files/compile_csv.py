import pandas as pd
import csv
from datetime import date
import os
import sys

cities_dictionary=  {
    "בית חירות": "Beit Herut",
    "חיפה": "Haifa",
    "קרית ים": "Kiryat Yam",
    "רמלה": "Ramla",
    "ירושלים": "Jerusalem",
    "כרמיאל": "Karmiel",
    "גבעתיים": "Giv'atayim",
    "חריש": "Harish",
    "ראשון לציון": "Rishon LeZion",
    "פתח תקווה": "Petah Tikva",
    "יבנה": "Yavne",
    "רחובות": "Rehovot",
    "מעלות תרשיחא": "Ma'alot-Tarshiha",
    "קריית חיים": "Kiryat Haim",
    "אבו סנאן": "Abu Snan",
    "כסרא סמיע": "Kisra-Sumei",
    "כפר יאסיף": "Kafr Yasif",
    "שעב": "Sha'ab",
    "שפרעם": "Shefa-Amr",
    "קריית שמונה": "Kiryat Shmona",
    "טבריה": "Tiberias",
    "ראש פינה": "Rosh Pina",
    "קצרין": "Katzrin",
    "מושב מגדל": "Moshav Migdal",
    "יבנאל": "Yavne'el",
    "כפר כנא": "Kafr Kanna",
    "כפר מנדא": "Kafr Manda",
    "מג'דל שמס": "Majdal Shams",
    "כפר מראר": "Kafr Mraar",
    "שלומי": "Shlomi",
    "מעיין ברוך": "Ma'ayan Baruch",
    "פקיעין חדשה": "Peki'in Hadasha",
    "סחנין": "Sakhnin",
    "בני יהודה": "Bnei Yehuda",
    "גוש חלב": "Gush Halav",
    "ירכא": "Yarka",
    "פוריה": "Poria",
    "מירון": "Meron",
    "עראבה": "Arraba",
    "יאנוח-ג'ת": "Yanuh-Jat",
    "דיר אל-אסד": "Deir al-Asad",
    "עפולה": "Afula Illit",
    "סולם": "Sulam",
    "עפולה עלית": "Afula Illit",
    "רמת ישי": "Ramat Yishai",
    "נשר": "Nesher",
    "רוויה": "Revaya",
    "נצרת עילית": "Nazareth Illit",
    "נוף הגליל": "Nof HaGalil (Upper Nazareth)",
    "יפיע": "Yafia",
    "ריינה": "Reina",
    "כדורי": "Kadouri",
    "כפר תבור": "Kfar Tavor",
    "כפר סבא": "Kfar Saba",
    "נתניה": "Netanya",
    "פרדסיה": "Pardesiya",
    "כפר יונה": "Kfar Yona",
    "תל מונד": "Tel Mond",
    "כוכב יאיר": "Kokhav Ya'ir",
    "צורן-קדימה": "Tzoran-Kadima",
    "טירה": "Tira",
    "יקנעם עילית": "Yokneam Illit",
    "זכרון יעקב": "Zikhron Ya'akov",
    "פורדיס": "Fureidis",
    "עיר הכרמל": "Ir HaCarmel",
    "עתלית": "Atlit",
    "עוספיה": "Isfiya",
    "חדרה": "Hadera",
    "גבעת אולגה": "Givat Olga",
    "כפר קרע": "Kafr Qara",
    "פרדס חנה-כרכור": "Pardes Hanna-Karkur",
    "דאלית אל כרמל": "Daliyat al-Karmel",
    "ביתן אהרן": "Beit Aharon",
    "אלפי מנשה": "Alfei Menashe",
    "בני ברק": "Bnei Brak",
    "אזור": "Azor",
    "חולון": "Holon",
    "הרצליה": "Herzliya",
    "רעננה": "Ra'anana",
    "הוד השרון": "Hod HaSharon",
    "ראש העין": "Rosh HaAyin",
    "קיבוץ עינת": "Kibbutz Einat",
    "אורנית": "Oranit",
    "כפר קאסם": "Kafr Qasim",
    "קריית אונו": "Kiryat Ono",
    "אור יהודה": "Or Yehuda",
    "שוהם": "Shoham",
    "מודיעין": "Modi'in",
    "מודיעין עילית": "Modi'in Illit",
    "אלעד": "El'ad",
    "פתח תקוה": "Petah Tikva",
    "סביון": "Savyon",
    "תל אביב": "Tel Aviv",
    "ראשל\"צ": "Rishon LeZion",
    "נס ציונה": "Nes Tziona",
    "קריית עקרון": "Kiryat Ekron",
    "באר יעקב": "Be'er Ya'akov",
    "מזכרת בתיה": "Mazkeret Batya",
    "לוד": "Lod",
    "באר שבע": "Be'er Sheva",
    "בית שמש": "Beit Shemesh",
    "גדרה": "Gedera",
    "קריית מלאכי": "Kiryat Malachi",
    "גבעת זאב": "Givat Ze'ev",
    "יפית": "Yafit",
    "שורש": "Shoresh",
    "צור הדסה": "Tzur Hadassah",
    "קריית גת": "Kiryat Gat",
    "אשקלון": "Ashkelon",
    "אשדוד": "Ashdod",
    "שדה עוזיהו": "Sde Uziyahu",
    "אילת": "Eilat",
    "יד מרדכי": "Yad Mordechai",
    "עומר": "Omer",
    "שגב שלום": "Segev Shalom",
    "גאולים": "Geulim",
    "מודיעין-מכבים-רעות": "Modi'in-Maccabim-Re'ut",
    "צריפין": "Tzrifin",
    "זמרת": "Zemeret",
    "צמח": "Tzemah",
    "עספיא": "Isfiya",
    "זרזיר": "Zarzir",
    "ראשלצ": "Rishon LeZion",
    "קדימה - צורן": "Kadima - Tzoran",
    "יהוד - מונסון": "Yehud - Monoson",
    "ביענה": "Bi'ina",
    "יוקנעם": "Yokneam",
    "ג'לג'וליה": "Jaljulia",
    "בני דרור": "Bnei Dror",
    "נחף": "Nahf",
    "בית העמק": "Beit HaEmek",
    "בנימינה": "Binyamina",
    "אכסאל": "Iksal",
    "ג'סר א-זרקא": "Jisr az-Zarqa",
    "עילבון": "Ilabon",
    "מסעדה": "Mas'ade",
    "מגאר": "Maghar",
    "קרית שמונה": "Kiryat Shmona",
    "טובא-זנגריה": "Tuba-Zangariyye",
    "עין תמר": "Ein Tamar",
    "הר ברכה": "Har Bracha",
    "פארק תעשיות הגליל": "Galilee Industrial Park",
    "תל אביב - יפו": "Tel Aviv - Jaffa",
    "תימורים": "Timorim",
    "קציר-חריש": "Katzir-Harish",
    "עין בוקק": "Ein Bokek",
    "אבן יהודה": "Even Yehuda",
    "זיתן": "Zitan",
    "קרני שומרון": "Karnei Shomron",
    "עין יהב": "Ein Yahav",
    "טוראן": "Turan",
    "מצפה רמון": "Mitzpe Ramon",
    "צור יצחק": "Tzur Yitzhak",
    "מושב ברק": "Moshav Barak",
    "מודיעין, מכבים-רעות": "Modi'in, Maccabim-Re'ut",
    "יסוד המעלה": "Yesod HaMa'ala",
    "ירוחם": "Yeruham",
    "באקה אל גרביה": "Baqa al-Gharbiyye",
    "עזר": "Ezer",
    "חבל מודיעין": "Hevel Modi'in",
    "נווה אילן": "Neve Ilan",
    "קרית ביאליק": "Kiryat Bialik",
    "תפח תקווה": "Petah Tikva",
    "גפן": "Gefen",
    "קדימה-צורן": "Kadima-Tzoran",
    "קרית מוצקין": "Kiryat Motzkin",
    "גבע בנימין": "Geva Binyamin",
    "קרית ענבים": "Kiryat Anavim",
    "אפרתה": "Efrata",
    "בית אריה": "Beit Aryeh",
    "כפר אדומים": "Kfar Adumim",
    "יגור": "Yagur",
    "שריד": "Sarid",
    "כמהין": "Kmehin",
    "אפרת": "Efrat",
    "אלומות": "Alumot",
    "שדה אילן": "Sde Ilan",
    "קרית עקרון": "Kiryat Ekron",
    "עין ורד": "Ein Vered",
    "ג'דיידה-מכר": "Jadeidi-Makr",
    "ביתן אהרון": "Bitan Aharon",
    "דימונה": "Dimona",
    "שדרות": "Sderot",
    "רהט": "Rahat",
    "אור עקיבא": "Or Akiva",
    "קרית אונו": "Kiryat Ono",
    "עכו":"Acre",
    "בית שאן": "Beit She'an",
    "נהרייה" : "Nahariya",
    "בת ים": "Bat Yam",
    "טירת הכרמל": "Tirat HaCarmel",
    "גני תקווה": "Ganei Tikva",
    "רמת גן": "Ramat Gan",
    "פרדס חנה כרכור": "Pardes Hanna-Karkur",
    "מגדל העמק": "Migdal HaEmek",
    "יקנעם": "Yokneam",
    "קריית ים": "Kiryat Yam",
    "קריית מוצקין": "Kiryat Motzkin",
    "קריית ביאליק": "Kiryat Bialik",
    "מעלות-תרשיחא": "Ma'alot-Tarshiha",
    "אעבלין": "Ibilin",
    "רמת השרון": "Ramat HaSharon",
    "אשדות יעקב": "Ashdot Ya'akov",
    "מבשרת ציון": "Mevaseret Zion",
    "כאבול": "Kabul",
    "קרית אתא": "Kiryat Ata",
}



ISP_dictionary = {
    "הוט": "HOT",
    "הוט מובייל": "HOT",
    "טריפל": "TRIPLE",
    "טריפל C": "TRIPLE",
    "סלקום": "TRIPLE",
    "פלאפון (טריפל C סלולר)": "TRIPLE"
}


reseller_dictionary = {
    "חיפה": "Haifa",
    "נגב": "Negev",
    "גליל": "Galil",
    "גוש דן": "Gush_dan",
    "שרון": "Sharon",
    "מרכז": "Merkaz",
    "ירושלים": "Jerusalem"
}


class CSVRow:
    def __init__(self, identifier, net_name, station_number, city, reseller, ISP, SHM, STM, SVHM, SVTM, deployDate):
        self.identifier = identifier
        self.net_name = net_name
        self.station_number = station_number
        self.city = city
        self.reseller = reseller
        self.ISP = ISP
        self.SHM = SHM
        self.STM = STM
        self.SVHM = SVHM
        self.SVTM = SVTM
        self.deployDate = deployDate
    
    def __str__(self):
        return f"{self.identifier},{self.net_name},{self.station_number},{self.city},{self.reseller},{self.ISP},{self.SHM},{self.STM},{self.SVHM},{self.SVTM},{self.deployDate}"

class PriorityData:
    def __init__(self, station_id_extended, ip_address, reseller, station_id, address, status, city, ISP, phone_num):
        self.station_id_extended = station_id_extended
        self.ip_address = ip_address
        self.reseller = reseller
        self.station_id = station_id
        self.address = address
        self.status = status
        self.city = city
        self.ISP = ISP
        self.phone_num = phone_num
    
    def __str__(self):
        return f"station_id_extended: {self.station_id_extended}, ip_address: {self.ip_address}, reseller: {self.reseller}, station_id: {self.station_id}, address: {self.address}, status: {self.status}, city: {self.city}, ISP: {self.ISP}, phone_num: {self.phone_num}"

# priority_data = pd.read_excel('Database_automations/priority.xlsx')
# hostname_data = pd.read_csv('Database_automations/hosts.csv', encoding='utf-8')
# stations = pd.read_csv('Database_automations/stations.csv', encoding='utf-8', header=0)
# extractor_data = pd.read_csv('Database_automations/playerData.csv')

def check_none(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg is None:
                print(f"Alert: Argument in function {func.__name__} is None: {arg}")
        for key, value in kwargs.items():
            if value is None:
                print(f"Alert: Keyword argument {key} in function {func.__name__} is None: {value}")
        return func(*args, **kwargs)
    return wrapper

@check_none
def get_all_players_of_station(station_number, hostname_data):
    players = []
    for index, row in hostname_data.iterrows():
        station = str(row['Host']).split("-")[0]
        if station == str(station_number):
            players.append(row['Host'])
    return players

@check_none
def get_data_of_player(machine_name , priority_data, extractor_data):
    shortend_name = machine_name.split("-")[0] + "-" + machine_name.split("-")[1]
    
    priority_player = priority_data.loc[priority_data['station_id_extended'].str.contains(shortend_name)]
    
    if priority_player.empty:
        print(f"No matching priority data found for machine name: {machine_name}")
        return None
    
    if priority_player['status'].values[0] != 'פעיל':
        print(f"Player {machine_name} is not active.")
        return None
    
    priority_data_obj = PriorityData(
        station_id_extended=priority_player['station_id_extended'].values[0],
        ip_address=priority_player['ip_address'].values[0],
        reseller=priority_player['reseller'].values[0],
        station_id=priority_player['station_id'].values[0],
        address=priority_player['address'].values[0],
        status=priority_player['status'].values[0],
        city=priority_player['city'].values[0],
        ISP=priority_player['ISP'].values[0],
        phone_num=priority_player['phone_num'].values[0]
    )
    
    extractor_player = extractor_data.loc[extractor_data['machineName'] == machine_name]
    
    if extractor_player.empty:
        print(f"No matching extractor data found for machine name: {machine_name}")
        return None
    
    return [priority_data_obj, extractor_player]

@check_none
def join_data(priority_data, extractor_data):
    if priority_data is None:
        print("Priority data is empty. Skipping this player.")
        return

    if extractor_data is None or extractor_data.empty:
        print("Extractor data is empty. Skipping this player.")
        return

    if 'prefix' not in extractor_data.columns or 'machineName' not in extractor_data.columns:
        print("Extractor data does not contain required columns. Skipping this player.")
        return

    try:
        fullIdentifier = str(extractor_data['prefix'].values[0]) + '-' + str(extractor_data['machineName'].values[0])
        net_name = str(extractor_data['machineName'].values[0])
        station_number = str(priority_data.station_id)
        city = str(priority_data.city)
        reseller = str(priority_data.reseller)
        ISP = str(priority_data.ISP)
        SHM = "false"
        STM = "false"
        SVHM = "false"
        SVTM = "false"
        today = date.today()
        deployDate = today.strftime("%d/%m/%Y")
        csv_row = CSVRow(fullIdentifier, net_name, station_number, city, reseller, ISP, SHM, STM, SVHM, SVTM, deployDate)
        return csv_row
    except AttributeError as e:
        print(f"AttributeError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")

def transalte_city(city_hebrew):
    return cities_dictionary[city_hebrew]
def translate_ISP(ISP_hebrew):
    return ISP_dictionary[ISP_hebrew]
def translate_reseller(reseller_hebrew):
    return reseller_dictionary[reseller_hebrew]

# def main():
#     for index, station in stations.iterrows():
#         print('-----------------------------------')
#         print(f"Station: {station['Station']}")
#         try:
#             players = get_all_players_of_station(station['Station'])
#             print(f"Players: {players}")
#             for index, player in enumerate(players):
#                 print(f"Player: {player}")
#                 data = get_data_of_player(player)
#                 if data is not None:
#                     row = join_data(data[0], data[1])
#                     if row is not None:
#                         csv_file = 'compiled_data.csv'
#                         if not os.path.exists(csv_file):
#                             with open(csv_file, 'w', newline='', encoding='UTF-8') as file:
#                                 writer = csv.writer(file)
#                                 writer.writerow(['identifier', 'net_name', 'station_number', 'city', 'reseller', 'ISP', 'SHM', 'STM', 'SVHM', 'SVTM', 'deployDate'])

#                         with open(csv_file, 'a', newline='', encoding='UTF-8') as file:
#                             writer = csv.writer(file)
#                             writer.writerow([row.identifier, row.net_name, row.station_number,transalte_city(row.city),translate_reseller(row.reseller),translate_ISP(row.ISP), row.SHM, row.STM, row.SVHM, row.SVTM, row.deployDate])
#         except Exception as e:
#             print("Error occurred while processing station.")
#             print(e)
#             continue


def main():
    if len(sys.argv) != 5:
        print("Usage: python script.py <playerdata_path> <stations_path> <priority_path> <hosts_path>")
        sys.exit(1)

    playerdata_path = sys.argv[1]
    stations_path = sys.argv[2]
    priority_path = sys.argv[3]
    hosts_path = sys.argv[4]

    # Load data from files
    priority_data = pd.read_excel(priority_path)
    hostname_data = pd.read_csv(hosts_path, encoding='utf-8')
    stations = pd.read_csv(stations_path, encoding='utf-8', header=0)
    extractor_data = pd.read_csv(playerdata_path)
    for index, station in stations.iterrows():
        print('-----------------------------------')
        print(f"Station: {station['Station']}")
        try:
            players = get_all_players_of_station(station['Station']  , hostname_data)
            print(f"Players: {players}")
            for index, player in enumerate(players):
                print(f"Player: {player}")
                data = get_data_of_player(player, priority_data , extractor_data)
                if data is not None:
                    row = join_data(data[0], data[1])
                    if row is not None:
                        csv_file = 'compiled_data.csv'
                        if not os.path.exists(csv_file):
                            with open(csv_file, 'w', newline='', encoding='UTF-8') as file:
                                writer = csv.writer(file)
                                writer.writerow(['identifier', 'net_name', 'station_number', 'city', 'reseller', 'ISP', 'SHM', 'STM', 'SVHM', 'SVTM', 'deployDate'])

                        with open(csv_file, 'a', newline='', encoding='UTF-8') as file:
                            writer = csv.writer(file)
                            writer.writerow([row.identifier, row.net_name, row.station_number,transalte_city(row.city),translate_reseller(row.reseller),translate_ISP(row.ISP), row.SHM, row.STM, row.SVHM, row.SVTM, row.deployDate])
        except Exception as e:
            print("Error occurred while processing station.")
            print(e)
            continue
if __name__ == "__main__":
    main()