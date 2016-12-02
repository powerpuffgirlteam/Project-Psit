"""Graph route of train program"""
import pygal
def show_graph():
    """Function program that make graph route of train"""
    pie_chart = pygal.Pie()
    pie_chart.title = "Statistics average delays of trains Thailand divided by route (in minutes)" + "\n" + "1 September 2016"
    pie_chart.add('Northern Line', 15.26315789)
    pie_chart.add('North Eastern Line', 14.44)
    pie_chart.add('Eastern Line', 5.863636364)
    pie_chart.add('Southern Line', 32.18)
    pie_chart.render_to_file('pie_chart1.svg')
show_graph()
