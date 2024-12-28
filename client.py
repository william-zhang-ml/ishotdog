"""
App for asking server if something is a hotdog or not.
"""
import json
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
            self._button.disabled = True  # disable user input
            self._camera.play = False     # pause camera

            # prep request body
            req_body = {
                'mode': self._camera.texture.colorfmt.upper(),
                'size': self._camera.texture.size,
                'data': self._camera.texture.pixels.hex()
            }

            # submit image and wait
            req = UrlRequest(
                'http://127.0.0.1:8000/score/',
                req_headers={'Content-Type': 'application/json'},
                req_body=json.dumps(req_body),
                on_success=self._handle_response  # show result
            )
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
        ishotdog: bool
    ) -> None:
        """Process server response to a submitted image.

        Args:
            req (UrlRequest): HTTP(S) request
            ishotdog (bool): hotdog or not hotdog
        """
        if ishotdog:
            self._label.text = 'HOTDOG'
            self._label.color = (0, 1, 0, 1)
        else:
            self._label.text = 'NOT HOTDOG'
            self._label.color = (1, 0, 0, 1)
        self._button.text = 'Reset!'   # inform user
        self._button.disabled = False  # enable user input


class ClientApp(App):
    """Main application class. """
    def build(self) -> None:
        return UserInterface()


if __name__ == '__main__':
    ClientApp().run()
