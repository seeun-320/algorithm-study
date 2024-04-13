SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM (SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES, ROW_NUMBER() OVER(PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS RANKING -- 음식 종류 별 즐겨찾기 순위를 함께 저장
    FROM REST_INFO)
WHERE RANKING = 1 -- 음식 종류 별 즐겨찾기가 가장 많은 식당만 출력
ORDER BY 1 DESC