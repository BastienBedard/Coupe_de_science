import shutil

# Define the source and destination file paths
source_file = 'zone_de_jeu_backup.py'
destination_file = 'zone_de_jeu.py'

# Copy the contents of the source file to the destination file
shutil.copyfile(source_file, destination_file)

print(f"Copied contents of {source_file} to {destination_file}")