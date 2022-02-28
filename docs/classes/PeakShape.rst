PeakShape
=========

.. py:class:: PeakShape


   Bases: :py:class:`object`


Cython implementation of _PeakShape


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakShape.html


 Internal representation of a peak shape (used by the PeakPickerCWT)
 -----
 It defines an asymmetric Lorentzian and asymmetric hyperbolic squared secan function




.. py:attribute:: PeakShape.PeakShape_Type


alias of :py:class:`pyopenms.pyopenms_7.__PeakShape_Type`


.. py:attribute:: PeakShape.area




.. py:method:: PeakShape.getFWHM


Cython signature: double getFWHM()
Estimates the full width at half maximum




.. py:method:: PeakShape.getSymmetricMeasure


Cython signature: double getSymmetricMeasure()
Computes symmetry measure of the peak shape, which is corresponds to the ratio of the left and right width parameters




.. py:attribute:: PeakShape.height




.. py:method:: PeakShape.iteratorsSet


Cython signature: bool iteratorsSet()
Check if endpoint iterators are provided




.. py:attribute:: PeakShape.left_width




.. py:attribute:: PeakShape.mz_position




.. py:attribute:: PeakShape.r_value




.. py:attribute:: PeakShape.right_width




.. py:attribute:: PeakShape.signal_to_noise




.. py:attribute:: PeakShape.type




.. py:attribute:: PeakSpectrum


alias of :py:class:`pyopenms.pyopenms_7.MSSpectrum`


