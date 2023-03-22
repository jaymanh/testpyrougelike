from typing import Optional

import tcod.event # type: ignore

from actions import Action, BumpAction, EscapeAction 

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.KeyDown) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = NotImplemented

        key = event.sym

        if key == tcod.event.K_UP:
            action = BumpAction()
            action.dx, action.dy = 0, -1
        elif key == tcod.event.K_DOWN:
            action = BumpAction()
            action.dx, action.dy = 0, 1
        elif key == tcod.event.K_LEFT:
            action = BumpAction()
            action.dx, action.dy = -1, 0
        elif key == tcod.event.K_RIGHT:
            action = BumpAction()
            action.dx, action.dy = 1, 0
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        return action
