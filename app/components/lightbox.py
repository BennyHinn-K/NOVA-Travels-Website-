import reflex as rx
from app.states.lightbox_state import LightboxState


def lightbox() -> rx.Component:
    return rx.cond(
        LightboxState.is_open,
        rx.el.div(
            rx.el.div(
                class_name="absolute inset-0 bg-black/90 backdrop-blur-sm transition-opacity",
                on_click=LightboxState.close_lightbox,
            ),
            rx.el.button(
                rx.icon("x", class_name="w-8 h-8 text-white"),
                class_name="absolute top-4 right-4 z-50 p-2 hover:bg-white/10 rounded-full transition-colors",
                on_click=LightboxState.close_lightbox,
            ),
            rx.el.button(
                rx.icon("chevron-left", class_name="w-10 h-10 text-white"),
                class_name="absolute left-4 top-1/2 -translate-y-1/2 z-50 p-2 hover:bg-white/10 rounded-full transition-colors",
                on_click=LightboxState.prev_image,
            ),
            rx.el.button(
                rx.icon("chevron-right", class_name="w-10 h-10 text-white"),
                class_name="absolute right-4 top-1/2 -translate-y-1/2 z-50 p-2 hover:bg-white/10 rounded-full transition-colors",
                on_click=LightboxState.next_image,
            ),
            rx.el.div(
                rx.image(
                    src=LightboxState.images[LightboxState.current_index],
                    class_name="max-h-[90vh] max-w-[90vw] object-contain rounded-lg shadow-2xl animate-fade-in",
                ),
                class_name="relative z-40 flex items-center justify-center w-full h-full p-4",
            ),
            class_name="fixed inset-0 z-[60] flex items-center justify-center animate-fade-in",
        ),
    )