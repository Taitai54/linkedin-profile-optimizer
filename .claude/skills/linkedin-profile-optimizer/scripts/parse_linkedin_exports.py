"""Parse LinkedIn AggregateAnalytics Excel exports in a workspace folder.

Usage:
    python parse_linkedin_exports.py [directory_path]
"""
import glob
import os
import sys
import openpyxl


def parse_analytics(directory: str) -> None:
    pattern = os.path.join(directory, "*Analytics*.xlsx")
    files = sorted(glob.glob(pattern))
    if not files:
        print("No *Analytics*.xlsx files found in:", directory)
        return

    for filepath in files:
        print("=" * 60)
        print(f"FILE: {os.path.basename(filepath)}")
        wb = openpyxl.load_workbook(filepath, data_only=True)
        for name in wb.sheetnames:
            sheet = wb[name]
            rows = [r for r in sheet.iter_rows(values_only=True) if any(r)]
            print(f"\n--- Sheet: {name} ({len(rows)} non-empty rows) ---")
            if name in ("DISCOVERY", "DEMOGRAPHICS", "TOP POSTS"):
                for r in rows[:35]:
                    print(" ", r)
            elif name == "FOLLOWERS":
                for r in rows[:5]:
                    print(" ", r)
            elif name == "ENGAGEMENT":
                total_imp = 0
                total_eng = 0
                for r in rows[1:]:
                    try:
                        total_imp += int(str(r[1]).replace(",", ""))
                        total_eng += int(str(r[2]).replace(",", ""))
                    except (ValueError, IndexError, TypeError):
                        pass
                print(f"  Total Impressions across period: {total_imp}")
                print(f"  Total Engagements across period: {total_eng}")


if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    parse_analytics(target_dir)
