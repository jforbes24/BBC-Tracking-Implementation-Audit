# Web IPlayer Screaming Frog Extraction
# This script processes a CSV file extracted from Screaming Frog for BBC iPlayer URLs.	
# It limits the number of entries per container to 5 and saves the results in a new CSV file.

import pandas as pd

# Load the CSV from Screaming Frog
df = pd.read_csv('/Users/forbej02/Documents/Screaming Frog/web_iplayer_screamingFrog_extraction.csv')

# Identify columns for each extraction type
container_cols = [col for col in df.columns if 'data-bbc-container' in col]
contentLabel_cols = [col for col in df.columns if 'data-bbc-content-label' in col]
metadata_cols = [col for col in df.columns if 'data-bbc-metadata' in col]
result_cols = [col for col in df.columns if 'data-bbc-result' in col]  # NEW
href_cols = [col for col in df.columns if 'href' in col]

# Initialize output list for long-format data
output = []

# Process each URL row
for _, row in df.iterrows():
    # Collect non-empty metadata, container, and href values
    containers = [row[col] for col in container_cols if pd.notna(row[col])]
    content_labels = [row[col] for col in contentLabel_cols if pd.notna(row[col])]
    metadata = [row[col] for col in metadata_cols if pd.notna(row[col])]
    results = [row[col] for col in result_cols if pd.notna(row[col])]  # NEW
    hrefs = [row[col] for col in href_cols if pd.notna(row[col])]

    # Pair containers, content-labels, metadata, results, and hrefs
    paired_data = [
        (c, l, m, r, h)
        for c, l, m, r, h in zip(containers, content_labels, metadata, results, hrefs)
    ]

        # Group by data-bbc-container
    grouped = {}
    for c, l, m, r, h in paired_data:
        if pd.notna(c):
            if c not in grouped:
                grouped[c] = []
            grouped[c].append((l, m, r, h))

    # Limit to 5 entries per container and add to output
    for container, items in grouped.items():
        limited_items = items[:5]  # Limit to first 5 entries
        for i, (content_labels, metadata, result, href) in enumerate(limited_items, 1):
            output.append({
                'URL': row['Address'],
                'data-bbc-container': container,
                'Index': i,
                'data-bbc-content-label': content_labels,
                'data-bbc-metadata': metadata,
                'data-bbc-result': result,  # NEW
                'href': href
            })

# Convert to DataFrame and save to CSV
output_df = pd.DataFrame(output)
output_df.to_csv('/Users/forbej02/Documents/GitHub//BBC-Tracking-Implementation-Audit/screamingFrog/web_iplayer_extractions_limited.csv', index=False)

print("Processed data saved to 'web_iplayer_screamingFrog_limited.csv'")