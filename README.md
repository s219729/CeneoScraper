# CeneoScraper
## Etap 1 - Pobranie składowych pojedynczej opinii o wybranym produkcie z serwisu Ceneo.pl (https://www.ceneo.pl)
* Pobranie kodu pojedynczej strony z opiniami o wskazanym produkcie 
* Analiza kodu HTML pojedynczej opinii 

+---------------+------------+--------------+----------+
|Składowa opinii|Selektor CSS|Nazwa zmiennej|Typ danych|
+:==============+============+==============+==========+
|Opinia|div.js_product-review|opinion||
+---------------+------------+--------------+----------+
|Identyfikator opinii|`["data-entry-id"]`|opinion_id|
+---------------+------------+--------------+----------+
|Autor|span.user-post__author-name|author||
+---------------+------------+--------------+----------+
|Rekomendacja|span.user-post__author-recomendation|recomm|
+---------------+------------+--------------+----------+
|Liczba gwiazdek|span.user-post__score-count|stars||
+---------------+------------+--------------+----------+
|Treść|div.user-post__text|content|
+---------------+------------+--------------+----------+
|Lista zalet|review-feature__col:has(> div.review-feature__title--positives) > review-feature__item\|||
||review-feature__col:has(> div[class*="positives"]) > review-feature__item\|||
||div.review-feature__title--positives ~ review-feature__item|||
+---------------+------------+--------------+----------+
|Lista wad|review-feature__col:has(> div.review-feature__title--negatives) > review-feature__item\|||
||review-feature__col:has(> div[class*="negatives"]) > review-feature__item\|||
||div.review-feature__title--negatives ~ review-feature__item||| 
+---------------+------------+--------------+----------+
|Dla ilu osób uzyteczna|span`[id^="votes-yes"]`\|||
||button.vote-yes > span\|||
||button.vote-yes`[data-total-vote"]`|||
+---------------+------------+--------------+----------+
|Dla ilu osób nieuzyteczna|span`[id^="votes-no"]`\|||
||button.vote-no > span\|||
||button.vote-no`[data-total-vote"]`|||
+---------------+------------+--------------+----------+
|Czy opinia potwierdzona zakupem|div.review-pz|||
+---------------+------------+--------------+----------+
|Data wystawienia opinii|span.user-post__published > time:nth-child(1)`["datetime"]`|||
+---------------+------------+--------------+----------+
|Data zakupu produktu|span.user-post__published > time:nth-child(2)`["datetime"]`|||
+---------------+------------+--------------+----------+
