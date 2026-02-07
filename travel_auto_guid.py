import random
from itertools import permutations
import random
import time
import folium
from folium.plugins import MarkerCluster
import math


# 확장된 유럽 여행지 데이터 (관광지 5배, 음식점 3배 증가)
travel_data = {
        "Paris": [
            {"name": "Eiffel Tower", "open": 9, "close": 23, "duration": 2, "move_time": 0, "latitude": 48.8584, "longitude": 2.2945},
            {"name": "Louvre Museum", "open": 9, "close": 18, "duration": 3, "move_time": 15, "latitude": 48.8606, "longitude": 2.3376},
            {"name": "Seine River Cruise", "open": 10, "close": 22, "duration": 1.5, "move_time": 20, "latitude": 48.8566, "longitude": 2.3522},
            {"name": "Montmartre", "open": 8, "close": 22, "duration": 2, "move_time": 25, "latitude": 48.8867, "longitude": 2.3431},
            {"name": "Champs-Élysées", "open": 10, "close": 22, "duration": 1, "move_time": 10, "latitude": 48.8696, "longitude": 2.3079},
            {"name": "Notre Dame", "open": 9, "close": 18, "duration": 1.5, "move_time": 15, "latitude": 48.8529, "longitude": 2.3500},
            {"name": "Luxembourg Gardens", "open": 7, "close": 20, "duration": 1, "move_time": 30, "latitude": 48.8462, "longitude": 2.3372},
            {"name": "Orsay Museum", "open": 9, "close": 18, "duration": 2.5, "move_time": 20, "latitude": 48.8600, "longitude": 2.3266},
            {"name": "Montparnasse Tower", "open": 9, "close": 23, "duration": 1.5, "move_time": 10, "latitude": 48.8428, "longitude": 2.3201},
            {"name": "The Pantheon", "open": 10, "close": 18, "duration": 2, "move_time": 15, "latitude": 48.8462, "longitude": 2.3460},
            {"name": "Le Marais District", "open": 9, "close": 22, "duration": 2, "move_time": 15, "latitude": 48.8584, "longitude": 2.3571},
            {"name": "Versailles Palace", "open": 9, "close": 18, "duration": 4, "move_time": 45, "latitude": 48.8049, "longitude": 2.1204},
            {"name": "Arc de Triomphe", "open": 9, "close": 23, "duration": 1.5, "move_time": 10, "latitude": 48.8738, "longitude": 2.2950},
            {"name": "Place de la Concorde", "open": 9, "close": 22, "duration": 1, "move_time": 10, "latitude": 48.8656, "longitude": 2.3212},
            {"name": "Petit Palais", "open": 10, "close": 18, "duration": 2, "move_time": 15, "latitude": 48.8695, "longitude": 2.3128},
            {"name": "Pantheon de Paris", "open": 9, "close": 18, "duration": 1.5, "move_time": 20, "latitude": 48.8462, "longitude": 2.3460},
            {"name": "Musee de l'Orangerie", "open": 9, "close": 18, "duration": 2, "move_time": 15, "latitude": 48.8639, "longitude": 2.3215},
            {"name": "Sacré-Cœur Basilica", "open": 6, "close": 22, "duration": 2, "move_time": 30, "latitude": 48.8867, "longitude": 2.3431},
            {"name": "Cité des Sciences", "open": 9, "close": 18, "duration": 2.5, "move_time": 30, "latitude": 48.8971, "longitude": 2.3960},
            {"name": "Le Louvre Pyramid", "open": 9, "close": 20, "duration": 1, "move_time": 15, "latitude": 48.8606, "longitude": 2.3376},
            {"name": "Tuileries Garden", "open": 7, "close": 20, "duration": 1, "move_time": 15, "latitude": 48.8645, "longitude": 2.3272}
        ],
        "London": [
            {"name": "Big Ben", "open": 0, "close": 24, "duration": 1, "move_time": 0, "latitude": 51.5007, "longitude": -0.1246},
            {"name": "Buckingham Palace", "open": 10, "close": 17, "duration": 2, "move_time": 15, "latitude": 51.5014, "longitude": -0.1419},
            {"name": "Tower Bridge", "open": 9, "close": 17, "duration": 1.5, "move_time": 20, "latitude": 51.5055, "longitude": -0.0754},
            {"name": "British Museum", "open": 10, "close": 17, "duration": 3, "move_time": 25, "latitude": 51.5194, "longitude": -0.1270},
            {"name": "Hyde Park", "open": 0, "close": 24, "duration": 1, "move_time": 10, "latitude": 51.5074, "longitude": -0.1657},
            {"name": "Camden Market", "open": 9, "close": 18, "duration": 2, "move_time": 15, "latitude": 51.5415, "longitude": -0.1447},
            {"name": "London Eye", "open": 10, "close": 22, "duration": 1.5, "move_time": 10, "latitude": 51.5033, "longitude": -0.1195},
            {"name": "Trafalgar Square", "open": 0, "close": 24, "duration": 1, "move_time": 10, "latitude": 51.5074, "longitude": -0.1278},
            {"name": "St. Paul's Cathedral", "open": 9, "close": 19, "duration": 2, "move_time": 15, "latitude": 51.5138, "longitude": -0.0984},
            {"name": "Shakespeare's Globe Theatre", "open": 9, "close": 23, "duration": 2, "move_time": 20, "latitude": 51.5080, "longitude": -0.0964},
            {"name": "Westminster Abbey", "open": 9, "close": 18, "duration": 2, "move_time": 10, "latitude": 51.4993, "longitude": -0.1273},
            {"name": "Natural History Museum", "open": 10, "close": 18, "duration": 2.5, "move_time": 20, "latitude": 51.4967, "longitude": -0.1764},
            {"name": "Victoria and Albert Museum", "open": 10, "close": 17, "duration": 3, "move_time": 25, "latitude": 51.4966, "longitude": -0.1724},
            {"name": "Kensington Gardens", "open": 7, "close": 20, "duration": 2, "move_time": 15, "latitude": 51.5074, "longitude": -0.1807},
            {"name": "Covent Garden", "open": 9, "close": 22, "duration": 2, "move_time": 10, "latitude": 51.5128, "longitude": -0.1238},
            {"name": "Hyde Park Corner", "open": 10, "close": 22, "duration": 1.5, "move_time": 15, "latitude": 51.5049, "longitude": -0.1456},
            {"name": "The Shard", "open": 10, "close": 23, "duration": 1.5, "move_time": 20, "latitude": 51.5045, "longitude": -0.0859},
            {"name": "Regent's Park", "open": 9, "close": 20, "duration": 1.5, "move_time": 10, "latitude": 51.5310, "longitude": -0.1470},
            {"name": "Notting Hill", "open": 0, "close": 24, "duration": 1, "move_time": 15, "latitude": 51.5093, "longitude": -0.2026}
        ],
        "Berlin": [
            {"name": "Brandenburg Gate", "open": 0, "close": 24, "duration": 1, "move_time": 0, "latitude": 52.5163, "longitude": 13.3777},
            {"name": "Museum Island", "open": 10, "close": 18, "duration": 3, "move_time": 15, "latitude": 52.5160, "longitude": 13.4010},
            {"name": "East Side Gallery", "open": 0, "close": 24, "duration": 2, "move_time": 20, "latitude": 52.5033, "longitude": 13.4390},
            {"name": "Berlin Wall Memorial", "open": 9, "close": 19, "duration": 1.5, "move_time": 15, "latitude": 52.5371, "longitude": 13.3902},
            {"name": "Checkpoint Charlie", "open": 9, "close": 18, "duration": 1, "move_time": 10, "latitude": 52.5076, "longitude": 13.3904},
            {"name": "Pergamon Museum", "open": 10, "close": 18, "duration": 3, "move_time": 20, "latitude": 52.5170, "longitude": 13.3960},
            {"name": "Charlottenburg Palace", "open": 9, "close": 18, "duration": 2, "move_time": 30, "latitude": 52.5200, "longitude": 13.2955},
            {"name": "Alexanderplatz", "open": 0, "close": 24, "duration": 1.5, "move_time": 10, "latitude": 52.5219, "longitude": 13.4132},
            {"name": "Berlin Cathedral", "open": 9, "close": 18, "duration": 2, "move_time": 15, "latitude": 52.5194, "longitude": 13.4010},
            {"name": "Gendarmenmarkt", "open": 9, "close": 22, "duration": 1, "move_time": 10, "latitude": 52.5136, "longitude": 13.3929},
            {"name": "Berlin Zoo", "open": 9, "close": 19, "duration": 2.5, "move_time": 20, "latitude": 52.5081, "longitude": 13.3374},
            {"name": "Holocaust Memorial", "open": 0, "close": 24, "duration": 1, "move_time": 15, "latitude": 52.5145, "longitude": 13.3792},
            {"name": "Victory Column", "open": 9, "close": 22, "duration": 1.5, "move_time": 15, "latitude": 52.5140, "longitude": 13.3500},
            {"name": "Bebelplatz", "open": 9, "close": 22, "duration": 1, "move_time": 10, "latitude": 52.5143, "longitude": 13.3931},
            {"name": "Kaiser Wilhelm Memorial Church", "open": 9, "close": 18, "duration": 1.5, "move_time": 15, "latitude": 52.5046, "longitude": 13.3312},
            {"name": "Berlin Philharmonic", "open": 9, "close": 18, "duration": 2, "move_time": 10, "latitude": 52.5076, "longitude": 13.3801},
            {"name": "Berlin TV Tower", "open": 9, "close": 23, "duration": 1.5, "move_time": 20, "latitude": 52.5208, "longitude": 13.4095},
            {"name": "Kreuzberg", "open": 0, "close": 24, "duration": 1, "move_time": 15, "latitude": 52.4991, "longitude": 13.3900}
        ]

    }

# 음식점 데이터 (도시별로 나누어 추가)
restaurants_data = {
        "Paris": [
            {"name": "Le Cinq", "latitude": 48.8667, "longitude": 2.3065, "open": 12, "close": 23, "duration": 2, "move_time": 0},
            {"name": "Le Jules Verne", "latitude": 48.8584, "longitude": 2.2945, "open": 12, "close": 23, "duration": 2, "move_time": 10},
            {"name": "L'Arpège", "latitude": 48.8535, "longitude": 2.3136, "open": 12, "close": 23, "duration": 2, "move_time": 15},
            {"name": "Chez L'Ami Jean", "latitude": 48.8592, "longitude": 2.3095, "open": 12, "close": 23, "duration": 2, "move_time": 20},
            {"name": "Le Meurice Alain Ducasse", "latitude": 48.8666, "longitude": 2.3219, "open": 12, "close": 23, "duration": 2, "move_time": 25},
            {"name": "L'Atelier de Joël Robuchon", "latitude": 48.8662, "longitude": 2.3223, "open": 12, "close": 23, "duration": 2, "move_time": 30},
            {"name": "Pierre Gagnaire", "latitude": 48.8707, "longitude": 2.3086, "open": 12, "close": 23, "duration": 2, "move_time": 20},
            {"name": "Le Bernardin", "latitude": 48.8587, "longitude": 2.3120, "open": 12, "close": 23, "duration": 2, "move_time": 15},
            {"name": "Le Procope", "latitude": 48.8527, "longitude": 2.3405, "open": 12, "close": 23, "duration": 2, "move_time": 10},
            {"name": "Bistrot Paul Bert", "latitude": 48.8507, "longitude": 2.3063, "open": 12, "close": 23, "duration": 2, "move_time": 10},
            {"name": "L'Epicure", "latitude": 48.8703, "longitude": 2.3119, "open": 12, "close": 23, "duration": 2, "move_time": 15},
            {"name": "L'Ambroisie", "latitude": 48.8561, "longitude": 2.3615, "open": 12, "close": 23, "duration": 2, "move_time": 20},
            {"name": "Café de Flore", "latitude": 48.8551, "longitude": 2.3321, "open": 7, "close": 23, "duration": 1.5, "move_time": 15},
            {"name": "Le Relais de l'Entrecôte", "latitude": 48.8675, "longitude": 2.3223, "open": 12, "close": 23, "duration": 1.5, "move_time": 10},
            {"name": "Le Comptoir du Relais", "latitude": 48.8525, "longitude": 2.3321, "open": 12, "close": 23, "duration": 1.5, "move_time": 20},
            {"name": "L'As du Fallafel", "latitude": 48.8596, "longitude": 2.3733, "open": 10, "close": 22, "duration": 1.5, "move_time": 10}
        ],
        "London": [
            {"name": "The Ledbury", "latitude": 51.5182, "longitude": -0.1974, "open": 12, "close": 23, "duration": 2, "move_time": 0},
            {"name": "Sketch", "latitude": 51.3938, "longitude": -0.1922, "open": 12, "close": 23, "duration": 2, "move_time": 10},
            {"name": "The Ritz Restaurant", "latitude": 51.5072, "longitude": -0.1423, "open": 12, "close": 23, "duration": 2, "move_time": 15},
            {"name": "Barrafina", "latitude": 51.5100, "longitude": -0.1273, "open": 12, "close": 23, "duration": 1.5, "move_time": 10},
            {"name": "Dishoom", "latitude": 51.5177, "longitude": -0.1323, "open": 12, "close": 23, "duration": 2, "move_time": 20},
            {"name": "The Ivy", "latitude": 51.5133, "longitude": -0.1395, "open": 12, "close": 23, "duration": 2, "move_time": 15},
            {"name": "Duck & Waffle", "latitude": 51.5075, "longitude": -0.0755, "open": 12, "close": 23, "duration": 2, "move_time": 30},
            {"name": "Hakkasan", "latitude": 51.5670, "longitude": -0.1405, "open": 12, "close": 23, "duration": 2, "move_time": 20},
            {"name": "Nopi", "latitude": 51.5137, "longitude": -0.1344, "open": 12, "close": 23, "duration": 2, "move_time": 15},
            {"name": "Le Gavroche", "latitude": 51.5136, "longitude": -0.1244, "open": 12, "close": 23, "duration": 2, "move_time": 10}
        ],
        "Berlin": [
            {"name": "Nobelhart & Schmutzig", "latitude": 52.5087, "longitude": 13.4069, "open": 12, "close": 23, "duration": 2, "move_time": 0},
            {"name": "Sauvage", "latitude": 52.5177, "longitude": 13.4131, "open": 12, "close": 23, "duration": 2, "move_time": 10},
            {"name": "Café Einstein Stammhaus", "latitude": 52.5079, "longitude": 13.3106, "open": 7, "close": 23, "duration": 1.5, "move_time": 15},
            {"name": "Rutz", "latitude": 52.5086, "longitude": 13.3733, "open": 12, "close": 23, "duration": 2, "move_time": 15},
            {"name": "Fischers Fritz", "latitude": 52.5076, "longitude": 13.3964, "open": 12, "close": 23, "duration": 2, "move_time": 20},
            {"name": "Tim Raue", "latitude": 52.5072, "longitude": 13.3990, "open": 12, "close": 23, "duration": 2, "move_time": 20},
            {"name": "Katz Orange", "latitude": 52.5071, "longitude": 13.4074, "open": 12, "close": 23, "duration": 2, "move_time": 30},
            {"name": "Hugos", "latitude": 52.5167, "longitude": 13.3785, "open": 12, "close": 23, "duration": 2, "move_time": 10},
            {"name": "Neni", "latitude": 52.5180, "longitude": 13.4076, "open": 12, "close": 23, "duration": 1.5, "move_time": 20},
            {"name": "Zenkichi", "latitude": 52.5148, "longitude": 13.3842, "open": 12, "close": 23, "duration": 1.5, "move_time": 15}
        ]
    }


# 호텔 데이터 (도시별로 나누어 추가)
hotels_data = {
        "Paris": [
            {"name": "Le Meurice", "latitude": 48.8666, "longitude": 2.3219, "open": 0, "close": 24, "duration": 1, "move_time": 0},
            {"name": "The Ritz Paris", "latitude": 48.8674, "longitude": 2.3140, "open": 0, "close": 24, "duration": 1, "move_time": 5},
            {"name": "Hotel de Crillon", "latitude": 48.8691, "longitude": 2.3194, "open": 0, "close": 24, "duration": 1, "move_time": 10},
            {"name": "Four Seasons Hotel George V", "latitude": 48.8682, "longitude": 2.3005, "open": 0, "close": 24, "duration": 1, "move_time": 10},
            {"name": "Shangri-La Hotel Paris", "latitude": 48.8643, "longitude": 2.2982, "open": 0, "close": 24, "duration": 1, "move_time": 15},
            {"name": "Mandarin Oriental Paris", "latitude": 48.8689, "longitude": 2.3264, "open": 0, "close": 24, "duration": 1, "move_time": 15},
            {"name": "Le Royal Monceau", "latitude": 48.8843, "longitude": 2.3054, "open": 0, "close": 24, "duration": 1, "move_time": 20},
            {"name": "Hotel Plaza Athénée", "latitude": 48.8697, "longitude": 2.3049, "open": 0, "close": 24, "duration": 1, "move_time": 20},
            {"name": "Hotel du Louvre", "latitude": 48.8654, "longitude": 2.3319, "open": 0, "close": 24, "duration": 1, "move_time": 25},
            {"name": "Le Bristol Paris", "latitude": 48.8705, "longitude": 2.3115, "open": 0, "close": 24, "duration": 1, "move_time": 30},
            {"name": "La Réserve Paris", "latitude": 48.8664, "longitude": 2.2891, "open": 0, "close": 24, "duration": 1, "move_time": 30},
            {"name": "Hotel de la Paix", "latitude": 48.8670, "longitude": 2.3311, "open": 0, "close": 24, "duration": 1, "move_time": 20},
            {"name": "The Peninsula Paris", "latitude": 48.8671, "longitude": 2.3005, "open": 0, "close": 24, "duration": 1, "move_time": 15},
            {"name": "Hôtel Particulier Montmartre", "latitude": 48.8860, "longitude": 2.3311, "open": 0, "close": 24, "duration": 1, "move_time": 25},
            {"name": "Hotel Le Meurice", "latitude": 48.8666, "longitude": 2.3219, "open": 0, "close": 24, "duration": 1, "move_time": 20},
            {"name": "Hotel des Arts", "latitude": 48.8867, "longitude": 2.3382, "open": 0, "close": 24, "duration": 1, "move_time": 30},
            {"name": "InterContinental Paris", "latitude": 48.8738, "longitude": 2.3298, "open": 0, "close": 24, "duration": 1, "move_time": 10},
            {"name": "Hôtel d'Aubusson", "latitude": 48.8559, "longitude": 2.3381, "open": 0, "close": 24, "duration": 1, "move_time": 15},
            {"name": "Hotel Regina Louvre", "latitude": 48.8607, "longitude": 2.3317, "open": 0, "close": 24, "duration": 1, "move_time": 20},
            {"name": "Hôtel de la Porte Dorée", "latitude": 48.8415, "longitude": 2.4155, "open": 0, "close": 24, "duration": 1, "move_time": 15}

        ],
    "London": [
            {"name": "The Ritz London", "latitude": 51.5074, "longitude": -0.1419, "open": 0, "close": 24, "duration": 1, "move_time": 0},
            {"name": "Claridge's", "latitude": 51.5135, "longitude": -0.1450, "open": 0, "close": 24, "duration": 1, "move_time": 10},
            {"name": "The Langham", "latitude": 51.5171, "longitude": -0.1445, "open": 0, "close": 24, "duration": 1, "move_time": 15},
            {"name": "The Savoy", "latitude": 51.5074, "longitude": -0.1196, "open": 0, "close": 24, "duration": 1, "move_time": 5},
            {"name": "Mandarin Oriental Hyde Park", "latitude": 51.5047, "longitude": -0.1611, "open": 0, "close": 24, "duration": 1, "move_time": 15},
            {"name": "Four Seasons Hotel London", "latitude": 51.5070, "longitude": -0.1445, "open": 0, "close": 24, "duration": 1, "move_time": 10},
            {"name": "The Dorchester", "latitude": 51.5074, "longitude": -0.1504, "open": 0, "close": 24, "duration": 1, "move_time": 20},
            {"name": "The Connaught", "latitude": 51.5132, "longitude": -0.1454, "open": 0, "close": 24, "duration": 1, "move_time": 10},
            {"name": "St. Pancras Renaissance Hotel", "latitude": 51.5302, "longitude": -0.1260, "open": 0, "close": 24, "duration": 1, "move_time": 20},
            {"name": "Bulgari Hotel London", "latitude": 51.5060, "longitude": -0.1472, "open": 0, "close": 24, "duration": 1, "move_time": 10}
        ],
        "Berlin": [
            {"name": "Hotel Adlon Kempinski", "latitude": 52.5100, "longitude": 13.3783, "open": 0, "close": 24, "duration": 1, "move_time": 0},
            {"name": "The Ritz-Carlton, Berlin", "latitude": 52.5051, "longitude": 13.3794, "open": 0, "close": 24, "duration": 1, "move_time": 10},
            {"name": "Mandala Hotel", "latitude": 52.5058, "longitude": 13.3896, "open": 0, "close": 24, "duration": 1, "move_time": 15},
            {"name": "Waldorf Astoria Berlin", "latitude": 52.5075, "longitude": 13.2981, "open": 0, "close": 24, "duration": 1, "move_time": 5},
            {"name": "Hotel Zoo Berlin", "latitude": 52.5056, "longitude": 13.3209, "open": 0, "close": 24, "duration": 1, "move_time": 10},
            {"name": "Regent Berlin", "latitude": 52.5145, "longitude": 13.3963, "open": 0, "close": 24, "duration": 1, "move_time": 15},
            {"name": "Hotel Bristol Berlin", "latitude": 52.5074, "longitude": 13.3273, "open": 0, "close": 24, "duration": 1, "move_time": 20},
            {"name": "Berlin Marriott Hotel", "latitude": 52.5077, "longitude": 13.3833, "open": 0, "close": 24, "duration": 1, "move_time": 10},
            {"name": "InterContinental Berlin", "latitude": 52.5096, "longitude": 13.2939, "open": 0, "close": 24, "duration": 1, "move_time": 20},
            {"name": "Swissôtel Berlin", "latitude": 52.5055, "longitude": 13.3199, "open": 0, "close": 24, "duration": 1, "move_time": 15}
        ]
    }

import math
from itertools import permutations


# 총 이동 시간 및 방문 시간을 계산하는 함수
def calculate_total_travel_time(route, locations, speed):
    total_time = 0

    if len(route) == 0:  # 빈 경로가 전달되었을 경우 예외 처리
        return total_time

    for i in range(len(route) - 1):
        spot1 = locations[route[i]]
        spot2 = locations[route[i + 1]]

        # Haversine 공식을 사용하여 거리 계산
        distance = haversine(spot1['latitude'], spot1['longitude'], spot2['latitude'], spot2['longitude'])
        move_time = distance / speed  # 이동 속도를 반영한 시간 (시간 단위)

        total_time += spot1['duration'] + move_time  # 장소 방문 시간 + 이동 시간

    # 마지막 장소의 소요 시간을 더함
    total_time += locations[route[-1]]['duration']
    
    return total_time


# 두 지점 간 거리 계산 (Haversine 공식 사용)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # 지구 반지름 (km)
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi, delta_lambda = math.radians(lat2 - lat1), math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c  # 거리 (km)

from multiprocessing import Pool

# 최적 경로 계산 (병렬 처리)
def calculate_route_time(route, tourist_spots, speed):
    return calculate_total_travel_time(route, tourist_spots, speed)

def optimize_route(tourist_spots, speed):
    if len(tourist_spots) < 2:
        return tourist_spots

    all_permutations = list(permutations(range(len(tourist_spots))))
    with Pool() as pool:
        # 각 순열에 대해 총 이동 시간을 병렬로 계산
        results = pool.starmap(
            calculate_route_time,
            [(perm, tourist_spots, speed) for perm in all_permutations]
        )

    # 최적 경로 선택
    min_time = min(results)
    best_route_index = results.index(min_time)
    best_route = all_permutations[best_route_index]

    return [tourist_spots[i] for i in best_route]

# 도시 선택 함수 (남은 관광지 및 음식점 개수 반영)
def select_city_for_day(day_number, selected_tourist_spots, selected_restaurants):
    cities = ["Paris", "London", "Berlin"]
    print(f"\n📌 Day {day_number}: 방문할 도시를 선택하세요.")

    for i, city in enumerate(cities, 1):
        remaining_tourist_spots = len(travel_data[city]) - len(selected_tourist_spots.get(city, set()))
        remaining_restaurants = len(restaurants_data[city]) - len(selected_restaurants.get(city, set()))

        print(f"{i}. {city} (남은 관광지: {remaining_tourist_spots}개, 남은 음식점: {remaining_restaurants}개)")

    return cities[int(input("도시 번호를 선택하세요: ")) - 1]

# 하루 일정 생성
def generate_itinerary_for_day(city, num_tourist_spots, num_restaurants, speed, selected_tourist_spots, selected_restaurants):
    selected_tourist_spots.setdefault(city, set())
    selected_restaurants.setdefault(city, set())

    available_tourist_spots = [spot for spot in travel_data[city] if spot['name'] not in selected_tourist_spots[city]]
    available_restaurants = [restaurant for restaurant in restaurants_data[city] if restaurant['name'] not in selected_restaurants[city]]

    num_tourist_spots = min(num_tourist_spots, len(available_tourist_spots))
    num_restaurants = min(num_restaurants, len(available_restaurants))

    optimized_tourist_spots = optimize_route(available_tourist_spots[:num_tourist_spots], speed)

    selected_tourist_spots[city].update(spot['name'] for spot in optimized_tourist_spots)
    selected_restaurants[city].update(restaurant['name'] for restaurant in available_restaurants[:num_restaurants])

    remaining_tourist_spots = len(travel_data[city]) - len(selected_tourist_spots[city])
    remaining_restaurants = len(restaurants_data[city]) - len(selected_restaurants[city])

    print(f"✅ {city} 남은 관광지 개수: {remaining_tourist_spots}, 남은 음식점 개수: {remaining_restaurants}")

    return {
        "city": city,
        "tourist_spots": optimized_tourist_spots,
        "restaurants": available_restaurants[:num_restaurants]
    }

# 전체 일정 생성
def generate_itinerary():
    itinerary = []
    selected_tourist_spots, selected_restaurants = {}, {}

    for day in range(1, 4):
        city = select_city_for_day(day, selected_tourist_spots, selected_restaurants)

        remaining_tourist_spots = len(travel_data[city]) - len(selected_tourist_spots.get(city, set()))
        remaining_restaurants = len(restaurants_data[city]) - len(selected_restaurants.get(city, set()))

        num_tourist_spots = int(input(f"{city}에서 방문할 관광지 개수 (최대 {remaining_tourist_spots}개): "))
        num_restaurants = int(input(f"{city}에서 방문할 음식점 개수 (최대 {remaining_restaurants}개): "))

        speed = float(input("이동 속도 (km/h)를 입력하세요: "))

        day_plan = generate_itinerary_for_day(city, num_tourist_spots, num_restaurants, speed, selected_tourist_spots, selected_restaurants)
        itinerary.append(day_plan)

    return itinerary

# 일정 출력
def display_time_slots(day_plan, start_hour=9):
    current_time = start_hour
    print(f"\n📅 {day_plan['city']} 일정 (시작 시간: {start_hour}:00)")

    for spot in day_plan['tourist_spots']:
        visit_start_time, visit_end_time = current_time, current_time + spot['duration']
        print(f"  🏛 관광지: {spot['name']} ({visit_start_time}:00 - {visit_end_time}:00)")
        current_time = visit_end_time

    total_tourist_time = sum(spot['duration'] for spot in day_plan['tourist_spots'])
    total_restaurant_time = sum(restaurant['duration'] for restaurant in day_plan['restaurants'])
    meal_interval = (total_tourist_time + total_restaurant_time) // (len(day_plan['restaurants']) + 1) if day_plan['restaurants'] else 0

    for restaurant in day_plan['restaurants']:
        visit_start_time, visit_end_time = current_time, current_time + restaurant['duration']
        print(f"  🍽 음식점: {restaurant['name']} ({visit_start_time}:00 - {visit_end_time}:00)")
        current_time = visit_end_time + meal_interval

# 실행
itinerary = generate_itinerary()

# 일정 출력
for day_number, day_plan in enumerate(itinerary, 1):
    print(f"\n🗓 Day {day_number} ({day_plan['city']}):")
    display_time_slots(day_plan, 9)

# 두 지점 간 거리 계산 (Haversine 공식 사용)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # 지구 반지름 (km)
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi, delta_lambda = math.radians(lat2 - lat1), math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c  # 거리 (km)

# 위치 데이터와 관련된 정보
def create_map_for_day(day_plan, city_coordinates):
    # 기본 지도 설정 (도시 중심으로 설정)
    city_map = folium.Map(location=city_coordinates, zoom_start=12)

    # 마커 클러스터를 추가하여 마커를 클러스터링
    marker_cluster = MarkerCluster().add_to(city_map)

    # 관광지 및 음식점의 위치와 시간을 마커로 추가
    all_places = []
    current_time = 9  # 하루 일정을 시작하는 시간 (예: 9시)

    # 관광지 마커 추가
    for i, spot in enumerate(day_plan['tourist_spots']):
        lat, lon = spot['latitude'], spot['longitude']
        visit_end_time = current_time + spot['duration']
        folium.Marker(
            location=[lat, lon],
            popup=f"{i+1}. {spot['name']} ({current_time}:00 - {visit_end_time}:00)\n",
            icon=folium.Icon(color='blue')
        ).add_to(marker_cluster)
        all_places.append((lat, lon, f"{i+1}. {spot['name']}"))  # 순서 추가
        current_time = visit_end_time

    # 음식점 마커 추가
    for i, restaurant in enumerate(day_plan['restaurants']):
        lat, lon = restaurant['latitude'], restaurant['longitude']
        visit_end_time = current_time + restaurant['duration']
        folium.Marker(
            location=[lat, lon],
            popup=f"{len(day_plan['tourist_spots']) + i + 1}. {restaurant['name']} ({current_time}:00 - {visit_end_time}:00)\n",
            icon=folium.Icon(color='green')
        ).add_to(marker_cluster)
        all_places.append((lat, lon, f"{len(day_plan['tourist_spots']) + i + 1}. {restaurant['name']}"))  # 순서 추가
        current_time = visit_end_time

    # 모든 장소를 이어주는 경로 추가 (관광지와 음식점 간의 경로도 연결)
    for i in range(len(all_places) - 1):
        lat1, lon1, name1 = all_places[i]
        lat2, lon2, name2 = all_places[i + 1]
        distance = haversine(lat1, lon1, lat2, lon2)
        
        folium.PolyLine(
            locations=[(lat1, lon1), (lat2, lon2)],
            color='red', weight=2.5, opacity=1
        ).add_to(city_map)

        # 경로의 거리 표시
        midpoint_lat = (lat1 + lat2) / 2
        midpoint_lon = (lon1 + lon2) / 2
        folium.Marker(
            location=[midpoint_lat, midpoint_lon],
            popup=f"거리: {distance:.2f} km",
            icon=folium.Icon(color='orange', icon='info-sign')
        ).add_to(city_map)

    # 지도 반환
    return city_map

# 각 도시의 첫 번째 관광지 좌표를 기준으로 중심 좌표 정의
def get_city_coordinates(city, travel_data):
    if city in travel_data and len(travel_data[city]) > 0:
        first_spot = travel_data[city][0]  # 첫 번째 관광지
        return first_spot['latitude'], first_spot['longitude']
    else:
        return None, None  # 데이터가 없으면 None 반환

# 일차별로 각 도시 지도 생성
for day_number, day_plan in enumerate(itinerary, 1):
    city = day_plan['city']
    latitude, longitude = get_city_coordinates(city, travel_data)

    if latitude is not None and longitude is not None:
        city_coordinates = [latitude, longitude]
        city_map = create_map_for_day(day_plan, city_coordinates)
        
        # 지도 HTML 파일로 저장
        city_map.save(f"day_{day_number}_itinerary_map.html")
        print(f"\n🗺 Day {day_number} 지도 생성 완료: day_{day_number}_itinerary_map.html")
    else:
        print(f"{city}에 대한 관광지 정보가 부족합니다.")

