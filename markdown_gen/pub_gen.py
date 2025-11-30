"""
Publications Page Generator

This script generates a Jekyll markdown page for publications with interactive 
tag filtering functionality from an Excel file.

Usage:
    python pub_gen.py

Requirements:
    - pandas
    - openpyxl
"""

import pandas as pd
import re
import os

# ============================================================================
# Configuration
# ============================================================================

PRIORITY_TAGS = ['AI', 'Medical', 'XR']
PANTONE_COLORS = [
    '#F2D4D7',  # Pantone 698 C – blush pink
    '#F5D5C8',  # Pantone 9160 C – soft peach
    '#F5E6A3',  # Pantone 607 C – pale yellow
    '#B8E2D8',  # Pantone 628 C – pastel aqua
    '#C4C5E8',  # Pantone 552 C – lavender blue
    '#E6D4E8',  # Pantone 7436 C – pale lilac
    '#B8D4E8',  # Pantone 7457 C – powder blue
    '#C8E6D4',  # Pantone 7470 C – soft mint
    '#F5C4B8',  # Pantone 9040 C – light coral
    '#D4E6D4',  # Pantone 9064 C – pastel sage
]
OUTPUT_FILE = "../pubs.md"
EXCEL_FILE = "publications.xlsx"

# ============================================================================
# Helper Functions
# ============================================================================

def process_authors(authors):
    """Format author list with Tim Chen in bold."""
    author_list = [x.strip(' ') for x in authors.split(',')]
    s = ''
    for i in range(len(author_list)):
        author = author_list[i].replace('Tim Chen', '**Tim Chen**')
        s += author
        if i != len(author_list) - 1:
            s += ', '
        else:
            s += '<br>'
    return s

def get_tag_color(tag, color_palette):
    """Assign consistent color to tag based on hash."""
    hash_val = hash(tag)
    color_index = abs(hash_val) % len(color_palette)
    return color_palette[color_index]

def extract_tags(pubs, tags_column):
    """Extract all tags from publications and return tag lists per paper."""
    all_tags = set()
    paper_tags_list = []
    
    for idx, row in pubs.iterrows():
        tags_str = row[tags_column]
        if pd.notna(tags_str) and str(tags_str).strip():
            tags = [tag.strip() for tag in str(tags_str).split(',') if tag.strip()]
            paper_tags_list.append(tags)
            all_tags.update(tags)
        else:
            paper_tags_list.append([])
    
    return all_tags, paper_tags_list

def sort_tags(all_tags, priority_tags):
    """Sort tags with priority tags first, then alphabetically."""
    all_tags_list = list(all_tags)
    priority_found = [tag for tag in priority_tags if tag in all_tags_list]
    remaining_tags = [tag for tag in all_tags_list if tag not in priority_tags]
    remaining_tags.sort()
    return priority_found + remaining_tags

def create_color_mapping(tags, color_palette):
    """Create color mapping for all tags."""
    return {tag: get_tag_color(tag, color_palette) for tag in tags}

# ============================================================================
# HTML Generation Functions
# ============================================================================

def generate_front_matter():
    """Generate Jekyll front matter."""
    return "---\nlayout: page\ntitle: \"Publications\"\n---\n\n"

def generate_tag_filter_ui(all_tags, tag_colors):
    """Generate tag filter buttons HTML."""
    html = '''<div id="tag-filter-container" style="margin-bottom: 30px;">
  <div style="margin-bottom: 15px;">
    <strong>Filter by tags:</strong>
  </div>
  <div id="tag-buttons" style="margin-bottom: 15px;">
'''
    for tag in all_tags:
        tag_id = re.sub(r'[^a-zA-Z0-9]', '_', tag)
        tag_color = tag_colors[tag]
        html += f'    <button class="tag-filter-btn" data-tag="{tag}" id="tag_{tag_id}" style="margin: 5px; padding: 8px 15px; border: 1px solid {tag_color}; background-color: {tag_color}; border-radius: 4px; cursor: pointer; font-size: 14px; color: #333;">{tag}</button>\n'
    html += '    <button id="clear-filter-btn" style="margin: 5px; padding: 8px 15px; border: 1px solid #999; background-color: #f5f5f5; color: #333; border-radius: 4px; cursor: pointer; font-size: 14px;">Clear Filter</button>\n'
    html += '  </div>\n</div>\n'
    return html

def generate_css():
    """Generate CSS styles for tags and filtering."""
    return '''<style>
.tag-filter-btn.active {
  opacity: 1 !important;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
  transform: scale(1.05);
}

.tag-filter-btn:not(.active) {
  opacity: 0.7;
}

.tag-filter-btn:hover {
  opacity: 1 !important;
  transform: scale(1.05);
  transition: all 0.2s ease;
}

.paper-tag {
  display: inline-block;
  margin: 3px 5px 3px 0;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  color: #333;
  font-weight: 500;
}

.paper-row {
  transition: opacity 0.3s ease;
}

.paper-row.hidden {
  display: none;
}
</style>
'''

def generate_table_header():
    """Generate HTML table header."""
    return '''<table>
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<tbody>
'''

def generate_paper_row(row, tags, tag_colors):
    """Generate HTML row for a single paper."""
    data_tags = ' '.join([re.sub(r'[^a-zA-Z0-9]', '_', tag) for tag in tags]) if tags else ''
    
    html = f'<tr class="paper-row" data-tags="{data_tags}">\n'
    html += f'<td><img src="/assets/img/{row["IMG"]}" width="250"></td>'
    html += f'<td markdown="span">'
    html += f"**{row['TITLE'].strip()}**<br><br>"
    html += process_authors(row['AUTHORS'])
    html += f"*{row['VENUE']}* {row['YEAR']}<br>"
    
    # Paper link
    if pd.notna(row['PAPER_NAME']):
        html += f'<a href="/assets/publications/{row["PAPER_NAME"]}" target="_blank">[paper]</a>'
    else:
        html += "[paper]"
    
    # YouTube link
    html += '  '
    if pd.notna(row['YOUTUBE']):
        html += f'<a href="{row["YOUTUBE"]}" target="_blank">[youtube]</a>'
    else:
        html += " "
    
    # Tags
    if tags:
        html += '<br><br>'
        for tag in tags:
            tag_color = tag_colors.get(tag, '#e9ecef')
            html += f'<span class="paper-tag" style="background-color: {tag_color}; border: 1px solid {tag_color};">{tag}</span>'
    
    html += '</td>\n</tr>\n'
    return html

def generate_javascript():
    """Generate JavaScript for tag filtering."""
    return '''<script>
(function() {
  var selectedTags = new Set();
  var tagButtons = document.querySelectorAll('.tag-filter-btn');
  var clearFilterBtn = document.getElementById('clear-filter-btn');
  var paperRows = document.querySelectorAll('.paper-row');
  
  function filterPapers() {
    if (selectedTags.size === 0) {
      paperRows.forEach(function(row) {
        row.classList.remove('hidden');
      });
    } else {
      paperRows.forEach(function(row) {
        var rowTags = row.getAttribute('data-tags').split(' ').filter(function(t) { return t.length > 0; });
        var hasMatch = false;
        
        selectedTags.forEach(function(selectedTag) {
          var selectedTagId = selectedTag.replace(/[^a-zA-Z0-9]/g, '_');
          if (rowTags.indexOf(selectedTagId) !== -1) {
            hasMatch = true;
          }
        });
        
        if (hasMatch) {
          row.classList.remove('hidden');
        } else {
          row.classList.add('hidden');
        }
      });
    }
  }
  
  tagButtons.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var tag = this.getAttribute('data-tag');
      
      if (this.classList.contains('active')) {
        this.classList.remove('active');
        selectedTags.delete(tag);
      } else {
        this.classList.add('active');
        selectedTags.add(tag);
      }
      
      filterPapers();
    });
  });
  
  clearFilterBtn.addEventListener('click', function() {
    selectedTags.clear();
    tagButtons.forEach(function(btn) {
      btn.classList.remove('active');
    });
    filterPapers();
  });
})();
</script>
'''

# ============================================================================
# Main Execution
# ============================================================================

def main():
    """Main function to generate publications page."""
    # Read Excel file
    print(f"Reading Excel file: {EXCEL_FILE}")
    pubs = pd.read_excel(EXCEL_FILE)
    tags_column = pubs.columns[-1]
    print(f"Found {len(pubs)} publications")
    print(f"Tags column: {tags_column}")
    
    # Extract and process tags
    print("Extracting tags...")
    all_tags, paper_tags_list = extract_tags(pubs, tags_column)
    all_tags = sort_tags(all_tags, PRIORITY_TAGS)
    tag_colors = create_color_mapping(all_tags, PANTONE_COLORS)
    print(f"Found {len(all_tags)} unique tags")
    
    # Generate markdown content
    print("Generating HTML...")
    md = generate_front_matter()
    md += generate_tag_filter_ui(all_tags, tag_colors)
    md += generate_css()
    md += generate_table_header()
    
    # Generate paper rows
    for idx, row in pubs.iterrows():
        tags = paper_tags_list[idx]
        md += generate_paper_row(row, tags, tag_colors)
    
    md += '</tbody>\n</table>\n'
    md += generate_javascript()
    
    # Write output file
    print(f"Writing output file: {OUTPUT_FILE}")
    with open(OUTPUT_FILE, 'w', encoding='utf8') as f:
        f.write(md)
    
    print('✓ Publications page generated successfully!')
    print(f'✓ Output file: {OUTPUT_FILE}')
    print(f'✓ Total papers: {len(pubs)}')
    print(f'✓ Total tags: {len(all_tags)}')

if __name__ == "__main__":
    main()

