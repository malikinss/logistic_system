from models import Truck, Package
from typing import List, Optional, Tuple


class WarehouseService:
    def __init__(self):
        self._trucks: dict[str, Truck] = {}
        self._packages: dict[str, Package] = {}

    def add_truck(self, length: float, width: float, height: float) -> str:
        """
        Creates a new truck and returns its unique ID.
        """
        truck = Truck(length, width, height)
        self._trucks[truck.id] = truck
        return truck.id

    def add_package(self, length: float, width: float, height: float) -> str:
        """
        Creates a new package and returns its unique ID.
        """
        package = Package(length, width, height)
        self._packages[package.id] = package
        return package.id

    def _validate_package_ids(self, package_ids: List[str]) -> List[Package]:
        if not package_ids:
            raise ValueError("No packages provided")
        if not all(pid in self._packages for pid in package_ids):
            raise ValueError("One or more package IDs are invalid")
        return [self._packages[pid] for pid in package_ids]

    def _try_assign_full(
        self, packages: List[Package], package_ids: List[str]
    ) -> Tuple[Optional[str], List[str], float]:
        total_volume = sum(p.volume for p in packages)
        best_truck_id = None
        best_fill_percentage = 0.0

        for truck_id, truck in self._trucks.items():
            truck_volume = truck.volume
            if total_volume <= truck_volume:
                fill_percentage = (total_volume / truck_volume) * 100
                filled_enough = fill_percentage >= 80
                if filled_enough and fill_percentage > best_fill_percentage:
                    best_truck_id = truck_id
                    best_fill_percentage = fill_percentage

        if best_truck_id:
            assigned_packages = package_ids
        else:
            assigned_packages = []

        return best_truck_id, assigned_packages, best_fill_percentage

    def _try_assign_partial(
        self, packages: List[Package]
    ) -> Tuple[Optional[str], List[str], float]:
        best_truck_id = None
        best_assigned_packages = []
        best_fill_percentage = 0.0

        for truck_id, truck in self._trucks.items():
            truck_volume = truck.volume
            current_volume = 0.0
            assigned_packages = []
            for pkg in packages:
                if current_volume + pkg.volume <= truck_volume:
                    current_volume += pkg.volume
                    assigned_packages.append(pkg.id)
            fill_percentage = (current_volume / truck_volume) * 100
            filled_enough = fill_percentage >= 80
            if filled_enough and fill_percentage > best_fill_percentage:
                best_truck_id = truck_id
                best_assigned_packages = assigned_packages
                best_fill_percentage = fill_percentage

        return best_truck_id, best_assigned_packages, best_fill_percentage

    def _update_truck_packages(self, truck_id: str, package_ids: List[str]):
        """
        Update the truck by adding the assigned packages.

        Args:
            truck_id (str): The truck's unique ID.
            package_ids (List[str]): List of assigned package IDs.
        """
        for pid in package_ids:
            self._trucks[truck_id].add_package(pid)

    def _get_result_msg(
        self,
        packages=None, tid=None,
        remain=None, percentage=None,
    ):
        """
        Generates a message about the truck assignment status.

        This method creates a message based on the provided information about
        truck assignment. It handles different cases: no truck found,
        packages assigned to a truck, or partial assignment with deferred
        packages.

        Args:
            packages (list, optional): List of package IDs that are assigned
                                       to the truck. Defaults to None.
            tid (str, optional): Truck ID. Defaults to None.
            remain (list, optional): List of deferred package IDs.
                                     Defaults to None.
            percentage (float, optional): Fill percentage of the truck after
                                          assignment. Defaults to None.

        Returns:
            Tuple[str, list, str]: A tuple containing the truck ID, the list
                                   of assigned packages, and the generated
                                   message.
        """
        if packages is None:
            packages = []

        msg = "No suitable truck found, deferring to next day"

        if tid:
            if packages and remain:
                msg = f"Assigned {len(packages)} packages to truck {tid}, "
                f"{len(remain)} deferred"

            elif percentage:
                msg = f"Assigned to truck {tid} with {percentage:.2f}% fill"

        return (tid, packages, msg)

    def assign_truck(
        self, package_ids: List[str]
    ) -> Tuple[Optional[str], List[str], str]:
        """
        Assign a truck to the given list of package IDs.

        Args:
            package_ids (List[str]): List of package IDs to be assigned to
                                     a truck.

        Returns:
            Tuple[Optional[str], List[str], str]: Truck ID, assigned
                                                  package IDs, and the result
                                                  message.
        """
        packages = self._validate_package_ids(package_ids)

        # Trying to assing full truck
        truck_id, assigned_packages, fill_percentage = self._try_assign_full(packages, package_ids)
        if truck_id:
            self._update_truck_packages(truck_id, assigned_packages)
            return self._get_result_msg(
                tid=truck_id,
                packages=assigned_packages,
                percentage=fill_percentage
            )

        # Trying to assing partial truck
        truck_id, assigned_packages, fill_percentage = self._try_assign_partial(packages)
        if truck_id:
            self._update_truck_packages(truck_id, assigned_packages)
            remaining_packages = [
                pid
                for pid in package_ids
                if pid not in assigned_packages
            ]
            return self._get_result_msg(
                tid=truck_id,
                packages=assigned_packages,
                remain=remaining_packages
            )

        return self._get_result_msg()
