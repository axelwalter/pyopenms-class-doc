HMMState
========

.. py:class:: HMMState


   Bases: :py:class:`object`


Cython implementation of _HMMState


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1HMMState.html




.. py:method:: HMMState.addPredecessorState


Cython signature: void addPredecessorState(HMMState * state)
Adds the given predecessor state to the list




.. py:method:: HMMState.addSuccessorState


Cython signature: void addSuccessorState(HMMState * state)
Add the given successor state to the list




.. py:method:: HMMState.deletePredecessorState


Cython signature: void deletePredecessorState(HMMState * state)
Deletes the given predecessor state from the list




.. py:method:: HMMState.deleteSuccessorState


Cython signature: void deleteSuccessorState(HMMState * state)
Deletes the given successor state from the list




.. py:method:: HMMState.getName


Cython signature: String getName()
Returns the name of the state




.. py:method:: HMMState.getPredecessorStates


Cython signature: libcpp_set[HMMState *] getPredecessorStates()
Returns the predecessor states of the state




.. py:method:: HMMState.getSuccessorStates


Cython signature: libcpp_set[HMMState *] getSuccessorStates()
Returns the successor states of the state




.. py:method:: HMMState.isHidden


Cython signature: bool isHidden()
Returns true if the state is hidden




.. py:method:: HMMState.setHidden


Cython signature: void setHidden(bool hidden)
Sets the hidden property to the state




.. py:method:: HMMState.setName


Cython signature: void setName(const String & name)
Sets the name of the state




