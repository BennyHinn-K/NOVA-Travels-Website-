import reflex as rx
import asyncio
from typing import TypedDict


class Tour(TypedDict):
    id: int
    title: str
    price: str
    duration: str
    rating: float
    image: str
    category: str


class Testimonial(TypedDict):
    id: int
    name: str
    location: str
    rating: int
    text: str
    image: str


class Feature(TypedDict):
    title: str
    description: str
    icon: str


class HomeState(rx.State):
    featured_tours: list[Tour] = [
        {
            "id": 1,
            "title": "Beach Safari Experience",
            "price": "$150",
            "duration": "1 Day",
            "rating": 4.8,
            "image": "https://picsum.photos/seed/safari/800/600",
            "category": "Adventure",
        },
        {
            "id": 2,
            "title": "Diving Adventure",
            "price": "$120",
            "duration": "4 Hours",
            "rating": 4.9,
            "image": "https://picsum.photos/seed/diving/800/600",
            "category": "Water Sports",
        },
        {
            "id": 3,
            "title": "Old Town Cultural Walk",
            "price": "$45",
            "duration": "3 Hours",
            "rating": 4.7,
            "image": "https://picsum.photos/seed/oldtown/800/600",
            "category": "Culture",
        },
        {
            "id": 4,
            "title": "Sunset Dhow Cruise",
            "price": "$85",
            "duration": "2 Hours",
            "rating": 5.0,
            "image": "https://picsum.photos/seed/dhow/800/600",
            "category": "Relaxation",
        },
        {
            "id": 5,
            "title": "Haller Park Wildlife",
            "price": "$60",
            "duration": "Half Day",
            "rating": 4.6,
            "image": "https://picsum.photos/seed/haller/800/600",
            "category": "Wildlife",
        },
        {
            "id": 6,
            "title": "Swahili Food Tour",
            "price": "$55",
            "duration": "3 Hours",
            "rating": 4.9,
            "image": "https://picsum.photos/seed/food/800/600",
            "category": "Culinary",
        },
    ]
    features: list[Feature] = [
        {
            "title": "15+ Years Experience",
            "description": "Trusted by thousands of travelers for over a decade.",
            "icon": "award",
        },
        {
            "title": "Local Expertise",
            "description": "Guides born and raised in Mombasa who know every hidden gem.",
            "icon": "map-pin",
        },
        {
            "title": "Best Prices",
            "description": "Luxury experiences at competitive local rates.",
            "icon": "wallet",
        },
        {
            "title": "24/7 Support",
            "description": "We are here for you anytime, day or night.",
            "icon": "headset",
        },
    ]
    testimonials: list[Testimonial] = [
        {
            "id": 1,
            "name": "Sarah Johnson",
            "location": "United Kingdom",
            "rating": 5,
            "text": "The most magical experience of my life! The beach safari was perfectly organized and the guides were so knowledgeable.",
            "image": "https://picsum.photos/seed/sarah_j/200/200",
        },
        {
            "id": 2,
            "name": "Michael Chen",
            "location": "Singapore",
            "rating": 5,
            "text": "Incredible service from start to finish. The sunset cruise is a must-do. Highly recommended for anyone visiting Mombasa.",
            "image": "https://picsum.photos/seed/michael_c/200/200",
        },
        {
            "id": 3,
            "name": "Amara Okafor",
            "location": "Nigeria",
            "rating": 5,
            "text": "I felt so safe and welcomed. The cultural walk opened my eyes to the rich history of this beautiful city.",
            "image": "https://picsum.photos/seed/amara_o/200/200",
        },
    ]
    current_testimonial_index: int = 0
    auto_advance_running: bool = False

    @rx.event
    def set_testimonial_index(self, index: int):
        self.current_testimonial_index = index

    @rx.event(background=True)
    async def start_testimonial_carousel(self):
        if self.auto_advance_running:
            return
        async with self:
            self.auto_advance_running = True
        while True:
            await asyncio.sleep(5)
            async with self:
                next_index = (self.current_testimonial_index + 1) % len(
                    self.testimonials
                )
                self.current_testimonial_index = next_index