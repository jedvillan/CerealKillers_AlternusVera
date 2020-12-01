# -*- coding: utf-8 -*-
"""PsychologicalUtility.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JmVBCUdI3OXUuqkwMPa8SR1HnOhC-bMz
"""

import autogluon.core as ag
import pandas as pd
import numpy as np
from autogluon import TabularPrediction as task2
from autogluon import TextPrediction as task

class CerealKillers_PsychologicalUtility:
  def __init__(self):
    self.predictor_rank = task2.load('/content/CerealKillers_AlternusVera/PU/ag_predict')
    self.predictor_sts = task.load('/content/CerealKillers_AlternusVera/PU/saved_dir')

  def predict(self, text, bt=0,f=0,ht=0,mt=0,po=0):
    rank_test = pd.DataFrame(np.array([[bt,f,ht,mt,po]]), columns=['BARELY TRUE', 'FALSE', 'HALF TRUE', 'MOSTLY TRUE', 'PANTS ON'])
    rank_score = self.predictor_rank.predict(rank_test)

    sen_score = predictor_sts.predict_proba({"text": [text]})

    #print("RANK:", rank_score[0]/6)
    #print("SENTI:",sen_score[0][1])
    total_score = 0.5*rank_score[0]/6 + 0.5*sen_score[0][1]
    return total_score









