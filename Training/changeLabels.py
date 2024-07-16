import os

labels_dir = '{}'  # Replace with the actual directory

# Iterate through the label files
for filename in os.listdir(labels_dir):
    if filename.startswith('{}'):  # Add prefix condition
        filepath = os.path.join(labels_dir, filename)
    with open(filepath, 'r') as f:
        lines = f.readlines()

        # Modify the first column of each line
        modified_lines = []
    for line in lines:
        parts = line.strip().split()
        if parts:  # Check if the line is not empty
            parts[0] = 'new_label'  # Change the first column to the new label
            modified_lines.append(' '.join(parts) + '\n')

        # Write the modified lines back to the file
    with open(filepath, 'w') as f:
        f.writelines(modified_lines)
