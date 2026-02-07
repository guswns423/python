# 데이터 구조를 확인하고 아래와 같이 변경합니다.
travel_data = {
    "Paris": {
        "tourist_spots": [
            {"name": "Eiffel Tower", "open": 9, "close": 23, "duration": 2, "move_time": 0},
            {"name": "Louvre Museum", "open": 9, "close": 18, "duration": 3, "move_time": 15}
        ],
        "restaurants": [
            {"name": "Le Meurice", "type": "French", "price": "Expensive", "rating": 5},
            {"name": "L'Avenue", "type": "French", "price": "Expensive", "rating": 4.5}
        ],
        "hotels": [
            {"name": "Shangri-La Paris", "rating": 5, "price": "Expensive"},
            {"name": "Le Meurice", "rating": 5, "price": "Expensive"}
        ]
    },
    "London": {
        "tourist_spots": [
            {"name": "Big Ben", "open": 9, "close": 20, "duration": 1, "move_time": 15},
            {"name": "Tower of London", "open": 9, "close": 18, "duration": 2, "move_time": 20}
        ],
        "restaurants": [
            {"name": "The Ledbury", "type": "British", "price": "Expensive", "rating": 5},
            {"name": "Sketch", "type": "Modern European", "price": "Expensive", "rating": 4.5}
        ],
        "hotels": [
            {"name": "The Ritz London", "rating": 5, "price": "Expensive"},
            {"name": "Claridge's", "rating": 5, "price": "Expensive"}
        ]
    },
    "Berlin": {
        "tourist_spots": [
            {"name": "Brandenburg Gate", "open": 9, "close": 21, "duration": 1, "move_time": 10},
            {"name": "Alexanderplatz", "open": 9, "close": 20, "duration": 2, "move_time": 15}
        ],
        "restaurants": [
            {"name": "Restaurant Tim Raue", "type": "Asian Fusion", "price": "Expensive", "rating": 5},
            {"name": "Neni Berlin", "type": "Mediterranean", "price": "Moderate", "rating": 4.5}
        ],
        "hotels": [
            {"name": "Hotel Adlon Kempinski", "rating": 5, "price": "Expensive"},
            {"name": "The Ritz-Carlton Berlin", "rating": 5, "price": "Expensive"}
        ]
    }
}

# 도시를 선택하는 함수
def select_city_for_day(day_number):
    cities = ["Paris", "London", "Berlin"]
    print(f"Day {day_number}: 선택할 도시를 고르세요.")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")
    
    city_choice = int(input("도시 번호를 선택하세요: ")) - 1
    return cities[city_choice]

# 관광지 및 음식점 개수 선택 후 동선 짜기
def select_places_for_city(city):
    # 도시별 관광지, 음식점 목록을 불러와서 개수만큼 선택
    print(f"\n{city}에서 방문할 장소들을 선택하세요.")
    
    # 관광지 선택
    print("\n관광지를 몇 개 선택할지 입력하세요:")
    num_tourist_spots = int(input(f"{city}의 관광지 개수: "))
    print("\n관광지 목록:")
    for i, spot in enumerate(travel_data[city]["tourist_spots"], 1):
        print(f"{i}. {spot['name']}")
    
    # 선택한 개수 만큼 관광지 선택
    tourist_spots_choice = []
    for _ in range(num_tourist_spots):
        choice = int(input(f"선택할 관광지 번호 (1 ~ {len(travel_data[city]['tourist_spots'])}): ")) - 1
        tourist_spots_choice.append(travel_data[city]["tourist_spots"][choice])
    
    # 음식점 선택
    print("\n음식점을 몇 개 선택할지 입력하세요:")
    num_restaurants = int(input(f"{city}의 음식점 개수: "))
    print("\n음식점 목록:")
    for i, restaurant in enumerate(travel_data[city]["restaurants"], 1):
        print(f"{i}. {restaurant['name']}")
    
    # 선택한 개수 만큼 음식점 선택
    restaurants_choice = []
    for _ in range(num_restaurants):
        choice = int(input(f"선택할 음식점 번호 (1 ~ {len(travel_data[city]['restaurants'])}): ")) - 1
        restaurants_choice.append(travel_data[city]["restaurants"][choice])
    
    return tourist_spots_choice, restaurants_choice

# 일정 생성 함수
def generate_itinerary():
    itinerary = []
    
    for day in range(1, 4):
        # 1. 각 일차에 방문할 도시 선택
        city = select_city_for_day(day)
        
        # 2. 해당 도시에서 관광지, 음식점 개수 선택
        tourist_spots, restaurants = select_places_for_city(city)
        
        # 3. 선택된 관광지, 음식점, 호텔을 바탕으로 일정 생성
        day_plan = {
            "city": city,
            "tourist_spots": tourist_spots,
            "restaurants": restaurants
        }
        itinerary.append(day_plan)
        
    return itinerary

# 일정 생성 함수 호출
itinerary = generate_itinerary()

# 결과 출력
for day_number, day_plan in enumerate(itinerary, 1):
    print(f"\nDay {day_number} ({day_plan['city']}):")
    print("관광지:")
    for spot in day_plan["tourist_spots"]:
        print(f"  - {spot['name']}")
    print("음식점:")
    for restaurant in day_plan["restaurants"]:
        print(f"  - {restaurant['name']}")
