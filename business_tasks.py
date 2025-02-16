# business_functions.py
import httpx
import json
import sqlite3
from PIL import Image
import markdown
import csv
from pathlib import Path
import os
from base_logger import logger

async def fetch_api_data(url: str, output_path: str) -> None:
    """B3: Fetch data from an API and save it"""
    logger.info(f"Fetching data from {url}")
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(response.json(), f)
    logger.info(f"Data saved to {output_path}")

async def run_sql_query(db_path: str, query: str, output_path: str) -> None:
    """B5: Run SQL query and save results"""
    logger.info(f"Running SQL query on {db_path}")
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        results = cursor.execute(query).fetchall()
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(results, f)
        logger.info(f"Query results saved to {output_path}")
    finally:
        conn.close()

async def process_image(image_path: str, output_path: str, operation: str, quality: int = 85, dimensions: dict = None) -> None:
    """B7: Process image (compress/resize)"""
    logger.info(f"Processing image {image_path} with operation {operation}")
    with Image.open(image_path) as img:
        if operation == "compress":
            img.save(output_path, optimize=True, quality=quality)
        elif operation == "resize" and dimensions:
            width = dimensions.get('width', 800)
            height = dimensions.get('height', 800)
            img.thumbnail((width, height))
            img.save(output_path)
    logger.info(f"Processed image saved to {output_path}")

async def convert_markdown(md_path: str, html_path: str) -> None:
    """B9: Convert Markdown to HTML"""
    logger.info(f"Converting markdown file {md_path}")
    with open(md_path, 'r') as f:
        md_content = f.read()
    
    html_content = markdown.markdown(md_content)
    
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    with open(html_path, 'w') as f:
        f.write(html_content)
    logger.info(f"HTML saved to {html_path}")

async def filter_csv(csv_path: str, filter_criteria: dict, output_path: str) -> None:
    """B10: Filter CSV file based on criteria"""
    logger.info(f"Filtering CSV file {csv_path}")
    filtered_data = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if all(row.get(k) == v for k, v in filter_criteria.items()):
                filtered_data.append(row)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(filtered_data, f)
    logger.info(f"Filtered data saved to {output_path}")