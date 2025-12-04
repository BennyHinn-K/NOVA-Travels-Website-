import reflex as rx
from app.states.tours_state import ToursState


def filter_sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3("Filters", class_name="text-xl font-bold text-[#015C92] mb-6"),
            rx.el.div(
                rx.el.label(
                    "Search", class_name="block text-sm font-medium text-gray-700 mb-2"
                ),
                rx.el.input(
                    placeholder="Search tours...",
                    on_change=ToursState.set_search_query,
                    class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#015C92] focus:border-transparent outline-none",
                ),
                class_name="mb-8",
            ),
            rx.el.div(
                rx.el.label(
                    "Category",
                    class_name="block text-sm font-medium text-gray-700 mb-2",
                ),
                rx.el.select(
                    rx.el.option("All", value="All"),
                    rx.el.option("Adventure", value="Adventure"),
                    rx.el.option("Culture", value="Culture"),
                    rx.el.option("Water Sports", value="Water Sports"),
                    rx.el.option("Wildlife", value="Wildlife"),
                    rx.el.option("Relaxation", value="Relaxation"),
                    rx.el.option("Culinary", value="Culinary"),
                    value=ToursState.selected_category,
                    on_change=ToursState.set_category,
                    class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#015C92] focus:border-transparent outline-none bg-white",
                ),
                class_name="mb-8",
            ),
            rx.el.div(
                rx.el.label(
                    "Max Price",
                    class_name="block text-sm font-medium text-gray-700 mb-2",
                ),
                rx.el.div(
                    rx.el.span("$", class_name="text-gray-500"),
                    rx.el.span(
                        ToursState.max_price.to_string(),
                        class_name="text-[#015C92] font-bold",
                    ),
                    class_name="flex justify-between mb-2",
                ),
                rx.el.input(
                    type="range",
                    default_value=ToursState.max_price,
                    min="0",
                    max="1000",
                    step="10",
                    key="max_price",
                    on_change=ToursState.set_max_price.throttle(50),
                    class_name="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-[#015C92]",
                ),
                class_name="mb-6",
            ),
        ),
        class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100 h-fit sticky top-24",
    )