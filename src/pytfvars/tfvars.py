
indent_increment = 2
indent_multiply = 2


def __remove_empty_lines(text):
    lines = text.split('\n')
    non_empty_lines = filter(lambda line: line.strip() != '', lines)
    return '\n'.join(non_empty_lines)


def get_indent_string(indent_no:int):
    indent_ch = ' '
    indent_str = ''
    for c in range(0, indent_no * indent_multiply):
        indent_str = indent_str + indent_ch

    return indent_str


def __convert_str_kv(contents: str, str_key: str, str_value: str, indent_no: int):
    indent_str = get_indent_string(indent_no)
    if str_key.__contains__(":"):
        str_key = "\"{}\"".format(str_key)
    elif str_key.__contains__("="):
        str_key = "\"{}\"".format(str_key)

    if str_value.__contains__("\n"):
        str_value = "<<EOF\n{}\nEOF".format(str_value)
        contents = "{}\n{} = {}".format(contents, str_key, str_value)
    else:
        contents = "{}\n{}{} = \"{}\"".format(contents, indent_str, str_key, str_value)
    return contents


def __convert_str_v(contents: str, str_value: str, indent_no: int):
    indent_str = get_indent_string(indent_no)
    if contents.endswith("["):
        contents = "{}{}{}".format(contents, indent_str, str_value)
    else:
        contents = "{},{}{}".format(contents, indent_str, str_value)
    return contents


def __convert_bool(contents: str, bool_key: str, bool_value: bool, indent_no: int) :
    indent_str = get_indent_string(indent_no)
    contents = "\n{}\n{}{} = {}".format(contents, indent_str, bool_key, "true" if bool_value else "false")
    return contents


def __convert_list(contents: str, list_value: list, indent_no: int) :
    indent_str = get_indent_string(indent_no)
    for l in list_value:
        if type(l) is dict:
            contents = '{}\n{}{}\n'.format(contents, indent_str, '{')
            contents = __convert_dict(contents, l, indent_no + indent_increment)
            contents = '\n{}\n{}{}'.format(contents, indent_str, '},')
        elif type(l) is list:
            contents = __convert_list(contents, l, indent_no)
        elif type(l) is str:
            contents = __convert_str_v(contents, l, indent_no)
    return contents


def __convert_dict(contents: str, dict_value: dict, indent_no: int) :
    indent_str = get_indent_string(indent_no)
    for d_k, d_v in dict_value.items() :
        if type(d_v) is dict:
            contents = '{}\n{}{} = {}\n'.format(contents, indent_str, d_k, '{')
            contents = __convert_dict(contents, d_v, indent_no + indent_increment)
            contents = '{}\n{}{}'.format(contents, indent_str, '}')
        elif type(d_v) is list:
            contents = '{}\n{}{} = {}\n'.format(contents, indent_str, d_k, '[')
            contents = __convert_list(contents, d_v, indent_no + indent_increment)
            contents = '{}\n{}{}\n'.format(contents, indent_str, ']')
        elif type(d_v) is bool:
            contents = __convert_bool(contents, d_k, d_v, indent_no)
        elif type(d_v) is str:
            contents = __convert_str_kv(contents, d_k, d_v, indent_no)
    return contents


def convert(obj: dict):
    """Convert dictionary object to tfvars formatted string

    :param obj: dictionary object to convert
    :return: tfvars formatted string
    """

    indent_no = 0
    indent_str = get_indent_string(indent_no)

    contents = ''
    for k, v in obj.items():
        if type(v) is dict:
            contents = '{}\n{}{} = {}\n'.format(contents, indent_str, k, '{')
            contents = __convert_dict(contents, v, indent_no + indent_increment)
            contents = '\n{}\n{}{}'.format(contents, indent_str, '}')
        elif type(v) is list:
            contents = '{}\n{}{} = {}'.format(contents, indent_str, k, '[')
            contents = __convert_list(contents, v, indent_no + indent_increment)
            contents = '{}{}{}\n'.format(contents, indent_str, ']')
        elif type(v) is bool:
            contents = __convert_bool(contents, k, v, indent_no)
        elif type(v) is str:
            contents = __convert_str_kv(contents, k, v, indent_no)

    contents = __remove_empty_lines(contents)
    print(contents)
    return contents
