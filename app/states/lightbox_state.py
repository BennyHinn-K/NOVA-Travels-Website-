import reflex as rx


class LightboxState(rx.State):
    is_open: bool = False
    images: list[str] = []
    current_index: int = 0

    @rx.event
    def open_lightbox(self, images: list[str], index: int = 0):
        self.images = images
        self.current_index = index
        self.is_open = True

    @rx.event
    def close_lightbox(self):
        self.is_open = False

    @rx.event
    def next_image(self):
        self.current_index = (self.current_index + 1) % len(self.images)

    @rx.event
    def prev_image(self):
        self.current_index = (self.current_index - 1 + len(self.images)) % len(
            self.images
        )