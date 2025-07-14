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
from amaranth.build import Platform

### amarant-stuff deps
from general_logic_for_amaranth import StreamWidthReducerMsbFirst
from testing_for_amaranth import Story, TestSuiteRunner


def test_StreamWidthReducerMsbFirst():
    TestSuiteRunner(
        lambda: StreamWidthReducerMsbFirst(16, 12),
        lambda dut, clockDomain: {
            "rst": clockDomain.rst,
            # ...etc...
        },
        [
            Story(
                "should output adapted data",
                {
                    "rst": [1, 0, 0, 0] + [0, 0, 0, 0] + [0, 0, 0, 0] + [0, 0, 0],
                    "data_in": [0, 0x1234, 0x5678, 0x9ABC]
                    + [0x9ABC, 0x1234, 0x5678, 0x9ABC]
                    + [0x9ABC, 0x1234, 0x5678, 0x9ABC]
                    + [0x9ABC, 0x1234, 0x5678],
                    "data_in_read": [0, 1, 1, 0]
                    + [1, 1, 1, 0]
                    + [1, 1, 1, 0]
                    + [1, 1, 1],
                },
                given=["rst", "data_in"],
            ),
        ],
    ).run()
