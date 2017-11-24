# waterfallcharts

A simple graphing tool that attempts to generate a standard waterfall chart in generic Python.

The idea was first brought to my attention by [Jeremy Howard](https://twitter.com/jeremyphoward), who complained that no such easy to use package
existed. The underlying method borrows from Chris Moffitt's [stacked bar charts approach](http://pbpython.com/waterfall-chart.html), 
and improves upon data range reliability, appearance, and chart options.

The primary aim of the package is to provide a quick and reliable way to generate waterfall charts on a whim, for both accounting and 
random forest interpretation purposes.

## Functionality

There is currently one function: 
* `quick_charts()`: Given two sequences ordered appropriately, of contribution amounts and labels, generate a standard waterfall chart<br><img src=images/image1.png width=900>

There are three features: 

* sorted_value: Sorts contributions by absolute value in the chart

* threshold: Groups all contributions under a certain threshold value into an 'other' group

* formatting: Formats Y axis labels and bar chart labels to the specified input

Additionally, there are several arguments that control for chart title, axis names, bar colors, and custom bar labels for 
'other' and 'net'<br><img src=images/image2.png width=900>


Check out the [examples](https://github.com/chrispaulca/hosted_waterfall/blob/master/Examples.ipynb).


## Installation

Simply install the Python `waterfallcharts` package:

```bash
$ pip install waterfallcharts
```

or upgrade to the latest version:

```bash
$ pip install -U waterfallcharts
```


## Usage

As detailed in the [example](https://github.com/chrispaulca/hosted_waterfall/blob/master/Examples.ipynb) and source code, the function assumes two list inputs, one of the contribution NAMES and the other of the contribution AMOUNTS. Please note that the NET SUM of all contributions is not an input to the function, and is calculated for you.


```python
from waterfallcharts import quick_charts as qc
a = ['sales','returns','credit fees','rebates','late charges','shipping']
b = [350000,-30000,-7500,-25000,95000,-7000]
plot = qc.waterfall(a,b)
```


## Implementation notes

### Deploy

```bash
$ python setup.py sdist upload
```






