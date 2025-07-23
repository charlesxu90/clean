from Bio import SeqIO
import argparse
from loguru import logger
import os


def split_fasta(input_fasta_path, num_files, output_dir="split_fasta_files"):
    """
    Splits a large FASTA file into a specified number of smaller FASTA files.

    Args:
        input_fasta_path (str): Path to the input FASTA file (e.g., 'nr.fasta').
        num_files (int): The desired number of output FASTA files.
        output_dir (str): Directory where the split files will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    else:
        # Optional: Clear existing files in the directory if you want a clean slate
        # for f in os.listdir(output_dir):
        #     os.remove(os.path.join(output_dir, f))
        pass

    print(f"Counting records in {input_fasta_path}...")
    # Count total records
    total_records = 0
    with open(input_fasta_path, "r") as handle:
        for _ in SeqIO.parse(handle, "fasta"):
            total_records += 1
    print(f"Total records found: {total_records}")

    if total_records == 0:
        print("No records found in the input FASTA file. Exiting.")
        return

    records_per_file = (total_records + num_files - 1) // num_files # Ceiling division
    print(f"Targeting {records_per_file} records per file.")

    current_file_index = 0
    current_records_in_file = 0
    output_handle = None

    try:
        with open(input_fasta_path, "r") as in_handle:
            for record in SeqIO.parse(in_handle, "fasta"):
                if current_records_in_file == 0:
                    # Open a new output file
                    current_file_index += 1
                    output_filename = os.path.join(output_dir, f"output_part_{current_file_index:04d}.fasta")
                    print(f"Opening new file: {output_filename}")
                    if output_handle:
                        output_handle.close() # Close previous handle if any
                    output_handle = open(output_filename, "w")

                SeqIO.write(record, output_handle, "fasta")
                current_records_in_file += 1

                if current_records_in_file >= records_per_file and current_file_index < num_files:
                    # Reset counter for the next file, ensuring we don't prematurely close if it's the last file
                    current_records_in_file = 0
                    output_handle.close() # Close current file
                    output_handle = None # Ensure it's treated as closed

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if output_handle:
            output_handle.close() # Ensure the last file handle is closed
        print(f"Splitting complete. Created {current_file_index} files in '{output_dir}'.")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--original_data", type=str, default="nr.fasta", help="Path to the original FASTA file to be split.")
    parser.add_argument("--output_dir", type=str, default="split_fasta_files", help="Directory to save the split FASTA files.")
    parser.add_argument("--n_files", type=int, default=1000, help="Number of output FASTA files.")

    return parser.parse_args()

# --- How to use the function ---
if __name__ == "__main__":
    args = get_args()
    # Replace 'nr.fasta' with the actual pasth to your NCBI nr database FASTA file
    # Make sure this file is accessible from where you run the script.
    input_fasta_file = args.original_data
    desired_num_files = args.n_files
    output_dir = args.output_dir

    split_fasta(input_fasta_file, desired_num_files, output_dir)