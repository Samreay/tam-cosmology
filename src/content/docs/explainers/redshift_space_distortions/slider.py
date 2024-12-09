import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import json
from defaults import colours

names = {}
here = Path(__file__).parent


def plot(i: int):
    fig, ax = plt.subplots(figsize=(8, 4))
    x = np.arange(0, 2 * np.pi, 0.01)
    ax.plot(x, np.sin((1 + 0.4 * i) * x), c=colours[i])
    ax.set_xlim(0, 2 * np.pi)
    path = here / f"slider_{i}.png"
    fig.savefig(path, bbox_inches="tight")
    names[path] = f"Slider {i}, which has colour {colours[i]}"


for i in range(5):
    plot(i)

# json data files need to be a data dir, not in the content dir. Dont ask me why.
label_file = Path(str(here / "labels.json").replace("/src/content", "/src/data"))
label_file.parent.mkdir(parents=True, exist_ok=True)
with label_file.open("w") as f:
    # The keys need to start with /src/data
    names_to_write = {
        "/src/content" + str(path).split("/src/content")[-1]: val
        for path, val in names.items()
    }
    json.dump(names_to_write, f, indent=2)
