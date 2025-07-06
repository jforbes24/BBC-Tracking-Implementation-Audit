# Web IPlayer Screaming Frog Extraction
# This script processes a CSV file extracted from Screaming Frog for BBC iPlayer URLs.	
# It limits the number of entries per container to 5 and saves the results in a new CSV file.

import pandas as pd

# Load the CSV from Screaming Frog
df = pd.read_csv('/Users/forbej02/Documents/Screaming Frog/web_iplayer_screamingFrog_extraction.csv')

# Identify columns for each extraction type
metadata_cols = [col for col in df.columns if 'data-bbc-metadata' in col]
container_cols = [col for col in df.columns if 'data-bbc-container' in col]
href_cols = [col for col in df.columns if 'href' in col]

# Initialize output list for long-format data
output = []

# Process each URL row
for _, row in df.iterrows():
    # Collect non-empty metadata, container, and href values
    metadata = [row[col] for col in metadata_cols if pd.notna(row[col])]
    containers = [row[col] for col in container_cols if pd.notna(row[col])]
    hrefs = [row[col] for col in href_cols if pd.notna(row[col])]

    # Pair metadata, container, and href values
    paired_data = [(m, c, h) for m, c, h in zip(metadata, containers, hrefs)]

    # Group by data-bbc-container
    grouped = {}
    for m, c, h in paired_data:
        if pd.notna(c):
            if c not in grouped:
                grouped[c] = []
            grouped[c].append((m, h))

    # Limit to 5 entries per container and add to output
    for container, items in grouped.items():
        limited_items = items[:5]  # Limit to first 5 entries
        for i, (metadata, href) in enumerate(limited_items, 1):
            output.append({
                'URL': row['Address'],
                'data-bbc-container': container,
                'Index': i,
                'data-bbc-metadata': metadata,
                'href': href
            })

# Convert to DataFrame and save to CSV
output_df = pd.DataFrame(output)
output_df.to_csv('web_iplayer_extractions_limited.csv', index=False)

print("Processed data saved to 'web_iplayer_screamingFrog_limited.csv'")