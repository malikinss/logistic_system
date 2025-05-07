# Warehouse Management System - Backend Assignment

## Overview

This project implements a warehouse management system that handles the storage and assignment of trucks ands and packages, ensuring packages are assigned to trucks based on volume constraints (at least 80% truck capacity).
The system is built using Python and follows a modular, maintainable design with basic error handling.

## Setup Instructions

1. **Prerequisites**:

    - Python 3.9+
    - No additional libraries are required.

2. **Installation**:

    - Clone the repository or unzip the provided source code.
    - No external dependencies need to be installed.

3. **Running the Application**:

    - The core logic is implemented in the provided Python files.
    - To test the system, you can create an instance of `WarehouseService` and use its methods (`add_truck`, `add_package`, `assign_truck`) as shown below:

    ```python
    from warehouse_service import WarehouseService

    service = WarehouseService()
    truck_id = service.add_truck(10, 10, 10)
    package_id = service.add_package(2, 2, 2)
    truck_id, assigned_packages, message = service.assign_truck([package_id])
    print(message)
    ```

4. **File Structure**:
    - `warehouse_service.py`: Main service logic for managing trucks and packages.
    - `models/truck.py`: Truck model with dimension validation and package tracking.
    - `models/package.py`: Package model with dimension validation.
    - `utils/shape.py`: Base class for dimension validation and volume calculation.
    - `utils/auto_id_mixin.py`: Mixin for generating unique IDs.

## Data Model

-   **Truck**:
    -   Attributes: `id` (unique), `length`, `width`, `height`, `volume`, `packages` (list of package IDs).
    -   Constraints: Dimensions must be positive numbers.
    -   Volume is calculated as `length * width * height`.
-   **Package**:
    -   Attributes: `id` (unique), `length`, `width`, `height`, `volume`.
    -   Constraints: Dimensions must be positive numbers.
    -   Volume is calculated as `length * width * height`.
-   **Storage**:
    -   Trucks and packages are stored in in-memory dictionaries (`_trucks` and `_packages`) within `WarehouseService`.
-   **Error Handling**:
    -   Validates dimensions to ensure they are positive.
    -   Checks for invalid or missing package IDs.
    -   Handles cases where no trucks are available or packages exceed truck capacity.

## Truck Assignment Logic

-   **AssignTruck**:
    -   Takes a list of package IDs and attempts to assign them to a truck.
    -   First checks if the total package volume can fill a truck to at least 80% of its capacity.
    -   If not possible, tries to assign a subset of packages to maximize truck utilization (at least 80%).
    -   Packages that cannot be assigned are deferred to the next day.
    -   Returns the truck ID, assigned package IDs, and a descriptive message.
-   **Optimization**:
    -   Selects the truck with the highest fill percentage (closest to full) when multiple trucks meet the 80% threshold.
-   **Edge Cases**:
    -   No trucks available: Defers all packages.
    -   Empty package list: Raises an error.
    -   Invalid package IDs: Raises an error.
    -   Packages too large: Assigns as many as possible and defers the rest.

## System Architecture

-   **Components**:
    -   `WarehouseService`: Central service for managing trucks and packages, handling CRUD operations and assignment logic.
    -   `Truck` and `Package`: Data models with validation and utility methods.
    -   `Shape`: Abstract base class for shared dimension logic.
    -   `AutoIDMixin`: Utility for generating unique IDs.
-   **Flow**:
    1. Request received (e.g., add truck, add package, assign truck).
    2. Data validated (dimensions, IDs).
    3. Logic executed (e.g., volume calculation, truck selection).
    4. Response returned (e.g., truck ID, assigned packages, message).
-   **Diagram**:
    ```
    [Request] --> [WarehouseService]
                          |
                          v
            [Truck] <--> [Logic] <--> [Package]
                          |
                          v
                     [Response]
    ```

## Bonus: Bin Packing (Not Implemented)

Due to the 3-hour time constraint, the optional bin packing feature was not implemented. A potential approach would involve:

-   Using a First-Fit or Best-Fit heuristic to arrange packages in 3D space.
-   Checking physical constraints (e.g., package orientation, stacking).
-   Trade-offs: Increased complexity, longer runtime, but more accurate space utilization.

## Assumptions and Notes

-   **Simplifications**:
    -   In-memory storage (no database) for simplicity.
    -   Volume-based checks instead of full bin packing due to time constraints.
    -   No persistence between sessions.
    -   Unique IDs are simple incrementing integers.
-   **Edge Cases**:
    -   Handles negative or zero dimensions by raising errors.
    -   Defers packages if no suitable truck is found.
    -   Partial assignments are supported when total volume exceeds truck capacity.
-   **Resources Used**:
    -   Python documentation for standard library features.
    -   General knowledge of backend design and data modeling.
    -   No external libraries or APIs were used.

## Limitations

-   No REST API or CLI implemented due to time constraints.
-   Bin packing not implemented, relying on volume checks.
-   No unit tests included (would be added in a production environment).
-   Assumes all packages are available at the time of assignment.
