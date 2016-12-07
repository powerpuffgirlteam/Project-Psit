""" Statistics delays of trains Thailand Project
    This program shows chart of September 2016 that show statistics average delays of Thai trains divided by types
"""
import pygal
def make_chart():
    """This function use to make chart of September 2016 that show statistics average delays
    of Thai trains divided by types"""
    from pygal.style import RotateStyle
    dark_rotate_style = RotateStyle('#9e6ffe')
    chart = pygal.StackedLine(fill=True, interpolate='cubic', style=dark_rotate_style)
    chart.title = 'Statistics average delays of Thai trains divided by types of September 2016'
    chart.x_labels = map(str, range(1, 31))
    chart.add('Special express trains', [164.00, 105.33, 102.00, 100.33, 94.00, 135.67, 102.33, 157.33, 109.67, 60.67, 125.00, 198.00,
        129.33, 280.00, 209.33, 116.67, 209.00, 126.33, 170.33, 238.00, 204.33, 146.67, 145.67, 226.33, 160.33, 122.33, 169.67,
        186.00, 120.33, 113.33])
    chart.add('Express trains', [80.67, 62.00, 45.33, 70.67, 66.00, 121.00, 72.67, 117.33, 68.33, 125.33, 35.33, 37.67,
        116.00, 56.33, 99.00, 60.00, 153.00, 58.33, 99.33, 106.67, 159.67, 121.33, 123.00, 169.67, 92.67, 145.67, 93.00,
        78.33, 92.00, 137.00])
    chart.add('Rapid trains', [319.67, 188.67, 199.67, 89.33, 275.00, 219.67, 120.33, 102.33, 125.33, 193.00, 116.67, 207.33,
        261.67, 186.67, 309.67, 251.00, 276.33, 354.67, 266.33, 372.00, 244.33, 167.00, 257.67, 275.00, 212.33, 247.33, 216.67,
        234.33, 283.00, 325.33])
    chart.add('Ordinary trains', [107.00, 105.00, 183.00, 183.00, 140.00, 162.00, 132.50, 133.75, 158.50, 147.00, 134.00, 233.75,
        120.25, 115.25, 120.00, 127.25, 223.75, 83.00, 163.25, 110.00, 138.25, 144.50, 231.00, 130.25, 124.75, 137.75, 129.25,
        169.25, 129.00, 190.75])
    chart.add('Ordinary diesel rail cars', [34.50, 13.50, 9.00, 2.50, 43.50, 76.00, 93.50, 30.50, 40.00, 0.00, 93.50, 18.00,
        7.50, 11.00, 10.00, 61.50, 20.00, 0.00, 57.50, 39.50, 15.00, 19.50, 49.00, 0.00, 0.00, 33.00, 12.50,
        78.50, 45.50, 119.00])
    chart.add('Special diesel rail cars', [276.67, 160.00, 246.00, 78.33, 108.67, 122.67, 159.67, 72.33, 87.00, 188.00, 174.33, 148.00,
        212.67, 248.33, 167.33, 299.00, 189.33, 359.00, 233.00, 284.33, 199.00, 189.00, 303.33, 277.00, 232.67, 209.33, 218.67,
        245.33, 187.00, 238.00])
    chart.add('Express diesel rail cars', [10.00, 15.00, 12.50, 5.00, 8.00, 61.00, 63.50, 42.50, 63.50, 28.00, 20.00, 48.50,
        40.00, 8.50, 17.50, 3.50, 5.00, 2.50, 31.00, 48.00, 67.50, 22.50, 76.50, 2.50, 12.50, 38.50, 32.50,
        0.00, 21.50, 32.00])
    chart.render_to_file('typechart_month.svg')

make_chart()
