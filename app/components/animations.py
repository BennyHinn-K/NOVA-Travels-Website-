import reflex as rx


def scroll_animation(children: rx.Component, delay: str = "0") -> rx.Component:
    """Wrapper for scroll-triggered animations."""
    return rx.el.div(children, class_name=f"scroll-animation delay-{delay}")