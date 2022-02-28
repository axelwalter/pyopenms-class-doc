ConvexHull2D
============

.. py:class:: ConvexHull2D


   Bases: :py:class:`object`


Cython implementation of _ConvexHull2D


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ConvexHull2D.html




.. py:method:: ConvexHull2D.addPoint


Cython signature: bool addPoint(DPosition2 point)
Adds a point to the hull if it is not already contained. Returns if the point was added. This will trigger recomputation of the outer hull points (thus points set with setHullPoints() will be lost)




.. py:method:: ConvexHull2D.addPointXY


Parameters:
x (double)
y (double)




.. py:method:: ConvexHull2D.addPoints


Cython signature: void addPoints(libcpp_vector[DPosition2] points)
Adds points to the hull if it is not already contained. This will trigger recomputation of the outer hull points (thus points set with setHullPoints() will be lost)




.. py:method:: ConvexHull2D.addPointsNPY


Parameters:
points (np.ndarray[np.float32_t, ndim=2])




.. py:method:: ConvexHull2D.clear


Cython signature: void clear()
Removes all points




.. py:method:: ConvexHull2D.compress


Cython signature: size_t compress()
Allows to reduce the disk/memory footprint of a hull




.. py:method:: ConvexHull2D.encloses


Cython signature: bool encloses(DPosition2)
Returns if the `point` lies in the feature hull




.. py:method:: ConvexHull2D.enclosesXY


Parameters:
x (float)
y (float)


Returns:
int




.. py:method:: ConvexHull2D.expandToBoundingBox


Cython signature: void expandToBoundingBox()
Expand a convex hull to its bounding box.




.. py:method:: ConvexHull2D.getBoundingBox


Cython signature: DBoundingBox2 getBoundingBox()
Returns the bounding box of the feature hull points




.. py:method:: ConvexHull2D.getBoundingBox2D


Returns:
((double,double),(double,double))




.. py:method:: ConvexHull2D.getHullPoints


Cython signature: libcpp_vector[DPosition2] getHullPoints()
Accessor for the outer points




.. py:method:: ConvexHull2D.getHullPointsNPY


Returns:
result (np.ndarray[np.float32_t, ndim=2])




.. py:method:: ConvexHull2D.setHullPoints


Cython signature: void setHullPoints(libcpp_vector[DPosition2])
Accessor for the outer(!) points (no checking is performed if this is actually a convex hull)




.. py:method:: ConvexHull2D.setHullPointsNPY


Parameters:
points (np.ndarray[np.float32_t, ndim=2])




