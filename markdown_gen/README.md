# Publications Page Generator

This tool generates a Jekyll markdown page for publications with interactive tag filtering functionality.

## Features

- **Interactive Tag Filtering**: Click tags to filter papers (OR logic - shows papers matching any selected tag)
- **Color-Coded Tags**: Each tag is assigned a unique Pantone pastel color
- **Priority Tags**: AI, Medical, and XR tags appear first, followed by other tags alphabetically
- **Visual Tag Display**: Tags are displayed both as filter buttons and on each paper

## Requirements

- Python 3.x
- pandas
- openpyxl (for reading Excel files)

Install dependencies:
```bash
pip install pandas openpyxl
```

## Usage

### 1. Prepare Your Data

1. Place your publication images in `assets/img/`
2. Place your PDF files in `assets/publications/`
3. Update `publications.xlsx` with your publication data

### 2. Excel File Format

The Excel file should have the following columns:
- `TITLE`: Paper title
- `AUTHORS`: Comma-separated list of authors
- `VENUE`: Publication venue
- `YEAR`: Publication year
- `IMG`: Image filename (should be in `assets/img/`)
- `PAPER_NAME`: PDF filename (should be in `assets/publications/`)
- `YOUTUBE`: YouTube video URL (optional)
- **Last column**: Tags (comma-separated, e.g., "AI, Medical, XR")

### 3. Generate the Page

**Option A: Using Python script (recommended)**
```bash
cd markdown_gen
python pub_gen.py
```

**Option B: Using Jupyter notebook**
1. Open `pub_gen.ipynb` in Jupyter
2. Run the generator cell
3. The output file `pubs.md` will be generated in the parent directory

### 4. Test Locally

```bash
# Install Jekyll dependencies (if needed)
bundle install

# Start Jekyll server
bundle exec jekyll serve
# or
jekyll serve
```

Visit `http://localhost:4000/pubs.html` to view the page.

### 5. Commit to GitHub

After testing, commit the changes:
```bash
git add pubs.md
git commit -m "Update publications page"
git push
```

## Configuration

You can customize the following in the notebook:

- **Priority Tags**: Modify `PRIORITY_TAGS` to change which tags appear first
- **Color Palette**: Modify `PANTONE_COLORS` to change tag colors
- **Output File**: Change `OUTPUT_FILE` to generate a different filename

## Tag Colors

The following Pantone colors are used:
1. Pantone 698 C – blush pink (#F2D4D7)
2. Pantone 9160 C – soft peach (#F5D5C8)
3. Pantone 607 C – pale yellow (#F5E6A3)
4. Pantone 628 C – pastel aqua (#B8E2D8)
5. Pantone 552 C – lavender blue (#C4C5E8)
6. Pantone 7436 C – pale lilac (#E6D4E8)
7. Pantone 7457 C – powder blue (#B8D4E8)
8. Pantone 7470 C – soft mint (#C8E6D4)
9. Pantone 9040 C – light coral (#F5C4B8)
10. Pantone 9064 C – pastel sage (#D4E6D4)

Each tag is assigned a color consistently based on its name (using hash function).

## How It Works

1. **Data Extraction**: Reads the Excel file and extracts publication data and tags
2. **Tag Processing**: Sorts tags with priority tags first, then alphabetically
3. **Color Assignment**: Assigns consistent colors to each tag
4. **HTML Generation**: Generates HTML with:
   - Tag filter buttons at the top
   - CSS styling for tags and filtering
   - Table with publication entries
   - JavaScript for interactive filtering
5. **Output**: Writes the generated markdown file

## Troubleshooting

### Tags not showing up
- Ensure the last column in Excel contains comma-separated tags
- Check that tags are not empty or just whitespace

### Colors not displaying
- Verify that the color hex codes are correct
- Check browser console for any JavaScript errors

### Filtering not working
- Ensure JavaScript is enabled in your browser
- Check that the generated HTML includes the JavaScript section

## Notes

- Table style can be customized in `assets/css/beautifuljekyll.css`
- The generator automatically bolds "Tim Chen" in author lists
- Empty tag cells are handled gracefully (papers without tags won't break)

