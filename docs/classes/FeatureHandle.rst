FeatureHandle
=============

.. py:class:: FeatureHandle


   Bases: :py:class:`object`


Cython implementation of _FeatureHandle


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureHandle.html
 -- Inherits from ['Peak2D', 'UniqueIdInterface']




.. py:method:: FeatureHandle.clearUniqueId


Cython signature: size_t clearUniqueId()
Clear the unique id. The new unique id will be invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: FeatureHandle.ensureUniqueId


Cython signature: size_t ensureUniqueId()
Assigns a valid unique id, but only if the present one is invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: FeatureHandle.getCharge


Cython signature: int getCharge()
Returns the charge




.. py:method:: FeatureHandle.getIntensity


Cython signature: float getIntensity()
Returns the data point intensity (height)




.. py:method:: FeatureHandle.getMZ


Cython signature: double getMZ()
Returns the m/z coordinate (index 1)




.. py:method:: FeatureHandle.getMapIndex


Cython signature: uint64_t getMapIndex()
Returns the map index




.. py:method:: FeatureHandle.getRT


Cython signature: double getRT()
Returns the RT coordinate (index 0)




.. py:method:: FeatureHandle.getUniqueId


Cython signature: size_t getUniqueId()
Returns the unique id




.. py:method:: FeatureHandle.getWidth


Cython signature: float getWidth()
Returns the width (FWHM)




.. py:method:: FeatureHandle.hasInvalidUniqueId


Cython signature: size_t hasInvalidUniqueId()
Returns whether the unique id is invalid. Returns 1 if the unique id is invalid, 0 otherwise




.. py:method:: FeatureHandle.hasValidUniqueId


Cython signature: size_t hasValidUniqueId()
Returns whether the unique id is valid. Returns 1 if the unique id is valid, 0 otherwise




.. py:method:: FeatureHandle.isValid


Cython signature: bool isValid(uint64_t unique_id)
Returns true if the unique_id is valid, false otherwise




.. py:method:: FeatureHandle.setCharge


Cython signature: void setCharge(int charge)
Sets the charge




.. py:method:: FeatureHandle.setIntensity


Cython signature: void setIntensity(float)
Returns the data point intensity (height)




.. py:method:: FeatureHandle.setMZ


Cython signature: void setMZ(double)
Returns the m/z coordinate (index 1)




.. py:method:: FeatureHandle.setMapIndex


Cython signature: void setMapIndex(uint64_t i)
Sets the map index




.. py:method:: FeatureHandle.setRT


Cython signature: void setRT(double)
Returns the RT coordinate (index 0)




.. py:method:: FeatureHandle.setUniqueId


Cython signature: void setUniqueId(uint64_t rhs)
Assigns a new, valid unique id. Always returns 1




.. py:method:: FeatureHandle.setWidth


Cython signature: void setWidth(float width)
Sets the width (FWHM)




