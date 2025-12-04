import reflex as rx
from app.states.navbar_state import NavbarState
from app.components.shared import primary_button


def nav_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name="text-[#1F2937] dark:text-gray-200 hover:text-[#015C92] dark:hover:text-[#3faae0] font-medium transition-colors duration-200",
    )


def mobile_nav_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        on_click=NavbarState.close_mobile_menu,
        class_name="text-lg font-medium text-[#1F2937] dark:text-gray-200 hover:text-[#015C92] dark:hover:text-[#3faae0] block py-2",
    )


def theme_toggle() -> rx.Component:
    return rx.el.button(
        rx.cond(
            rx.color_mode == "light",
            rx.icon("moon", class_name="w-5 h-5 text-gray-600 dark:text-gray-300"),
            rx.icon("sun", class_name="w-5 h-5 text-yellow-400"),
        ),
        on_click=rx.toggle_color_mode,
        class_name="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors",
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "tree_palm",
                    class_name="w-8 h-8 text-[#015C92] dark:text-[#3faae0] mr-2",
                ),
                rx.el.span(
                    "Mombasa",
                    class_name="text-2xl font-bold text-[#015C92] dark:text-[#3faae0]",
                ),
                rx.el.span("Tours", class_name="text-2xl font-light text-[#D4AF37]"),
                class_name="flex items-center cursor-pointer",
            ),
            rx.el.div(
                nav_link("Home", "/"),
                nav_link("Tours", "/tours"),
                nav_link("About", "/about"),
                nav_link("Community", "/community"),
                nav_link("Contact", "/contact"),
                class_name="hidden md:flex items-center space-x-8",
            ),
            rx.el.div(
                theme_toggle(),
                rx.el.button(
                    "Book Now",
                    class_name="bg-[#015C92] dark:bg-[#3faae0] text-white px-6 py-2.5 rounded-lg font-medium hover:bg-[#014a75] dark:hover:bg-[#2d8ac0] transition-colors shadow-lg shadow-[#015C92]/20 hidden md:block",
                ),
                rx.el.button(
                    rx.icon(
                        "menu", class_name="w-6 h-6 text-[#1F2937] dark:text-white"
                    ),
                    on_click=NavbarState.toggle_mobile_menu,
                    class_name="md:hidden p-2 focus:outline-none",
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "x", class_name="w-6 h-6 text-[#1F2937] dark:text-white"
                        ),
                        on_click=NavbarState.toggle_mobile_menu,
                        class_name="absolute top-6 right-6 p-2 cursor-pointer",
                    ),
                    mobile_nav_link("Home", "/"),
                    mobile_nav_link("Tours", "/tours"),
                    mobile_nav_link("About", "/about"),
                    mobile_nav_link("Community", "/community"),
                    mobile_nav_link("Contact", "/contact"),
                    rx.el.button(
                        "Book Now",
                        class_name="w-full mt-6 bg-[#015C92] text-white px-6 py-3 rounded-lg font-medium hover:bg-[#014a75] transition-colors",
                    ),
                    class_name="flex flex-col space-y-4 mt-16 px-6",
                ),
                class_name=rx.cond(
                    NavbarState.is_mobile_menu_open,
                    "fixed inset-y-0 right-0 w-full sm:w-80 bg-white dark:bg-gray-900 shadow-2xl transform translate-x-0 transition-transform duration-300 ease-in-out z-50",
                    "fixed inset-y-0 right-0 w-full sm:w-80 bg-white dark:bg-gray-900 shadow-2xl transform translate-x-full transition-transform duration-300 ease-in-out z-50",
                ),
            ),
            rx.cond(
                NavbarState.is_mobile_menu_open,
                rx.el.div(
                    class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-40",
                    on_click=NavbarState.toggle_mobile_menu,
                ),
            ),
        ),
        class_name="fixed top-0 left-0 right-0 z-50 bg-white/90 dark:bg-gray-900/90 backdrop-blur-md border-b border-gray-100 dark:border-gray-800 shadow-sm transition-all duration-300",
    )