# Quick script to help me visualize the output of some string manipulation.
print("Filename:")
file_name = input()
file_name = file_name.replace('../', '')
file_path = "user_files" + '/%s/%s' % ("id_number", file_name)
print("Full filepath: /%s" % file_path)
