import reflex as rx
from app.states.tours_state import ToursState
from app.states.lightbox_state import LightboxState
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.timeline import timeline
from app.components.shared import primary_button
from app.components.lightbox import lightbox
from app.components.animations import scroll_animation


def gallery_section(images: list[str]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=images[0],
                class_name="w-full h-[400px] object-cover rounded-xl hover:scale-[1.02] transition-transform duration-500 cursor-pointer shadow-md",
                on_click=lambda: LightboxState.open_lightbox(images, 0),
            ),
            class_name="col-span-2",
        ),
        rx.el.div(
            rx.foreach(
                rx.Var.range(images.length()),
                lambda i: rx.image(
                    src=images[i],
                    class_name="w-full h-[190px] object-cover rounded-xl hover:opacity-90 transition-opacity cursor-pointer shadow-sm",
                    on_click=lambda: LightboxState.open_lightbox(images, i),
                ),
            ),
            class_name="grid grid-cols-1 gap-4",
        ),
        class_name="grid grid-cols-1 md:grid-cols-3 gap-4 mb-12",
    )


def booking_form() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Book This Tour", class_name="text-xl font-bold text-[#015C92] mb-6"),
        rx.el.form(
            rx.el.div(
                rx.el.label(
                    "Full Name",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.input(
                    placeholder="John Doe",
                    class_name="w-full rounded-lg border-gray-300 focus:border-[#015C92] focus:ring-[#015C92]",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Email", class_name="block text-sm font-medium text-gray-700 mb-1"
                ),
                rx.el.input(
                    type="email",
                    placeholder="john@example.com",
                    class_name="w-full rounded-lg border-gray-300 focus:border-[#015C92] focus:ring-[#015C92]",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Date", class_name="block text-sm font-medium text-gray-700 mb-1"
                ),
                rx.el.input(
                    type="date",
                    class_name="w-full rounded-lg border-gray-300 focus:border-[#015C92] focus:ring-[#015C92]",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Guests", class_name="block text-sm font-medium text-gray-700 mb-1"
                ),
                rx.el.input(
                    type="number",
                    min="1",
                    default_value="2",
                    class_name="w-full rounded-lg border-gray-300 focus:border-[#015C92] focus:ring-[#015C92]",
                ),
                class_name="mb-6",
            ),
            primary_button("Send Inquiry", class_name="w-full"),
            class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100 sticky top-24",
        ),
    )


def tour_details_page() -> rx.Component:
    tour = ToursState.current_tour
    return rx.el.div(
        lightbox(),
        navbar(),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    tour["category"],
                    class_name="inline-block px-4 py-1.5 bg-[#D4AF37] text-white text-sm font-bold uppercase tracking-wide rounded-full mb-4 shadow-sm",
                ),
                rx.el.h1(
                    tour["title"],
                    class_name="text-4xl md:text-6xl font-bold text-white mb-6 leading-tight",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon("clock", class_name="w-5 h-5 text-[#D4AF37] mr-2"),
                        rx.el.span(
                            tour["duration"], class_name="text-white font-medium"
                        ),
                        class_name="flex items-center mr-8",
                    ),
                    rx.el.div(
                        rx.icon("star", class_name="w-4 h-4 text-[#D4AF37] mr-2"),
                        rx.el.span(
                            f"{tour['rating']} ({tour['reviews']} reviews)",
                            class_name="text-white font-medium",
                        ),
                        class_name="flex items-center",
                    ),
                    class_name="flex flex-wrap items-center",
                ),
                class_name="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full flex flex-col justify-end pb-16",
            ),
            rx.el.div(
                rx.image(src=tour["image"], class_name="w-full h-full object-cover"),
                class_name="absolute inset-0 z-0",
            ),
            rx.el.div(
                class_name="absolute inset-0 bg-gradient-to-t from-[#015C92]/90 via-[#015C92]/40 to-transparent z-0"
            ),
            class_name="relative w-full h-[60vh] min-h-[500px]",
            id="hero",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        scroll_animation(
                            rx.el.div(
                                rx.el.h2(
                                    "Overview",
                                    class_name="text-2xl font-bold text-[#015C92] dark:text-[#3faae0] mb-4",
                                ),
                                rx.el.p(
                                    tour["description"],
                                    class_name="text-gray-600 dark:text-gray-300 leading-relaxed mb-8 text-lg",
                                ),
                                class_name="mb-12",
                            )
                        ),
                        gallery_section(tour["gallery"]),
                        scroll_animation(
                            rx.el.div(
                                rx.el.h2(
                                    "Itinerary",
                                    class_name="text-2xl font-bold text-[#015C92] dark:text-[#3faae0] mb-6",
                                ),
                                timeline(tour["itinerary"]),
                                class_name="mb-12",
                            ),
                            "100",
                        ),
                        scroll_animation(
                            rx.el.div(
                                rx.el.h2(
                                    "What's Included",
                                    class_name="text-2xl font-bold text-[#015C92] dark:text-[#3faae0] mb-6",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.h4(
                                            "Inclusions",
                                            class_name="font-bold text-green-600 dark:text-green-400 mb-3",
                                        ),
                                        rx.foreach(
                                            tour["inclusions"],
                                            lambda item: rx.el.div(
                                                rx.icon(
                                                    "check",
                                                    class_name="w-5 h-5 text-green-500 mr-2",
                                                ),
                                                rx.el.span(
                                                    item,
                                                    class_name="text-gray-600 dark:text-gray-300",
                                                ),
                                                class_name="flex items-center mb-2",
                                            ),
                                        ),
                                        class_name="bg-green-50 dark:bg-green-900/20 p-6 rounded-xl",
                                    ),
                                    rx.el.div(
                                        rx.el.h4(
                                            "Exclusions",
                                            class_name="font-bold text-red-600 dark:text-red-400 mb-3",
                                        ),
                                        rx.foreach(
                                            tour["exclusions"],
                                            lambda item: rx.el.div(
                                                rx.icon(
                                                    "x",
                                                    class_name="w-5 h-5 text-red-500 mr-2",
                                                ),
                                                rx.el.span(
                                                    item,
                                                    class_name="text-gray-600 dark:text-gray-300",
                                                ),
                                                class_name="flex items-center mb-2",
                                            ),
                                        ),
                                        class_name="bg-red-50 dark:bg-red-900/20 p-6 rounded-xl",
                                    ),
                                    class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
                                ),
                                class_name="mb-12",
                            ),
                            "200",
                        ),
                    ),
                    class_name="md:col-span-2",
                ),
                rx.el.div(
                    scroll_animation(
                        rx.el.div(
                            rx.el.div(
                                rx.el.span(
                                    tour["price_display"],
                                    class_name="text-3xl font-bold text-[#015C92] dark:text-[#3faae0]",
                                ),
                                rx.el.span(
                                    " / per person",
                                    class_name="text-gray-500 dark:text-gray-400",
                                ),
                                class_name="mb-6 p-6 bg-gray-50 dark:bg-gray-800 rounded-xl border border-gray-100 dark:border-gray-700 text-center",
                            ),
                            booking_form(),
                            class_name="sticky top-24",
                        ),
                        "300",
                    ),
                    class_name="md:col-span-1",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-12 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16",
            ),
            class_name="bg-white dark:bg-gray-900 min-h-screen transition-colors duration-300",
        ),
        footer(),
        class_name="font-sans bg-white dark:bg-gray-900",
        on_mount=ToursState.load_tour,
    )