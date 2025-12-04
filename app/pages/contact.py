import reflex as rx
from app.states.contact_state import ContactState
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.shared import section_header, primary_button
from app.components.animations import scroll_animation


def contact_info_card(
    icon: str, title: str, content: str, sub_content: str = ""
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="w-8 h-8 text-[#D4AF37]"),
            class_name="w-16 h-16 bg-[#015C92]/5 dark:bg-[#015C92]/20 rounded-full flex items-center justify-center mb-6 mx-auto",
        ),
        rx.el.h3(
            title,
            class_name="text-xl font-bold text-[#015C92] dark:text-[#3faae0] mb-3 text-center",
        ),
        rx.el.p(
            content,
            class_name="text-gray-600 dark:text-gray-300 text-center font-medium",
        ),
        rx.cond(
            sub_content != "",
            rx.el.p(
                sub_content,
                class_name="text-gray-500 dark:text-gray-400 text-center text-sm mt-1",
            ),
        ),
        class_name="bg-white dark:bg-gray-800 p-8 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 hover:shadow-lg transition-all duration-300 hover:-translate-y-1",
    )


def contact_form() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Send us a Message",
            class_name="text-2xl font-bold text-[#015C92] dark:text-[#3faae0] mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.label(
                    "Full Name",
                    class_name="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2",
                ),
                rx.el.input(
                    placeholder="John Doe",
                    on_change=ContactState.set_name,
                    class_name="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white focus:ring-2 focus:ring-[#015C92] focus:border-transparent outline-none transition-all",
                    default_value=ContactState.name,
                ),
                class_name="mb-6",
            ),
            rx.el.div(
                rx.el.label(
                    "Email Address",
                    class_name="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2",
                ),
                rx.el.input(
                    type="email",
                    placeholder="john@example.com",
                    on_change=ContactState.set_email,
                    class_name="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white focus:ring-2 focus:ring-[#015C92] focus:border-transparent outline-none transition-all",
                    default_value=ContactState.email,
                ),
                class_name="mb-6",
            ),
            rx.el.div(
                rx.el.label(
                    "Phone Number",
                    class_name="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2",
                ),
                rx.el.input(
                    placeholder="+254 700 000 000",
                    on_change=ContactState.set_phone,
                    class_name="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white focus:ring-2 focus:ring-[#015C92] focus:border-transparent outline-none transition-all",
                    default_value=ContactState.phone,
                ),
                class_name="mb-6",
            ),
            rx.el.div(
                rx.el.label(
                    "Interested In",
                    class_name="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2",
                ),
                rx.el.select(
                    rx.el.option("General Inquiry", value="General Inquiry"),
                    rx.el.option("Book a Tour", value="Book a Tour"),
                    rx.el.option("Custom Package", value="Custom Package"),
                    rx.el.option("Partnership", value="Partnership"),
                    value=ContactState.interest,
                    on_change=ContactState.set_interest,
                    class_name="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white focus:ring-2 focus:ring-[#015C92] focus:border-transparent outline-none transition-all",
                ),
                class_name="mb-6",
            ),
            rx.el.div(
                rx.el.label(
                    "Message",
                    class_name="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2",
                ),
                rx.el.textarea(
                    placeholder="Tell us about your travel plans...",
                    on_change=ContactState.set_message,
                    rows=5,
                    class_name="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white focus:ring-2 focus:ring-[#015C92] focus:border-transparent outline-none transition-all",
                    default_value=ContactState.message,
                ),
                class_name="mb-8",
            ),
            rx.el.button(
                rx.cond(
                    ContactState.is_loading,
                    rx.el.span("Sending...", class_name="animate-pulse"),
                    "Send Message",
                ),
                on_click=ContactState.handle_submit,
                disabled=ContactState.is_loading,
                class_name="w-full bg-[#015C92] dark:bg-[#3faae0] text-white font-bold py-4 px-8 rounded-lg hover:bg-[#014a75] dark:hover:bg-[#2d8ac0] transition-all duration-300 hover:-translate-y-1 disabled:opacity-70 disabled:cursor-not-allowed shadow-lg shadow-[#015C92]/20",
            ),
            class_name="bg-white dark:bg-gray-800 p-8 md:p-10 rounded-2xl shadow-lg border border-gray-100 dark:border-gray-700",
        ),
    )


def google_map() -> rx.Component:
    return rx.el.div(
        rx.el.iframe(
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3979.8474582345!2d39.66359!3d-4.05466!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x184012e1c7b216c9%3A0x940b62a2c8e3341!2sFort%20Jesus%20Museum!5e0!3m2!1sen!2ske!4v1625000000000!5m2!1sen!2ske",
            width="100%",
            height="100%",
            allowfullscreen="",
            loading="lazy",
            class_name="absolute inset-0 w-full h-full rounded-2xl grayscale hover:grayscale-0 transition-all duration-500",
        ),
        class_name="relative w-full h-[400px] md:h-full min-h-[400px] rounded-2xl overflow-hidden shadow-lg border-4 border-white dark:border-gray-700",
    )


def contact_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Get in Touch",
                    class_name="text-4xl md:text-6xl font-bold text-white mb-6 text-center",
                ),
                rx.el.p(
                    "We'd love to hear from you. Start planning your dream coastal getaway today.",
                    class_name="text-xl text-white/90 max-w-2xl text-center",
                ),
                class_name="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full flex flex-col justify-center items-center",
            ),
            rx.el.div(
                rx.image(
                    src="https://picsum.photos/seed/contact_hero/1920/1080",
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
                    contact_info_card(
                        "map-pin",
                        "Visit Us",
                        "Moi Avenue, Mombasa",
                        "2nd Floor, Ocean View Plaza",
                    ),
                    contact_info_card(
                        "phone", "Call Us", "+254 700 000 000", "Mon-Sat, 8am - 6pm"
                    ),
                    contact_info_card(
                        "mail",
                        "Email Us",
                        "hello@mombasatours.com",
                        "We reply within 24 hours",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-8 -mt-20 relative z-20",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
            )
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    contact_form(),
                    rx.el.div(
                        google_map(),
                        rx.el.div(
                            rx.el.h4(
                                "Chat on WhatsApp",
                                class_name="font-bold text-[#015C92] dark:text-[#3faae0] mb-3",
                            ),
                            rx.el.p(
                                "Need a quick response? Chat with our agents directly.",
                                class_name="text-gray-600 dark:text-gray-300 mb-4 text-sm",
                            ),
                            rx.el.a(
                                rx.icon("message-circle", class_name="w-5 h-5 mr-2"),
                                "Start WhatsApp Chat",
                                href="https://wa.me/254700000000?text=I'm%20interested%20in%20booking%20a%20tour",
                                target="_blank",
                                class_name="inline-flex items-center justify-center w-full bg-[#25D366] text-white font-bold py-3 px-6 rounded-lg hover:bg-[#1ebd59] transition-colors shadow-md",
                            ),
                            class_name="mt-8 bg-[#25D366]/10 p-6 rounded-xl border border-[#25D366]/20",
                        ),
                        class_name="flex flex-col",
                    ),
                    class_name="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20",
            ),
            class_name="bg-gray-50 dark:bg-gray-900 transition-colors duration-300",
        ),
        footer(),
        class_name="font-sans bg-white dark:bg-gray-900",
    )