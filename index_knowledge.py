import re
import json
import os

# Use relative path from script location
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "ANLY500-Analytics-I", "Knowledge", "Field_ea_2012_Discovering_Statistics_using_R_normalized.txt")

def index_file(path):
    index = {
        "headers": [],
        "keywords": {
            "Data Screening": [],
            "Accuracy": [],
            "Missing Data": [],
            "Outlier": [],
            "Mahalanobis": [],
            "MICE": [],
            "MCAR": [],
            "MNAR": []
        }
    }
    
    # Regex for headers like 1.1., 1.2., 5.5.1.
    header_pattern = re.compile(r'^\s*(\d+(\.\d+)+)\.?\s+(.+)$')
    
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
                
            # Check for headers
            header_match = header_pattern.match(line)
            if header_match:
                index["headers"].append({
                    "line": i + 1,
                    "section": header_match.group(1),
                    "title": header_match.group(3)
                })
            
            # Check for keywords
            for keyword in index["keywords"]:
                if keyword.lower() in line.lower():
                    # Store context (line number and content)
                    index["keywords"][keyword].append({
                        "line": i + 1,
                        "content": line[:100] + "..." if len(line) > 100 else line
                    })
                    
        return index

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    result = index_file(file_path)
    # Print a summary to avoid huge output
    summary = {
        "headers_count": len(result.get("headers", [])),
        "headers_sample": result.get("headers", [])[:10],
        "keywords_hits": {k: len(v) for k, v in result.get("keywords", {}).items()},
        "keywords_locations": {k: v[:5] for k, v in result.get("keywords", {}).items()} # Show first 5 hits per keyword
    }
    print(json.dumps(summary, indent=2))
