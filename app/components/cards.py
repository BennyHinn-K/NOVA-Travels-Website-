import reflex as rx
from app.states.home_state import Tour, Feature


def tour_card(tour: Tour) -> rx.Component:
    """A card component for displaying tour information."""
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=tour["image"],
                alt=tour["title"],
                class_name="w-full h-64 object-cover transition-transform duration-500 group-hover:scale-110",
            ),
            rx.el.div(
                rx.el.span(
                    tour["category"],
                    class_name="px-3 py-1 bg-[#D4AF37] text-white text-xs font-bold uppercase tracking-wide rounded-full shadow-sm",
                ),
                class_name="absolute top-4 left-4 z-10",
            ),
            class_name="relative overflow-hidden",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    tour["title"],
                    class_name="text-xl font-bold text-[#1F2937] dark:text-white mb-2 group-hover:text-[#015C92] dark:group-hover:text-[#3faae0] transition-colors",
                ),
                rx.el.div(
                    rx.icon("star", class_name="w-4 h-4 text-[#D4AF37] fill-current"),
                    rx.el.span(
                        tour["rating"].to_string(),
                        class_name="text-sm font-medium text-gray-600 dark:text-gray-300 ml-1",
                    ),
                    class_name="flex items-center mb-3",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "clock",
                        class_name="w-4 h-4 text-gray-400 dark:text-gray-500 mr-2",
                    ),
                    rx.el.span(
                        tour["duration"],
                        class_name="text-sm text-gray-600 dark:text-gray-300",
                    ),
                    class_name="flex items-center",
                ),
                rx.el.div(
                    rx.el.span(
                        "From",
                        class_name="text-xs text-gray-500 dark:text-gray-400 mr-1",
                    ),
                    rx.el.span(
                        tour["price"],
                        class_name="text-lg font-bold text-[#015C92] dark:text-[#3faae0]",
                    ),
                    class_name="flex items-baseline",
                ),
                class_name="flex justify-between items-center border-t border-gray-100 dark:border-gray-700 pt-4",
            ),
            rx.el.button(
                "View Details",
                class_name="w-full mt-4 py-2 border border-[#015C92] dark:border-[#3faae0] text-[#015C92] dark:text-[#3faae0] rounded hover:bg-[#015C92] hover:text-white dark:hover:bg-[#3faae0] dark:hover:text-white transition-colors duration-300 font-medium text-sm",
            ),
            class_name="p-6",
        ),
        class_name="group bg-white dark:bg-gray-800 rounded-xl shadow-sm hover:shadow-2xl transition-all duration-300 overflow-hidden border border-gray-100 dark:border-gray-700 hover:-translate-y-2",
    )


def feature_card(feature: Feature) -> rx.Component:
    """A card displaying a feature or highlight."""
    return rx.el.div(
        rx.el.div(
            rx.icon(
                feature["icon"], class_name="w-8 h-8 text-[#015C92] dark:text-[#3faae0]"
            ),
            class_name="w-16 h-16 bg-[#F5E4C3]/30 dark:bg-[#015C92]/20 rounded-full flex items-center justify-center mb-6 group-hover:bg-[#015C92] dark:group-hover:bg-[#3faae0] group-hover:text-white transition-colors duration-300",
        ),
        rx.el.h3(
            feature["title"],
            class_name="text-xl font-bold text-[#1F2937] dark:text-white mb-3",
        ),
        rx.el.p(
            feature["description"],
            class_name="text-gray-600 dark:text-gray-300 leading-relaxed",
        ),
        class_name="group bg-white dark:bg-gray-800 p-8 rounded-xl border border-gray-100 dark:border-gray-700 hover:shadow-lg hover:border-[#F5E4C3] dark:hover:border-[#015C92] transition-all duration-300 hover:-translate-y-1",
    )


def team_member_card(member: dict) -> rx.Component:
    """A card displaying a team member."""
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=member["image"],
                alt=member["name"],
                class_name="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110",
            ),
            rx.el.div(
                class_name="absolute inset-0 bg-gradient-to-t from-[#015C92]/90 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"
            ),
            rx.el.div(
                rx.el.p(
                    member["bio"],
                    class_name="text-white text-sm leading-relaxed translate-y-4 group-hover:translate-y-0 transition-transform duration-300",
                ),
                class_name="absolute bottom-0 left-0 right-0 p-6 opacity-0 group-hover:opacity-100 transition-opacity duration-300",
            ),
            class_name="relative w-full h-80 overflow-hidden rounded-xl mb-4",
        ),
        rx.el.h3(
            member["name"], class_name="text-xl font-bold text-[#1F2937] text-center"
        ),
        rx.el.p(
            member["role"], class_name="text-[#015C92] font-medium text-center text-sm"
        ),
        class_name="group",
    )


def project_card(project: dict) -> rx.Component:
    """A card displaying a community project."""
    return rx.el.div(
        rx.image(
            src=project["image"], class_name="w-full h-64 object-cover rounded-t-xl"
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    project["category"],
                    class_name="text-xs font-bold text-[#D4AF37] uppercase tracking-wider",
                ),
                rx.el.h3(
                    project["title"],
                    class_name="text-xl font-bold text-[#015C92] mt-2 mb-3",
                ),
                rx.el.p(
                    project["description"],
                    class_name="text-gray-600 mb-4 text-sm leading-relaxed",
                ),
                rx.el.div(
                    rx.icon("trending-up", class_name="w-5 h-5 text-[#D4AF37] mr-2"),
                    rx.el.span(
                        project["impact"], class_name="font-bold text-[#1F2937] text-sm"
                    ),
                    class_name="flex items-center bg-gray-50 p-3 rounded-lg border border-gray-100",
                ),
            ),
            class_name="p-6 border border-t-0 border-gray-100 rounded-b-xl bg-white shadow-sm hover:shadow-md transition-shadow",
        ),
        class_name="flex flex-col h-full",
    )