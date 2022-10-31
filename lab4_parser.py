from json_file import subjects
import xmltodict
import re


isu = 373753

print("Вариант", isu % 36)


# парсим без библиотек
def withoutlib(json_file):
    timetable = ["subject1", "subject2", "subject3", "subject4"]
    for subject in timetable:
        print('<' + subject + '>')
        for key in subjects[subject]:
            print('\t', '<' + key + '>' + json_file[subject][key] + '</' + key + '>')
        print('</' + subject + '>')


# парсим с приминением библиотеки xmltodict
def withlib(json_file):
    json_to_xml = xmltodict.unparse(json_file, full_document=False, pretty=True)
    print(json_to_xml)


# парсим с приминением регулярных выражений
def withregular(json_file):
        timetable = ["subject1", "subject2", "subject3", "subject4"]
        json_file = str(json_file).replace('{', '')
        key = re.findall(r"\'(\w+)\'\:", json_file)  # ищем ключи
        word = re.findall(r"\:\s\'([а-яА-Я0-9/\s.^()-]+)\'", json_file)  # ищем значения
        for i in timetable:
            if i == "subject1":
                print('<' + key[0] + '>')
                key1 = key[1:8]
                word1 = word[0:7]
                for j in range(len(key1)):
                    print("\t", '<' + key1[j] + '>' + word1[j] + '</' + key1[j] + '>')
                print('</' + key[0] + '>')
            if i == "subject2":
                print('<' + key[8] + '>')
                key2 = key[9:16]
                word2 = word[7:14]
                for j in range(len(key2)):
                    print("\t", '<' + key2[j] + '>' + word2[j] + '</' + key2[j] + '>')
                print('</' + key[8] + '>')
            if i == "subject3":
                print('<' + key[16] + '>')
                key3 = key[17:24]
                word3 = word[14:22]
                for j in range(len(key3)):
                    print("\t", '<' + key3[j] + '>' + word3[j] + '</' + key3[j] + '>')
                print('</' + key[16] + '>')
            if i == "subject4":
                print('<' + key[24] + '>')
                key4 = key[25:32]
                word4 = word[21:29]
                for q in range(len(key4)):
                    print("\t", '<' + key4[q] + '>' + word4[q] + '</' + key4[q] + '>')
                print('</' + key[24] + '>')


# withoutlib(subjects)
withlib(subjects)
# withregular(subjects)
