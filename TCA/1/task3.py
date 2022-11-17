import re


def readFile(filename: str) -> str:
    """
    Read the file and return the content as a string.
    """
    with open(filename, "r") as file:
        return file.read()


def breakIntoTokens(data: str) -> list:
    """
    Break the data/file (as string) into tokens.
    """
    data = re.sub(r"[^\w\s]", "", data)  # remove punctuation and special characters
    tokens = data.split()
    tokens = [token.lower() for token in tokens]  # convert all tokens to lowercase
    return tokens


def breakIntoSentences(data: str) -> list:
    """
    Break the data/file (as string) into sentences.
    """
    sentences = data.split(".")
    sentences = [sentence.strip() for sentence in sentences]  # remove extra whitespace
    return sentences


def countTokens(data: str) -> int:
    """
    Return the number of tokens in the data/list.
    """
    tokens = breakIntoTokens(data)
    return len(tokens)


def countToken(token: str, data: list[str]) -> int:
    """
    Return the number of times the token appears in the data/list.
    """
    count = 0
    for item in data:
        if item == token.lower():
            count += 1
    return count


def normalisedFrequency(token: str, data: list[str]) -> float:
    """
    Return the normalised frequency of the token in the data.
    """
    return countToken(token, data) / len(data)


def sentenceCount(data: str) -> int:
    """
    Return the number of sentences in the data.
    """
    sentences = breakIntoSentences(data)
    return len(sentences)


def sentencesContaining(token: str, data: str) -> list:
    """
    Return a list of sentences containing the token.
    """
    sentences = breakIntoSentences(data)
    sentences_containing_token = []
    for sentence in sentences:
        current_sentence_tokens = breakIntoTokens(sentence.lower())
        for current_sentence_token in current_sentence_tokens:
            if current_sentence_token == token.lower():
                sentences_containing_token.append(sentence)
                break
    return sentences_containing_token


def main():
    try:
        filename = input("Enter the name of the file to read from: ")
        data = readFile(filename)
        num_tokens = countTokens(data)
        sentence_count = sentenceCount(data)
        print(f">> The number of tokens in the file is: {num_tokens}")
        print(f">> The number of sentences in the file is: {sentence_count}")
        token = input("Enter the token to count: ")
        split_data = breakIntoTokens(data)
        num_token = countToken(token, split_data)
        print(f">> The number of times the token '{token}' appears in the file is: {num_token}")
        sentences_containing_token = sentencesContaining(token, data)
        print(f">> The number of sentences containing the token '{token}' are: {len(sentences_containing_token)}")
        normalised_frequency = normalisedFrequency(token, split_data)
        print(f">> The normalised frequency of the token '{token}' is: {normalised_frequency}")
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid data in file.")
    except IndexError:
        print("Invalid data in file.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
