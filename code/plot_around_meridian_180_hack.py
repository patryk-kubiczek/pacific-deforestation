from matplotlib import pyplot as plt
from matplotlib.lines import Line2D

def plot_around_meridian_180(gdf, column, world_gdf, xlim, ylim,
                             landcolor="grey", edgecolor="black", oceancolor="lightblue",
                             figsize=(10, 10), dpi=96, cmap="viridis", leg_prec=0, **plot_kwargs):

    xlims = [[xlim[0], 180], [-180, xlim[1]]]
    width_ratios = [lim[1] - lim[0] for lim in xlims]
    fig, axes = plt.subplots(ncols=2, sharey=True, figsize=figsize,
                             gridspec_kw={'width_ratios': width_ratios}, dpi=dpi)

    cmap = plt.get_cmap(cmap)
    max_val, min_val = max(gdf[column]), min(gdf[column])
    d = max_val - min_val
    n_levels = 5
    custom_legend = [Line2D([0], [0], marker='o', color='lightgrey', markersize='12',
                            label="{:.{prec}f}".format(min_val + i * d / (n_levels - 1), prec=leg_prec),
                            markerfacecolor=cmap(i / (n_levels - 1)))
                     for i in range(n_levels)]

    for ax, lim in zip(axes[:3], xlims):
        ax = world.plot(ax=ax, color=landcolor, edgecolor=edgecolor)
        ax.set_facecolor(oceancolor);
        ax.grid()
        ax = gdf.plot(ax=ax, column=column, legend=False, cmap=cmap, **plot_kwargs)
        ax.set_xlim(lim)
        ax.set_ylim(ylim)

    axes[0].spines["right"].set_visible(False)
    axes[1].spines["left"].set_visible(False)
    axes[1].yaxis.set_ticks_position("right")
    axes[1].get_xticklabels()[0].set_visible(False)
    axes[1].legend(handles=custom_legend, title=column,
                   facecolor='lightgrey', edgecolor="black",
                   framealpha=1, fancybox=False, loc='center right')

    fig.subplots_adjust(wspace=0)
    return fig
