import matplotlib.pyplot as plt


def draw_neural_net(ax, left, right, bottom, top, layer_sizes):
    # n_layers = len(layer_sizes)
    v_spacing = (top - bottom) / float(max(layer_sizes))
    h_spacing = (right - left) / float(len(layer_sizes) - 1)
    # Nodes
    for n, layer_size in enumerate(layer_sizes):
        layer_top = 0.5 * (v_spacing * (layer_size - 1) + (top + bottom))
        for m in range(layer_size):
            circle = plt.Circle(
                (n * h_spacing + left, layer_top - m * v_spacing),
                v_spacing / 4.,
                color='w', ec='k', zorder=4)
            ax.add_artist(circle)
    # Edges
    for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        layer_top_a = 0.5 * (v_spacing * (layer_size_a - 1) + (top + bottom))
        layer_top_b = 0.5 * (v_spacing * (layer_size_b - 1) + (top + bottom))
        for m in range(layer_size_a):
            for o in range(layer_size_b):
                line = plt.Line2D(
                    [n * h_spacing + left, (n + 1) * h_spacing + left],
                    [layer_top_a - m * v_spacing, layer_top_b - o * v_spacing],
                    c='k')
                ax.add_artist(line)


if __name__ == "__main__":
    fig = plt.figure(figsize=(8, 8))
    ax = fig.gca()
    ax.axis('off')
    draw_neural_net(ax, .1, .9, .1, .9, [3, 4, 1])
    plt.savefig("nn.png")
