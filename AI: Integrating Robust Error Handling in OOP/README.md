# AI: Integrating Robust Error Handling in OOP

## Task Overview

This task applies AI-assisted scaffolding (via **Gemini Code Assist** in VS
Code) to add robust data validation and error handling to a simple
Object-Oriented `Product` / `InventoryManager` inventory system.

The starting code (`initial_code.py`) allowed `price` and `quantity` on a
`Product` to be set to any value at all — including negative numbers —
with no validation anywhere in the class. The goal was to close that gap
using Python's `@property` decorators and a custom exception, without
changing how `InventoryManager` is used from the outside.

## AI Tool Used

**Gemini Code Assist** (VS Code sidebar extension)

## Files

| File | Description |
| --- | --- |
| `initial_code.py` | The original, unvalidated `Product` / `InventoryManager` code provided as the task's starting point |
| `refactored_code.py` | The AI-refactored version, adding `@property` getters/setters for `price` and `quantity`, a custom `InvalidProductDataError` exception, and a test case demonstrating the validation |

## The AI Prompt

The following single prompt was given to Gemini Code Assist:

> Refactor the `Product` class below to add robust data validation and
> error handling, while keeping the rest of the `InventoryManager`
> behavior the same:
>
> 1. Define a custom exception class `InvalidProductDataError(Exception)`
>    to be raised whenever invalid data is assigned to a Product.
> 2. Convert `price` and `quantity` on the `Product` class into
>    properties using Python's `@property` decorator, each with a
>    corresponding setter method.
> 3. In the setters, `price` must be a non-negative number and `quantity`
>    must be a non-negative integer, otherwise raise
>    `InvalidProductDataError` with a clear message.
> 4. Update `__init__` to assign through the setters so validation runs
>    on construction too.
> 5. Do not change the public interface of `InventoryManager`.
>
> Also explain the design choices: why `@property` setters enforce
> encapsulation and prevent an invalid state, and why a custom exception
> improves data integrity over a generic exception or a silent failure.

## What Changed

- Added `InvalidProductDataError(Exception)`, a custom exception specific
  to bad product data.
- `price` and `quantity` are now private attributes (`__price`,
  `__quantity`) exposed only through `@property` getters and validated
  `@x.setter` methods.
- The `price` setter rejects anything that isn't a non-negative number;
  the `quantity` setter rejects anything that isn't a non-negative
  integer. Both raise `InvalidProductDataError` with a descriptive
  message instead of allowing the bad value through.
- `__init__` assigns via `self.price = price` / `self.quantity =
  quantity` (not directly to private fields), so validation runs the
  moment a `Product` is constructed — not just on later updates.
- `InventoryManager`'s public methods (`add_product`,
  `update_quantity`, `calculate_total_value`, `display_inventory`) are
  untouched. Because `update_quantity` sets `product.quantity = ...`,
  it now benefits from the validation automatically, with no changes
  to its own code.

## Test Case & Result

```python
print("\n--- Testing Invalid Input ---")
try:
    manager.inventory[0].quantity = -5
except Exception as e:
    print(f"Test result: {e}")
```

Output:

```
--- Testing Invalid Input ---
Test result: Invalid quantity: Quantity must be a non-negative integer, but got -5.
```

## Analysis

Before this refactor, `product.quantity = -5` was a plain attribute
assignment — Python has no way to stop it, so the object silently
entered an invalid state (negative stock), and any code relying on
`quantity` being sane (like `calculate_total_value`) would produce wrong
results without any warning.

With `@property`, `quantity` looks like a normal attribute from the
outside, but every assignment is intercepted by the `quantity.setter`
method first. This is the core of encapsulation: the class, not the
caller, decides what counts as a valid value, and that rule lives in
exactly one place no matter how many times or where in the codebase
`quantity` gets set. The setter always runs *before* the private
attribute is touched, so an invalid value can never reach
`self.__quantity` — the object either ends up valid, or the assignment
never completes.

Raising a custom `InvalidProductDataError` instead of a generic
`ValueError` (or worse, doing nothing) matters because it gives calling
code something specific to catch. A `try/except InvalidProductDataError`
can distinguish "you gave this inventory system bad product data" from
any other kind of failure in the program, and the message itself
(`"Quantity must be a non-negative integer, but got -5."`) tells the
caller exactly what went wrong and why — turning what would have been a
silent data-corruption bug into an immediate, catchable, descriptive
error.
