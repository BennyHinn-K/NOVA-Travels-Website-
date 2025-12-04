import reflex as rx
from app.states.about_state import AboutState
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.shared import section_header
from app.components.cards import team_member_card


def about_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Our Story",
                    class_name="text-4xl md:text-6xl font-bold text-white mb-6 text-center",
                ),
                class_name="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full flex flex-col justify-center items-center",
            ),
            rx.el.div(
                rx.image(
                    src="https://picsum.photos/seed/about_hero/1920/1080",
                    class_name="w-full h-full object-cover",
                ),
                class_name="absolute inset-0 z-0",
            ),
            rx.el.div(class_name="absolute inset-0 bg-[#015C92]/80 z-0"),
            class_name="relative w-full h-[40vh] min-h-[300px]",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "We Are Mombasa",
                        class_name="text-3xl font-bold text-[#015C92] mb-6",
                    ),
                    rx.el.p(
                        "Founded in 2008, Mombasa Tours began with a simple mission: to show the world the true, authentic beauty of the Kenyan coast. We believe in tourism that respects local culture, uplifts communities, and preserves our natural heritage.",
                        class_name="text-lg text-gray-600 leading-relaxed mb-6",
                    ),
                    rx.el.p(
                        "From humble beginnings as a walking tour operator in Old Town, we have grown into a premier travel agency offering bespoke experiences across the coast.",
                        class_name="text-lg text-gray-600 leading-relaxed",
                    ),
                ),
                rx.el.div(
                    rx.image(
                        src="https://picsum.photos/seed/mombasa_history/800/600",
                        class_name="rounded-2xl shadow-xl w-full h-full object-cover",
                    ),
                    class_name="h-[400px]",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-12 items-center max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
            ),
            class_name="py-20 bg-white",
        ),
        rx.el.section(
            rx.el.div(
                section_header(
                    "Meet Our Team",
                    "The passionate locals behind your unforgettable experiences.",
                ),
                rx.el.div(
                    rx.foreach(AboutState.team, team_member_card),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
            ),
            class_name="py-20 bg-gray-50",
        ),
        footer(),
        class_name="font-sans",
    )