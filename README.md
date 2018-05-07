<a href="http://www.numpy.org"><img alt="NumPy" src="https://cdn.rawgit.com/numpy/numpy/master/branding/icons/numpylogo.svg" height="60"></a> &nbsp;
<a href="http://bottlepy.org/"><img alt="BottlePy" src="http://bottlepy.org/docs/dev/_static/logo_nav.png" height="60"></a>

# Контрастный цветоопределитель на нейронных сетях

(звучит круто, на деле ничего особенного)

Сразу отметим, что **для этой задачи вообще нет большого резона использовать нейронные сети**, она выбрана для демонстрации общего принципа.

Проект сделан для презентация к [фестивалю ЛШ2018](http://fest.letnyayashkola.org) от мастерской [Deep Learning](http://www.letnyayashkola.org/deeplearning).
Простая proof-of-concept нейронная сеть, которая учится по вводу пользователя угадывать белый или чёрный логотип надо использовать для рандомно выбранного цвета.

Интерфейс на html/js/jquery, "бэкенд" на [bottlepy](http://bottlepy.org/), нейронная сеть на чистом numpy.
Идея от [codetrain](https://www.youtube.com/watch?v=L9InSe46jkw) + [Jabrills](https://www.youtube.com/watch?v=KO7W0Qq8yUE)

# Установка и запуск

Проверено только для python3.6+. Если из virtualenv, то можно в принципе поставить numpy и bottle самостоятельно или из requirements.txt

     $ pip -r requirements.txt
     $ python server.py  # или 'make run'

После чего открываем браузер по адресу `http://localhost:8080`

Под виндой не пробовал, но наверное можно сделать `conda intstal bottle` и потом попробовать `python server.py`

## &laquo;Что можно сделать ещё

* Попробовать поменять число нейронов в скрытом слое.
* Имплементировать другую активационную функцию: для этого надо дописать их в файле `neural_networks.py` и подменить соответствующие места в методах `train` и `predict` (или сделать свой класс)
* Сделать то же самое на другом методе машинного обучения (DecisionTree например) и сравнить результат

Наконец, как совсем хорошее улучшение можно расширить всё это так чтобы на выходе было три вывода (r, g, b) и соответственно сеть обучалась делать "дополняющий цвет" а не просто бинарно белый/чёрный. Но тут ещё надо будет придумать как собрать входные данные для обучения и как измерять "точность".
