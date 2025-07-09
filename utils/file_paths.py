import re
from pathlib import Path
from images_files import excel_utils

folder_path = Path(__file__).parent
excel_file_path = folder_path / "Roombr_Testdata.xlsx"
one_img = folder_path / "one.png"
two_img = folder_path / "two.png"
three_img = folder_path / "three.jpg"
four_img = folder_path / "four.png"

#print("Full path to file:", folder_path)

sheet_name = "Activity_Validations"

count_tags = "(12 Results found)"

text = re.search(r'\((\d+)', count_tags).group(1)
print(text)

get_rows = excel_utils.getRowCount(excel_file_path, sheet_name)
# write_data = excel_utils.writeData(excel_file_path, "Feed_post", 2,8, "like")
# print(get_rows)
