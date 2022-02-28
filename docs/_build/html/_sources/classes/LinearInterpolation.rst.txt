LinearInterpolation
===================

.. py:class:: LinearInterpolation


   Bases: :py:class:`object`


Cython implementation of _LinearInterpolation[double,double]


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::Math_1_1LinearInterpolation[double,double].html


 Provides access to linearly interpolated values (and
 derivatives) from discrete data points.  Values beyond the given range
 of data points are implicitly taken as zero.
 -----
 The input is just a vector of values ("Data").  These are interpreted
 as the y-coordinates at the x-coordinate positions 0,...,data_.size-1.
 -----
 The interpolated data can also be scaled and shifted in
 the x-dimension by an affine mapping.  That is, we have "inside" and
 "outside" x-coordinates.  The affine mapping can be specified in two
 ways:
 - using setScale() and setOffset(),
 - using setMapping()
 -----
 By default the identity mapping (scale=1, offset=0) is used.
 -----
 Using the value() and derivative() methods you can sample linearly
 interpolated values for a given x-coordinate position of the data and
 the derivative of the data




.. py:method:: LinearInterpolation.addValue


Cython signature: void addValue(double arg_pos, double arg_value)
Performs linear resampling. The `arg_value` is split up and added to the data points around `arg_pos`




.. py:method:: LinearInterpolation.derivative


Cython signature: double derivative(double arg_pos)
Returns the interpolated derivative




.. py:method:: LinearInterpolation.empty


Cython signature: bool empty()
Returns `true` if getData() is empty




.. py:method:: LinearInterpolation.getData


Cython signature: libcpp_vector[double] getData()
Returns the internal random access container from which interpolated values are being sampled




.. py:method:: LinearInterpolation.getInsideReferencePoint


Cython signature: double getInsideReferencePoint()




.. py:method:: LinearInterpolation.getOffset


Cython signature: double getOffset()
"Offset" is the point (in "outside" units) which corresponds to "Data[0]"




.. py:method:: LinearInterpolation.getOutsideReferencePoint


Cython signature: double getOutsideReferencePoint()




.. py:method:: LinearInterpolation.getScale


Cython signature: double getScale()
"Scale" is the difference (in "outside" units) between consecutive entries in "Data"




.. py:method:: LinearInterpolation.index2key


Cython signature: double index2key(double pos)
The transformation from "inside" to "outside" coordinates




.. py:method:: LinearInterpolation.key2index


Cython signature: double key2index(double pos)
The transformation from "outside" to "inside" coordinates




.. py:method:: LinearInterpolation.setData


Cython signature: void setData(libcpp_vector[double] & data)
Assigns data to the internal random access container from which interpolated values are being sampled




.. py:method:: LinearInterpolation.setMapping


- Cython signature: void setMapping(double & scale, double & inside, double & outside)
- Cython signature: void setMapping(double & inside_low, double & outside_low, double & inside_high, double & outside_high)




.. py:method:: LinearInterpolation.setOffset


Cython signature: void setOffset(double & offset)
"Offset" is the point (in "outside" units) which corresponds to "Data[0]"




.. py:method:: LinearInterpolation.setScale


Cython signature: void setScale(double & scale)
"Scale" is the difference (in "outside" units) between consecutive entries in "Data"




.. py:method:: LinearInterpolation.supportMax


Cython signature: double supportMax()




.. py:method:: LinearInterpolation.supportMin


Cython signature: double supportMin()




.. py:method:: LinearInterpolation.value


Cython signature: double value(double arg_pos)
Returns the interpolated value




