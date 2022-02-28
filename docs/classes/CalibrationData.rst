CalibrationData
===============

.. py:class:: CalibrationData


   Bases: :py:class:`object`


Cython implementation of _CalibrationData


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1CalibrationData.html




.. py:method:: CalibrationData.clear


Cython signature: void clear()
Remove all calibration points




.. py:method:: CalibrationData.empty


Cython signature: bool empty()
Returns `True` if there are no peaks




.. py:method:: CalibrationData.getError


Cython signature: double getError(size_t)
Retrieve the error for i'th calibrant in either ppm or Th (depending on usePPM())




.. py:method:: CalibrationData.getGroup


Cython signature: int getGroup(size_t i)
Retrieve the group of the i'th calibration point




.. py:method:: CalibrationData.getIntensity


Cython signature: double getIntensity(size_t)
Retrieve the intensity of the i'th calibration point




.. py:method:: CalibrationData.getMZ


Cython signature: double getMZ(size_t)
Retrieve the observed m/z of the i'th calibration point




.. py:method:: CalibrationData.getMetaValues


Cython signature: StringList getMetaValues()




.. py:method:: CalibrationData.getNrOfGroups


Cython signature: size_t getNrOfGroups()
Number of peak groups (can be 0)




.. py:method:: CalibrationData.getRT


Cython signature: double getRT(size_t)
Retrieve the observed RT of the i'th calibration point




.. py:method:: CalibrationData.getRefMZ


Cython signature: double getRefMZ(size_t)
Retrieve the theoretical m/z of the i'th calibration point




.. py:method:: CalibrationData.getWeight


Cython signature: double getWeight(size_t)
Retrieve the weight of the i'th calibration point




.. py:method:: CalibrationData.insertCalibrationPoint


Cython signature: void insertCalibrationPoint(double rt, double mz_obs, float intensity, double mz_ref, double weight, int group)




.. py:method:: CalibrationData.median


Cython signature: CalibrationData median(double, double)
Compute the median in the given RT range for every peak group




.. py:method:: CalibrationData.setUsePPM


Cython signature: void setUsePPM(bool)




.. py:method:: CalibrationData.size


Cython signature: size_t size()
Number of calibration points




.. py:method:: CalibrationData.sortByRT


Cython signature: void sortByRT()
Sort calibration points by RT, to allow for valid RT chunking




.. py:method:: CalibrationData.usePPM


Cython signature: bool usePPM()
Current error unit (ppm or Th)




