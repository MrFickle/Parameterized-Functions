"""
This script contains functions that are used only for plotting data.
"""

# Modules
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.ticker as mticker
import matplotlib
matplotlib.use('Agg')


# Create a fully parametrized function that plots single or multiple [x, y] distributions of points with the settings
# desired and stores the figure at given path.
def plot_x_y_multiple_data(data_dictionary_x, data_dictionary_y, xlabel, ylabel, figure_title, data_path_out,
                           color_dictionary=None, legend_dictionary=None, lw_dict=None, ls_dict=None, fs_dict=None,
                           m_dict=None, ms_dict=None, figure_size=None, xticks_values=None, yticks_values=None,
                           xticks_labels=None, yticks_labels=None, legend_loc="best"):

    """
    :param data_dictionary_x: Contains all of the x values for all the data distributions stored as data_dictionary_x['distribution_name'] = x_vector
    :param data_dictionary_y: Contains all of the y values for all the data distributions stored as data_dictionary_y['distribution_name'] = y_vector
    :param xlabel: Name given to x axis
    :param ylabel: Name given to y axis
    :param figure_title: The figure title
    :param data_path_out: The filepath + filename where the figure will be stored
    :param color_dictionary: Contains a color for each of the data distributions as color_dictionary['distribution_name'] = color
    :param legend_dictionary: Contains a legend for each of the data distributions as legend_dictionary['distribution_name'] = legend
    :param lw_dict: Contains a linewidth value for each of the data distributions as lw_dict['distribution_name'] = linewidth
    :param ls_dict: Contains a linestyle value for each of the data distributions as ls_dict['distribution_name'] = linestyle
    :param fs_dict: The font_size of the 'title', 'xlabel', 'ylabel', 'xticks', 'yticks', 'legends' separately in a dictionary
    :param m_dict: Contains a marker style for each of the data distributions as m_dict['distribution_name'] = marker style
    :param ms_dict: Contains a marker size value for each of the data distributions as ms_dict['distribution_name'] = marker size
    :param figure_size: The size of the figure in a tuple (width, height)
    :param xticks_values: The values of the xticks in a numpy array
    :param yticks_values: The values of the yticks in a numpy array
    :param xticks_labels: Names given to the xticks labels in a list with strings
    :param yticks_labels: Names given to the yticks labels in a list with strings
    :return: Store figure at data_path_out
    """

    # Turn off interactive mode so that the plots don't show unless commanded.
    plt.ioff()

    # Get the keys of the dictionaries
    dict_keys = [j for j in data_dictionary_x.keys()]

    # If any of the arguments are None then set their values for all keys to default
    # Color Default = Blue
    if not color_dictionary:
        color_dictionary = {}
        for key in dict_keys:
            color_dictionary[key] = 'blue'

    # Linewidth Default = 2
    if not lw_dict:
        lw_dict = {}
        for key in dict_keys:
            lw_dict[key] = 2

    # Linestyle Default = 'solid'
    if not ls_dict:
        ls_dict = {}
        for key in dict_keys:
            ls_dict[key] = 'solid'

    # Font size Default = 16
    if not fs_dict:
        fs_dict = {}
        fs_dict['title'] = 16
        fs_dict['xlabel'] = 16
        fs_dict['ylabel'] = 16
        fs_dict['xticks'] = 16
        fs_dict['yticks'] = 16

    # Marker Default = None
    if not m_dict:
        m_dict = {}
        for key in dict_keys:
            m_dict[key] = None

    # Marker Size Default = None
    if not ms_dict:
        ms_dict = {}
        for key in dict_keys:
            ms_dict[key] = None

    # Initialize plot
    if figure_size:
        fig, ax = plt.subplots(figsize=figure_size)
    # Figure Size Default = (12, 8)
    else:
        fig, ax = plt.subplots(figsize=(12, 8))
    # For every key in the dictionary plot its points with the respective settings
    for key in dict_keys:
        ax.plot(data_dictionary_x[key], data_dictionary_y[key], color=color_dictionary[key], linewidth=lw_dict[key],
                linestyle=ls_dict[key], marker=m_dict[key], markersize=ms_dict[key])

    # Set title, xlabel, ylabel, xticks, yticks
    ax.set_title(figure_title, fontsize=fs_dict['title'])
    ax.set_xlabel(xlabel, fontsize=fs_dict['xlabel'])
    ax.set_ylabel(ylabel, fontsize=fs_dict['ylabel'])

    # Set xticks if given, otherwise use default
    if not isinstance(None, type(xticks_values)):
        ax.set_xticks(xticks_values)
    # Set yticks if given, otherwise use default
    if not isinstance(None, type(yticks_values)):
        ax.set_yticks(yticks_values)

    # Plot xticklabels if given
    if not isinstance(None, type(xticks_labels)):
        ax.set_xticklabels(labels=xticks_labels, fontsize=fs_dict['xticks'])
    # Plot yticklabels if given
    if not isinstance(None, type(yticks_labels)):
        ax.set_xticklabels(labels=yticks_labels, fontsize=fs_dict['yticks'])

    # Plot legends if given
    if legend_dictionary:
        legend_handles = list()
        for key in dict_keys:
            legend_handles.append(mlines.Line2D([], [], linestyle=ls_dict[key], color=color_dictionary[key],
                                                label=legend_dictionary[key], linewidth=lw_dict[key],
                                                marker=m_dict[key], markersize=ms_dict[key]))

        ax.legend(handles=legend_handles, loc=legend_loc, frameon=False)

    fig.tight_layout(pad=3)
    # Save the figure
    fig.savefig(data_path_out)
