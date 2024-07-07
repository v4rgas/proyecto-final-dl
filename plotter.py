import matplotlib.pyplot as plt
import pandas as pd
from os.path import join


def plot_data(data: pd.DataFrame, title: str, save: bool = True):
    average_biases = data.mean()
    average_biases.sort_values(inplace=True)

    plt.figure(figsize=(10, 6))
    plt.barh(average_biases.index, average_biases)
    plt.xlabel("Average bias")
    plt.xlim(-1, 1)
    plt.ylabel("Profession")
    plt.title(title)
    if save:
        plt.savefig(join("plots", f"{title}.png"))

def plot_grouped_data(data: pd.DataFrame, data2: pd.DataFrame, data3: pd.DataFrame, title: str):
    means = [data.mean(), data2.mean(), data3.mean()]
    prompts_dict = {
        "Normal": means[0].values,
        "Bad": means[1].values,
        "Good": means[2].values
    }
    width = 0.25
    fig, ax = plt.subplots(layout="constrained")
    x = range(len(means[0]))
    for i, (label, values) in enumerate(prompts_dict.items()):
        ax.barh(x, values, width, label=label)
        x = [a + width for a in x]
    ax.set_yticks([a + width for a in range(len(means[0]))])
    ax.set_yticklabels(data.columns)
    ax.set_xlabel("Average bias")
    ax.set_title(title)
    ax.legend()

# # Phi3 mini
phi3_normal = pd.read_csv(join("output", "phi3.csv"))
phi3_bad = pd.read_csv(join("output", "phi3_bad.csv"))
phi3_good = pd.read_csv(join("output", "phi3_good.csv"))

plot_data(phi3_normal, "Average bias for each profession (Phi-3-mini-128k-instruct)")
plot_data(phi3_bad, "Average bias for each profession (Phi-3-mini-128k-instruct) (bad professional)")
plot_data(phi3_good, "Average bias for each profession (Phi-3-mini-128k-instruct) (good professional)")

# NSFW
nsfw_normal = pd.read_csv(join("output", "nsfw.csv"))
nsfw_bad = pd.read_csv(join("output", "nsfw_bad.csv"))
nsfw_good = pd.read_csv(join("output", "nsfw_good.csv"))

plot_data(nsfw_normal, "Average bias for each profession (NSFW-3B)")
plot_data(nsfw_bad, "Average bias for each profession (NSFW-3B) (bad professional)")
plot_data(nsfw_good, "Average bias for each profession (NSFW-3B) (good professional)")

# Differences

phi3_diff1 = phi3_good - phi3_normal
phi3_diff2 = phi3_bad - phi3_normal
plot_data(phi3_diff1, "Difference between good and normal prompts (Phi-3-mini-128k-instruct)")
plot_data(phi3_diff2, "Difference between bad and normal prompts (Phi-3-mini-128k-instruct)")

nsfw_diff1 = nsfw_good - nsfw_normal
nsfw_diff2 = nsfw_bad - nsfw_normal
plot_data(nsfw_diff1, "Difference between good and normal prompts (NSFW-3B)")
plot_data(nsfw_diff2, "Difference between bad and normal prompts (NSFW-3B)")

phi3_nsfw_diff = phi3_normal - nsfw_normal
plot_data(phi3_nsfw_diff, "Difference between Phi-3-mini and NSFW-3B")

# plot_grouped_data(phi3_normal, phi3_bad, phi3_good, "Average bias for each profession (Phi-3-mini-128k-instruct)")

plt.show()