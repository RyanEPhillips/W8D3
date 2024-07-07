# Shape Class Hierarchy

This Python project demonstrates a class hierarchy for representing different shapes using object-oriented programming principles. The project includes a base `Shape` class and derived classes `Circle`, `Rectangle`, and `Triangle`. Each shape class implements methods to calculate its area and perimeter, showcasing polymorphism and inheritance.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Shape Classes](#shape-classes)
  - [Shape](#shape)
  - [Circle](#circle)
  - [Rectangle](#rectangle)
  - [Triangle](#triangle)
- [Running the Code](#running-the-code)
- [Contributing](#contributing)
- [License](#license)

## Overview

The project focuses on creating a class hierarchy where the base `Shape` class defines common attributes like `color` and declares abstract methods for calculating `area` and `perimeter`. The derived classes (`Circle`, `Rectangle`, `Triangle`) inherit from `Shape` and provide shape-specific implementations for these methods.

## Project Structure

The project consists of the following files:
- `shapes.py`: Contains the implementation of the `Shape`, `Circle`, `Rectangle`, and `Triangle` classes.
- `README.md`: This file, providing an overview of the project.

## Usage

The primary usage of this project is to demonstrate:
- **Inheritance**: Derived classes inherit attributes and methods from the base class (`Shape`).
- **Polymorphism**: Different shapes (`Circle`, `Rectangle`, `Triangle`) are handled uniformly through the use of overridden methods (`calculate_area()` and `calculate_perimeter()`).
- **Object-oriented principles**: Encapsulation, inheritance, and polymorphism are utilized to create a modular and extensible shape representation.

## Shape Classes

### Shape

The `Shape` class serves as the base class for all shapes. It includes:
- `color`: A string representing the color of the shape.
- Abstract methods:
  - `calculate_area()`: To be overridden by derived classes to calculate the area of the shape.
  - `calculate_perimeter()`: To be overridden by derived classes to calculate the perimeter of the shape.

### Circle

The `Circle` class inherits from `Shape` and includes:
- `radius`: A numeric attribute representing the radius of the circle.
- Methods:
  - `calculate_area()`: Computes the area of the circle using the formula π * r^2.
  - `calculate_perimeter()`: Computes the perimeter of the circle using the formula 2 * π * r.
  - Additional methods: `get_radius()`, `set_radius()`: Getter and setter methods for the radius attribute.

### Rectangle

The `Rectangle` class inherits from `Shape` and includes:
- `width` and `height`: Numeric attributes representing the dimensions of the rectangle.
- Methods:
  - `calculate_area()`: Computes the area of the rectangle using the formula width * height.
  - `calculate_perimeter()`: Computes the perimeter of the rectangle using the formula 2 * (width + height).

### Triangle

The `Triangle` class inherits from `Shape` and includes:
- `side1`, `side2`, `side3`: Numeric attributes representing the sides of the triangle.
- Methods:
  - `calculate_area()`: Computes the area of the triangle using Heron's formula.
  - `calculate_perimeter()`: Computes the perimeter of the triangle by summing its sides.

## Running the Code

To run the code:
1. Ensure you have Python installed on your system.
2. Clone or download the `shapes.py` file to your local machine.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `shapes.py`.
5. Run the file using the command: `python shapes.py`.

## Resources
ChatGPT helped show how to preform proper math functions in code for measurments and import.  Also showed how to initialize main class ABC and @abstractmethod. I was having issues with that part.