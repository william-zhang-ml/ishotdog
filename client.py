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
        """Handle button press, either submit an image or reset. """

        if self._camera.play:
            self._button.disabled = True             # disable user input
            self._camera.play = False                # pause camera
            pass                                     # submit image and wait
            self._label.text = 'HOTDOG'              # show result
            self._label.color = (0, 1, 0, 1)         # show result
            self._button.text = 'Reset!'             # inform user
            self._button.disabled = False            # enable user input
        else:
            self._button.disabled = True             # disable user input
            self._camera.play = True                 # unpause camera
            self._label.text = 'Take a picture!'     # reset prompt
            self._label.color = (1, 1, 1, 1)         # reset prompt
            self._button.text = 'Is this a hotdog?'  # inform user
            self._button.disabled = False            # enable user input

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
