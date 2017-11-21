'''
A function that attempts to generate a standard waterfall chart in generic Python. Requires two sequences,
one of labels and one of values, ordered accordingly.

The idea was first brought to my attention by Jeremy Howard, who complained no such easy to use package
existed. The underlying method borrows from Chris Moffitt's idea at 
http://pbpython.com/waterfall-chart.html
but is substantially improved upon with respect to appearance, data range reliability, and options.
'''


from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#------------------------------------------

def waterfall(index, data, Title="Example chart", x_lab="Example Increment", y_lab="example values",
              formatting = "{:,.1f}", green_color='#29EA38', red_color='#FB3C62', blue_color='#24CAFF',
             sorted_value = False, threshold=None, other_label='other', net_label='net'):
    '''
    Given two sequences ordered appropriately, generate a standard waterfall chart.
    Optionally modify the title, axis labels, number formatting, bar colors, 
    increment sorting, and thresholding. Thresholding groups lower magnitude changes
    into a combined group to display as a single entity on the chart.
    '''
    
    #convert data and index to np.array
    index=np.array(index)
    data=np.array(data)
    
    #sorted by absolute value 
    if sorted_value: 
        abs_data = abs(data)
        data_order = np.argsort(abs_data)[::-1]
        data = data[data_order]
        index = index[data_order]
    
    #group contributors less than the threshold into 'other' 
    if threshold:
        
        abs_data = abs(data)
        threshold_v = abs_data.max()*threshold
        
        if threshold_v > abs_data.min():
            index = np.append(index[abs_data>=threshold_v],other_label)
            data = np.append(data[abs_data>=threshold_v],sum(data[abs_data<threshold_v]))
    
    changes = {'amount' : data}
    
    #define format formatter
    def money(x, pos):
        'The two args are the value and tick position'
        return formatting.format(x)
    formatter = FuncFormatter(money)

    #Store data and create a blank series to use for the waterfall
    trans = pd.DataFrame(data=changes,index=index)
    blank = trans.amount.cumsum().shift(1).fillna(0)
    
    trans['positive'] = trans['amount'] > 0

    #Get the net total number for the final element in the waterfall
    total = trans.sum().amount
    trans.loc[net_label]= total
    blank.loc[net_label] = total

    #The steps graphically show the levels as well as used for label placement
    step = blank.reset_index(drop=True).repeat(3).shift(-1)
    step[1::3] = np.nan

    #When plotting the last element, we want to show the full bar,
    #Set the blank to 0
    blank.loc[net_label] = 0
    
    #define bar colors for net bar
    trans.loc[trans['positive'] > 1, 'positive'] = 99
    trans.loc[trans['positive'] < 0, 'positive'] = 99
    trans.loc[(trans['positive'] > 0) & (trans['positive'] < 1), 'positive'] = 99
    

    #Plot and label
    my_plot = trans['amount'].plot(kind='bar', stacked=True, bottom=blank,legend=None, 
                                   figsize=(10, 5), title=Title, 
                                   color=trans.positive.map({1: green_color, 0: red_color, 99:blue_color, 
                                                             100:"gray"}))
    
    # connecting lines
    my_plot.plot(step.index, step.values,'k', linewidth = 0.3, color = "gray", )
    
    #axis labels
    my_plot.set_xlabel("\n" + x_lab)
    my_plot.set_ylabel(y_lab + "\n")
    
    #Format the axis for dollars
    my_plot.yaxis.set_major_formatter(formatter)

    #Get the y-axis position for the labels
    y_height = trans.amount.cumsum().shift(1).fillna(0)
    
    temp = list(trans.amount)
    
    # create dynamic chart range
    for i in range(len(temp)):
        if (i > 0) & (i < (len(temp) - 1)):
            temp[i] = temp[i] + temp[i-1]
    
    trans['temp'] = temp
            
    plot_max = trans['temp'].max()
    plot_min = trans['temp'].min()
    
    #Make sure the plot doesn't accidentally focus only on the changes in the data
    if all(i >= 0 for i in temp):
        plot_min = 0
    if all(i < 0 for i in temp):
        plot_max = 0
    
    if abs(plot_max) >= abs(plot_min):
        maxmax = abs(plot_max)   
    else:
        maxmax = abs(plot_min)
        
    pos_offset = maxmax / 50
    
    plot_offset = maxmax / 15 ## needs to me cumulative sum dynamic

    #Start label loop
    loop = 0
    for index, row in trans.iterrows():
        # For the last item in the list, we don't want to double count
        if row['amount'] == total:
            y = y_height[loop]
        else:
            y = y_height[loop] + row['amount']
        # Determine if we want a neg or pos offset
        if row['amount'] > 0:
            y += (pos_offset*1.4)
            my_plot.annotate(formatting.format(row['amount']),(loop,y),ha="center", color = 'g')
        else:
            y -= (pos_offset*3.6)
            my_plot.annotate(formatting.format(row['amount']),(loop,y),ha="center", color = 'r')
        loop+=1

    #Scale up the y axis so there is room for the labels
    my_plot.set_ylim(plot_min-round(2*plot_offset, 7),plot_max+round(2*plot_offset, 7))
    #Rotate the labels
    my_plot.set_xticklabels(trans.index,rotation=40)
    my_plot.axhline(0, color='black', linewidth = 0.6)

    return my_plot