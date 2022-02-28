HiddenMarkovModel
=================

.. py:class:: HiddenMarkovModel


   Bases: :py:class:`object`


Cython implementation of _HiddenMarkovModel


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1HiddenMarkovModel.html




.. py:method:: HiddenMarkovModel.addNewState


- Cython signature: void addNewState(HMMState * state)
  Registers a new state to the HMM


- Cython signature: void addNewState(const String & name)
  Registers a new state to the HMM




.. py:method:: HiddenMarkovModel.addSynonymTransition


Cython signature: void addSynonymTransition(const String & name1, const String & name2, const String & synonym1, const String & synonym2)
Add a new synonym transition to the given state names




.. py:method:: HiddenMarkovModel.clear


Cython signature: void clear()
Clears all data




.. py:method:: HiddenMarkovModel.clearInitialTransitionProbabilities


Cython signature: void clearInitialTransitionProbabilities()
Clears the initial probabilities




.. py:method:: HiddenMarkovModel.clearTrainingEmissionProbabilities


Cython signature: void clearTrainingEmissionProbabilities()
Clear the emission probabilities




.. py:method:: HiddenMarkovModel.disableTransition


Cython signature: void disableTransition(const String & s1, const String & s2)
Disables the transition; deletes the nodes from the predecessor/successor list respectively




.. py:method:: HiddenMarkovModel.disableTransitions


Cython signature: void disableTransitions()
Disables all transitions




.. py:method:: HiddenMarkovModel.dump


Cython signature: void dump()
Writes some stats to cerr




.. py:method:: HiddenMarkovModel.enableTransition


Cython signature: void enableTransition(const String & s1, const String & s2)
Enables a transition; adds s1 to the predecessor list of s2 and s2 to the successor list of s1




.. py:method:: HiddenMarkovModel.estimateUntrainedTransitions


Cython signature: void estimateUntrainedTransitions()
Estimates the transition probabilities of not trained transitions by averages similar trained ones




.. py:method:: HiddenMarkovModel.evaluate


Cython signature: void evaluate()
Evaluate the HMM, estimates the transition probabilities from the training




.. py:method:: HiddenMarkovModel.forwardDump


Cython signature: void forwardDump()
Writes some info of the forward "matrix" to cerr




.. py:method:: HiddenMarkovModel.getNumberOfStates


Cython signature: size_t getNumberOfStates()
Returns the number of states




.. py:method:: HiddenMarkovModel.getPseudoCounts


Cython signature: double getPseudoCounts()
Returns the pseudo counts




.. py:method:: HiddenMarkovModel.getState


Cython signature: HMMState * getState(const String & name)
Returns the state with the given name




.. py:method:: HiddenMarkovModel.getTransitionProbability


Cython signature: double getTransitionProbability(const String & s1, const String & s2)
Returns the transition probability of the given state names




.. py:method:: HiddenMarkovModel.setInitialTransitionProbability


Cython signature: void setInitialTransitionProbability(const String & state, double prob)
Sets the initial transition probability of the given state to prob




.. py:method:: HiddenMarkovModel.setPseudoCounts


Cython signature: void setPseudoCounts(double pseudo_counts)
Sets the pseudo count that are added instead of zero




.. py:method:: HiddenMarkovModel.setTrainingEmissionProbability


Cython signature: void setTrainingEmissionProbability(const String & state, double prob)
Sets the emission probability of the given state to prob




.. py:method:: HiddenMarkovModel.setTransitionProbability


Cython signature: void setTransitionProbability(const String & s1, const String & s2, double prob)
Sets the transition probability of the given state names to prob




.. py:method:: HiddenMarkovModel.setVariableModifications


Cython signature: void setVariableModifications(StringList & modifications)




.. py:method:: HiddenMarkovModel.train


Cython signature: void train()
Trains the HMM. Initial probabilities and emission probabilities of the emitting states should be set




.. py:method:: HiddenMarkovModel.writeGraphMLFile


Cython signature: void writeGraphMLFile(const String & filename)
Writes the HMM into a file in GraphML format




