import reflex as rx


def footer_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name="text-[#015C92]/80 hover:text-[#015C92] hover:underline transition-colors",
    )


def social_icon(icon: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="w-5 h-5"),
        href=href,
        class_name="w-10 h-10 rounded-full bg-[#015C92]/10 flex items-center justify-center text-[#015C92] hover:bg-[#015C92] hover:text-white transition-all duration-300",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("tree_palm", class_name="w-6 h-6 text-[#015C92] mr-2"),
                        rx.el.span(
                            "Mombasa", class_name="text-xl font-bold text-[#015C92]"
                        ),
                        rx.el.span(
                            "Tours", class_name="text-xl font-light text-[#D4AF37]"
                        ),
                        class_name="flex items-center mb-6",
                    ),
                    rx.el.p(
                        "Creating unforgettable coastal memories since 2008. We specialize in sustainable, community-driven tourism experiences.",
                        class_name="text-[#015C92]/80 mb-6 leading-relaxed max-w-sm",
                    ),
                    rx.el.div(
                        social_icon("facebook", "#"),
                        social_icon("instagram", "#"),
                        social_icon("twitter", "#"),
                        social_icon("phone", "#"),
                        class_name="flex space-x-4",
                    ),
                ),
                rx.el.div(
                    rx.el.h3(
                        "Quick Links",
                        class_name="font-bold text-[#015C92] mb-6 text-lg",
                    ),
                    rx.el.div(
                        footer_link("Home", "#"),
                        footer_link("Our Tours", "#"),
                        footer_link("About Us", "#"),
                        footer_link("Community Impact", "#"),
                        footer_link("Contact", "#"),
                        class_name="flex flex-col space-y-3",
                    ),
                ),
                rx.el.div(
                    rx.el.h3(
                        "Contact Us", class_name="font-bold text-[#015C92] mb-6 text-lg"
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "map-pin", class_name="w-5 h-5 text-[#D4AF37] mr-3 mt-1"
                            ),
                            rx.el.span(
                                "Moi Avenue, Mombasa, Kenya",
                                class_name="text-[#015C92]/80",
                            ),
                            class_name="flex items-start",
                        ),
                        rx.el.div(
                            rx.icon(
                                "mail", class_name="w-5 h-5 text-[#D4AF37] mr-3 mt-1"
                            ),
                            rx.el.span(
                                "hello@mombasatours.com", class_name="text-[#015C92]/80"
                            ),
                            class_name="flex items-start",
                        ),
                        rx.el.div(
                            rx.icon(
                                "phone", class_name="w-5 h-5 text-[#D4AF37] mr-3 mt-1"
                            ),
                            rx.el.span(
                                "+254 700 000 000", class_name="text-[#015C92]/80"
                            ),
                            class_name="flex items-start",
                        ),
                        class_name="flex flex-col space-y-4",
                    ),
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-12 lg:gap-24",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2024 Mombasa Tours. All rights reserved.",
                    class_name="text-[#015C92]/60 text-sm text-center",
                ),
                class_name="mt-16 pt-8 border-t border-[#015C92]/10",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16",
        ),
        class_name="bg-[#F5E4C3] w-full",
    )