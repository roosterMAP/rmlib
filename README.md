# rmlib

`rmlib` is a shared library for the `rmKit` and `rmKit_uv` Blender addons. It provides reusable utilities and classes to simplify addon development.

## Features
- Utility functions for working with Blender data.
- Shared classes for managing element sets.
- General math and helper functions.

## Installation
1. Download the `rmlib` folder.
2. Place it in Blender's `scripts/modules` directory.

## Usage
Import `rmlib` in your addon:
```python
from rmlib import elem_set, util