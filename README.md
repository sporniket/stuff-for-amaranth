# Stuff for Amaranth by Sporniket

> [WARNING] Please read carefully this note before using this project. It contains important facts.

Content

1. What is **Stuff for Amaranth by Sporniket**, and when to use it ?
2. What should you know before using **Stuff for Amaranth by Sporniket** ?
3. How to use **Stuff for Amaranth by Sporniket** ?
4. Known issues
5. Miscellanous

## 1. What is **Stuff for Amaranth by Sporniket**, and when to use it ?

**Stuff for Amaranth by Sporniket** is my collection of essential code written using the **Amaranth hdl**.

[Amaranth HDL, previously nMigen](https://github.com/amaranth-lang/amaranth) is a python library to generate an abstract syntax tree of an hardware design, in order to e.g. configure a supported FPGA.

**Stuff for Amaranth by Sporniket** aims at :

* Providing some reusable basic design to build more complex systems.
* Providing a helper library to —hopefully— write formal verification tests more easily.
* Serves as dependency manager toward the mains amaranth libraries (`amaranth` and `amaranth-boards`) by the way of transitive dependencies.


### Licence
 **Stuff for Amaranth by Sporniket** is free software: you can redistribute it and/or modify it under the terms of the
 GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your
 option) any later version.

 **Stuff for Amaranth by Sporniket** is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for
 more details.

 You should have received a copy of the GNU Lesser General Public License along with **Stuff for Amaranth by Sporniket**.
 If not, see http://www.gnu.org/licenses/ .


## 2. What should you know before using **Stuff for Amaranth by Sporniket** ?

**Stuff for Amaranth by Sporniket** requires a set of tools to work :

* **Python 3.10 or later, pip and pdm**.

* Amaranth main libraries.
  * [amaranth](https://github.com/amaranth-lang/amaranth).
  * [amaranth-boards](https://github.com/amaranth-lang/amaranth-boards).

* Formal verification testing requires [Yices2](https://yices.csl.sri.com/).

> Do not use **Stuff for Amaranth by Sporniket** if this project is not suitable for your project

## 3. How to use **Stuff for Amaranth by Sporniket** ?

### As a dependency in your python project

> It is expected that a compatible version of python is used

In your project descriptor (`pyproject.toml` file), add a dependency pointing to this repository, optionnally with a specific tag (better for build stability, requires manual updating), e.g.

    'stuff-for-amaranth-by-sporniket @ git+https://github.com/sporniket/stuff-for-amaranth@v0.0.4',

You MAY specify a commit hash instead (e.g. latest before a change breaking your project), e.g.

    'stuff-for-amaranth-by-sporniket @ git+https://github.com/sporniket/stuff-for-amaranth@a738ace61839390dfdaa8ef06baa17d32482d771',

A build tool like [pdm](https://pdm.fming.dev) can be used to manage dependencies in a normalized manner. 
After updating the dependency specification in the pyproject.toml, use `pdm update stuff-for-amaranth-by-sporniket`.
You MAY need to use `pdm update amaranth` and `pdm update amaranth-boards` afterwards.

### Working on the sources

> It is expected that a compatible version of python is used, and that pip and pdm are also installed.

	git clone https://github.com/sporniket/stuff-for-amaranth.git
	cd stuff-for-amaranth
    python3 -m pdm sync
    python3 -m pdm ci

## 4. Known issues
See the [project issues](https://github.com/sporniket/stuff-for-amaranth/issues) page.

## 5. Miscellanous

### Report issues
Use the [project issues](https://github.com/sporniket/stuff-for-amaranth/issues) page.
