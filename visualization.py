import matplotlib.pyplot as plt


# Take a dictionary tpe

def pie_chart(data: dict):
    if type(data) is not dict: raise TypeError(
        'pie_chart requires a dict as input: you inserted a {}'.format(type(data)))
    labels = list(data.keys())
    sizes = list(data.values())
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.tight_layout()
    plt.show()


def simple_plot(data):
    plt.plot(data.keys(), data.values())
    plt.show()

