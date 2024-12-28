"""
App for asking server if something is a hotdog or not.
"""
from typing import Any
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class UserInterface(BoxLayout):
    """Interface for testing image sending and receiving. """
    _label = ObjectProperty(None)
    _camera = ObjectProperty(None)
    _button = ObjectProperty(None)

    def _handle_press(self) -> None:
        return

    def _handle_response(
        self,
        req: UrlRequest,
        result: Any
    ) -> None:
        """Process server response to a submitted image.

        Args:
            req (UrlRequest): HTTP(S) request
            result (Any): request result
        """
        return


class ClientApp(App):
    """Main application class. """
    def build(self) -> None:
        return UserInterface()


if __name__ == '__main__':
    ClientApp().run()
