IMSElement
==========

.. py:class:: IMSElement


   Bases: :py:class:`object`


Cython implementation of _IMSElement


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::ims::IMSElement_1_1IMSElement.html




.. py:method:: IMSElement.getAverageMass


Cython signature: double getAverageMass()
Gets element's average mass




.. py:method:: IMSElement.getIonMass


Cython signature: double getIonMass(int electrons_number)
Gets ion mass of element. By default ion lacks 1 electron, but this can be changed by setting other 'electrons_number'




.. py:method:: IMSElement.getIsotopeDistribution


Cython signature: IMSIsotopeDistribution getIsotopeDistribution()
Gets element's isotope distribution




.. py:method:: IMSElement.getMass


Cython signature: double getMass(int index)
Gets mass of element's isotope 'index'




.. py:method:: IMSElement.getName


Cython signature: libcpp_string getName()
Gets element's name




.. py:method:: IMSElement.getNominalMass


Cython signature: unsigned int getNominalMass()
Gets element's nominal mass




.. py:method:: IMSElement.getSequence


Cython signature: libcpp_string getSequence()
Gets element's sequence




.. py:method:: IMSElement.setIsotopeDistribution


Cython signature: void setIsotopeDistribution(IMSIsotopeDistribution & isotopes)
Sets element's isotope distribution




.. py:method:: IMSElement.setName


Cython signature: void setName(libcpp_string & name)
Sets element's name




.. py:method:: IMSElement.setSequence


Cython signature: void setSequence(libcpp_string & sequence)
Sets element's sequence




