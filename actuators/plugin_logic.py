# Copyright (c) 2024 Martín Abente Lahaye.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from gameeky.common.definitions import Action

from gameeky.plugins import Actuator as Plugin


class Actuator(Plugin):
    NAMES = ["Chicken", "Pig", "Sheep"]
    ended = False

    def tick(self) -> None:    
        if self.ended:
            return
        if not self.ready:
            return

        # Find how many farm animals are remaining
        remaining = [e for e in self.entity.scene.mutables if e.name in self.NAMES]

        if remaining:
            return super().tick()

        # Notify player that the game has ended
        for player in self.entity.scene.playables:
            player.tell("Game Over...")
            player.perform(Action.DESTROY)

        self.ended = True
