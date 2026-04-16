import imageio.v2 as imageio
import os

def make_gif(folder="frames", output="artemis.gif", fps=30):
    frames = []

    for f in sorted(os.listdir(folder)):
        if f.endswith(".png"):
            frames.append(imageio.imread(os.path.join(folder, f)))

    imageio.mimsave(output, frames, fps=fps)


def make_mp4(folder="frames", output="artemis.mp4", fps=30):
    writer = imageio.get_writer(output, fps=fps)

    for f in sorted(os.listdir(folder)):
        if f.endswith(".png"):
            writer.append_data(imageio.imread(os.path.join(folder, f)))

    writer.close()