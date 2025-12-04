import reflex as rx
from typing import TypedDict


class TeamMember(TypedDict):
    name: str
    role: str
    image: str
    bio: str


class AboutState(rx.State):
    team: list[TeamMember] = [
        {
            "name": "Amani Juma",
            "role": "Founder & CEO",
            "image": "https://picsum.photos/seed/amani/400/400",
            "bio": "With over 20 years in tourism, Amani founded Mombasa Tours to share the authentic beauty of his hometown with the world.",
        },
        {
            "name": "Sarah Kamau",
            "role": "Head of Experiences",
            "image": "https://picsum.photos/seed/sarah/400/400",
            "bio": "Sarah curates every tour to ensure deep cultural immersion and unforgettable moments for our guests.",
        },
        {
            "name": "David Ochieng",
            "role": "Lead Guide",
            "image": "https://picsum.photos/seed/david/400/400",
            "bio": "David's knowledge of marine life and local history is unmatched. He leads our signature diving and safari expeditions.",
        },
        {
            "name": "Fatuma Ali",
            "role": "Community Liaison",
            "image": "https://picsum.photos/seed/fatuma/400/400",
            "bio": "Fatuma ensures our operations directly benefit the local communities through our CSR initiatives.",
        },
    ]