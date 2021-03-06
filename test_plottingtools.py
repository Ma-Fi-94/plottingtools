import matplotlib.pyplot as plt  # type: ignore
import matplotlib.figure  # type: ignore
import numpy as np
from scipy import stats  # type: ignore

import pytest
import sys
import io

import plottingtools as pt

######################
# General Aesthetics #
######################


def test_tex_on_off():
    pt.texon()
    pt.texoff()


def test_light_and_darkmode():
    pt.lightmode()
    pt.darkmode()


####################
# Types of layouts #
####################


def test_singleplot():
    fig, ax = pt.singleplot()
    assert type(fig) == matplotlib.figure.Figure

    fig, ax = pt.singleplot(size=(7, 5))
    assert type(fig) == matplotlib.figure.Figure

    fig, ax = pt.singleplot(size=[7, 5])
    assert type(fig) == matplotlib.figure.Figure
    plt.close()

    fig, ax = pt.singleplot(size=np.array([7, 5]))
    assert type(fig) == matplotlib.figure.Figure
    plt.close()


def test_singleplot_pathological():
    with pytest.raises(AssertionError) as exception_info:
        pt.singleplot(size=1)
    plt.close()


def test_multiplot():
    fig, ax = pt.multiplot(nrows=3, ncols=2, size_xy=(20, 12))
    plt.close()


def test_multiplot_pathological():
    with pytest.raises(AssertionError) as exception_info:
        pt.multiplot(nrows=-2, ncols=5, size_xy=(20, 20))
    with pytest.raises(AssertionError) as exception_info:
        pt.multiplot(nrows="abc", ncols=5, size_xy=(20, 20))
    with pytest.raises(AssertionError) as exception_info:
        pt.multiplot(nrows=5, ncols=-2, size_xy=(20, 20))
    with pytest.raises(AssertionError) as exception_info:
        pt.multiplot(nrows=5, ncols="abc", size_xy=(20, 20))
    with pytest.raises(AssertionError) as exception_info:
        pt.multiplot(nrows=2, ncols=3, size_xy=(-20, 20))
    with pytest.raises(AssertionError) as exception_info:
        pt.multiplot(nrows=2, ncols=3, size_xy=(20, -20))
    with pytest.raises(AssertionError) as exception_info:
        pt.multiplot(nrows=2, ncols=3, size_xy=(20, "abc"))
    with pytest.raises(AssertionError) as exception_info:
        pt.multiplot(nrows=2, ncols=3, size_xy=("abc", 20))


#############################
# Adding elements to a plot #
#############################


def test_title():
    fig, ax = pt.singleplot()
    pt.title(ax, "abcdef", fontsize=25, pad=10)
    assert ax.get_title() == "abcdef"
    plt.close()


def test_title_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.title(ax, title="title", fontsize="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.title(ax, title="title", fontsize=-54321)
    with pytest.raises(AssertionError) as exception_info:
        pt.title(ax, title="title", pad="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.title(ax=123, title="title")
    plt.close()


def test_labels():
    fig, ax = pt.singleplot()
    pt.labels(ax, xlabel="xlabel", ylabel="ylabel", fontsize=10, pad=5)
    assert ax.get_xlabel() == "xlabel"
    assert ax.get_ylabel() == "ylabel"
    plt.close()


def test_labels_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.labels(ax, xlabel="xlabel", ylabel="label", pad="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.labels(ax, xlabel="xlabel", ylabel="label", fontsize="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.labels(ax, xlabel="xlabel", ylabel="label", fontsize=-5)
    with pytest.raises(AssertionError) as exception_info:
        pt.labels(ax="abc", xlabel="xlabel", ylabel="ylabel")
    plt.close()


def test_diagonal():
    fig, ax = pt.singleplot()
    pt.diagonal(ax)
    plt.close()


def test_diagonal_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.diagonal(ax, alpha="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.diagonal(ax, alpha=-1234)
    with pytest.raises(AssertionError) as exception_info:
        pt.diagonal(ax, linestyle="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.diagonal(ax, linestyle=1234)
    with pytest.raises(AssertionError) as exception_info:
        pt.diagonal(ax, linewidth=-1234)
    with pytest.raises(AssertionError) as exception_info:
        pt.diagonal(ax="abc", linewidth=1)
    plt.close()


def test_rectangle():
    fig, ax = pt.singleplot()
    pt.rectangle(ax,
                 x1=1,
                 x2=2,
                 y1=1,
                 y2=2,
                 linewidth=3,
                 linestyle=":",
                 fill=True)
    plt.close()


def test_rectangle_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1="abc", x2=2, y1=1, y2=2)
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1=1, x2="abc", y1=1, y2=2)
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1=1, x2=2, y1="abc", y2=2)
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1=1, x2=2, y1=1, y2="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1=1, x2=2, y1=1, y2=2, linewidth=-1234)
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1=1, x2=2, y1=1, y2=2, linestyle=-1234)
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1=1, x2=2, y1=1, y2=2, fill="abcde")
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax=123, x1=1, x2=2, y1=1, y2=2)
    plt.close()


def test_star():
    fig, ax = pt.singleplot()
    pt.star(ax, x=1, y=2, colour="blue", fontsize=25)
    plt.close()


def test_star_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.star(ax, x="abc", y=2)
    with pytest.raises(AssertionError) as exception_info:
        pt.star(ax, x=1, y="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.star(ax=123, x=1, y=2)
    plt.close()


def test_lines():
    fig, ax = pt.singleplot()
    pt.lines(ax, which="x", pos=[1, 2, 3, -5])
    pt.lines(ax, which="y", pos=[1, 2, 3, -5])
    plt.close()


def test_lines_pathological():
    fig, ax = pt.singleplot()

    with pytest.raises(AssertionError) as exception_info:
        pt.lines(ax, which=1234, pos=[7, 8, 9])
    with pytest.raises(AssertionError) as exception_info:
        pt.lines(ax, which="abcde", pos=[7, 8, 9])
    with pytest.raises(AssertionError) as exception_info:
        pt.lines(ax=123, which="x", pos=[1, 2, 3])

    for which in ["x", "y"]:
        with pytest.raises(AssertionError) as exception_info:
            pt.lines(ax, which=which, pos=[])
        with pytest.raises(AssertionError) as exception_info:
            pt.lines(ax, which=which, pos=[1, 2, "abc"])
        with pytest.raises(AssertionError) as exception_info:
            pt.lines(ax, which=which, pos="abc")
        with pytest.raises(AssertionError) as exception_info:
            pt.lines(ax, which=which, pos=[1, 2, 3], linestyle="abc")
        with pytest.raises(AssertionError) as exception_info:
            pt.lines(ax, which=which, pos=[1, 2, 3], linestyle=1)
        with pytest.raises(AssertionError) as exception_info:
            pt.lines(ax, which=which, pos=[1, 2, 3], alpha=-0.3)
        with pytest.raises(AssertionError) as exception_info:
            pt.lines(ax, which=which, pos=[1, 2, 3], alpha="abc")
        with pytest.raises(AssertionError) as exception_info:
            pt.lines(ax, which=which, pos=[1, 2, 3], linewidth=-12345)
        with pytest.raises(AssertionError) as exception_info:
            pt.lines(ax, which=which, pos=[1, 2, 3], linewidth="abc")
        with pytest.raises(AssertionError) as exception_info:
            pt.lines(ax, which=which, pos=[1, 2, 3], zorder="abc")


def test_grid():
    fig, ax = pt.singleplot()
    pt.grid(ax)
    plt.close()


def test_grid_pathological():
    pass  # TBD


#############################
# Change elements of a plot #
#############################


def test_despine():
    fig, ax = pt.singleplot()
    pt.despine(ax, ['top', 'left', 'bottom', 'right'])
    plt.close()


def test_despine_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.despine(ax, which=['bla'])
    with pytest.raises(AssertionError) as exception_info:
        pt.despine(ax, which=123)
    with pytest.raises(AssertionError) as exception_info:
        pt.despine(ax="abc", which=["left"])
    plt.close()


def test_ticklabelsize():
    fig, ax = pt.singleplot()
    pt.ticklabelsize(ax, size=25)
    plt.close()


def test_ticklabelsize_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.ticklabelsize(ax, size="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.ticklabelsize(ax=123, size=10)
    plt.close()


def test_limits():
    fig, ax = pt.singleplot()
    pt.limits(ax, xlimits=(3, 5), ylimits=None)
    pt.limits(ax, xlimits=None, ylimits=(4, 6))
    assert ax.get_xlim() == (3, 5)
    assert ax.get_ylim() == (4, 6)
    plt.close()


def test_limits_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.limits(ax, xlimits=12345, ylimits=None)
    with pytest.raises(AssertionError) as exception_info:
        pt.limits(ax, xlimits=None, ylimits=12345)
    with pytest.raises(AssertionError) as exception_info:
        pt.limits(ax, xlimits=[12345], ylimits=None)
    with pytest.raises(AssertionError) as exception_info:
        pt.limits(ax, xlimits=None, ylimits=[12345])
    with pytest.raises(AssertionError) as exception_info:
        pt.limits(ax, xlimits=[12345, "abc"], ylimits=None)
    with pytest.raises(AssertionError) as exception_info:
        pt.limits(ax, xlimits=None, ylimits=[12345, "def"])
    with pytest.raises(AssertionError) as exception_info:
        pt.limits(ax=123, xlimits=None, ylimits=[1, 2])
    plt.close()


def test_ticks_and_labels():
    fig, ax = pt.singleplot()
    pt.ticks_and_labels(ax, which="x", ticks=[-0.14, 1, 2], labels=None)
    pt.ticks_and_labels(ax, which="y", ticks=[-0.14, 1, 2], labels=None)
    pt.ticks_and_labels(ax, which="xy", ticks=[-0.14, 1, 2], labels=None)
    pt.ticks_and_labels(ax, which="yx", ticks=[-0.14, 1, 2], labels=None)


def test_ticks_and_labels_pathological():
    fig, ax = pt.singleplot()

    with pytest.raises(AssertionError) as exception_info:
        pt.ticks_and_labels(ax,
                            which="x",
                            ticks=[-0.14, 1, 2, "a"],
                            labels=None)
    with pytest.raises(AssertionError) as exception_info:
        pt.ticks_and_labels(ax,
                            which="y",
                            ticks=[-0.14, 1, 2, 3.5],
                            labels=["a"])
    with pytest.raises(AssertionError) as exception_info:
        pt.ticks_and_labels(ax,
                            which="abc",
                            ticks=[-0.14, 1, 2, 3.5],
                            labels=["a", "b", "c"])
    with pytest.raises(AssertionError) as exception_info:
        pt.ticks_and_labels(ax=123,
                            which="x",
                            ticks=[-0.14, 1, 2, 3.5],
                            labels=["a", "b", "c"])
    plt.close()


@pytest.mark.filterwarnings('ignore::UserWarning')
def test_rotate_ticklabels():
    fig, ax = pt.singleplot()
    pt.rotate_ticklabels(ax, which="x", rotation=10.5)
    pt.rotate_ticklabels(ax, which="y", rotation=-10.5)
    pt.rotate_ticklabels(ax, which="xy", rotation=10.5)
    pt.rotate_ticklabels(ax, which="yx", rotation=-10.5)
    pt.rotate_ticklabels(ax, which="both", rotation=-10.5)
    plt.close()


def test_rotate_ticklabels_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.rotate_ticklabels(ax, which="abcde", rotation=10.5)
    with pytest.raises(AssertionError) as exception_info:
        pt.rotate_ticklabels(ax, which="x", rotation="abcde")
    with pytest.raises(AssertionError) as exception_info:
        pt.rotate_ticklabels(ax, which=12345, rotation=10.5)
    with pytest.raises(AssertionError) as exception_info:
        pt.rotate_ticklabels(ax=123, which="x", rotation=10.5)
    plt.close()


@pytest.mark.filterwarnings('ignore::UserWarning')
def test_align_ticklabels():
    fig, ax = pt.singleplot()
    pt.align_ticklabels(ax, which="x", horizontal=None, vertical="center")
    pt.align_ticklabels(ax, which="y", horizontal=None, vertical="top")
    pt.align_ticklabels(ax, which="x", horizontal="right", vertical=None)
    pt.align_ticklabels(ax, which="y", horizontal="left", vertical=None)
    plt.close()


def test_align_ticklabels_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.align_ticklabels(ax, which="abcde", horizontal=None, vertical="top")
    with pytest.raises(AssertionError) as exception_info:
        pt.align_ticklabels(ax, which="x", horizontal="abcde", vertical="top")
    with pytest.raises(AssertionError) as exception_info:
        pt.align_ticklabels(ax, which="x", horizontal=None, vertical="abcde")
    with pytest.raises(AssertionError) as exception_info:
        pt.align_ticklabels(ax, which="x", horizontal=None, vertical=12345)
    with pytest.raises(AssertionError) as exception_info:
        pt.align_ticklabels(ax=123,
                            which="x",
                            horizontal=None,
                            vertical="center")
    plt.close()


#########
# Plots #
#########


def test_similarity_matrix():
    assert np.array_equal(pt._similarity_matrix([[1, 2, 3, 4], [1, 3]]),
                          np.array([[1, 0.5], [0.5, 1]]))

    f = lambda x, y: len(set.intersection(x, y)) / len(set.union(x, y))
    assert np.array_equal(
        pt._similarity_matrix([[1, 2, 3, 4], [1, 3]], method=f),
        np.array([[1, 0.5], [0.5, 1]]))


def test_similarity_matrix_pathological():
    with pytest.raises(NotImplementedError) as exception_info:
        x = pt._similarity_matrix([[1, 2, 3, 4], [1, 3]], method="abcdef")
    with pytest.raises(NotImplementedError) as exception_info:
        x = pt._similarity_matrix([[1, 2, 3, 4], [1, 3]], method=12345)


def test_similarity_heatmap():
    fig, ax = pt.singleplot()
    pt.similarity_heatmap(ax=ax,
                          list_of_lists=[[1, 2, 3], [1]],
                          method="jaccard")
    plt.close()


def test_masked_heatmap():
    fig, ax = pt.singleplot()
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    pt.masked_heatmap(ax=ax, data=data, mask="upperdiag")
    pt.masked_heatmap(ax=ax, data=data, mask="upper")
    pt.masked_heatmap(ax=ax, data=data, mask="lowerdiag")
    pt.masked_heatmap(ax=ax, data=data, mask="lower")
    plt.close()


def test_masked_heatmap_pathological():  #TBD
    pass


def test_correlation_matrix():
    res = pt._correlation_matrix([[1, 2, 3], [4, 5, 6]])
    assert np.all(np.abs(res) - 1 < 1e-6)

    res = pt._correlation_matrix([[1, 2, 3], [4, 5, 6]], method="spearman")
    assert np.all(np.abs(res) - 1 < 1e-6)

    res = pt._correlation_matrix([[1, 2, 3], [4, 5, 6]], method="kendall")
    assert np.all(np.abs(res) - 1 < 1e-6)

    res = pt._correlation_matrix([[1, 2, 3], [4, 5, 6]],
                                 method=lambda a, b: stats.pearsonr(a, b)[0])
    assert np.all(np.abs(res) - 1 < 1e-6)

    res = pt._correlation_matrix([[1, 2, 3], [6, 5, 6]])
    assert np.abs(res[0][1]) < 1e-6
    assert np.abs(res[1][0]) < 1e-6
    assert np.abs(res[0][0] - 1) < 1e-6
    assert np.abs(res[1][1] - 1) < 1e-6


def test_correlation_matrix_pathological():
    with pytest.raises(NotImplementedError) as exception_info:
        x = pt._correlation_matrix([[1, 2, 3, 4], [1, 3]], method="abcdef")
    with pytest.raises(NotImplementedError) as exception_info:
        x = pt._correlation_matrix([[1, 2, 3, 4], [1, 3]], method=12345)


##################
# Export figures #
##################


def test_save_png_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.save_png(filename="")
    with pytest.raises(AssertionError) as exception_info:
        pt.save_png(filename="filename", dpi=-12345)
    with pytest.raises(AssertionError) as exception_info:
        pt.save_png(filename="filename", dpi="abcde")
    plt.close()


def test_save_svg_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.save_svg(filename="")
    plt.close()


def test_save_pdf_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.save_pdf(filename="")
    plt.close()


######################
# Default parameters #
######################


def test_heatmap_cbar_kws():
    assert type(pt.heatmap_cbar_kws()) == dict


def test_heatmap_annot_kws():
    assert type(pt.heatmap_annot_kws()) == dict
