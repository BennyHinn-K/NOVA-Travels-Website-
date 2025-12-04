import reflex as rx
from app.states.tours_state import ToursState
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.cards import tour_card
from app.components.filters import filter_sidebar
from app.components.shared import section_header


def tours_grid() -> rx.Component:
    return rx.el.div(
        rx.cond(
            ToursState.filtered_tours.length() > 0,
            rx.el.div(
                rx.foreach(
                    ToursState.filtered_tours,
                    lambda tour: rx.el.a(
                        tour_card(tour), href=f"/tours/{tour['id']}", class_name="block"
                    ),
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
            rx.el.div(
                rx.icon("search", class_name="w-16 h-16 text-gray-300 mx-auto mb-4"),
                rx.el.h3(
                    "No tours found", class_name="text-xl font-bold text-gray-600"
                ),
                rx.el.p("Try adjusting your filters.", class_name="text-gray-500"),
                class_name="text-center py-20 col-span-full bg-gray-50 rounded-xl border border-gray-100",
            ),
        )
    )


def tours_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Explore Our Tours",
                    class_name="text-4xl md:text-5xl font-bold text-white mb-4",
                ),
                rx.el.p(
                    "Find your perfect Mombasa adventure.",
                    class_name="text-xl text-white/90 max-w-2xl",
                ),
                class_name="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full flex flex-col justify-center",
            ),
            rx.el.div(
                rx.image(
                    src="https://picsum.photos/seed/tours_hero/1920/1080",
                    class_name="w-full h-full object-cover",
                ),
                class_name="absolute inset-0 z-0",
            ),
            rx.el.div(class_name="absolute inset-0 bg-[#015C92]/70 z-0"),
            class_name="relative w-full h-[40vh] min-h-[300px]",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(filter_sidebar(), class_name="md:col-span-1"),
                rx.el.div(tours_grid(), class_name="md:col-span-3"),
                class_name="grid grid-cols-1 md:grid-cols-4 gap-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16",
            ),
            class_name="bg-white min-h-screen",
        ),
        footer(),
        class_name="font-sans",
    )