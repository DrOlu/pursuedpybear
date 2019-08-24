import logging
import warnings
from typing import Callable

from ppb import events
from ppb_vector import Vector
from ppb.engine import GameEngine
from ppb.scenes import BaseScene
from ppb.sprites import BaseSprite as OldBaseSprite
from ppb.systems import Image
from ppb.systems import Sound

__all__ = (
    # Shortcuts
    'Vector', 'BaseScene', 'BaseSprite', 'Image', 'Sound', 'events',
    # Local stuff
    'run', 'make_engine',
)


class BaseSprite(OldBaseSprite):
    """
    A stub that raises a deprecation warning when a user uses
    ``ppb.BaseSprite.``
    """
    __warning = """Using ppb.BaseSprite is deprecated.
    
    You probably want ppb.Sprite. If you're wanting to use BaseSprite and
    mixins to change what features your sprites have, import
    ppb.sprites.BaseSprite.
    """

    def __init__(self, *args, **kwargs):
        warnings.warn(self.__warning, DeprecationWarning)


class Sprite(OldBaseSprite):
    """
    A stub pointing to current functionality under the new name.
    """


def _make_kwargs(setup, title, engine_opts):
    kwargs = {
        "resolution": (800, 600),
        "scene_kwargs": {
            "set_up": setup,
        },
        "window_title": title,
        **engine_opts
    }
    return kwargs


def run(setup: Callable[[BaseScene], None] = None, *, log_level=logging.WARNING,
        starting_scene=BaseScene, title="PursuedPyBear", **engine_opts):
    """
    Run a small game.

    The resolution will 800 pixels wide by 600 pixels tall.

    setup is a callable that accepts a scene and returns None.

    log_level let's you set the expected log level. Consider logging.DEBUG if
    something is behaving oddly.

    starting_scene let's you change the scene used by the engine.
    """
    logging.basicConfig(level=log_level)

    with make_engine(setup, starting_scene=starting_scene, title=title, **engine_opts) as eng:
        eng.run()


def make_engine(setup: Callable[[BaseScene], None] = None, *,
                starting_scene=BaseScene, title="PursedPyBear",
                **engine_opts):
    return GameEngine(starting_scene, **_make_kwargs(setup, title, engine_opts))
