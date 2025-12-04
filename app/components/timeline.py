import reflex as rx
from app.states.tours_state import ItineraryItem


def timeline_item(item: ItineraryItem, index: int, total: int) -> rx.Component:
    is_last = index == total - 1
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                class_name="w-4 h-4 rounded-full bg-[#015C92] border-4 border-[#E0F2FE]"
            ),
            rx.cond(
                ~is_last, rx.el.div(class_name="w-0.5 h-full bg-gray-200 my-2 mx-auto")
            ),
            class_name="flex flex-col items-center mr-4 mt-1",
        ),
        rx.el.div(
            rx.el.h4(item["title"], class_name="text-lg font-bold text-[#1F2937]"),
            rx.el.p(item["description"], class_name="text-gray-600 mt-1"),
            class_name="pb-8",
        ),
        class_name="flex",
    )


def timeline(items: list[ItineraryItem]) -> rx.Component:
    return rx.el.div(
        rx.foreach(items, lambda item, i: timeline_item(item, i, items.length())),
        class_name="mt-8",
    )