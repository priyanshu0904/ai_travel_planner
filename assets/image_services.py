#images categorized based on the travel style
import random

IMAGE_CATEGORIES = {

    "Adventure": [
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
        "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",
        "https://images.unsplash.com/photo-1500534623283-312aade485b7",
        "https://images.unsplash.com/photo-1521335629791-ce4aec67ddaf",
        "https://images.unsplash.com/photo-1549880338-65ddcdfd017b",
        "https://images.unsplash.com/photo-1523978591478-c753949ff840",
        "https://images.unsplash.com/photo-1500534314210-4d42f84a0c5b",
        "https://images.unsplash.com/photo-1501785888041-af3ef285b470"
    ],

    "Nature": [
        "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        "https://images.unsplash.com/photo-1519681393784-d120267933ba",
        "https://images.unsplash.com/photo-1500534314210-4d42f84a0c5b",
        "https://images.unsplash.com/photo-1500534623283-312aade485b7",
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
        "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb"
    ],

    "Luxury Travel": [
        "https://images.unsplash.com/photo-1501117716987-c8e1ecb210f9",
        "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267",
        "https://images.unsplash.com/photo-1566073771259-6a8506099945",
        "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb",
        "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa",
        "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b",
        "https://images.unsplash.com/photo-1505691723518-36a5ac3b2a77",
        "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267"
    ],

    "Spiritual": [
        "https://images.unsplash.com/photo-1519985176271-adb1088fa94c",
        "https://images.unsplash.com/photo-1506784983877-45594efa4cbe",
        "https://images.unsplash.com/photo-1548013146-72479768bada",
        "https://images.unsplash.com/photo-1541417904950-b855846fe074",
        "https://images.unsplash.com/photo-1524492412937-b28074a5d7da",
        "https://images.unsplash.com/photo-1500534314210-4d42f84a0c5b",
        "https://images.unsplash.com/photo-1506784983877-45594efa4cbe",
        "https://images.unsplash.com/photo-1519985176271-adb1088fa94c"
    ],

    "Culture & Heritage": [
        "https://images.unsplash.com/photo-1524492412937-b28074a5d7da",
        "https://images.unsplash.com/photo-1558980394-0a3c37d6814b",
        "https://images.unsplash.com/photo-1526779259212-756e8b1e0f15",
        "https://images.unsplash.com/photo-1548013146-72479768bada",
        "https://images.unsplash.com/photo-1541417904950-b855846fe074",
        "https://images.unsplash.com/photo-1506784983877-45594efa4cbe",
        "https://images.unsplash.com/photo-1524492412937-b28074a5d7da",
        "https://images.unsplash.com/photo-1558980394-0a3c37d6814b"
    ],

    "Nightlife": [
        "https://images.unsplash.com/photo-1497032205916-ac775f0649ae",
        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4",
        "https://images.unsplash.com/photo-1504674900247-0877df9cc836",
        "https://images.unsplash.com/photo-1544145945-f90425340c7e",
        "https://images.unsplash.com/photo-1492724441997-5dc865305da7",
        "https://images.unsplash.com/photo-1532634896-26909d0d4b6a",
        "https://images.unsplash.com/photo-1481833761820-0509d3217039",
        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4"
    ],

    "Photography": [
        "https://images.unsplash.com/photo-1519681393784-d120267933ba",
        "https://images.unsplash.com/photo-1491553895911-0055eca6402d",
        "https://images.unsplash.com/photo-1511765224389-37f0e77cf0eb",
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
        "https://images.unsplash.com/photo-1500534314210-4d42f84a0c5b",
        "https://images.unsplash.com/photo-1506784983877-45594efa4cbe",
        "https://images.unsplash.com/photo-1519681393784-d120267933ba",
        "https://images.unsplash.com/photo-1491553895911-0055eca6402d"
    ]
}


def get_image(travel_style, count=3):
    images = IMAGE_CATEGORIES.get(travel_style, [])
    if not images:
        return []

    return random.sample(images, min(count, len(images)))
