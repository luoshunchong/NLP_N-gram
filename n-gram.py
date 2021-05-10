def text_filter(text: str) -> str:
    """
    文本过滤器：过滤掉文本数据中的标点符号和其他特殊字符
    :param text: 待过滤的文本
    :return: 过滤后的文本
    """
    result = str()
    for t in text:
        if t.isalnum():
            if t.isalpha():
                t = t.lower()
            result += str(t)
    return result


def slide_word(text, windows):
    """
    滑动取词器
    Input: text='abcd',l=2
    Output: ['ab','bc','cd']
    :param text: 过滤后的文本 （只包含小写数字/字母）
    :param windows: 滑动窗口长度，默认为 5
    :return:
    """
    # tf = text_filter(text)
    tf = text
    result = list()
    for l in windows:
        if len(tf) < l:
            return result
        if len(tf) == l:
            result.append(tf)
            return result
        for i in range(len(tf)):
            word = tf[i:i + l]
            if len(word) < l:
                break
            result.append(word)
    return result


if __name__ == '__main__':
    f = open('./test1.txt', 'a+', encoding='utf-8')
    with open('./test.txt', 'r', encoding='utf-8') as fr:
        data = fr.readlines()
        # print(data)
        for line in data:
            line = line.strip('\n')
            # print(line)
            t = line[2:]
            banner = t
            windows = [3, 4, 5]
            result = slide_word(banner, windows)
            f.write(str(line) + '\t' + str(result)+'\n')
    f.close()
