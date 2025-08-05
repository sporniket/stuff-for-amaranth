"""
---
(c) 2022~2025 David SPORN
---
This is part of Sporniket's "Amaranth Stuff" project.

Sporniket's "Amaranth Stuff" project is free software: you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

Sporniket's "Amaranth Stuff" project is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.

See the GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License along with Sporniket's "Amaranth Stuff" project.
If not, see <https://www.gnu.org/licenses/>.
---
"""

### amaranth -- main deps
from amaranth.hdl import Elaboratable, Module, Signal, Const
from amaranth.build import Platform


class Multiplexer(Elaboratable):
    def __init__(self, *, inputs: list[Signal]):
        self._selector = Signal(range(len(inputs)))
        self._inputs = [i for i in inputs]
        self._output = Signal(inputs[0].shape())

    @property
    def selector(self) -> Signal:
        return self._selector

    @property
    def dataOut(self) -> Signal:
        return self._output

    @property
    def dataIn(self) -> list[Signal]:
        return self._inputs

    def ports(self) -> list[Signal]:
        return [self.selector] + self.dataIn + [self.dataOut]

    def elaborate(self, platform: Platform) -> Module:
        m = Module()

        for i, s in enumerate(self._inputs):
            with m.If(self._selector == i):
                m.d.sync += [self._output.eq(self._inputs[i])]

        return m
