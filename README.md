# waterfallcharts

Fill in description of waterfallchars


## Functionality

There a currently one function: 
* `quick_charts()`: Fill in descipion of the function here please 

There are two features: 

* sorted_value:

* threshold: 



Check out the [examples](**notebook's name here**).


## Installation

```bash
pip install waterfallcharts
```


## Usage

As detailed in the [example](https://github.com/chrispaulca/waterfall/blob/master/packageTest.ipynb) and source code, the function assumes two list inputs, one of the contribution NAMES and the other of the contribution AMOUNTS. Please note that the NET SUM of all contributions is not an input to the function, and is calculated for you.


```python
from waterfallcharts import quick_charts as qc
a = ['sales','returns','credit fees','rebates','late charges','shipping']
b = [350000,-30000,-7500,-25000,95000,-7000]
plot = qc.waterfall()
```



## Preferences


## Implementation notes













------------------------------------------------------------------------------------------------------------
!! This is a work in progress package !!

Waterfall_charts attempts to provide an easy and quick way to plot basic (for now) and more advanced (to come) waterfall charts of the accounting and finance type.

<img src="images/sample.png" width=400>

## Guide

```bash
pip install waterfallcharts
```

to your file imports add 

```python
from waterfallcharts import quick_charts as qc  
```
