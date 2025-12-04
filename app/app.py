import reflex as rx
from app.pages.home import home_page
from app.pages.tours import tours_page
from app.pages.tour_details import tour_details_page
from app.pages.about import about_page
from app.pages.community import community_page
from app.pages.contact import contact_page
from app.states.home_state import HomeState
from app.states.tours_state import ToursState


def index() -> rx.Component:
    return rx.el.div(
        home_page(), on_mount=HomeState.start_testimonial_carousel, class_name="w-full"
    )


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap",
        "/animations.css",
    ],
    head_components=[
        rx.el.title("Mombasa Tours | Premium Coastal Experiences"),
        rx.el.meta(
            name="description",
            content="Discover the beauty of Mombasa with our premium tours.",
        ),
        rx.el.script(src="/observer.js"),
    ],
    theme=rx.theme(appearance="light"),
)
app.add_page(index, route="/")
app.add_page(tours_page, route="/tours")
app.add_page(tour_details_page, route="/tours/[id]")
app.add_page(about_page, route="/about")
app.add_page(community_page, route="/community")
app.add_page(contact_page, route="/contact")