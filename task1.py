# TODO Напишите функцию для поиска индекса товара


def retIndex(spis, tovar):
    j = 0
    if tovar in spis:
        for i in spis:
            if i == tovar:
                return j
            j+=1

    else:
        return None




items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']



for find_item in ['банан', 'груша', 'персик']:
    index_item =  retIndex(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
