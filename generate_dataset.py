import random

import pandas as pd

# Specify the path to your input text file and output file
input_file = "E:/Programs/opensource/examples/language_translation/data/deu.txt"
output_file = "E:/Programs/opensource/examples/language_translation/data/en-deu.txt"

def remove_tags():
    # Open the input file for reading and output file for writing
    with open(input_file, "r", encoding="utf-8") as f_input, open(output_file, "w", encoding="utf-8") as f_output:
        # Iterate over each line in the input file
        for line in f_input:
            # only keep english german sentences and remove the rest which come after them
            line = line.split("\t")
            eng= line[0]
            ger = line[1]
            line= eng + "\t" + ger + "\n"
    
            # Write the modified line to the output file
            f_output.write(line)
    
    # Print a message indicating the process is complete
    print("Tag removal complete.")


def split_dataset():

    # Specify the desired split ratios
    train_ratio = 0.7  # 70% of the data for training
    test_ratio = 0.2   # 20% of the data for testing
    val_ratio = 0.1    # 10% of the data for validation
    
    # Open the input file for reading
    with open(output_file, "r", encoding="utf-8") as f_input:
        # Read all lines from the input file
        lines = f_input.readlines()
    
    # Shuffle the lines randomly
    random.shuffle(lines)
    
    # Calculate the number of lines for each split
    num_lines = len(lines)
    num_train = int(num_lines * train_ratio)
    num_test = int(num_lines * test_ratio)
    
    # Split the lines into separate lists
    train_lines = lines[:num_train]
    test_lines = lines[num_train:num_train+num_test]
    val_lines = lines[num_train+num_test:]
    
    # Write the train lines to the train file
    with open(output_file, "r", encoding="utf-8"):
        # creates lists containing each pair
        original_word_pairs = [[w for w in l.split('\t')] for l in train_lines]
        #remove all the \n
        original_word_pairs = [[w.replace("\n", "") for w in l] for l in original_word_pairs]
        train_data = pd.DataFrame(original_word_pairs, columns=["eng", "deu"])
        train_data.to_csv("E:/Programs/opensource/examples/language_translation/data/train.csv", index=False)
    
    # Write the test lines to the test file
    with open(output_file, "r", encoding="utf-8"):
        # creates lists containing each pair
        original_word_pairs = [[w for w in l.split('\t')] for l in test_lines]
        #remove all the \n
        original_word_pairs = [[w.replace("\n", "") for w in l] for l in original_word_pairs]
        test_data = pd.DataFrame(original_word_pairs, columns=["eng", "deu"])
        test_data.to_csv("E:/Programs/opensource/examples/language_translation/data/test.csv", index=False)
    
    # Write the validation lines to the validation file
    with open(output_file, "r", encoding="utf-8"):
        # creates lists containing each pair
        original_word_pairs = [[w for w in l.split('\t')] for l in val_lines]
        #remove all the \n
        original_word_pairs = [[w.replace("\n", "") for w in l] for l in original_word_pairs]
        valid_data = pd.DataFrame(original_word_pairs, columns=["eng", "deu"])
        valid_data.to_csv("E:/Programs/opensource/examples/language_translation/data/valid.csv", index=False)
    
    # Print a message indicating the process is complete
    print("Dataset splitting complete.")

remove_tags(),split_dataset()