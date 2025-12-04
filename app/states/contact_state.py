import reflex as rx
import asyncio


class ContactState(rx.State):
    name: str = ""
    email: str = ""
    phone: str = ""
    interest: str = "General Inquiry"
    message: str = ""
    is_loading: bool = False

    @rx.event
    def set_name(self, name: str):
        self.name = name

    @rx.event
    def set_email(self, email: str):
        self.email = email

    @rx.event
    def set_phone(self, phone: str):
        self.phone = phone

    @rx.event
    def set_interest(self, interest: str):
        self.interest = interest

    @rx.event
    def set_message(self, message: str):
        self.message = message

    @rx.event
    async def handle_submit(self):
        if not self.name or not self.email or (not self.message):
            yield rx.toast.error(
                "Please fill in all required fields.", position="bottom-right"
            )
            return
        self.is_loading = True
        yield
        await asyncio.sleep(1.5)
        self.is_loading = False
        yield rx.toast.success(
            "Message sent successfully! We'll get back to you soon.",
            position="bottom-right",
        )
        self.name = ""
        self.email = ""
        self.phone = ""
        self.interest = "General Inquiry"
        self.message = ""