""" entity """
from typing import List, Optional

from simpy import Environment, Resource, Process


class Entity:
    """flow object which is moved between components"""

    def __init__(self, env: Environment, name: str):
        self.env = env
        self.name = f"деталь_{name.split('_')[1]}"
        self.current_process: Optional[Process] = None

        # requested resources, info needed for release
        self.seized_resources: List[Resource] = []
        self.time_of_last_arrival: float = -1

        self.block_resource_request = None

        # optional special icon path, checked by process_visualizer
        self.process_animation_icon_path: Optional[str] = None
