import reflex as rx
from app.states.community_state import CommunityState
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.shared import section_header, primary_button
from app.components.cards import project_card


def impact_metric(metric: dict) -> rx.Component:
    return rx.el.div(
        rx.icon(metric["icon"], class_name="w-10 h-10 text-[#D4AF37] mb-4 mx-auto"),
        rx.el.h3(metric["value"], class_name="text-4xl font-bold text-white mb-2"),
        rx.el.p(
            metric["label"],
            class_name="text-blue-200 font-medium uppercase tracking-wider text-sm",
        ),
        class_name="text-center p-6",
    )


def community_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Community & Impact",
                    class_name="text-4xl md:text-6xl font-bold text-white mb-6 text-center",
                ),
                rx.el.p(
                    "Travel with purpose. See how your visit changes lives.",
                    class_name="text-xl text-white/90 max-w-2xl text-center",
                ),
                class_name="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full flex flex-col justify-center items-center",
            ),
            rx.el.div(
                rx.image(
                    src="https://picsum.photos/seed/community_hero/1920/1080",
                    class_name="w-full h-full object-cover",
                ),
                class_name="absolute inset-0 z-0",
            ),
            rx.el.div(class_name="absolute inset-0 bg-[#015C92]/80 z-0"),
            class_name="relative w-full h-[40vh] min-h-[300px]",
        ),
        rx.el.section(
            rx.el.div(
                rx.foreach(CommunityState.metrics, impact_metric),
                class_name="grid grid-cols-2 md:grid-cols-4 gap-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
            ),
            class_name="py-12 bg-[#015C92]",
        ),
        rx.el.section(
            rx.el.div(
                section_header(
                    "Our Projects",
                    "We invest 10% of all profits back into these community initiatives.",
                ),
                rx.el.div(
                    rx.foreach(CommunityState.projects, project_card),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-8",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
            ),
            class_name="py-20 bg-white",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Volunteer With Us",
                        class_name="text-3xl font-bold text-[#1F2937] mb-4",
                    ),
                    rx.el.p(
                        "Want to make a hands-on difference? Join one of our weekly volunteer programs during your stay.",
                        class_name="text-lg text-gray-600 mb-8",
                    ),
                    primary_button("Apply to Volunteer"),
                    class_name="max-w-2xl",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
            ),
            class_name="py-20 bg-[#F5E4C3]/30",
        ),
        footer(),
        class_name="font-sans",
    )