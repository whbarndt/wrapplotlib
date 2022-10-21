from matplotlib import test
import src.wrapplotlib as wrap


def test_bar_graphical_atributes():
    """Testing bar chart categories."""

    test_bar_args = wrap.default_bar_args

    assert test_bar_args['figure_height'] > 0

    assert test_bar_args['figure_width'] > 0

    assert isinstance(test_bar_args['title'], str)

    assert test_bar_args['titlefontsize'] > 0

    assert isinstance(test_bar_args['xlabel'], str)

    assert isinstance(test_bar_args['ylabel'], str)

    assert test_bar_args['axislabelsize'] > 0

    assert isinstance(test_bar_args['ticklabelsize'], str) or isinstance(
        test_bar_args['ticklabelsize'], int)

    assert isinstance(test_bar_args['custom_bar_colors'], str) or isinstance(
        test_bar_args['custom_bar_colors'], list)

    assert isinstance(test_bar_args['edgecolor'], str)

    assert test_bar_args['linewidth'] >= 0

    assert isinstance(test_bar_args['legend'], bool)

    assert isinstance(test_bar_args['legend_title'], str)

    assert isinstance(test_bar_args['transparent'], bool)

    assert isinstance(test_bar_args['bar_labels'],
                      list) or test_bar_args['bar_labels'] is None


def test_plot_graphical_atributes():
    """Testing bounds and types of plotting categories."""

    test_plot_args = wrap.default_plot_args

    assert test_plot_args['figure_height'] > 0

    assert test_plot_args['figure_width'] > 0

    assert isinstance(test_plot_args['title'], str)

    assert test_plot_args['titlefontsize'] > 0

    assert isinstance(test_plot_args['xlabel'], str)

    assert isinstance(test_plot_args['ylabel'], str)

    assert test_plot_args['axislabelsize'] > 0

    assert isinstance(test_plot_args['ticklabelsize'], str) or isinstance(
        test_plot_args['ticklabelsize'], int)

    assert isinstance(test_plot_args['color'], str)

    assert test_plot_args['linewidth'] >= 0

    assert isinstance(test_plot_args['legend'], bool)

    assert isinstance(test_plot_args['legend_title'], str)

    assert isinstance(test_plot_args['datetimeformat'], str)

    assert isinstance(test_plot_args['scale_x'], bool)

    assert isinstance(test_plot_args['scale_y'], bool)

    assert isinstance(test_plot_args['transparent'], bool)
