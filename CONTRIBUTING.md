# Contributing Guidelines

Thank you for your interest in contributing to this project! We welcome contributions of all kinds, including code, documentation, and training data.

## How to Contribute

1. **Fork the repository** and create your branch from `main`.
2. **Make your changes** (code, documentation, or training data).
3. **Test your changes** to ensure they work as expected.
4. **Submit a pull request** with a clear description of your changes.

## Reporting Issues

If you find a bug or have a feature request, please open an issue. Include as much detail as possible to help us understand and address your concern.

## Coding Standards

- Follow existing code style and conventions.
- Write clear, concise commit messages.
- Add comments where necessary for clarity.

## Training Data Contributions

If you are contributing training data or custom fonts for Tesseract, please ensure your files are properly formatted and documented. Refer to the steps below for guidance.

## Contact

For questions or help, open an issue or reach out to the maintainers.


## Training custom font with tesseract and training tools:**

1. **Prepare training text** → plain UTF-8 text with your characters.
2. **Generate images** → `text2image` renders text using fonts.
3. **Extract character set** → `unicharset_extractor` from the training text.
4. **Box files** → `text2image` also makes `.box` files mapping chars to glyphs.
5. **Feature extraction** → run `tesseract image.tif image box.train` to get `.tr` files.
6. **Cluster training data** → use `mftraining`, `cntraining`, `shapeclustering` on `.tr` files to produce `inttemp`, `pffmtable`, `normproto`, `shapetable`.
7. **Combine into traineddata** → `combine_lang_model` merges everything (plus wordlists, configs) into a single `yourlang.traineddata`.
8. **Install model** → move `yourlang.traineddata` into `tessdata/` so Tesseract can use it.

That’s the full loop: text → images → features → model → `.traineddata` → usable by Tesseract.

