import re

def split_into_sentences(paragraph):

    # splits  paragraph into a list of sentences using regular expressions with a look-ahead based on logic from the provided text



    sentence_pattern = r'[A-Z0-9].*?[.!?](?=\s+[A-Z0-9]|$)'

    # re.DOTALL flag lets '.' match newline characters
    # re.MULTILINE flag helps with matching at the end of lines ($)
    sentences = re.findall(sentence_pattern, paragraph, flags=re.DOTALL | re.MULTILINE)
    return sentences

def analyze_paragraph():

    # gets input from the user analyzes it to find sentences and displays each sentence along with total count

    # get paragraph input from the user
    paragraph = input("Please enter a paragraph and press Enter:\n")

    if not paragraph.strip():
        print("\nNo input received. Exiting.")
        return

    # use function to split paragraph into sentences
    found_sentences = split_into_sentences(paragraph)

    print("\nIndividual Sentences Found:")
    if found_sentences:
        for i, sentence in enumerate(found_sentences, 1):
            # .strip() cleans up leading/trailing whitespace from newlines
            print(f"{i}: {sentence.strip()}")

        print("\nSummary:   ")
        print(f"Total number of sentences found: {len(found_sentences)}")
    else:
        print("Could not find any sentences that match the required pattern.")

# main part of program that runs analysis
if __name__ == "__main__":
    analyze_paragraph()
