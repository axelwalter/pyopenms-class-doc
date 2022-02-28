Sample
======

.. py:class:: Sample


   Bases: :py:class:`object`


Cython implementation of _Sample


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Sample.html
 -- Inherits from ['MetaInfoInterface']




.. py:attribute:: Sample.SampleState


alias of :py:class:`pyopenms.pyopenms_2.__SampleState`


.. py:method:: Sample.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: Sample.countTreatments


Cython signature: int countTreatments()
Returns the number of sample treatments




.. py:method:: Sample.getComment


Cython signature: String getComment()
Returns the comment (default "")




.. py:method:: Sample.getConcentration


Cython signature: double getConcentration()
Returns the concentration (in g/l) (default 0.0)




.. py:method:: Sample.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: Sample.getMass


Cython signature: double getMass()
Returns the mass (in gram) (default 0.0)




.. py:method:: Sample.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: Sample.getName


Cython signature: String getName()




.. py:method:: Sample.getNumber


Cython signature: String getNumber()
Returns the sample number




.. py:method:: Sample.getOrganism


Cython signature: String getOrganism()




.. py:method:: Sample.getState


Cython signature: SampleState getState()
Returns the state of aggregation (default SAMPLENULL)




.. py:method:: Sample.getSubsamples


Cython signature: libcpp_vector[Sample] getSubsamples()
Returns a reference to the vector of subsamples that were combined to create this sample




.. py:method:: Sample.getVolume


Cython signature: double getVolume()
Returns the volume (in ml) (default 0.0)




.. py:method:: Sample.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: Sample.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: Sample.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: Sample.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: Sample.removeTreatment


Cython signature: void removeTreatment(unsigned int position)
Brief removes the sample treatment at the given position




.. py:method:: Sample.setComment


Cython signature: void setComment(String comment)
Sets the comment (may contain newline characters)




.. py:method:: Sample.setConcentration


Cython signature: void setConcentration(double concentration)
Sets the concentration (in g/l)




.. py:method:: Sample.setMass


Cython signature: void setMass(double mass)
Sets the mass (in gram)




.. py:method:: Sample.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: Sample.setName


Cython signature: void setName(String name)




.. py:method:: Sample.setNumber


Cython signature: void setNumber(String number)
Sets the sample number (e.g. sample ID)




.. py:method:: Sample.setOrganism


Cython signature: void setOrganism(String organism)




.. py:method:: Sample.setState


Cython signature: void setState(SampleState state)
Sets the state of aggregation




.. py:method:: Sample.setSubsamples


Cython signature: void setSubsamples(libcpp_vector[Sample] subsamples)
Sets the vector of subsamples that were combined to create this sample




.. py:method:: Sample.setVolume


Cython signature: void setVolume(double volume)
Sets the volume (in ml)




