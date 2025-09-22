# Web IPlayer Screaming Frog Extraction
# This script processes a CSV file extracted from Screaming Frog for BBC iPlayer URLs.	
# It limits the number of entries per container to 5 and saves the results in a new CSV file.

import pandas as pd

import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

logging.info("Loading CSV file...")
df = pd.read_csv('/Users/forbej02/Documents/GitHub/BBC-Tracking-Implementation-Audit/screamingFrog/web_iplayer_screamingFrog_extraction.csv')
logging.info(f"CSV loaded with {len(df)} rows and {len(df.columns)} columns.")

# Identify columns for each extraction type
container_cols = [col for col in df.columns if 'data-bbc-container' in col]
contentLabel_cols = [col for col in df.columns if 'data-bbc-content-label' in col]
metadata_cols = [col for col in df.columns if 'data-bbc-metadata' in col]
result_cols = [col for col in df.columns if 'data-bbc-result' in col]
href_cols = [col for col in df.columns if 'href' in col]

logging.info(f"Container columns: {container_cols}")
logging.info(f"Content label columns: {contentLabel_cols}")
logging.info(f"Metadata columns: {metadata_cols}")
logging.info(f"Result columns: {result_cols}")
logging.info(f"Href columns: {href_cols}")

output = []

for idx, row in df.iterrows():
    containers = [row[col] for col in container_cols if pd.notna(row[col])]
    content_labels = [row[col] for col in contentLabel_cols if pd.notna(row[col])]
    metadata = [row[col] for col in metadata_cols if pd.notna(row[col])]
    results = [row[col] for col in result_cols if pd.notna(row[col])]
    hrefs = [row[col] for col in href_cols if pd.notna(row[col])]

    logging.debug(f"Row {idx}: containers={containers}, content_labels={content_labels}, metadata={metadata}, results={results}, hrefs={hrefs}")

    max_len = max(len(containers), len(content_labels), len(metadata), len(results), len(hrefs))
    if max_len == 0:
        logging.warning(f"Row {idx} has no extracted data.")

    def pad(lst):
        return lst + [None] * (max_len - len(lst))

    containers = pad(containers)
    content_labels = pad(content_labels)
    metadata = pad(metadata)
    results = pad(results)
    hrefs = pad(hrefs)

    paired_data = [
        (c, l, m, r, h)
        for c, l, m, r, h in zip(containers, content_labels, metadata, results, hrefs)
    ]

    grouped = {}
    for c, l, m, r, h in paired_data:
        if pd.notna(c):
            if c not in grouped:
                grouped[c] = []
            grouped[c].append((l, m, r, h))

    for container, items in grouped.items():
        limited_items = items[:5]
        for i, (content_label, metadata, result, href) in enumerate(limited_items, 1):
            output.append({
                'URL': row['Address'],
                'data-bbc-container': container,
                'Index': i,
                'data-bbc-content-label': content_label,
                'data-bbc-metadata': metadata,
                'data-bbc-result': result,
                'href': href
            })
        logging.info(f"Row {idx}: Container '{container}' - {len(limited_items)} items added.")

output_df = pd.DataFrame(output)
logging.info(f"Total output rows: {len(output_df)}")
output_df.to_csv('/Users/forbej02/Documents/GitHub//BBC-Tracking-Implementation-Audit/screamingFrog/web_iplayer_extractions_limited.csv', index=False)

logging.info("Processed data saved to 'web_iplayer_extractions_limited.csv'")