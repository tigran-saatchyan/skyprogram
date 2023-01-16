import json


def set_suffix(number):
    number %= 100

    if 11 <= number <= 14:
        return "ев"

    number %= 10

    if number >= 5:
        return "ев"
    elif number < 2:
        if number == 0:
            return "ев"
        else:
            return "й"
    else:
        return "я"


def convert_tags_to_links(post):
    temp_content_word_list = []
    for word in post["content"].split(" "):
        if word.startswith('#'):
            temp_content_word_list.append(
                f'<a href="/tag/{word[1:]}">{word}</a>'
            )
        else:
            temp_content_word_list.append(word)
    post["content"] = " ".join(temp_content_word_list)

    return post


def read_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        result = json.load(file)
    return result


def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
