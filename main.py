import pandas as pd
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_2

def make_checkbox(choices, message, name):
    questions = [
        {
            'type': 'checkbox',
            'qmark': 'o',
            'message': message,
            'name': name,
            'choices': choices
        }
    ]

    selected_columns = make_menu(questions)
    return selected_columns

def make_menu(questions):
    answers = prompt(questions, style=custom_style_2)
    return answers

def get_titles(price_dataframe):
    price_titles = []
    for price_row in price_dataframe.values:
        if pd.isna(price_row[1]):
            price_titles.append(price_row[0])
    return price_titles

def remove_useless_from_titles(price_dataframe, price_titles):
    useless_titles = make_checkbox([{'name': i} for i in price_titles], 'choose non-title rows',
                                      'non-title rows')['non-title rows']

    t = []
    for useless_title in useless_titles:
        t.append(*price_dataframe.index[price_dataframe['Код'] == useless_title].tolist())
    price_dataframe = price_dataframe.drop(t)
    print(price_dataframe)

def get_code_blocks(price_dataframe, titles):
    columns = ('Код', 'Наименование исследования', 'Цена, руб')
    is_title = True
    code_block = []
    for price_row in price_dataframe:
        if pd.isna(price_row.values[1]):
            is_title = True
            if is_title:
                code_frame = pd.DataFrame(code_block, columns=columns)
                code_block = []
                is_title = not is_title
            continue
        code_block.append((price_row['Код'], price_row['Наименование исследования'], price_row['Цена, руб']))




input_list = pd.read_excel('price_info.xlsx')
#print(input_list)
titles = get_titles(input_list)
#print(titles)

remove_useless_from_titles(input_list, titles)