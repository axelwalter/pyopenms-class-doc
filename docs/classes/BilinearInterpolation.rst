BilinearInterpolation
=====================

.. py:class:: BilinearInterpolation


   Bases: :py:class:`object`


Cython implementation of _BilinearInterpolation[double,double]


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::Math_1_1BilinearInterpolation[double,double].html




.. py:method:: BilinearInterpolation.addValue


Cython signature: void addValue(double arg_pos_0, double arg_pos_1, double arg_value)
Performs bilinear resampling. The arg_value is split up and added to the data points around arg_pos. ("forward resampling")




.. py:method:: BilinearInterpolation.empty


Cython signature: bool empty()




.. py:method:: BilinearInterpolation.getData


Cython signature: MatrixDouble getData()




.. py:method:: BilinearInterpolation.getInsideReferencePoint_0


Cython signature: double getInsideReferencePoint_0()




.. py:method:: BilinearInterpolation.getInsideReferencePoint_1


Cython signature: double getInsideReferencePoint_1()




.. py:method:: BilinearInterpolation.getOffset_0


Cython signature: double getOffset_0()
Accessor. "Offset" is the point (in "outside" units) which corresponds to "Data(0,0)"




.. py:method:: BilinearInterpolation.getOffset_1


Cython signature: double getOffset_1()
Accessor. "Offset" is the point (in "outside" units) which corresponds to "Data(0,0)"




.. py:method:: BilinearInterpolation.getOutsideReferencePoint_0


Cython signature: double getOutsideReferencePoint_0()




.. py:method:: BilinearInterpolation.getOutsideReferencePoint_1


Cython signature: double getOutsideReferencePoint_1()




.. py:method:: BilinearInterpolation.getScale_0


Cython signature: double getScale_0()




.. py:method:: BilinearInterpolation.getScale_1


Cython signature: double getScale_1()




.. py:method:: BilinearInterpolation.index2key_0


Cython signature: double index2key_0(double pos)
The transformation from "inside" to "outside" coordinates




.. py:method:: BilinearInterpolation.index2key_1


Cython signature: double index2key_1(double pos)
The transformation from "inside" to "outside" coordinates




.. py:method:: BilinearInterpolation.key2index_0


Cython signature: double key2index_0(double pos)
The transformation from "outside" to "inside" coordinates




.. py:method:: BilinearInterpolation.key2index_1


Cython signature: double key2index_1(double pos)
The transformation from "outside" to "inside" coordinates




.. py:method:: BilinearInterpolation.setData


Cython signature: void setData(MatrixDouble & data)
Assigns data to the internal random access container storing the data. SourceContainer must be assignable to ContainerType




.. py:method:: BilinearInterpolation.setMapping_0


- Cython signature: void setMapping_0(double & scale, double & inside, double & outside)
- Cython signature: void setMapping_0(double & inside_low, double & outside_low, double & inside_high, double & outside_high)




.. py:method:: BilinearInterpolation.setMapping_1


- Cython signature: void setMapping_1(double & scale, double & inside, double & outside)
- Cython signature: void setMapping_1(double & inside_low, double & outside_low, double & inside_high, double & outside_high)




.. py:method:: BilinearInterpolation.setOffset_0


Cython signature: void setOffset_0(double & offset)




.. py:method:: BilinearInterpolation.setOffset_1


Cython signature: void setOffset_1(double & offset)




.. py:method:: BilinearInterpolation.setScale_0


Cython signature: void setScale_0(double & scale)




.. py:method:: BilinearInterpolation.setScale_1


Cython signature: void setScale_1(double & scale)




.. py:method:: BilinearInterpolation.supportMax_0


Cython signature: double supportMax_0()
Upper boundary of the support, in "outside" coordinates




.. py:method:: BilinearInterpolation.supportMax_1


Cython signature: double supportMax_1()
Upper boundary of the support, in "outside" coordinates




.. py:method:: BilinearInterpolation.supportMin_0


Cython signature: double supportMin_0()
Lower boundary of the support, in "outside" coordinates




.. py:method:: BilinearInterpolation.supportMin_1


Cython signature: double supportMin_1()
Lower boundary of the support, in "outside" coordinates




.. py:method:: BilinearInterpolation.value


Cython signature: double value(double arg_pos_0, double arg_pos_1)




