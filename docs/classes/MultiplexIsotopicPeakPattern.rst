MultiplexIsotopicPeakPattern
============================

.. py:class:: MultiplexIsotopicPeakPattern


   Bases: :py:class:`object`


Cython implementation of _MultiplexIsotopicPeakPattern


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MultiplexIsotopicPeakPattern.html




.. py:method:: MultiplexIsotopicPeakPattern.getCharge


Cython signature: int getCharge()
Returns charge




.. py:method:: MultiplexIsotopicPeakPattern.getMZShiftAt


Cython signature: double getMZShiftAt(int i)
Returns m/z shift at position i




.. py:method:: MultiplexIsotopicPeakPattern.getMZShiftCount


Cython signature: unsigned int getMZShiftCount()
Returns number of m/z shifts




.. py:method:: MultiplexIsotopicPeakPattern.getMassShiftAt


Cython signature: double getMassShiftAt(int i)
Returns mass shift at position i




.. py:method:: MultiplexIsotopicPeakPattern.getMassShiftCount


Cython signature: unsigned int getMassShiftCount()
Returns number of mass shifts i.e. the number of peptides in the multiplet




.. py:method:: MultiplexIsotopicPeakPattern.getMassShiftIndex


Cython signature: int getMassShiftIndex()
Returns mass shift index




.. py:method:: MultiplexIsotopicPeakPattern.getMassShifts


Cython signature: MultiplexDeltaMasses getMassShifts()
Returns mass shifts




.. py:method:: MultiplexIsotopicPeakPattern.getPeaksPerPeptide


Cython signature: int getPeaksPerPeptide()
Returns peaks per peptide




