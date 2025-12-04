import reflex as rx
from typing import TypedDict


class Project(TypedDict):
    title: str
    category: str
    description: str
    image: str
    impact: str


class Metric(TypedDict):
    value: str
    label: str
    icon: str


class CommunityState(rx.State):
    projects: list[Project] = [
        {
            "title": "Beach Cleanup Initiative",
            "category": "Environment",
            "description": "Weekly cleanups along the coastline involving 50+ local volunteers.",
            "image": "https://picsum.photos/seed/cleanup/800/600",
            "impact": "5 Tons of plastic removed",
        },
        {
            "title": "Education Scholarship Fund",
            "category": "Education",
            "description": "Providing school fees and supplies for underprivileged children in Old Town.",
            "image": "https://picsum.photos/seed/education/800/600",
            "impact": "120 Students supported",
        },
        {
            "title": "Coral Reef Restoration",
            "category": "Conservation",
            "description": "Working with marine biologists to replant coral fragments in damaged reef areas.",
            "image": "https://picsum.photos/seed/coral/800/600",
            "impact": "2000+ Coral fragments planted",
        },
    ]
    metrics: list[Metric] = [
        {"value": "15K+", "label": "Lives Touched", "icon": "heart"},
        {"value": "50+", "label": "Local Partners", "icon": "handshake"},
        {"value": "10K", "label": "Trees Planted", "icon": "tree-palm"},
        {"value": "$50K", "label": "Community Invested", "icon": "coins"},
    ]