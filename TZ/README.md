Game Answer

Необходимо ​ ответить на ​ вопрос:
Заказы с какими продуктами игроки чаще удаляют на карте заказов и почему?

Продукты производятся на фабриках и выращиваются на полях. Все они хранятся в
амбаре и используются в заказах от жителей города. Заказы делаются в интерфейсе
карты города. Если игроку не хочется выполнять заказ, то он может удалить
его (кнопка с урной), после этого потребуется время на генерацию нового заказа.
Для ответов на этот вопрос вам понадобится статистика игроков:
refused_order_products.csv  - где указано, сколько заказов, содержащих данный продукт, удалили пользователи на различных уровнях игры.
Для каждого сегмента эта строка с продуктами отсортирована по убыванию, то есть на
первом месте стоят продукты, которые чаще встречаются в удаляемых заказах.

product_info.csv - таблица с характеристиками продукта.

Blacklist Domains

Test task (attached 2 files to the test task): In this task you have a list of domains and the related blacklists they appear on. In addition, some of these domains were responsible for sending a file to the client. These files have been run through VirusTotal and the AV results are also available with the domains. The goal is to explore the data, find some structure and attempt to find a way to gain confidence in what domains are more malicious as a means of prioritization. As with any type of data exploration, it's not a silver bullet but perhaps you'll gain an understanding of the data.

Input data:
1. File Input - Blacklist Data The data for the lab is contained in host_detections.csv and has columns: host, detections, and detection_count.
2. File Input - VirusTotal The data is in a file named mal_domains.csv and has columns: host, count, and detections.
