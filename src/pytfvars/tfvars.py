import hcl


def __remove_empty_lines(text):
    lines = text.split('\n')
    non_empty_lines = filter(lambda line: line.strip() != '', lines)
    return '\n'.join(non_empty_lines)


def __convert_str_kv(contents: str, str_key: str, str_value: str) :
    if str_key.__contains__(":"):
        str_key = "\"{}\"".format(str_key)
    elif str_key.__contains__("="):
        str_key = "\"{}\"".format(str_key)

    if str_value.__contains__("\n"):
        str_value = "<<EOF\n{}\nEOF".format(str_value)
        contents = "{}\n{} = {}".format(contents, str_key, str_value)
    else:
        contents = "{}\n{} = \"{}\"".format(contents, str_key, str_value)
    return contents


def __convert_str_v(contents: str, str_value: str):
    if contents.endswith("["):
        contents = "{} {}".format(contents, str_value)
    else:
        contents = "{}, {}".format(contents, str_value)
    return contents


def __convert_bool(contents: str, bool_key: str, bool_value: bool) :
    contents = "\n{}\n{} = {}".format(contents, bool_key, "true" if bool_value else "false")
    return contents


def __convert_list(contents: str, list_value: list) :
    for l in list_value:
        if type(l) is dict:
            contents = '{}\n {}\n'.format(contents, '{')
            contents = __convert_dict(contents, l)
            contents = '\n{}\n{}'.format(contents, '},')
        elif type(l) is list:
            contents = __convert_list(contents, l)
        elif type(l) is str:
            contents = __convert_str_v(contents, l)
    return contents


def __convert_dict(contents: str, dict_value: dict) :
    for d_k, d_v in dict_value.items() :
        if type(d_v) is dict:
            contents = '{}\n {} = {}\n'.format(contents, d_k, '{')
            contents = __convert_dict(contents, d_v)
            contents = '{}\n{}'.format(contents, '}')
        elif type(d_v) is list:
            contents = '{} \n {} = {}\n'.format(contents, d_k, '[')
            contents = __convert_list(contents, d_v)
            contents = '{}\n{}\n'.format(contents, ']')
        elif type(d_v) is bool:
            contents = __convert_bool(contents, d_k, d_v)
        elif type(d_v) is str:
            contents = __convert_str_kv(contents, d_k, d_v)
    return contents


def convert(obj: dict):
    """Convert dictionary object to tfvars formatted string

    :param obj: dictionary object to convert
    :return: tfvars formatted string
    """
    contents = ''
    for k, v in obj.items():
        if type(v) is dict:
            contents = '{}\n {} = {}\n'.format(contents, k, '{')
            contents = __convert_dict(contents, v)
            contents = '\n{}\n{}'.format(contents, '}')
        elif type(v) is list:
            contents = '{} \n {} = {}'.format(contents, k, '[')
            contents = __convert_list(contents, v)
            contents = '{}{}\n'.format(contents, ']')
        elif type(v) is bool:
            contents = __convert_bool(contents, k, v)
        elif type(v) is str:
            contents = __convert_str_kv(contents, k, v)

    contents = __remove_empty_lines(contents)
    return contents
