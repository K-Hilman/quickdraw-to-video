# quickdraw-to-video

**quickdraw-to-video** is a Python tool that fetches doodles from the Google [Quick, Draw!](https://quickdraw.withgoogle.com/data) dataset, arranges them into customizable animated grids, and exports them as GIFs or MP4 videos. Instantly create mesmerizing visualizations and creative collages from real human sketch data!

## Features

- Fetches sketches by category (e.g., "star", "cat") and country code (e.g., "MY", "US") from QuickDraw
- Customizable grid layouts (square, portrait, landscape)
- Option to use randomization with a seed for reproducibility
- Automatically exports both GIF and high-quality MP4 video
- All output organized in a dedicated `quick draw/` folder

## Installation

Make sure you have [Python 3.7+](https://python.org/) installed.

```bash
git clone https://github.com/K-Hilman/quickdraw-to-video.git
cd quickdraw-to-video
pip install pillow moviepy quickdraw
```

## Usage

**Basic Example:**

```python
from quickdraw_to_video import qd_vid

# Create a 9x16 grid animation of "star" sketches from Malaysia
qd_vid('star', country='MY', ratio='st')
```

**Ratio options:**  
- `'sq'` — 10x10 (square grid, 100 doodles)
- `'st'` — 9x16 (portrait grid, 144 doodles)
- `'ls'` — 16x9 (landscape grid, 144 doodles)

**Other options:**  
- `seed=123` for reproducible random sampling
- `country='US'`, `'IN'`, etc. for other countries (using ISO codes)

Outputs will be in `quick draw/`, as both a `.gif` and `.mp4`.

## Example Output

![sample-animation](quick%20draw/star_MY_sq.gif)  
*Example animation grid of "star" drawings (Malaysian users, 9x16)*

## Project Structure

```
quickdraw-to-video/
│
├── quickdraw_to_video.py
├── README.md
└── requirements.txt
```

## Requirements

- Pillow
- moviepy
- quickdraw

Install them with:
```bash
pip install pillow moviepy quickdraw
```

## License

MIT License.  
See [LICENSE](LICENSE).

## Credits

- [Google Quick, Draw! Dataset](https://quickdraw.withgoogle.com/data)
- [python-quickdraw](https://github.com/sorki/python-quickdraw)
- [moviepy](https://zulko.github.io/moviepy/)

---

*Happy sketch-mashing!*