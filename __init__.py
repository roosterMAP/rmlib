"""
rmlib: A shared library for rmKit and rmKit_uv addons.
"""

bl_info = {
	"name": "rmlib",
	"author": "Your Name",
	"version": (1, 0, 0),
	"blender": (4, 4, 0),
	"location": "Shared Library",
	"description": "Shared utilities and classes for rmKit addons.",
	"warning": "",
	"wiki_url": "https://github.com/yourusername/rmlib",
	"tracker_url": "https://github.com/yourusername/rmlib/issues",
	"category": "Library",
}

from .item import rmMesh, iter_edit_meshes, iter_selected_meshes
from .elem_set import rmVertexSet, rmEdgeSet, rmPolygonSet, rmUVLoopSet, clear_tags
from .util import rmViewport, rmCustomOrientation, line2_dist, PlaneDistance, ReflectionMatrix, Angle2, AlmostEqual, AlmostEqual_v2, ProjectVector, CCW_Angle2D, HSV_to_RGB, EaseOutCircular, EaseInCircular, TriangleArea