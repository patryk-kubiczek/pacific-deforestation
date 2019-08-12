from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator
from geopandas import GeoDataFrame
import matplotlib as mpl

def custom_legend(ax, data, title, n_levels=5, leg_prec=1, cmap='viridis', alpha=0.6, **kwargs):
    cmap = plt.get_cmap(cmap)
    max_val, min_val = max(data), min(data)
    d = max_val - min_val
    levels = [min_val + i * d / (n_levels - 1) for i in range(n_levels)]
    colors = [cmap(i / (n_levels - 1)) for i in range(n_levels)]
    custom_legend = [Line2D([0], [0], marker='o', color='lightgrey', alpha=alpha, markersize='12',
                            label="{:.{prec}f}".format(level, prec=leg_prec), markerfacecolor=color)
                     for level, color in zip(levels, colors)]
    legend = ax.legend(handles=custom_legend, title=title,
                       facecolor='lightgrey', edgecolor="black",
                       framealpha=1, fancybox=False, loc="upper right", bbox_to_anchor=(0.997, 0.85))



def spatial_plot(gdf, column, world_gdf, labels=None,
                 landcolor="grey", edgecolor="dimgray", oceancolor="lightblue",
                 figwidth=6, n_levels=5, leg_prec=1, **plot_kwargs):
    figsize = (figwidth, 0.65 * figwidth)
    fig, ax = plt.subplots(figsize=figsize)
    world_gdf.plot(ax=ax, color=landcolor, edgecolor=edgecolor)
    ax.set_facecolor(oceancolor);
    gdf.plot(ax=ax, column=column, legend=False, **plot_kwargs)
    if type(labels) == GeoDataFrame:
        for xy, label in zip(labels.geometry, labels.index):
            ax.annotate(label, xy=xy.coords[0], xytext=(-10, -10), textcoords="offset points", fontsize=9)
    ax.set_xlim([130, 260])
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.set_ylim([-50, 30])
    ax.set_xlabel(r"Longitude [$\degree$]")
    ax.set_ylabel(r"Latitude [$\degree$]")
    ax.grid()
    custom_legend(ax, gdf[column], column, n_levels=n_levels, leg_prec=leg_prec, **plot_kwargs)
    return fig
