import reflex as rx


def primary_button(text: str, **props) -> rx.Component:
    """A reusable primary button component."""
    return rx.el.button(
        text,
        class_name=f"\n            bg-[#015C92] dark:bg-[#3faae0] text-white font-semibold py-3 px-8 rounded-lg \n            hover:bg-[#014a75] dark:hover:bg-[#2d8ac0] hover:shadow-lg hover:-translate-y-0.5 \n            transition-all duration-300 active:scale-95\n            {props.get('class_name', '')}\n        ",
        **{k: v for k, v in props.items() if k != "class_name"},
    )


def secondary_button(text: str, **props) -> rx.Component:
    """A reusable secondary button component."""
    return rx.el.button(
        text,
        class_name=f"\n            bg-transparent border-2 border-white text-white font-semibold py-3 px-8 rounded-lg \n            hover:bg-white hover:text-[#015C92] hover:shadow-lg hover:-translate-y-0.5 \n            transition-all duration-300 active:scale-95\n            {props.get('class_name', '')}\n        ",
        **{k: v for k, v in props.items() if k != "class_name"},
    )


def section_header(title: str, subtitle: str = "") -> rx.Component:
    """A reusable section header with animated underline."""
    return rx.el.div(
        rx.el.h2(
            title,
            class_name="text-3xl md:text-4xl font-bold text-[#015C92] dark:text-[#3faae0] mb-4 relative inline-block",
        ),
        rx.el.div(class_name="h-1 w-24 bg-[#D4AF37] mx-auto rounded-full mb-6"),
        rx.cond(
            subtitle != "",
            rx.el.p(
                subtitle,
                class_name="text-gray-600 dark:text-gray-300 max-w-2xl mx-auto text-lg",
            ),
        ),
        class_name="text-center mb-12 md:mb-16",
    )