Tagging
=======

.. py:class:: Tagging


   Bases: :py:class:`object`


Cython implementation of _Tagging


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Tagging.html


 Meta information about tagging of a sample e.g. ICAT labeling
 -----
 Holds information about the mass difference between light and heavy tag
 All other relevant information is provided by Modification




.. py:method:: Tagging.getMassShift


Cython signature: double getMassShift()
Returns the mass difference between light and heavy variant (default is 0.0)




.. py:method:: Tagging.getVariant


Cython signature: IsotopeVariant getVariant()
Returns the isotope variant of the tag (default is LIGHT)




.. py:method:: Tagging.setMassShift


Cython signature: void setMassShift(double mass_shift)
Sets the mass difference between light and heavy variant




.. py:method:: Tagging.setVariant


Cython signature: void setVariant(IsotopeVariant variant)
Sets the isotope variant of the tag




