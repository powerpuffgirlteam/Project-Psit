""" Statistics delays of trains Thailand Project
    This program shows chart of September 2016 that show statistics average delays of Thai trains divided by route
"""
import pygal
def make_chart():
    """This function use to make chart of September 2016 that show statistics average delays
    of Thai trains divided by route"""
    from pygal.style import NeonStyle
    chart = pygal.StackedLine(fill=True, interpolate='cubic', style=NeonStyle)
    chart.title = 'Statistics average delays of Thai trains divided by route of September 2016'
    chart.x_labels = map(str, range(1, 31))
    chart.add('Northern Line', [15.26, 12.72, 12.47, 14.89, 20.69, 23.33, 21.67, 19.40, 8.71, 8.00, 7.37, 11.66, 12.81, 16.36, 11.17, 10.55,
                29.42, 13.75, 18.98, 16.43, 14.49, 11.10, 14.36, 11.58, 9.22, 10.62, 9.36, 16.56, 11.64, 18.76])
    chart.add('North Eastern Line', [14.44, 8.40, 13.94, 7.12, 13.15, 14.64, 10.62, 9.42, 14.81, 7.85, 7.79, 9.50, 11.43, 12.76, 15.50, 13.89,
                12.49, 14.06, 8.21, 15.63, 12.35, 10.23, 14.30, 12.48, 10.45, 11.59, 14.39, 10.35, 9.63, 15.87])
    chart.add('Eastern Line', [5.86, 2.22, 5.95, 6.75, 4.47, 10.30, 9.30, 9.40, 11.91, 10.83, 6.06, 8.18, 9.91, 5.61, 6.65, 6.30, 11.89, 4.69,
                6.09, 8.05, 11.96, 7.86, 36.48, 5.75, 5.95, 2.59, 8.63, 12.70, 8.83, 9.23])
    chart.add('Southern Line', [32.18, 14.05, 32.45, 15.81, 12.67, 19.10, 13.74, 11.46, 11.53, 32.13, 23.66, 32.30, 26.72, 26.18, 29.19, 30.56,
                32.83, 36.06, 35.35, 36.47, 31.14, 26.78, 30.20, 44.67, 29.75, 34.78, 28.53, 31.12, 30.31, 33.84])
    chart.render_to_file('routechart_month.svg')

make_chart()
