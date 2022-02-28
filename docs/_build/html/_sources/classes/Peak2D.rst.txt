Peak2D
======

.. py:class:: Peak2D


   Bases: :py:class:`object`


Cython implementation of _Peak2D


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Peak2D.html


 A 2-dimensional raw data point or peak.
 -----
 This data structure is intended for continuous data or peak data.
 If you want to annotated single peaks with meta data, use RichPeak2D instead




.. py:method:: Peak2D.getIntensity


Cython signature: float getIntensity()
Returns the data point intensity (height)




.. py:method:: Peak2D.getMZ


Cython signature: double getMZ()
Returns the m/z coordinate (index 1)




.. py:method:: Peak2D.getRT


Cython signature: double getRT()
Returns the RT coordinate (index 0)




.. py:method:: Peak2D.setIntensity


Cython signature: void setIntensity(float)
Returns the data point intensity (height)




.. py:method:: Peak2D.setMZ


Cython signature: void setMZ(double)
Returns the m/z coordinate (index 1)




.. py:method:: Peak2D.setRT


Cython signature: void setRT(double)
Returns the RT coordinate (index 0)




