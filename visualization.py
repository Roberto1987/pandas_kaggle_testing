import matplotlib.pyplot as plt


# Take a dictionary tpe
from utilities import dict_check


def pie_chart(data: dict):
    dict_check('pie_chart',data)
    labels = list(data.keys())
    sizes = list(data.values())
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.tight_layout()
   # plt.show()


def simple_plot(data):
    plt.plot(data.keys(), data.values())
   # plt.show()
