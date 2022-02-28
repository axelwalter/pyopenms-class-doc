ParamValue
==========

.. py:class:: ParamValue


   Bases: :py:class:`object`


Cython implementation of _ParamValue


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ParamValue.html


 Class to hold strings, numeric values, vectors of strings and vectors of numeric values using the stl types
 -----
 - To choose one of these types, just use the appropriate constructor
 - Automatic conversion is supported and throws Exceptions in case of invalid conversions
 - An empty object is created with the default constructor




.. py:method:: ParamValue.isEmpty


Cython signature: int isEmpty()
Test if the value is empty




.. py:method:: ParamValue.toBool


Cython signature: bool toBool()
Converts the strings 'true' and 'false' to a bool




.. py:method:: ParamValue.toDouble




.. py:method:: ParamValue.toDoubleVector


Cython signature: libcpp_vector[double] toDoubleVector()
Explicitly convert ParamValue to DoubleList




.. py:method:: ParamValue.toInt




.. py:method:: ParamValue.toIntVector


Cython signature: libcpp_vector[int] toIntVector()
Explicitly convert ParamValue to IntList




.. py:method:: ParamValue.toString




.. py:method:: ParamValue.toStringVector


Cython signature: libcpp_vector[libcpp_utf8_string] toStringVector()
Explicitly convert ParamValue to string vector




.. py:method:: ParamValue.valueType


Cython signature: ValueType valueType()




