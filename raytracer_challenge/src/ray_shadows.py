"""TODO"""
from __future__ import annotations

import sys
sys.path.append('raytracer_challenge')

from imports import *

def is_shadowed(world: World, point: point) -> bool:
    """_summary_

    Args:
        world (World): _description_
        point (point): _description_

    Returns:
        bool: _description_
    """
    
    # Measure the distance from point to light source
    v = world.light.position - point
    distance = v.magnitude()
    direction = v.normal()
    
    # Create a ray from point toward the light source
    r = Ray(point, direction)
    # Intersect world with ray
    intersections = intersect_world(world, r)
    
    # Check if there was a hit, and whether t is less than distance
    h = hit(intersections)
    if h and h.t> 0 and h.t < distance:
        return True
    
    return False
