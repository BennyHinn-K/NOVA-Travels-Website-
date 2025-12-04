import reflex as rx
from typing import TypedDict


class ItineraryItem(TypedDict):
    title: str
    description: str


class Tour(TypedDict):
    id: str
    title: str
    price: int
    price_display: str
    duration: str
    rating: float
    reviews: int
    image: str
    gallery: list[str]
    category: str
    description: str
    location: str
    itinerary: list[ItineraryItem]
    inclusions: list[str]
    exclusions: list[str]


class ToursState(rx.State):
    search_query: str = ""
    selected_category: str = "All"
    max_price: int = 1000
    current_tour_id: str = ""
    all_tours: list[Tour] = [
        {
            "id": "1",
            "title": "Beach Safari Experience",
            "price": 150,
            "price_display": "$150",
            "duration": "1 Day",
            "rating": 4.8,
            "reviews": 124,
            "image": "https://picsum.photos/seed/safari/800/600",
            "gallery": [
                "https://picsum.photos/seed/safari_1/800/600",
                "https://picsum.photos/seed/safari_2/800/600",
                "https://picsum.photos/seed/safari_3/800/600",
            ],
            "category": "Adventure",
            "description": "Experience the best of both worlds with our signature Beach Safari. Start your day with a sunrise game drive in the coastal Shimba Hills Reserve, spotting rare sable antelopes and elephants, then cool off with an afternoon of snorkeling in the Kisite-Mpunguti Marine Park.",
            "location": "Shimba Hills & Kisite-Mpunguti",
            "itinerary": [
                {
                    "title": "06:00 AM",
                    "description": "Pickup from your hotel and drive to Shimba Hills National Reserve.",
                },
                {
                    "title": "09:00 AM",
                    "description": "Guided game drive and hike to Sheldrick Falls.",
                },
                {
                    "title": "01:00 PM",
                    "description": "Swahili seafood lunch on Wasini Island.",
                },
                {
                    "title": "03:00 PM",
                    "description": "Snorkeling and dolphin watching.",
                },
            ],
            "inclusions": ["Park fees", "Transport", "Lunch", "Snorkeling gear"],
            "exclusions": ["Tips", "Alcoholic beverages"],
        },
        {
            "id": "2",
            "title": "Old Town Cultural Walk",
            "price": 45,
            "price_display": "$45",
            "duration": "3 Hours",
            "rating": 4.9,
            "reviews": 89,
            "image": "https://picsum.photos/seed/oldtown/800/600",
            "gallery": [
                "https://picsum.photos/seed/oldtown_1/800/600",
                "https://picsum.photos/seed/oldtown_2/800/600",
            ],
            "category": "Culture",
            "description": "Step back in time as you wander the narrow, winding streets of Mombasa Old Town. Admire the ancient architecture, visit Fort Jesus, and smell the spices of the local markets.",
            "location": "Mombasa Old Town",
            "itinerary": [
                {"title": "09:00 AM", "description": "Meet at Fort Jesus entrance."},
                {
                    "title": "10:30 AM",
                    "description": "Walking tour of Old Town streets and architecture.",
                },
                {
                    "title": "11:30 AM",
                    "description": "Visit to the Old Port and spice market.",
                },
            ],
            "inclusions": ["Guide fees", "Museum entry", "Water"],
            "exclusions": ["Lunch", "Transport to meeting point"],
        },
        {
            "id": "3",
            "title": "Diving Adventure",
            "price": 120,
            "price_display": "$120",
            "duration": "4 Hours",
            "rating": 4.7,
            "reviews": 56,
            "image": "https://picsum.photos/seed/diving/800/600",
            "gallery": [
                "https://picsum.photos/seed/diving_1/800/600",
                "https://picsum.photos/seed/diving_2/800/600",
            ],
            "category": "Water Sports",
            "description": "Explore the vibrant coral reefs of the Indian Ocean. Suitable for beginners and experienced divers alike, this tour takes you to the best spots for marine life.",
            "location": "Mombasa Marine Park",
            "itinerary": [
                {
                    "title": "08:00 AM",
                    "description": "Boat departure from North Coast.",
                },
                {"title": "09:00 AM", "description": "First dive session."},
                {
                    "title": "11:00 AM",
                    "description": "Second dive or snorkeling session.",
                },
            ],
            "inclusions": ["Diving gear", "Instructor", "Boat ride"],
            "exclusions": ["Underwater photography (extra)"],
        },
        {
            "id": "4",
            "title": "Sunset Dhow Cruise",
            "price": 85,
            "price_display": "$85",
            "duration": "2 Hours",
            "rating": 5.0,
            "reviews": 210,
            "image": "https://picsum.photos/seed/dhow/800/600",
            "gallery": [
                "https://picsum.photos/seed/dhow_1/800/600",
                "https://picsum.photos/seed/dhow_2/800/600",
            ],
            "category": "Relaxation",
            "description": "Sail into the sunset on a traditional Arabian Dhow. Enjoy live music, seafood snacks, and the breathtaking colors of the Mombasa skyline at dusk.",
            "location": "Tudor Creek",
            "itinerary": [
                {"title": "05:00 PM", "description": "Boarding at the Tamarind Jetty."},
                {"title": "06:00 PM", "description": "Cruising and sunset viewing."},
                {"title": "07:00 PM", "description": "Return to dock."},
            ],
            "inclusions": ["Welcome drink", "Bitings", "Live music"],
            "exclusions": ["Full dinner (optional upgrade)"],
        },
        {
            "id": "5",
            "title": "Haller Park Wildlife",
            "price": 60,
            "price_display": "$60",
            "duration": "Half Day",
            "rating": 4.6,
            "reviews": 45,
            "image": "https://picsum.photos/seed/haller/800/600",
            "gallery": [
                "https://picsum.photos/seed/haller_1/800/600",
                "https://picsum.photos/seed/haller_2/800/600",
            ],
            "category": "Wildlife",
            "description": "Visit a miracle of nature reclamation. Haller Park is a thriving ecosystem created from a disused limestone quarry, now home to giraffes, hippos, and tortoises.",
            "location": "Bamburi",
            "itinerary": [
                {"title": "02:00 PM", "description": "Arrival and introduction."},
                {"title": "03:00 PM", "description": "Giraffe feeding session."},
                {"title": "04:00 PM", "description": "Nature walk and reptile park."},
            ],
            "inclusions": ["Entry fees", "Guide"],
            "exclusions": ["Transport"],
        },
        {
            "id": "6",
            "title": "Swahili Food Tour",
            "price": 55,
            "price_display": "$55",
            "duration": "3 Hours",
            "rating": 4.9,
            "reviews": 78,
            "image": "https://picsum.photos/seed/food/800/600",
            "gallery": [
                "https://picsum.photos/seed/food_1/800/600",
                "https://picsum.photos/seed/food_2/800/600",
            ],
            "category": "Culinary",
            "description": "Taste the flavors of the coast. From Biryani to Mahamri, this tour takes you to the best local eateries and street food vendors in town.",
            "location": "City Centre",
            "itinerary": [
                {"title": "11:00 AM", "description": "Meet at Mackinnon Market."},
                {"title": "12:00 PM", "description": "Street food tasting walk."},
                {"title": "01:30 PM", "description": "Sit-down Swahili lunch."},
            ],
            "inclusions": ["All food tastings", "Water", "Guide"],
            "exclusions": ["Extra drinks"],
        },
    ]

    @rx.var
    def filtered_tours(self) -> list[Tour]:
        tours = self.all_tours
        if self.search_query:
            tours = [
                t for t in tours if self.search_query.lower() in t["title"].lower()
            ]
        if self.selected_category != "All":
            tours = [t for t in tours if t["category"] == self.selected_category]
        tours = [t for t in tours if t["price"] <= self.max_price]
        return tours

    @rx.var
    def current_tour(self) -> Tour:
        if not self.current_tour_id:
            return self.all_tours[0]
        return next(
            (t for t in self.all_tours if t["id"] == self.current_tour_id),
            self.all_tours[0],
        )

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def set_category(self, category: str):
        self.selected_category = category

    @rx.event
    def set_max_price(self, price: str):
        self.max_price = int(price)

    @rx.event
    def load_tour(self):
        """Load the tour ID from the URL parameters."""
        params = self.router.page.params
        if "id" in params:
            self.current_tour_id = params["id"]