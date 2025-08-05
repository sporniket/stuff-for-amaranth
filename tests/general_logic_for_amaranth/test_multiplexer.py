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
from amaranth.hdl import Signal, unsigned

### amarant-stuff deps
from general_logic_for_amaranth import Multiplexer
from testing_for_amaranth import Story, TestSuiteRunner


def test_Multiplexer():
    sourceValues = [1, 4, 7, 2, 5]

    TestSuiteRunner(
        lambda: Multiplexer(inputs=[Signal(3, init=i) for i in sourceValues]),
        lambda dut, clockDomain: {
            "rst": clockDomain.rst,
            "selector": dut.selector,
            "dataOut": dut.dataOut,
        }
        | {f"dataIn{i}": s for i, s in enumerate(dut.dataIn)},
        [
            Story(
                "it should output selected input",
                {
                    "rst": [1, 0, 0, 0] + [0, 0, 0],
                    "dataIn0": [1, 1, 1, 1] + [1, 1, 1],
                    "dataIn1": [4, 4, 4, 4] + [4, 4, 4],
                    "dataIn2": [7, 7, 7, 7] + [7, 7, 7],
                    "dataIn3": [2, 2, 2, 2] + [2, 2, 2],
                    "dataIn4": [5, 5, 5, 5] + [5, 5, 5],
                    "selector": [0, 0, 2, 4] + [1, 3, 4],
                    "dataOut": [0, 1, 7, 5] + [4, 2, 5],
                },
                given=["rst", "selector"]
                + [f"dataIn{i}" for i in range(len(sourceValues))],
            )
        ],
    ).run()
