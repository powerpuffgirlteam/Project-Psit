"""This program that make graph with pygal"""
import pygal
def parameter():
    """This program that make graph with pygal"""
    bar_chart = pygal.Bar()
    bar_chart.title = 'Statistic average dalays of trains Thailand by type (in minute)' +"\n"+ '1 September 2016'
    bar_chart.add('Special Express trains', [164])
    bar_chart.add('Express trains', [80.66666667])
    bar_chart.add('Rapid trains ', [319.6666667])
    bar_chart.add('Ordinary trains', [107])
    bar_chart.add('Special diesel Rail Cars', [34.5])
    bar_chart.add('Ordinary diesel Rail Cars', [276.6666667])
    bar_chart.add('Express diesel Rail Cars', [10])
    bar_chart.render_to_file('bar_chart1.svg')
parameter()
