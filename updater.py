from pathlib import Path
from main import is_even

main_file_path = Path("main.py")
main_file_content = main_file_path.read_text()

numbers = [int(i) for i in main_file_content.split(" ") if i.isdigit()]
largest = max(numbers)
new = largest + 1
new_retval = not is_even(largest)
new_retval_str = str(new_retval).capitalize()

aux_replace = """        case _:"""

new_case = f"""case {new} | -{new}:
            return {new_retval_str}""" + "\n" + aux_replace

main_file_path.write_text(main_file_content.replace("case _:", new_case))
print(f"added case {new} | -{new} with return value of {new_retval_str}")

read_me_path = Path("README.md")
read_me_content = read_me_path.read_text()
read_me_path.write_text(read_me_content.replace(str(largest), str(new)))
print("updated readme")
