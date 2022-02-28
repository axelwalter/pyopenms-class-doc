Gradient
========

.. py:class:: Gradient


   Bases: :py:class:`object`


Cython implementation of _Gradient


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Gradient.html




.. py:method:: Gradient.addEluent


Cython signature: void addEluent(String eluent)
Adds an eluent at the end of the eluent array




.. py:method:: Gradient.addTimepoint


Cython signature: void addTimepoint(int timepoint)
Adds a timepoint at the end of the timepoint array




.. py:method:: Gradient.clearEluents


Cython signature: void clearEluents()
Removes all eluents




.. py:method:: Gradient.clearPercentages


Cython signature: void clearPercentages()
Sets all percentage values to 0




.. py:method:: Gradient.clearTimepoints


Cython signature: void clearTimepoints()
Removes all timepoints




.. py:method:: Gradient.getEluents


Cython signature: libcpp_vector[String] getEluents()
Returns a reference to the list of eluents




.. py:method:: Gradient.getPercentage


Cython signature: unsigned int getPercentage(String eluent, int timepoint)
Returns a const reference to the percentages




.. py:method:: Gradient.getTimepoints


Cython signature: libcpp_vector[int] getTimepoints()
Returns a reference to the list of timepoints




.. py:method:: Gradient.isValid


Cython signature: bool isValid()
Checks if the percentages of all timepoints add up to 100%




.. py:method:: Gradient.setPercentage


Cython signature: void setPercentage(String eluent, int timepoint, unsigned int percentage)
Sets the percentage of 'eluent' at 'timepoint'




