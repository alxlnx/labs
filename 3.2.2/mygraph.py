# My graphing functions for less generic code (setting grids, thicknesses, etc)
# see notes folder for how to define your style maybe you dont need custom functions at all
# AND PUT YOUR DATA IN .CSV AND READ WITH PANDAS
import numpy as np
import matplotlib.pyplot as plt

last_k, last_s_k, last_b, last_s_b = None, None, None, None
last_x = None

def linls(x: np.ndarray, y: np.ndarray, through_null: bool = False) -> tuple[float, float] | tuple[float, float, float, float]:
    ''' Return k and b coefficients for y = k*x + b by applying linear least squares to x and y.

        If through_null is set, return (k, error_k, b, error_b).
    '''
    global last_x; global last_k; global last_s_k; global last_b; global last_s_b
    last_x = x

    if isinstance(x, np.ndarray) and isinstance(y, np.ndarray):
        if len(x) != len(y):
            raise ValueError("Incompatible x and y vectors. They must have the same length.")
        if through_null:
            k = np.mean(x * y) / np.mean(x * x)
            s_k = np.sqrt(1 / len(x)) * np.sqrt(np.mean(y * y) / np.mean(x * x) - k ** 2)

            last_k, last_s_k = k, s_k

            return k, s_k
        else:
            xy = np.mean(x * y)
            x1y = np.mean(x) * np.mean(y)
            x2 = np.mean(x * x)
            x12 = np.mean(x) ** 2
            y2 = np.mean(y * y)
            y12 = np.mean(y) ** 2
            k = (xy - x1y) / (x2 - x12)
            b = np.mean(y) - k * np.mean(x)
            s_k = np.sqrt(1 / len(x)) * np.sqrt((y2 - y12) / (x2 - x12) - k ** 2)
            s_b = s_k * np.sqrt(x2 - x12)

            # last_k = k
            # last_s_k = s_k
            # last_b = b
            # last_s_b = s_b
            last_k, last_s_k, last_b, last_s_b = k, s_k, b, s_b

            return k, s_k, b, s_b
    else:
        raise ValueError("Invalid x or/and y type. Must be numpy.ndarray.") 
    
def display_linls(ax: plt.Axes, text: bool = True, color: str = 'r'):
    ''' Plot the line and optionally print the values from the last call to linls(). '''
    if not last_k:
        raise ValueError("linls() wasn't called before hence no data to show. ")
    ax.plot(last_x, last_x * last_k + last_b, color=color, zorder=-1)
    if text:
        print('Коэффиценты прямой: k, s_k, b, s_b')
        print(last_k, last_s_k, last_b, last_s_b, sep='\t')


def make_figure(dpi_mode: str = 'low', orientation='landscape') -> plt.figure:
    ''' Return a figure with my desired parameters. '''
    if dpi_mode == 'low':
        DPI = 80
    elif dpi_mode == 'high':
        DPI = 400
    else:
        raise ValueError('Invalid dpi mode set. Supported values are: low, high.')
        
    if orientation != 'landscape' and orientation != 'portrait':
        raise ValueError('Invalid orientation.')
    SIZE = (11.693, 8.268) if orientation == 'landscape' else (8.268, 11.693)

    return plt.figure(figsize=SIZE, dpi=DPI, layout='constrained')


def draw_errorbar(ax: plt.Axes, X: np.ndarray | list, Y: np.ndarray | list, x_err: float = 0, y_err: float = 0, label: str = ''):
    ''' Draw an errorbar of X and Y on axes ax. '''
    ax.errorbar(X, Y, 
                fmt='ks', linewidth=0, markersize=5, elinewidth=1, capsize=3, zorder=3,
                xerr=x_err, yerr=y_err, label=label)

def set_grids(fig: plt.Figure) -> None:
    ''' Set grids for all axes in a figure. '''
    [ax.minorticks_on() for ax in fig.axes]
    [ax.grid(which='major', linestyle='-', linewidth=0.5, zorder=-1) for ax in fig.axes]
    [ax.grid(which='minor', linestyle='--', linewidth=0.25, zorder=-1) for ax in fig.axes]

font = {'fontname': 'DejaVu Serif'}

def set_label(ax: plt.Axes, x_label: str = '', y_label:str = ''):
    ax.set_xlabel(x_label, **font)
    ax.set_ylabel(y_label, **font)

ax_count = 1

def set_title(ax: plt.Axes, title: str):
    global ax_count
    ax.set_title(f'Рис {ax_count}. ' + title, **font)
    ax_count += 1
