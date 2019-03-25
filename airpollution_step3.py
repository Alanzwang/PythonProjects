#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:01:23 2019

@author: zeliangwang

The first step is to prepare the pollution dataset for the LSTM.

This involves framing the dataset as a supervised learning problem and 
normalizing the input variables. We will frame the supervised learning problem 
as predicting the pollution at the current hour (t) given the pollution 
measurement and weather conditions at the prior time step.
This formulation is straightforward and just for this demonstration. 
Some alternate formulations you could explore include:
Predict the pollution for the next hour based on the weather conditions and 
pollution over the last 24 hours.
Predict the pollution for the next hour as above and given the “expected” 
weather conditions for the next hour.
"""

