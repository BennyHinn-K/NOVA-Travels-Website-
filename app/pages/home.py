import reflex as rx
from app.states.home_state import HomeState
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.shared import primary_button, secondary_button, section_header
from app.components.cards import tour_card, feature_card


def hero_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src="https://picsum.photos/seed/mombasa_hero/1920/1080",
                class_name="w-full h-full object-cover",
            ),
            class_name="absolute inset-0 z-0",
        ),
        rx.el.div(
            class_name="absolute inset-0 bg-gradient-to-r from-[#015C92]/90 to-[#015C92]/40 z-10"
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Discover Paradise in Mombasa",
                    class_name="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight animate-fade-in-up",
                ),
                rx.el.p(
                    "Experience the magic of the Kenyan coast. From pristine white sands to historic Old Town adventures, your perfect getaway starts here.",
                    class_name="text-xl md:text-2xl text-gray-100 mb-10 max-w-2xl leading-relaxed animate-fade-in-up delay-100",
                ),
                rx.el.div(
                    primary_button(
                        "Explore Tours",
                        class_name="bg-[#D4AF37] hover:bg-[#b5952f] text-[#015C92] border-transparent shadow-xl shadow-black/10",
                    ),
                    secondary_button("Learn More", class_name="ml-4"),
                    class_name="flex items-center animate-fade-in-up delay-200",
                ),
                class_name="relative z-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full flex flex-col justify-center",
            ),
            class_name="w-full h-full",
        ),
        class_name="relative w-full h-screen min-h-[600px] overflow-hidden",
    )


def tours_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            section_header(
                "Featured Tours",
                "Handpicked experiences designed to show you the very best of Mombasa.",
            ),
            rx.el.div(
                rx.foreach(HomeState.featured_tours, tour_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            rx.el.div(
                rx.el.button(
                    "View All Tours",
                    class_name="group inline-flex items-center text-[#015C92] font-bold text-lg hover:underline underline-offset-4 transition-all",
                ),
                class_name="text-center mt-12",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="py-20 bg-gray-50",
    )


def features_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            section_header("Why Choose Us"),
            rx.el.div(
                rx.foreach(HomeState.features, feature_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="py-20 bg-white",
    )


def testimonial_slide(testimonial: dict, index: int) -> rx.Component:
    """Renders a single testimonial slide."""
    is_active = HomeState.current_testimonial_index == index
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.image(
                    src=testimonial["image"],
                    class_name="w-20 h-20 rounded-full object-cover border-4 border-white shadow-lg mx-auto mb-6",
                ),
                rx.el.div(
                    rx.foreach(
                        rx.Var.range(5),
                        lambda i: rx.icon(
                            "star",
                            class_name="w-5 h-5 text-[#D4AF37] fill-current inline-block",
                        ),
                    ),
                    class_name="flex justify-center gap-1 mb-6",
                ),
                rx.el.p(
                    f'''"{testimonial["text"]}"''',
                    class_name="text-xl md:text-2xl text-[#1F2937] font-medium italic text-center mb-8 leading-relaxed",
                ),
                rx.el.div(
                    rx.el.h4(
                        testimonial["name"],
                        class_name="font-bold text-[#015C92] text-lg",
                    ),
                    rx.el.span(
                        testimonial["location"],
                        class_name="text-gray-500 text-sm block",
                    ),
                    class_name="text-center",
                ),
                class_name="max-w-3xl mx-auto bg-white p-8 md:p-12 rounded-2xl shadow-xl border border-gray-100",
            ),
            class_name=rx.cond(is_active, "block animate-fade-in", "hidden"),
        )
    )


def testimonials_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            section_header("What Our Guests Say"),
            rx.el.div(
                rx.foreach(
                    HomeState.testimonials, lambda t, i: testimonial_slide(t, i)
                ),
                rx.el.div(
                    rx.foreach(
                        rx.Var.range(HomeState.testimonials.length()),
                        lambda i: rx.el.button(
                            on_click=lambda: HomeState.set_testimonial_index(i),
                            class_name=rx.cond(
                                HomeState.current_testimonial_index == i,
                                "w-3 h-3 rounded-full bg-[#015C92] transition-all duration-300 scale-125 mx-1.5 p-1",
                                "w-3 h-3 rounded-full bg-gray-300 hover:bg-[#015C92]/50 transition-all duration-300 mx-1.5 p-1",
                            ),
                        ),
                    ),
                    class_name="flex justify-center mt-12",
                ),
                class_name="relative",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="py-20 bg-[#F5E4C3]/20",
    )


def home_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        hero_section(),
        features_section(),
        tours_section(),
        testimonials_section(),
        footer(),
        class_name="font-sans bg-white w-full overflow-x-hidden",
    )